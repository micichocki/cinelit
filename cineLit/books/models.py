from django.db import models

class Authors(models.Model):
    author_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'authors'
        unique_together = (('first_name', 'last_name'),)


class Authorsbooks(models.Model):
    author = models.OneToOneField(Authors, models.DO_NOTHING, primary_key=True)  # The composite primary key (author_id, book_id) found, that is not supported. The first column is selected.
    book = models.ForeignKey('Books', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authorsbooks'
        unique_together = (('author', 'book'),)


class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(unique=True, max_length=255)
    num_of_pages = models.IntegerField()
    cover_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books'


class Booksgenres(models.Model):
    book = models.OneToOneField(Books, models.DO_NOTHING, primary_key=True)  # The composite primary key (book_id, genre_id) found, that is not supported. The first column is selected.
    genre = models.ForeignKey('Genres', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'booksgenres'
        unique_together = (('book', 'genre'),)


class Collections(models.Model):
    user = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, book_id) found, that is not supported. The first column is selected.
    book = models.ForeignKey(Books, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'collections'
        unique_together = (('user', 'book'), ('user', 'book'),)

class Genres(models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre_name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'genres'


class Readingsessions(models.Model):
    session_id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Books, models.DO_NOTHING)
    end_date = models.DateTimeField()
    pages_read = models.IntegerField()
    user = models.ForeignKey('Users', models.DO_NOTHING)
    duration = models.IntegerField()
    start_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'readingsessions'


class Userbookstats(models.Model):
    user = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, book_id) found, that is not supported. The first column is selected.
    book = models.ForeignKey(Books, models.DO_NOTHING)
    total_reading_time = models.IntegerField()
    sessions_count = models.IntegerField()
    pages_read_count = models.IntegerField()
    last_session_end = models.DateTimeField()
    reading_speed = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'userbookstats'
        unique_together = (('user', 'book'),)
