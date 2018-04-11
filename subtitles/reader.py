# -*- coding: UTF-8 -*-
import re
import os
import chardet

from models import *

TAG_RE = re.compile(r'<[^>]+>')


def init_languages(source_language_code, destination_language_code):
    try:
        Language.objects.create(code=source_language_code)
    except:
        pass
    try:
        Language.objects.create(code=destination_language_code)
    except:
        pass


def list_subtitle_directory():
    subtitles_folder = 'assets/subtitles'
    folder_names = os.listdir(subtitles_folder)
    result = []
    for folder in folder_names:
        subtitles_path = os.path.join(subtitles_folder, folder)
        files = os.listdir(subtitles_path)
        if files:
            files = [os.path.join(subtitles_path, f) for f in files]
            result.append(files)
    return result


def init_movie(subtitle_pair):
    movie_title = subtitle_pair[0].split('/')[2]
    try:
        Movie.objects.create(title=movie_title)
    except:
        pass


def init_subtitle(subtitle_pair):
    movie_title = subtitle_pair[0].split('/')[2]
    movie = Movie.objects.get(title=movie_title)
    for subtitle in subtitle_pair:
        language_code = subtitle.split('/')[3].split('.')[-2]
        language = Language.objects.get(code=language_code)
        subtitle_object = Subtitle.objects.filter(language=language, movie=movie)
        if not subtitle_object:
            Subtitle.objects.create(language=language, movie=movie)


def init_dialogues(subtitle_pair):
    movie_title = subtitle_pair[0].split('/')[2]
    movie = Movie.objects.get(title=movie_title)
    for subtitle_path in subtitle_pair:
        language_code = subtitle_path.split('/')[3].split('.')[-2]
        language = Language.objects.get(code=language_code)
        subtitle_object = Subtitle.objects.get(language=language, movie=movie)
        try:
            store_dialogues(subtitle_object, subtitle_path)
        except Exception as e:
            print movie_title, e


def store_dialogues(subtitle_object, subtitle_path):
    f = open(subtitle_path)
    buffer_line = ''
    index = 0

    for l in f:
        decoded_line = l.decode(guess_encoding(l)).encode('utf-8').strip()
        try:
            int(decoded_line)
            continue
        except:
            pass
        if '-->' in decoded_line:
            start_time, end_time = decoded_line.split('-->')
            continue
        if len(decoded_line) == 0:
            Dialogue.objects.create(subtitle=subtitle_object, content=buffer_line, index=index,
                                    start_time=start_time.split(',')[0],
                                    end_time=end_time.split(',')[0])
            # print buffer_line
            buffer_line = ''
            index += 1
        else:
            decoded_line = remove_tags(decoded_line)
            decoded_line = re.sub(r'\(.*\)', '', decoded_line).strip()
        if buffer_line:
            buffer_line += ' ' + decoded_line
        else:
            buffer_line = decoded_line


def remove_tags(text):
    return TAG_RE.sub('', text)


def guess_encoding(content):
    # always try utf-8 first
    encodings = ['utf-8', 'windows-1256']
    # try to decode
    for encoding in encodings:
        try:
            content.decode(encoding)
        except UnicodeDecodeError:
            pass
        else:
            return encoding
    # fallback on chardet
    encoding = chardet.detect(content)['encoding']
    return encoding
