from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from . import views
from .views import (UserViewSet, GenreViewSet, CollectionViewSet,
                    add_session, get_session, UserItemStatViewSet, UserStatViewSet)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'genres', GenreViewSet)

users_router = NestedDefaultRouter(router, r'users', lookup='user')
users_router.register(r'collections', CollectionViewSet, basename='user-collections')
user_item_stat_detail = UserItemStatViewSet.as_view({'get': 'retrieve'})
user_stat_detail = UserStatViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include(users_router.urls)),
    path('', include('books.urls')),
    path('', include('films.urls')),
    path('register/', views.register),
    path('login/', views.login),
    path('api/users/<int:user_pk>/sessions/', add_session, name='add_session'),
    path('api/users/<int:user_pk>/sessions/<int:item_id>/', get_session, name='get_session'),
    path('api/users/<int:user_pk>/item/<int:item_id>/', user_item_stat_detail, name='user_item_stat_view'),
    path('api/users/<int:user_pk>/stats/', user_stat_detail, name='user_stat_view'),
]
