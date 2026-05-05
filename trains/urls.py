from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CrewViewSet,
    TrainTypeViewSet,
    TrainViewSet
)

router = DefaultRouter()
router.register(r'crews', CrewViewSet)
router.register(r'train-types', TrainTypeViewSet)
router.register(r'trains', TrainViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
