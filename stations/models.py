from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="cities"
    )

    class Meta:
        unique_together = ("name", "country")

    def __str__(self):
        return f"{self.name} - {self.country.name}"


class Station(models.Model):
    name = models.CharField(
        max_length=100,
        help_text="The name of the railway station"
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="stations",
        help_text="The city where this station is located"
    )
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
        help_text="Latitude of the station in decimal degrees"
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
        help_text="Longitude of the station in decimal degrees"
    )

    def __str__(self):
        return f"{self.name} - {self.city}"
