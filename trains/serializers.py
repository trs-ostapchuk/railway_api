from rest_framework import serializers
from .models import (
    Crew,
    TrainType,
    Train
)


class TrainTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainType
        fields = ["id", "name"]


class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = ["id", "first_name", "last_name"]


class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = [
            "id",
            "name",
            "cargo_num",
            "places_in_cargo",
            "train_type"
        ]
