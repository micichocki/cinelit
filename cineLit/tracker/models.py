from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    books = models.ManyToManyField('books.Book', related_name='book_owners', blank=True)
    films = models.ManyToManyField('films.film', related_name='film_owners', blank=True)


class Genre(models.Model):
    genre_name = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return f"{self.genre_name}"