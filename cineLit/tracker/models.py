from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import connection


class User(AbstractUser):
    books = models.ManyToManyField('books.Book', related_name='book_owners', blank=True)
    films = models.ManyToManyField('films.film', related_name='film_owners', blank=True)


class Genre(models.Model):
    genre_name = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return f"{self.genre_name}"


class CollectionItem(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            with connection.cursor() as cursor:
                cursor.execute("SELECT nextval('shared_sequence')")
                self.id = cursor.fetchone()[0]
                breakpoint()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
