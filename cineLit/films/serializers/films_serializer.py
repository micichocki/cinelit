from rest_framework import serializers
from films.models import Director, Film
from tracker.models import Genre
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

    def create(self, validated_data):
        genre_data = validated_data.pop('genre')
        directors_data = validated_data.pop('directors')

        film = Film.objects.filter(title=validated_data['title']).first()
        if film:
            return film

        genre, created = Genre.objects.get_or_create(**genre_data)

        directors = []
        for director_data in directors_data:
            director, created = Director.objects.get_or_create(**director_data)
            directors.append(director)

        film = Film.objects.create(genre=genre, **validated_data)
        film.directors.set(directors)
        return film
