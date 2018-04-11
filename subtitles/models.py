from mongoengine import *

connect('dialogue')


class Language(Document):
    code = StringField(required=True, unique=True, max_length=4)
    meta = {'db_alias': 'default'}


class Movie(Document):
    title = StringField(unique=True, max_length=500)
    meta = {'db_alias': 'default'}


class Subtitle(Document):
    movie = ReferenceField(Movie, required=True)
    language = ReferenceField(Language, required=True)
    meta = {'db_alias': 'default'}


class Dialogue(Document):
    subtitle = ReferenceField(Subtitle)
    content = StringField(max_length=2000)
    index = IntField()
    start_time = StringField(max_length=2000)
    end_time = StringField(max_length=2000)
    found = BooleanField(default=False)
    meta = {'db_alias': 'default', 'indexes': [('subtitle', 'start_time', 'end_time')]}
