from platform import release
from django.db import models

class watchlist(models.Model):
    title = models.CharField(max_length=255)
    watched = models.TextField()
    rating = models.IntegerField()
    release_date = models.TextField()
    review = models.TextField()
# Create your models here.
