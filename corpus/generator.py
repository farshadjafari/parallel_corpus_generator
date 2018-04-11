import codecs

import sys
from tqdm import tqdm

from matcher.models import Language, SentencePair


def generate_parallel_corpus(source_language, destination_language):
    source_language = Language.objects.get(code=source_language)
    destination_language = Language.objects.get(code=destination_language)
    sentence_pairs = SentencePair.objects.filter(source_language=source_language,
                                                 destination_language=destination_language)
    source_corpus = codecs.open('assets/corpora/dialogues.' + source_language.code, 'w', encoding='utf-8')
    destination_corpus = codecs.open('assets/corpora/dialogues.' + destination_language.code, 'w', encoding='utf-8')

    for sentence_pair in tqdm(sentence_pairs, desc='writing corpora'):
        source_corpus.write(sentence_pair.source_sentence + '\n')
        destination_corpus.write(sentence_pair.destination_sentence + '\n')

    source_corpus.close()
    destination_corpus.close()


if __name__ == "__main__":
    generate_parallel_corpus(sys.argv[1], sys.argv[2])
