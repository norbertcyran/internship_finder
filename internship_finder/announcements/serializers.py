from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from internship_finder.companies.models import Company
from internship_finder.companies.serializers import ShortCompanySerializer
from internship_finder.tags.models import Tag
from internship_finder.tags.serializers import TagSerializerField
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
    tags = TagSerializerField()

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
            'tags',
        )
        extra_kwargs = {'office': {'write_only': True}}

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        announcement = super().create(validated_data)
        for tag_name in tags:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            announcement.tags.add(tag)
        return announcement

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags')
        instance = super().update(instance, validated_data)
        instance.tags.clear()
        for tag_name in tags:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            instance.tags.add(tag)
        return instance


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
