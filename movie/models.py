# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from django.contrib.postgres.fields import ArrayField
from multiselectfield import MultiSelectField

class Movie(models.Model):
    action = 'action'
    drama = 'drama'
    comedy = 'comedy'
    genres = [(action, 'action'), (drama, 'drama'), (comedy,'comedy')]
    egypt = 'eg'
    america = 'us'
    france = 'fr'
    countries = [(egypt,'egypt'), (america,'america'), (france,'france')]
    title = models.CharField(max_length=100)
    #genre = models.ArrayField(max_length=100, choices=genres, default=action)
    genre = MultiSelectField(choices=genres,default=action)
    #lang = models.CharField(max_length=100, choices=languages, default=arabic)
    country = models.CharField(max_length=100, choices=countries, default=egypt)
    #pic = models.ImageField(default='default.jpg', upload_to='profile_pics')
    watched = models.BooleanField(default=False)
    link = models.CharField(max_length=100)
    #Actor = models.ManyToManyField(Actor)
    overview = models.TextField(max_length=100)
    vote_count = models.IntegerField(null=True)
    vote_average = models.FloatField(max_length=100,null=True)
    release_date = models.DateField(max_length=100,null=True)
    lang = models.CharField(max_length=100)
    img = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.title

class Actor(models.Model):
    name = models.CharField(max_length=100)
    Movie = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name
