# -*- coding: UTF-8 -*-
import logging

import re
from functools import partial

from models import SentencePair
from subtitles.models import Dialogue

logger = logging.getLogger(__name__)
from multiprocessing.dummy import Pool as ThreadPool


def match_dialogues(source_subtitle, destination_subtitle):
    source_dialogues = Dialogue.objects.filter(subtitle=source_subtitle, found=False).order_by('index')
    destination_dialogues = Dialogue.objects.filter(subtitle=destination_subtitle, found=False).order_by('index')

    match_dialogue_arg_filled = partial(match_dialogue, destination_dialogues=destination_dialogues)
    pool = ThreadPool(16)
    pool.map(match_dialogue_arg_filled, source_dialogues)


def match_dialogue(source_dialogue, destination_dialogues):
    # time check
    try:
        destination_dialogue = destination_dialogues.get(start_time=source_dialogue.start_time,
                                                         end_time=source_dialogue.end_time)
    except:
        logger.info('not found syncd dialogue')
        return
    source_content = source_dialogue.content
    destination_content = destination_dialogue.content
    # break quotes
    source_quotes, destination_quotes = break_quotes(source_content, destination_content)
    for i in range(len(source_quotes)):
        # break sentences
        source_sentences, destination_sentences = break_sentences(source_quotes[i], destination_quotes[i])
        # store sentences
        for j in range(len(source_sentences)):
            SentencePair.objects.create(source_sentence=source_sentences[j],
                                        destination_sentence=destination_sentences[j],
                                        source_language=source_dialogue.subtitle.language,
                                        destination_language=destination_dialogue.subtitle.language)
            source_dialogue.update(found=True)
            destination_dialogue.update(found=True)


def break_quotes(source_content, destination_content):
    source_quotes = split_quotes(source_content)
    destination_quotes = split_quotes(destination_content)
    if len(source_quotes) == len(destination_quotes):
        return source_quotes, destination_quotes
    else:
        return [re.sub('-', ' ', source_content)], [re.sub('-', ' ', destination_content)]


def break_sentences(source_content, destination_content):
    source_sentences = split_sentence_endings(source_content)
    destination_sentences = split_sentence_endings(destination_content)
    if len(source_sentences) == len(destination_sentences):
        return source_sentences, destination_sentences
    else:
        return [re.sub('\.|\!|\?', ', ', source_content)], [re.sub('\.|\!|\?', ', ', destination_content)]


def split_quotes(content):
    return [x for x in content.split('-') if x]


def split_sentence_endings(content):
    return [x for x in re.split('\.|\!|\?', content) if x]
