import sys
from tqdm import tqdm

from matcher import match_dialogues
from subtitles.models import Language, Subtitle, Movie


def match_sentence_pairs(source_language_code, destination_language_code):
    source_language = Language.objects.get(code=source_language_code)
    destination_language = Language.objects.get(code=destination_language_code)
    movies = Movie.objects.all()
    for movie in tqdm(movies, desc='store sentence pairs'):
        try:
            source_subtitle = Subtitle.objects.get(language=source_language, movie=movie)
            destination_subtitle = Subtitle.objects.get(language=destination_language, movie=movie)
            match_dialogues(source_subtitle, destination_subtitle)
        except Exception as e:
            print movie.title, e


if __name__ == "__main__":
    match_sentence_pairs(sys.argv[1], sys.argv[2])
