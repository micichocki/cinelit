from rest_framework import serializers
from books.models import Book, Author
from tracker.models import Genre
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

    def create(self, validated_data):
        genre_data = validated_data.pop('genre')
        authors_data = validated_data.pop('authors')

        book = Book.objects.filter(title=validated_data['title']).first()
        if book:
            return book

        genre, created = Genre.objects.get_or_create(**genre_data)

        authors = []
        for author_data in authors_data:
            author, created = Author.objects.get_or_create(**author_data)
            authors.append(author)

        book = Book.objects.create(genre=genre, **validated_data)
        book.authors.set(authors)
        return book