import sys
from tqdm import tqdm

from reader import init_languages, list_subtitle_directory, init_movie, init_subtitle, init_dialogues


def store_dialogues_in_db(source_language_code, destination_language_code):
    # create a db row for source destination language
    init_languages(source_language_code, destination_language_code)
    # read subtitle directory
    subtitle_pairs = list_subtitle_directory()
    # for each folder with subtitle pair
    for subtitle_pair in tqdm(subtitle_pairs, desc='storing dialogues'):
        # create a db rows for movie, subtitle, dialogues
        init_movie(subtitle_pair)
        init_subtitle(subtitle_pair)
        init_dialogues(subtitle_pair)


if __name__ == "__main__":
    store_dialogues_in_db(sys.argv[1], sys.argv[2])

