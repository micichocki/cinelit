from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import connection
from django.db.models import Sum, Avg


class User(AbstractUser):
    books = models.ManyToManyField('books.Book', related_name='book_owners', blank=True)
    films = models.ManyToManyField('films.film', related_name='film_owners', blank=True)


class UserStat(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_reading_time = models.IntegerField(blank=True, null=True)
    total_book_sessions_count = models.IntegerField(blank=True, null=True)
    total_film_sessions_count = models.IntegerField(blank=True, null=True)
    total_pages_read_count = models.IntegerField(blank=True, null=True)
    total_minutes_watched = models.IntegerField(blank=True, null=True)
    average_reading_speed = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"User: {self.user.username}"

    def update_stats(self):
        from books.models import UserBookStat

        user_book_stats = UserBookStat.objects.filter(user=self.user)

        total_reading_time = user_book_stats.aggregate(total_time=Sum('total_reading_time'))['total_time']
        self.total_reading_time = total_reading_time if total_reading_time else 0

        total_book_sessions_count = user_book_stats.aggregate(total_sessions=Sum('sessions_count'))['total_sessions']
        self.total_book_sessions_count = total_book_sessions_count if total_book_sessions_count else 0

        total_pages_read_count = user_book_stats.aggregate(total_pages=Sum('pages_read_count'))['total_pages']
        self.total_pages_read_count = total_pages_read_count if total_pages_read_count else 0

        average_reading_speed = user_book_stats.aggregate(average_speed=Avg('reading_speed'))['average_speed']
        self.average_reading_speed = average_reading_speed if average_reading_speed else 0

        from films.models import UserFilmStat

        user_film_stats = UserFilmStat.objects.filter(user=self.user)
        total_minutes_watched = user_film_stats.aggregate(total_minutes=Sum('total_watching_time'))['total_minutes']
        self.total_minutes_watched = total_minutes_watched if total_minutes_watched else 0

        total_film_sessions_count = user_film_stats.aggregate(total_sessions=Sum('sessions_count'))['total_sessions']
        self.total_film_sessions_count = total_film_sessions_count if total_film_sessions_count else 0

    def save(self, *args, **kwargs):
        self.update_stats()
        super().save(*args, **kwargs)


class Genre(models.Model):
    genre_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.genre_name}"


class CollectionItem(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            with connection.cursor() as cursor:
                cursor.execute("SELECT nextval('shared_sequence')")
                self.id = cursor.fetchone()[0]
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
