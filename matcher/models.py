from mongoengine import *

from subtitles.models import Language

connect('dialogue')


class SentencePair(Document):
    source_language = ReferenceField(Language)
    source_sentence = StringField(max_length=5000)
    destination_language = ReferenceField(Language)
    destination_sentence = StringField(max_length=5000)
    occurrence = FloatField()
    meta = {'db_alias': 'default'}
