from subliminal_downloader import download_single_subtitle, save_on_disk, get_subtitle_list


def download_movie_synchronized_subtitles(movie, source_language_code, destination_language_code):
    # get list of subs for 2 lang
    subtitles = get_subtitle_list(movie.title, source_language_code, destination_language_code)
    source_subtitles = [s for s in subtitles if s.language == source_language_code]
    destination_subtitles = [s for s in subtitles if s.language == destination_language_code]
    # find a synchronized subtitle pair
    first_try = True

    for source_subtitle in source_subtitles:
        if len(destination_subtitles) == 0:
            break

        download_single_subtitle(source_subtitle)

        if not source_subtitle.text:
            continue

        for destination_subtitle in destination_subtitles:

            if not destination_subtitle.text and first_try:
                download_single_subtitle(destination_subtitle)

            if not destination_subtitle.text:
                continue

            if is_syncd(source_subtitle, destination_subtitle):
                save_on_disk(movie.title, source_subtitle, destination_subtitle)
                movie.processed = True
                movie.found = True
                movie.save()
                return

        first_try = False

    movie.processed = True
    movie.found = False
    movie.save()


def is_syncd(source_subtitle, destination_subtitle):
    source_content = source_subtitle.text
    destination_content = destination_subtitle.text
    if source_content and destination_content:
        source_content = source_content.splitlines()
        destination_content = destination_content.splitlines()
    else:
        return False
    matched = 0
    not_matched = 0
    for line in source_content:
        if '-->' in line:
            if line in destination_content:
                matched += 1
            else:
                not_matched += 1
        if not_matched >= 500:
            return False
        if matched >= 500:
            return True
    return False

