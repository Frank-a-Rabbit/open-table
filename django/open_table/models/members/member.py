from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid  # To generate unique IDs


class Member(AbstractUser):
    # Unique Identifier
    member_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    # Primary Contact Information
    primary_contact_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    primary_contact_fname = models.CharField(max_length=50)
    primary_contact_lname = models.CharField(max_length=50)
    primary_contact_primary_phone = models.CharField(max_length=15)  # E.g., "+1234567890"
    primary_contact_secondary_phone = models.CharField(max_length=15, blank=True, null=True)
    primary_contact_email = models.EmailField()

    # Business Information
    business_name = models.CharField(max_length=255)
    business_address = models.TextField()
    business_web_url = models.URLField(blank=True, null=True)

    # Menu Dissemination
    menu = models.TextField()  # Store the menu as structured data (e.g., JSON or plain text)

    # Offers
    offers = models.ManyToManyField(
        'Offer', blank=True, related_name='members'
    )  # Link to offers created by the member

    def __str__(self):
        return f"{self.business_name} ({self.primary_contact_fname} {self.primary_contact_lname})"
