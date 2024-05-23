from rest_framework import serializers
from django.contrib.auth import get_user_model
from books.models import ReadingSession
from films.models import WatchingSession
from tracker.serializers.UserSerializer import UserSerializer
from books.serializers import ReadingSessionSerializer
from films.serializers import WatchiSessionSerializer
from books.serializers import BookSerializer


class SessionsSerializer(serializers.Serializer):
    WatchingSessions = WatchingSessionSerializer(many=True)
    ReadingSessions = ReadingSessionSerializer(many=True)
