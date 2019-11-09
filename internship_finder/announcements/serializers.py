from rest_framework import serializers

from .models import Announcement, Application


class AnnouncementSerializer(serializers.ModelSerializer):
    location = serializers.CharField(source='office.address_text', read_only=True)

    class Meta:
        model = Announcement
        fields = (
            'id',
            'title',
            'description',
            'company',
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
