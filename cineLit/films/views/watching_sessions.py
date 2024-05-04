from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from films.serializers.watching_session_serializer import WatchingSessionSerializer
from films.models import WatchingSession


class WatchingSessionViewSet(viewsets.ModelViewSet):
    serializer_class = WatchingSessionSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        queryset = WatchingSession.objects.filter(user_id=user_id)
        return queryset
