from django.utils.translation import gettext as _
from rest_framework import serializers

from internship_finder.companies.models import Company
from internship_finder.companies.serializers import CompanySerializer
from .models import User, StudentProfile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = (
            'github_profile',
            'linkedin_profile',
            'major'
        )


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'full_name',
            'date_joined',
            'user_type',
            'is_active',
            'is_staff',
            'is_superuser',
            'profile',
        )

        read_only_fields = ('email', 'is_staff', 'is_superuser', 'date_joined')


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(_('Passwords are not the same!'))
        data = super().validate(attrs)
        data.pop('password2')
        return data


class StudentRegistrationSerializer(RegistrationSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
            'password2',
            'profile',
        )
        extra_kwargs = {'password': {'write_only': True, 'style': {'input_type': 'password'}}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')

        user = User.objects.create_user(**validated_data, user_type=User.STUDENT_TYPE)

        StudentProfile.objects.create(user=user, **profile_data)

        return user


class CompanyRegistrationSerializer(RegistrationSerializer):
    company = CompanySerializer()

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
            'password2',
            'company'
        )
        extra_kwargs = {'password': {'write_only': True, 'style': {'input_type': 'password'}}}

    def create(self, validated_data):
        company_data = validated_data.pop('company')

        user = User.objects.create_user(**validated_data, user_type=User.COMPANY_TYPE)

        company = Company.objects.create(**company_data)
        company.managers.add(user)

        return user
