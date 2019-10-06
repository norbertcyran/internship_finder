from rest_framework import serializers

from .models import Company, Office


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office