from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField


class Company(models.Model):
    name = models.CharField(max_length=100)

    description = models.TextField()

    website = models.URLField(null=True, blank=True)

    industry = models.CharField(max_length=30)

    logo = models.ImageField(
        upload_to='companies',
        blank=True,
        null=True
    )

    verified = models.BooleanField(default=False)

    managers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='companies',
        help_text=_('Users with access to manage company page and offers.')
    )

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'companies'


class Office(models.Model):
    company = models.ForeignKey(
        Company,
        related_name='offices',
        on_delete=models.CASCADE
    )

    address = models.CharField(max_length=100)

    city = models.CharField(max_length=50)

    postal_code = models.CharField(max_length=20)

    country = CountryField()

