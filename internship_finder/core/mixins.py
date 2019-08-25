from django.db import models


class TimestampedModel(models.Model):
    """Abstract model with timestamp fields."""
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
