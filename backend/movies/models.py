from django.db import models


class Movie(models.Model):
    movie_id = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    youtube_trailer_url = models.CharField(max_length=200)
    release_date = models.DateField()
