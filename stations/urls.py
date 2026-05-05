from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RouteViewSet,
    StationViewSet,
    CityViewSet,
    CountryViewSet
)

router = DefaultRouter()
router.register(r'routes', RouteViewSet)
router.register(r'stations', StationViewSet)
router.register(r'cities', CityViewSet)
router.register(r'countries', CountryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
