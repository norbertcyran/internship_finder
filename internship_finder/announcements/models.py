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

    pay_range_bottom = models.IntegerField(
        null=True,
        blank=True
    )

    pay_range_top = models.IntegerField(
        null=True,
        blank=True
    )

    applicants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='applied_to'
    )
