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

from .models import Genre
from books.models import ReadingSession
from films.models import WatchingSession
from .serializers.UserSerializer import UserSerializer, UserLoginSerializer, UserRegisterSerializer
from .serializers.CollectionSerializer import CollectionSerializer
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

    @action(detail=True, methods=['get'])
    def collection(self, request, pk=None):
        user = self.get_object()
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


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


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


@swagger_auto_schema(method='post', request_body=UserLoginSerializer)
@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response('Wrong password', status=status.HTTP_401_UNAUTHORIZED)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({'token': token.key, 'user': serializer.data})
