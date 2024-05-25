from http import HTTPStatus

from films.serializers.film_stat_serializer import UserFilmStatSerializer
from prompt_toolkit.validation import ValidationError
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from films.models import Director, Film, UserFilmStat
from films.serializers.films_serializer import DirectorSerializer, FilmSerializer
from rest_framework.response import Response


class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class FilmViewSet(viewsets.GenericViewSet,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.CreateModelMixin):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        film = serializer.instance
        user.films.add(film)
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        user = request.user
        film_id = kwargs.get('id')
        film = Film.objects.get(id=film_id)
        if film is None:
            return ValidationError()
        user.books.remove(film)
        user.save()
        return Response(status=status.HTTP_200_OK)
