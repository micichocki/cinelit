from rest_framework import serializers
from films.models import Actor, Director, Film
from tracker.serializers.GenreSerializer import GenreSerializer


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'first_name', 'last_name', 'description']


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'first_name', 'last_name', 'description']


class FilmSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    directors = DirectorSerializer(many=True)
    actors = ActorSerializer(many=True)

    class Meta:
        model = Film
        fields = ['id', 'title', 'released', 'poster', 'genre', 'directors', 'actors', 'length', 'plot']
