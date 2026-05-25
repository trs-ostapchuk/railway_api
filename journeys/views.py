from rest_framework import viewsets
from .models import Journey
from .serializers import JourneySerializers


class JourneyViewSet(viewsets.ModelViewSet):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializers
