from models import Movie

movies = Movie.objects.all()
print 'all videos: ', movies.count()
movies = movies.filter(movie_type='video.movie')
print 'all movies: ', movies.count()
movies = movies.filter(year__gte=1960)
print 'after 60`s movies: ', movies.count()
movies = movies.filter(rate__gte=6)
print 'rate gte 6: ', movies.count()
movies = movies.filter(duration__gte=3600)
print 'longer than 60 min: ', movies.count()

TYPE_LIMIT = 'video.movie'
YEAR_LIMIT = 1960
RATE_LIMIT = 6
DURATION_LIMIT = 3600
