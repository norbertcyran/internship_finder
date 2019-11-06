from rest_framework import serializers

from .models import Company, Office


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = ('id', 'address', 'city', 'country', 'address_text')


class CompanySerializer(serializers.ModelSerializer):
    offices = OfficeSerializer(many=True, required=False)

    class Meta:
        model = Company
        fields = (
            'id',
            'name',
            'description',
            'website',
            'industry',
            'logo',
            'offices'
        )


class ShortCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'logo')


