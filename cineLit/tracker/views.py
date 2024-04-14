from rest_framework import viewsets
from .serializers import UserSerializer, GenreSerializer
from django.contrib.auth import get_user_model
from .models import Genre

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
