from django.db import models

class BarangWatchlist(models.Model):
    watched = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    rating = models.TextField()
    release_date = models.IntegerField()
    review = models.TextField()