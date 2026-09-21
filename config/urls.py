from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from stations.views import (
    RouteViewSet,
    StationViewSet,
    CityViewSet,
    CountryViewSet
)
from trains.views import (
    CrewViewSet,
    TrainTypeViewSet,
    TrainViewSet
)
from journeys.views import JourneyViewSet

router = DefaultRouter()

router.register(r"stations/routes", RouteViewSet, basename="route")
router.register(r"stations/stations", StationViewSet, basename="station")
router.register(r"stations/cities", CityViewSet, basename="city")
router.register(r"stations/countries", CountryViewSet, basename="country")

router.register(r"trains/crews", CrewViewSet, basename="crew")
router.register(r"trains/train-types", TrainTypeViewSet, basename="train-type")
router.register(r"trains/trains", TrainViewSet, basename="train")

router.register(r"journeys/journey", JourneyViewSet, basename="journey")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
]
