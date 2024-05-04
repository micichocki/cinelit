from rest_framework import serializers
from books.models import Book, Author
from tracker.serializers.GenreSerializer import GenreSerializer


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name']


class BookSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'cover', 'released', 'genre', 'authors', 'num_of_pages', 'plot']
