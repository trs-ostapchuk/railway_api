from rest_framework import serializers
from .models import (
    Country,
    City,
    Station,
    Route
)


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ["id", "name"]


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["id", "name", "country"]


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ["id", "name", "city", "latitude", "longitude"]


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ["id", "source", "destination", "travel_time"]

    def validate(self, data):
        if data["source"] == data["destination"]:
            raise serializers.ValidationError("Source and destination cannot be the same station.")

        if Route.objects.filter(source=data["source"], destination=data["destination"]).exists():
            raise serializers.ValidationError("This route already exists.")

        return data
