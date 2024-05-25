from rest_framework import serializers
from films.models import Director, Film
from tracker.serializers.GenreSerializer import GenreSerializer


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'first_name', 'last_name', 'description']


class FilmSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    directors = DirectorSerializer(many=True)

    class Meta:
        model = Film
        fields = ['id', 'title', 'released', 'poster', 'genre', 'directors', 'length', 'plot']
