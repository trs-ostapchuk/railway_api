from rest_framework import serializers
from .models import Journey


class JourneySerializers(serializers.ModelSerializer):

    class Meta:
        model = Journey
        fields = [
            "id",
            "route",
            "train",
            "crew",
            "departure_time",
            "arrival_time",
            "status",
            "created_at"
        ]
