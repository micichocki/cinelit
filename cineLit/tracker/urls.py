from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from . import views
from .views import UserViewSet, GenreViewSet, CollectionViewSet, FilmCollectionViewSet, BookCollectionViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'genres', GenreViewSet)

users_router = NestedDefaultRouter(router, r'users', lookup='user')
users_router.register(r'collections', CollectionViewSet, basename='user-collections')
users_router.register(r'films', FilmCollectionViewSet, basename='user-films')
users_router.register(r'books', BookCollectionViewSet, basename='user-books')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include(users_router.urls)),
    path('', include('books.urls')),
    path('', include('films.urls')),
    path('register/', views.register),
    path('login/', views.login),
]
