from django.contrib import admin
from .models import Film, Director, WatchingSession, UserFilmStat


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'released', 'genre')
    list_filter = ('released', 'genre')
    search_fields = ('title',)


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(WatchingSession)
class WatchingSessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'film', 'start_date', 'end_date', 'watching_time')
    list_filter = ('user', 'film', 'start_date', 'end_date')


@admin.register(UserFilmStat)
class UserFilmStatAdmin(admin.ModelAdmin):
    list_display = ('user', 'film', 'total_watching_time', 'sessions_count', 'last_session_end')
    list_filter = ('user', 'film', 'last_session_end')
