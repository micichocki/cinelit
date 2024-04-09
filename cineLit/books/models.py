from django.conf import settings
from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        unique_together = (('first_name', 'last_name'),)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(unique=True, max_length=255)
    num_of_pages = models.IntegerField()
    cover = models.FileField(blank=True, null=True)
    genre = models.ForeignKey('Genre', models.DO_NOTHING)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return f'{self.title}: {self.genre.genre_name}'

class Collection(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    book = models.ForeignKey(Book, models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Collection: {self.book.title}"

    class Meta:
        unique_together = (('user', 'book'),)

class Genre(models.Model):
    genre_name = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return f"{self.genre_name}"

class ReadingSession(models.Model):
    book = models.ForeignKey(Book, models.CASCADE)
    end_date = models.DateTimeField()
    pages_read = models.IntegerField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    duration = models.IntegerField()
    start_date = models.DateTimeField()

    def __str__(self):
        return f"Reading Session of '{self.book.title}' by {self.user.username}"

class UserBookStat(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    book = models.ForeignKey(Book, models.CASCADE)
    total_reading_time = models.IntegerField(blank=True)
    sessions_count = models.IntegerField(blank=True)
    pages_read_count = models.IntegerField(blank=True)
    last_session_end = models.DateTimeField()
    reading_speed = models.DecimalField(max_digits=5, decimal_places=5, help_text='Reading speed in pages per minute')

    def __str__(self):
        return f"User: {self.user.username}, Book: {self.book.title}"

    class Meta:
        unique_together = (('user', 'book'),)
