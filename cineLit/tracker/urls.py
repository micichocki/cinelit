from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import UserViewSet, GenreViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'genres', GenreViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('books/', include('books.urls')),
    path('films/', include('films.urls')),
    path('register', views.register),
    path('login', views.login),
]
