import sys
from tqdm import tqdm

from downloader.subliminal_downloader import init_cache
from downloader.subtitle_pair_checker import download_movie_synchronized_subtitles
from movies.models import Movie

"""
movie list filters
"""
TYPE_LIMIT = 'video.movie'
YEAR_LIMIT = 1960
RATE_LIMIT = 6
DURATION_LIMIT = 3600


def download_synchronized_subtitles(source_language_code, destination_language_code):
    init_cache()

    movies = Movie.objects.filter(movie_type=TYPE_LIMIT,
                                  year__gte=YEAR_LIMIT,
                                  rate__gte=RATE_LIMIT,
                                  duration__gte=DURATION_LIMIT,
                                  processed=False)[:20]

    for movie in tqdm(movies, desc='downloading syncd subtitles'):
        try:
            download_movie_synchronized_subtitles(movie, source_language_code, destination_language_code)
        except Exception as e:
            print movie.title
            print e


if __name__ == "__main__":
    download_synchronized_subtitles(sys.argv[1], sys.argv[2])
