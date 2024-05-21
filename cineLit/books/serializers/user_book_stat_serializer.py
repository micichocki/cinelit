from rest_framework import serializers
from tracker.serializers.UserSerializer import UserSerializer
from books.models import UserBookStat
from books.serializers.books_serializer import BookSerializer


class UserBookStatSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    book = BookSerializer(read_only=True)

    class Meta:
        model = UserBookStat
        fields = ['user', 'film', 'total_reading_time', 'sessions_count', 'last_session_end', 'book']

    def update(self, instance, validated_data):
        instance.total_watching_time = validated_data.get('total_watching_time', instance.total_watching_time)
        instance.sessions_count = validated_data.get('sessions_count', instance.sessions_count)
        instance.last_session_end = validated_data.get('last_session_end', instance.last_session_end)

        instance.update_stats()

        instance.save()
        return instance
