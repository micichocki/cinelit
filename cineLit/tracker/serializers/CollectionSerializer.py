from books.serializers.books_serializer import BookSerializer
from films.serializers.films_serializer import FilmSerializer
from films.serializers.film_stat_serializer import UserFilmStatSerializer
from films.serializers.watching_session_serializer import WatchingSessionSerializer
from rest_framework import serializers


class CollectionSerializer(serializers.Serializer):
    books = BookSerializer(many=True)
    films = FilmSerializer(many=True)

    class Meta:
        fields = ['books', 'films']


class FilmCollection(serializers.Serializer):
    films = FilmSerializer()
    watching_sessions = WatchingSessionSerializer(many=True)
    user_film_stat = UserFilmStatSerializer()
