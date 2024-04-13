from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Sum, Max
from tracker.models import Genre

User = get_user_model()

class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = (('first_name', 'last_name'),)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Director(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = (('first_name', 'last_name'),)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Film(models.Model):
    title = models.CharField(unique=True, max_length=255)
    released = models.DateField()
    poster = models.FileField(blank=True, null=True)
    genre = models.ForeignKey(Genre, models.DO_NOTHING)
    directors = models.ManyToManyField('films.Director', related_name='films', blank=True)
    actors = models.ManyToManyField('Actor', related_name='films', blank=True)
    length = models.IntegerField(help_text="The length of the film in minutes")
    plot = models.TextField(blank=True)


class WatchingSession(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    film = models.ForeignKey(Film, models.CASCADE)
    start_date = models.DateTimeField(help_text="Date time of watching session start")
    end_date = models.DateTimeField(help_text="Date time of watching session start")
    watching_time = models.IntegerField(blank=True,help_text="The number of minutes the user has watched")

    def __str__(self):
        return f"Reading Session of '{self.film.title}' by {self.user.username}"

class UserFilmStat(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    film = models.ForeignKey(Film, models.CASCADE)
    total_watching_time = models.IntegerField(blank=True, help_text="The number of minutes the user has watched totally")
    sessions_count = models.IntegerField(blank=True)
    last_session_end = models.DateTimeField()

    def __str__(self):
        return f"User: {self.user.username}, Film: {self.film.title}"

    class Meta:
        unique_together = (('user', 'film'),)

    def update_stats(self):
        total_time = WatchingSession.objects.filter(user=self.user, film=self.film).aggregate(total_time=Sum('watching_time'))['total_time']
        self.total_watching_time = total_time if total_time else 0

        sessions_count = WatchingSession.objects.filter(user=self.user, film=self.film).count()
        self.sessions_count = sessions_count

        last_session = WatchingSession.objects.filter(user=self.user, film=self.film).order_by('-end_date').first()
        self.last_session_end = last_session.end_date if last_session else None

    def save(self, *args, **kwargs):
        self.update_stats()
        super().save(*args, **kwargs)

