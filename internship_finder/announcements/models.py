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

    applicants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='enrollments',
        through='Enrollment'
    )

    class Meta:
        ordering = ('-created',)


class Enrollment(TimeStampedModel):
    """Model representing single enrollment for an internship."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    announcement = models.ForeignKey(
        Announcement,
        on_delete=models.CASCADE
    )

    additional_message = models.TextField(blank=True, null=True)


class EnrollmentData(models.Model):
    pass
