from django.contrib import admin

from books.models import Author, Book, Genre, ReadingSession, UserBookStat, Collection


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']

admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'get_authors']
    search_fields = ['title', 'genre']

    def get_authors(self, obj):
        return "\n".join([str(a) for a in obj.authors.all()])

admin.site.register(Book, BookAdmin)


class CollectionAdmin(admin.ModelAdmin):
    list_display = ['user', 'book']
    search_fields = ['user', 'book']

admin.site.register(Collection, CollectionAdmin)


class GenreAdmin(admin.ModelAdmin):
    list_display = ['genre_name']
    search_fields = ['genre_name']

admin.site.register(Genre, GenreAdmin)


class ReadingSessionAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'pages_read', 'start_date', 'end_date', 'duration']
    search_fields = ['user', 'book']

admin.site.register(ReadingSession, ReadingSessionAdmin)


class UserBookStatAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'book',
        'total_reading_time',
        'sessions_count',
        'pages_read_count',
        'last_session_end',
        'reading_speed'
    ]
    search_fields = ['user', 'book']

admin.site.register(UserBookStat, UserBookStatAdmin)
