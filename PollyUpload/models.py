from django.db import models


class TvSub(models.Model):
    name = models.CharField(max_length=150)
    season = models.IntegerField()
    episode = models.IntegerField()
    lang = models.CharField(max_length=2)


class MovieSub(models.Model):
    name = models.CharField(max_length=150)
    year = models.IntegerField()
    lang = models.CharField(max_length=2)
