from django.core.management.base import BaseCommand
from django.core.management import call_command
from films.models import UserFilmStat
from books.models import UserBookStat

class Command(BaseCommand):
    # Usage: python manage.py load_fixtures
    # Description: Loads all fixtures and updates stats
    help = 'Loads all fixtures and updates stats'

    def handle(self, *args, **options):
        fixtures = [
            'tracker/fixtures/genre_fixtures',
            'tracker/fixtures/user_fixtures',
            'films/fixtures/actor_fixtures',
            'films/fixtures/director_fixtures',
            'films/fixtures/film_fixtures',
            'films/fixtures/user_film_stat_fixtures',
            'films/fixtures/watching_session_fixtures',
            'books/fixtures/author_fixtures',
            'books/fixtures/book_fixtures',
            'books/fixtures/user_book_stat_fixtures',
            'books/fixtures/reading_session_fixtures'
        ]

        for fixture in fixtures:
            try:
                call_command('loaddata', fixture)
                self.stdout.write(self.style.SUCCESS(f'Successfully loaded {fixture}'))
            except:
                self.stdout.write(self.style.ERROR(f'Failed to load {fixture}'))

        # Update stats for all UserFilmStat objects
        for user_film_stat in UserFilmStat.objects.all():
            user_film_stat.save()

        # Update stats for all UserBookStat objects
        for user_book_stat in UserBookStat.objects.all():
            user_book_stat.save()