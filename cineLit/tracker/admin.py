from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Genre
from books.models import Book
from films.models import Film


class BookInline(admin.TabularInline):
    model = Book.book_owners.through
    extra = 0


class FilmInline(admin.TabularInline):
    model = Film.film_owners.through
    extra = 0


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    inlines = [BookInline, FilmInline]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['genre_name']
    search_fields = ['genre_name']
