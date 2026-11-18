
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    class Role(models.TextChoices):
        USER = "USER", "User"
        ADMIN = "ADMIN", "Administrator"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.USER
    )

    email = models.EmailField(
        max_length=255,
        unique=True,
        blank=False
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    contact_number = models.CharField(
        max_length=20,
        blank=True
    )

    def __str__(self):
        return self.username
