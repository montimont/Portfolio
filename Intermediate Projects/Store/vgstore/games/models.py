from django.db import models
from django.utils import timezone

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=255, default='')
    platform = models.CharField(max_length=255, default='')
    release_year = models.IntegerField()
    publisher = models.CharField(max_length=255, default='')
    number_in_stock = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
