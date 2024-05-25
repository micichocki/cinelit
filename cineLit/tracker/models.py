from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import connection


class User(AbstractUser):
    books = models.ManyToManyField('books.Book', related_name='book_owners', blank=True)
    films = models.ManyToManyField('films.film', related_name='film_owners', blank=True)


class UserStat(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_reading_time = models.IntegerField(blank=True, null=True)
    total_sessions_count = models.IntegerField(blank=True, null=True)
    total_pages_read_count = models.IntegerField(blank=True, null=True)
    average_reading_speed = models.DecimalField(max_digits=5, decimal_places=5, blank=True, null=True)

    def __str__(self):
        return f"User: {self.user.username}"

    def update_stats(self):
        user_book_stats = UserBookStat.objects.filter(user=self.user)

        total_reading_time = user_book_stats.aggregate(total_time=Sum('total_reading_time'))['total_time']
        self.total_reading_time = total_reading_time if total_reading_time else 0

        total_sessions_count = user_book_stats.aggregate(total_sessions=Sum('sessions_count'))['total_sessions']
        self.total_sessions_count = total_sessions_count if total_sessions_count else 0

        total_pages_read_count = user_book_stats.aggregate(total_pages=Sum('pages_read_count'))['total_pages']
        self.total_pages_read_count = total_pages_read_count if total_pages_read_count else 0

        average_reading_speed = user_book_stats.aggregate(average_speed=Avg('reading_speed'))['average_speed']
        self.average_reading_speed = average_reading_speed if average_reading_speed else 0

    def save(self, *args, **kwargs):
        self.update_stats()
        super().save(*args, **kwargs)


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
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
