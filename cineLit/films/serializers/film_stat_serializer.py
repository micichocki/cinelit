from rest_framework import serializers
from tracker.serializers.UserSerializer import UserSerializer
from films.models import UserFilmStat
from films.serializers.films_serializer import FilmSerializer


class UserFilmStatSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    film = FilmSerializer(read_only=True)

    class Meta:
        model = UserFilmStat
        fields = ['user', 'film', 'total_watching_time', 'sessions_count', 'last_session_end', 'user',
                  'film']

    def update(self, instance, validated_data):
        instance.total_watching_time = validated_data.get('total_watching_time', instance.total_watching_time)
        instance.sessions_count = validated_data.get('sessions_count', instance.sessions_count)
        instance.last_session_end = validated_data.get('last_session_end', instance.last_session_end)

        instance.update_stats()

        instance.save()
        return instance
