from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books.views.books import BookViewSet, AuthorViewSet
from books.views.reading_sessions import ReadingSessionViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'users/(?P<user_id>\d+)/reading_sessions', ReadingSessionViewSet, basename='user-reading-sessions')

urlpatterns = [
    path('api/', include(router.urls)),
]
