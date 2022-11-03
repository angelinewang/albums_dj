from django.db import models
from artists.models import Artist

# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=250)
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT)
    release_year = models.IntegerField()

    def __str__(self):
        return self.title
