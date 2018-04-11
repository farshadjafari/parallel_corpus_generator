# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from mongoengine import *


register_connection('movie', 'movie')


class Movie(Document):
    title = StringField(required=True, unique=True, max_length=1000)
    words_in_title = StringField(required=True, unique=True, max_length=1000)
    movie_type = StringField(max_length=1000)
    rate = FloatField()
    duration = IntField()
    year = IntField()

    processed = BooleanField(default=False)
    found = BooleanField(default=False)
    meta = {'db_alias': 'movie'}
