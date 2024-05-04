from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from books.serializers.reading_session_serializer import ReadingSessionSerializer
from books.models import ReadingSession


class ReadingSessionViewSet(viewsets.ModelViewSet):
    serializer_class = ReadingSessionSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        queryset = ReadingSession.objects.filter(user_id=user_id)
        return queryset
