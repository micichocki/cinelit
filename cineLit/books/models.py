from django.contrib.auth.models import User
from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        unique_together = (('first_name', 'last_name'),)

class AuthorBook(models.Model):
    author = models.OneToOneField(Author, models.CASCADE, primary_key=True)
    book = models.ForeignKey('Book', models.DO_NOTHING)

    def __str__(self):
        return f"{self.author.first_name} {self.author.last_name}'s Book: {self.book.title}"

    class Meta:
        unique_together = (('author', 'book'),)

class Book(models.Model):
    title = models.CharField(unique=True, max_length=255)
    num_of_pages = models.IntegerField()
    cover = models.FileField(blank=True, null=True)
    authors = models.ManyToManyField(Author, through=AuthorBook)
    genre = models.ForeignKey('Genre', models.DO_NOTHING)

    def __str__(self):
        return f'{self.title}: {self.genre.genre_name}'

class Collection(models.Model):
    user = models.OneToOneField(User, models.CASCADE, primary_key=True)
    book = models.ForeignKey(Book, models.DO_NOTHING)

    def __str__(self):
        return f"{self.user.username}'s Collection: {self.book.title}"

    class Meta:
        unique_together = (('user', 'book'), ('user', 'book'),)

class Genre(models.Model):
    genre_name = models.CharField(unique=True, max_length=255)

class ReadingSession(models.Model):
    book = models.ForeignKey(Book, models.DO_NOTHING)
    end_date = models.DateTimeField()
    pages_read = models.IntegerField(blank=True)
    user = models.ForeignKey(User, models.CASCADE)
    duration = models.IntegerField()
    start_date = models.DateTimeField()

    def __str__(self):
        return f"Reading Session of '{self.book.title}' by {self.user.username}"

class UserBookStat(models.Model):
    user = models.OneToOneField(User, models.CASCADE, primary_key=True)
    book = models.ForeignKey(Book, models.DO_NOTHING)
    total_reading_time = models.IntegerField(blank=True)
    sessions_count = models.IntegerField(blank=True)
    pages_read_count = models.IntegerField(blank=True)
    last_session_end = models.DateTimeField()
    reading_speed = models.DecimalField(max_digits=5, decimal_places=5, help_text='Reading speed in pages per minute')

    def __str__(self):
        return f"User: {self.user.username}, Book: {self.book.title}"

    class Meta:
        unique_together = (('user', 'book'),)
