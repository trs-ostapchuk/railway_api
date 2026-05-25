from django.core.exceptions import ValidationError
from django.db import models


class Journey(models.Model):
    """
    Represents a scheduled train journey.
    """

    STATUS_CHOICES = (
        ("scheduled", "Scheduled"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    )

    route = models.ForeignKey(
        "stations.Route",
        on_delete=models.CASCADE,
        related_name="journeys",
        help_text="Route assigned to the journey."
    )

    train = models.ForeignKey(
        "trains.Train",
        on_delete=models.CASCADE,
        related_name="journeys",
        help_text="Train assigned to the journey."
    )

    crew = models.ManyToManyField(
        "trains.Crew",
        related_name="journeys",
        blank=True,
        help_text="Crew members assigned to the journey."
    )

    departure_time = models.DateTimeField(
        help_text="Departure date and time."
    )

    arrival_time = models.DateTimeField(
        help_text="Arrival date and time."
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="scheduled",
        help_text="Current journey status."
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["departure_time"]
        indexes = [
            models.Index(fields=["departure_time"]),
            models.Index(fields=["status"]),
        ]

    def clean(self):
        """
        Validates journey business logic.
        """

        if self.arrival_time <= self.departure_time:
            raise ValidationError(
                {
                    "arrival_time":
                        "Arrival time must be later than departure time."
                }
            )

    def duration(self):
        """
        Returns journey duration.
        """
        return self.arrival_time - self.departure_time

    def __str__(self):
        return (
            f"{self.route} | "
            f"{self.departure_time.strftime('%Y-%m-%d %H:%M')}"
        )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
