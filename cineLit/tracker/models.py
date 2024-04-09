from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    books = models.ManyToManyField('books.Book', related_name='owners', blank=True)
