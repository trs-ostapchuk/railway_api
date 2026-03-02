from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user model for the Railway Management System.

    Extends Django's AbstractUser and adds role-based access control
    to differentiate between admins, managers, and customers.
    """

    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("manager", "Manager"),
        ("customer", "Customer")
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="customer"
    )

    created_at = models.DateTimeField(auto_now_add=True)
