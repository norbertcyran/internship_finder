import uuid

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField


def get_logo_path(instance: 'Company', filename: str):
    ext = filename.split('.')[-1]
    return f'companies/{instance.name.lower()}_{uuid.uuid4()}.{ext}'


class Company(models.Model):
    name = models.CharField(max_length=100)

    description = models.TextField()

    website = models.URLField(null=True, blank=True)

    industry = models.CharField(max_length=30)

    logo = models.ImageField(
        blank=True,
        null=True,
        upload_to=get_logo_path
    )

    verified = models.BooleanField(default=False)

    managers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='companies',
        help_text=_('Users with access to manage company page and offers.')
    )

    def __str__(self):
        return self.name

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

    country = CountryField()

    def __str__(self):
        return f'{self.company} - {self.address}, {self.city}, {self.country}'

    @property
    def address_text(self):
        return f'{self.address}, {self.city}'

