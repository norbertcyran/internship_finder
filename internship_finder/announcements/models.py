from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel


class Announcement(TimeStampedModel, TitleDescriptionModel):
    company = models.ForeignKey(
        'companies.Company',
        on_delete=models.CASCADE,
        related_name='announcements'
    )

    office = models.ForeignKey(
        'companies.Office',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True
    )

    paid = models.BooleanField()

    pay_range_bottom = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    pay_range_top = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.title} at {self.company}'

    class Meta:
        ordering = ('-created',)


class Application(TimeStampedModel):
    """Model representing single enrollment for an internship."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='applications'
    )

    announcement = models.ForeignKey(
        Announcement,
        on_delete=models.CASCADE,
        related_name='applications'
    )

    full_name = models.CharField(max_length=100)

    email = models.EmailField()

    cv = models.FileField()

    additional_message = models.TextField(blank=True, null=True)
