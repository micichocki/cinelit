from rest_framework import serializers
from films.models import WatchingSession
from films.serializers.films_serializer import FilmSerializer
from tracker.serializers.UserSerializer import UserSerializer


class WatchingSessionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    film = FilmSerializer(read_only=True)

    class Meta:
        model = WatchingSession
        fields = ['id', 'user', 'film', 'start_date', 'end_date', 'watching_time']
