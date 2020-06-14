from django.db import models

# Create your models here.
class Genres(models.Model):
    genres=models.CharField(max_length=15)

    def __str__(self):
        return self.genres
class myMovie(models.Model):
    movieId=models.IntegerField()
    flag=models.BooleanField(False)

    def __str__(self):
        return str(self.movieId)
