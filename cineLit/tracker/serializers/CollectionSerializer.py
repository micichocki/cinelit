from books.serializers.books_serializer import BookSerializer
from films.serializers.films_serializer import FilmSerializer
from rest_framework import serializers


class CollectionSerializer(serializers.Serializer):
    books = BookSerializer(many=True)
    films = FilmSerializer(many=True)

    class Meta:
        fields = ['books', 'films']
