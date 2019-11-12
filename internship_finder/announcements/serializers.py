from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from internship_finder.companies.models import Company
from internship_finder.companies.serializers import ShortCompanySerializer
from .models import Announcement, Application


class AnnouncementSerializer(serializers.ModelSerializer):
    location = serializers.CharField(source='office.address_text', read_only=True)
    company = ShortCompanySerializer(read_only=True)
    company_id = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(),
        write_only=True,
        label=_('Company'),
        source='company'
    )

    class Meta:
        model = Announcement
        fields = (
            'id',
            'title',
            'description',
            'company',
            'company_id',
            'location',
            'office',
            'paid',
            'pay_range_bottom',
            'pay_range_top',
        )
        extra_kwargs = {'office': {'write_only': True}}


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = (
            'id',
            'user',
            'full_name',
            'email',
            'cv',
            'additional_message',
        )
        extra_kwargs = {'user': {'read_only': True, 'required': False}}
