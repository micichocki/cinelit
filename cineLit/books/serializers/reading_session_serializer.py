from rest_framework import serializers
from books.models import ReadingSession
from books.serializers.books_serializer import BookSerializer
from tracker.serializers.UserSerializer import UserSerializer


class ReadingSessionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    book = BookSerializer(read_only=True)

    class Meta:
        model = ReadingSession
        fields = ['id', 'user', 'book', 'start_date', 'end_date', 'pages_read', 'duration']
