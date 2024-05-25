from books.serializers.user_book_stat_serializer import UserBookStatSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from films.serializers.film_stat_serializer import UserFilmStatSerializer
from rest_framework import status, viewsets, mixins
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from books.models import ReadingSession, Book, UserBookStat
from books.serializers.books_serializer import BookSerializer
from books.serializers.reading_session_serializer import ReadingSessionSerializer
from films.models import WatchingSession, Film, UserFilmStat

from films.serializers.films_serializer import FilmSerializer
from films.serializers.watching_session_serializer import WatchingSessionSerializer
from tracker.serializers.GenreSerializer import GenreSerializer
from .models import Genre, UserStat
from .serializers.CollectionSerializer import CollectionSerializer
from .serializers.UserSerializer import UserSerializer, UserLoginSerializer, UserRegisterSerializer, UserStatSerializer
from .serializers.UserSessionSerializer import AddSessionSerializer

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

    def list(self, request, user_pk=None, *args, **kwargs):
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


class UserItemStatViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            item_id = self.kwargs.get('item_id')
            if Book.objects.filter(id=item_id).exists():
                return UserBookStatSerializer
            else:
                return UserFilmStatSerializer

    def get_object(self):
        user_pk = self.kwargs['user_pk']
        item_id = self.kwargs['item_id']
        try:
            return get_object_or_404(UserBookStat, user_id=user_pk, book_id=item_id)
        except:
            return get_object_or_404(UserFilmStat, user_id=user_pk, film_id=item_id)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        if isinstance(instance, UserBookStat):
            serializer = UserBookStatSerializer(instance)
        else:
            serializer = UserFilmStatSerializer(instance)

        return Response(serializer.data)


class UserStatViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = UserStat.objects.all()
    serializer_class = UserStatSerializer

    def get_object(self):
        user_pk = self.kwargs['user_pk']
        return get_object_or_404(UserStat, user_id=user_pk)


@swagger_auto_schema(method='post', request_body=AddSessionSerializer)
@api_view(['POST'])
def add_session(request, user_pk):
    user = get_object_or_404(User, id=user_pk)
    serializer = AddSessionSerializer(data=request.data)
    item_id = request.data.get('item_id')
    film = Film.objects.filter(id=item_id)
    if film.exists():
        ws = WatchingSession()
        ws.user = user
        ws.film = film.get()
        ws.start_date = request.data.get('start_date')
        ws.end_date = request.data.get('end_date')
        ws.watching_time = request.data.get('watching_time')
        ws.save()
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    book = Book.objects.filter(id=item_id)
    if book.exists():
        rs = ReadingSession()
        rs.user = user
        rs.book = book.get()
        rs.start_date = request.data.get('start_date')
        rs.end_date = request.data.get('end_date')
        rs.duration = request.data.get('duration')
        rs.pages_read = request.data.get('pages_read')
        rs.save()
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_session(request, user_pk, item_id):
    user = get_object_or_404(User, id=user_pk)
    watching_sessions = WatchingSession.objects.filter(user=user, film_id=item_id)
    if watching_sessions.exists():
        serializer = WatchingSessionSerializer(watching_sessions, many=True)
        return Response(serializer.data)

    reading_sessions = ReadingSession.objects.filter(user=user, book_id=item_id)
    if reading_sessions.exists():
        serializer = ReadingSessionSerializer(reading_sessions, many=True)
        return Response(serializer.data)

    return Response({'detail': 'No session found'}, status=404)


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
