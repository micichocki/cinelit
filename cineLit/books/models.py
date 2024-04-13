from django.db import models
from django.contrib.auth import get_user_model
from tracker.models import Genre

User = get_user_model()


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        unique_together = (('first_name', 'last_name'),)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(unique=True, max_length=255)
    cover = models.FileField(blank=True, null=True)
    released = models.DateField()
    genre = models.ForeignKey(Genre, models.DO_NOTHING)
    authors = models.ManyToManyField(Author)
    num_of_pages = models.IntegerField()
    plot = models.TextField(blank=True)

    def __str__(self):
        return f'{self.title}: {self.genre.genre_name}'


class ReadingSession(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    book = models.ForeignKey(Book, models.CASCADE)
    start_date = models.DateTimeField(help_text="Date time of reading session start")
    end_date = models.DateTimeField(help_text="Date time of reading session end", null=True)
    pages_read = models.IntegerField(blank=True)
    duration = models.IntegerField()

    def __str__(self):
        return f"Reading Session of '{self.book.title}' by {self.user.username}"

class UserBookStat(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    book = models.ForeignKey(Book, models.CASCADE)
    total_reading_time = models.IntegerField(blank=True)
    sessions_count = models.IntegerField(blank=True)
    pages_read_count = models.IntegerField(blank=True)
    last_session_end = models.DateTimeField(help_text="Datetime of the end of last reading session", null=True)
    reading_speed = models.DecimalField(max_digits=5, decimal_places=5, help_text='Reading speed in pages per minute')

    def __str__(self):
        return f"User: {self.user.username}, Book: {self.book.title}"

    class Meta:
        unique_together = (('user', 'book'),)

    def update_stats(self):
        total_time = ReadingSession.objects.filter(user=self.user, book=self.book).aggregate(total_time=Sum('reading_time'))['total_time']
        self.total_reading_time = total_time if total_time else 0

        sessions_count = ReadingSession.objects.filter(user=self.user, book=self.book).count()
        self.sessions_count = sessions_count

        pages_read_count = ReadingSession.objects.filter(user=self.user, book=self.book).aggregate(pages_read_count=Sum('pages_read'))['pages_read_count']
        self.pages_read_count = pages_read_count if pages_read_count else 0

        last_session = ReadingSession.objects.filter(user=self.user, book=self.book).order_by('-end_date').first()
        self.last_session_end = last_session.end_date if last_session else None

        if total_time and pages_read_count:
            self.reading_speed = pages_read_count / total_time
        else:
            self.reading_speed = 0

    def save(self, *args, **kwargs):
        self.update_stats()
        super().save(*args, **kwargs)