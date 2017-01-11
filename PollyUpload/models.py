from django.db import models


class TvSub(models.Model):
    name = models.CharField(max_length=150)
    season = models.IntegerField()
    episode = models.IntegerField()
    lang = models.CharField(max_length=2)
    path = models.FileField(upload_to='uploads/tv/%Y/%m/%d', null=True)


class MovieSub(models.Model):
    name = models.CharField(max_length=150)
    year = models.IntegerField()
    lang = models.CharField(max_length=2)
    path = models.FileField(upload_to='uploads/movies/%Y/%m/%d', null=True)
