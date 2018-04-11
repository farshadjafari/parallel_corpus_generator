import os
from datetime import timedelta

from babelfish import Language
from subliminal import region, save_subtitles, Video, list_subtitles, download_subtitles, ProviderPool
from subliminal.cli import MutexLock


class FreePool(ProviderPool):
    def __init__(self):
        super(FreePool, self).__init__(providers=['podnapisi', 'shooter', 'thesubdb', 'tvsubtitles'])


def init_cache():
    cache_dir = 'cache'
    try:
        os.makedirs(cache_dir)
    except OSError:
        if not os.path.isdir(cache_dir):
            raise
    region.configure('dogpile.cache.dbm', expiration_time=timedelta(days=90),
                     arguments={'filename': os.path.join(cache_dir, 'cachefile.dbm'), 'lock_factory': MutexLock})


def get_subtitle_list(movie_title, source_language_code, destination_language_code):
    video = Video.fromname(movie_title)
    return list_subtitles([video],
                          {Language.fromalpha2(source_language_code), Language.fromalpha2(destination_language_code)},
                          FreePool)[video]


def download_single_subtitle(subtitle):
    download_subtitles([subtitle])


def save_on_disk(title, source_subtitle, destination_subtitle):
    try:
        os.makedirs('assets/subtitles/' + title)
    except:
        pass
    save_subtitles(Video.fromname(title), [source_subtitle, destination_subtitle],
                   directory='assets/subtitles/' + title)
