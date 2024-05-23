from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

from .models import Genre
from books.models import ReadingSession, UserBookStat, Book
from films.models import WatchingSession, Film, UserFilmStat
from .serializers.UserSerializer import UserSerializer, UserLoginSerializer, UserRegisterSerializer
from .serializers.CollectionSerializer import CollectionSerializer
from films.serializers.film_stat_serializer import UserFilmStatSerializer
from books.serializers.user_book_stat_serializer import UserBookStatSerializer
from books.serializers.books_serializer import BookSerializer
from films.serializers.films_serializer import FilmSerializer
from tracker.serializers.GenreSerializer import GenreSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CollectionSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class CollectionViewSet(viewsets.GenericViewSet,
                        mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = CollectionSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, user_pk=None):
        user = get_object_or_404(User, pk=user_pk)
        books = user.books.all()
        films = user.films.all()

        serialized_books = []
        serialized_films = []

        for book in books:
            is_readed = ReadingSession.objects.filter(book=book, user=user).exists()
            serialized_book = BookSerializer(book, context={'request': request}).data
            serialized_book['is_readed'] = is_readed
            serialized_books.append(serialized_book)

        for film in films:
            is_watched = WatchingSession.objects.filter(film=film, user=user).exists()
            serialized_film = FilmSerializer(film, context={'request': request}).data
            serialized_film['is_watched'] = is_watched
            serialized_films.append(serialized_film)

        return Response({'books': serialized_books, 'films': serialized_films}, status=status.HTTP_200_OK)


class BookCollectionViewSet(viewsets.GenericViewSet,
                            mixins.RetrieveModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, user_pk, id):
        user_book_stat = UserBookStat.objects.get(user_id=user_pk, book_id=id)
        serializer = UserBookStatSerializer(user_book_stat)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, user_pk, id):
        user = request.user
        book = Book.objects.get(id=id)
        if book is None:
            return ValidationError(detail='Not found', code=HTTPStatus.NOT_FOUND)
        user.books.remove(book)
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def add_to_collection(self, request, user_pk, id):
        user = get_object_or_404(User, id=user_pk)
        book = get_object_or_404(Book, id=id)
        user.books.add(book)
        user.save()
        serializer = self.get_serializer(book)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FilmCollectionViewSet(viewsets.GenericViewSet,
                            mixins.RetrieveModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.CreateModelMixin,

                            ):
    queryset = User.objects.all()
    serializer_class = FilmSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, user_pk, id):
        user_film_stat = UserFilmStat.objects.get(user_id=user_pk, film_id=id)
        serializer = UserFilmStatSerializer(user_film_stat)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, user_id, id):
        user = request.user
        film = Film.objects.get(id=id)
        if film is None:
            return ValidationError(detail='Not found', code=HTTPStatus.NOT_FOUND)
        user.books.remove(film)
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def add_to_collection(self, request, user_pk, id):
        user = get_object_or_404(User, id=user_pk)
        film = get_object_or_404(Film, id=id)
        user.film.add(film)
        user.save()
        serializer = self.get_serializer(film)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


@swagger_auto_schema(method='post', request_body=UserLoginSerializer)
@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response('Wrong password', status=status.HTTP_401_UNAUTHORIZED)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({'token': token.key, 'user': serializer.data})


@swagger_auto_schema(method='post', request_body=UserRegisterSerializer)
@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
