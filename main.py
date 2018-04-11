from corpus.generator import generate_parallel_corpus

import sys

from downloader.main import download_synchronized_subtitles
from matcher.main import match_sentence_pairs
from subtitles.main import store_dialogues_in_db


def main(source_language_code, destination_language_code):
    print 'parallel corpus generator'
    # download_synchronized_subtitles(source_language_code, destination_language_code)
    # store_dialogues_in_db(source_language_code, destination_language_code)
    match_sentence_pairs(source_language_code, destination_language_code)
    generate_parallel_corpus(source_language_code, destination_language_code)
    print 'done.'


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
