from django.db import models
import uuid


class Offer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    member = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='offers')
    title = models.CharField(max_length=255)
    description = models.TextField()
    condition = models.CharField(max_length=255)
    reward = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    expires = models.DateTimeField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id', 'member'], name='unique_offer_per_member')
        ]

    def __str__(self):
        return self.title
