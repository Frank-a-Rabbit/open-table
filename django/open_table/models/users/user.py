import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Unique identifier for the user
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    # Additional fields for the user
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)

    # Placeholder for a unique dashboard relationship
    dashboard = models.OneToOneField(
        'Dashboard',  # Dashboard model to be created later
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='user'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
