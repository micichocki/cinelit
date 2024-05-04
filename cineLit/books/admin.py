from django.contrib import admin

from books.models import Author, Book, ReadingSession, UserBookStat


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'genre', 'get_authors']
    search_fields = ['title', 'genre']

    def get_authors(self, obj):
        return "\n".join([str(a) for a in obj.authors.all()])


@admin.register(ReadingSession)
class ReadingSessionAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'pages_read', 'start_date', 'end_date', 'duration']
    search_fields = ['user', 'book']


@admin.register(UserBookStat)
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
