from django.urls import path, include
from rest_framework.routers import DefaultRouter
from films.views.films import FilmViewSet, DirectorViewSet, ActorViewSet
from films.views.watching_sessions import WatchingSessionViewSet

router = DefaultRouter()
router.register(r'films', FilmViewSet)
router.register(r'directors', ActorViewSet)
router.register(r'actors', DirectorViewSet)
router.register(r'users/(?P<user_id>\d+)/watching_sessions', WatchingSessionViewSet, basename='film-watching-sessions')

urlpatterns = [
    path('api/', include(router.urls)),
]
