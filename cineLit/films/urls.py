from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FilmViewSet, DirectorViewSet, ActorViewSet

router = DefaultRouter()
router.register(r'films', FilmViewSet)
router.register(r'directors', ActorViewSet)
router.register(r'actors', DirectorViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
