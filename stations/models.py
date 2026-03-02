from django.db import models


class Country(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="The name of the country, e.g., 'Ukraine'"
    )

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(
        max_length=100,
        help_text="The name of the city, e.g., 'Lviv'"
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="cities",
        help_text="The country this city belongs to"
    )

    class Meta:
        unique_together = ("name", "country")

    def __str__(self):
        return f"{self.name} - {self.country.name}"


class Station(models.Model):
    """
    Represents a railway station with geographic coordinates.
    """

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
