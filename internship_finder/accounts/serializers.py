from django.utils.translation import gettext as _
from rest_framework import serializers

from internship_finder.companies.models import Company
from internship_finder.companies.serializers import CompanySerializer
from internship_finder.tags.models import Tag
from internship_finder.tags.serializers import TagSerializerField
from .models import User, StudentProfile


class ProfileSerializer(serializers.ModelSerializer):
    followed_tags = TagSerializerField()

    class Meta:
        model = StudentProfile
        fields = (
            'github_profile',
            'linkedin_profile',
            'major',
            'followed_tags',
        )

    def update(self, instance, validated_data):
        tags = validated_data.pop('followed_tags')
        instance = super().update(instance, validated_data)

        instance.followed_tags.clear()
        for tag_name in tags:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            instance.followed_tags.add(tag)
        return instance


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
        tags = profile_data.pop('tags')

        user = User.objects.create_user(**validated_data, user_type=User.STUDENT_TYPE)

        profile = StudentProfile.objects.create(user=user, **profile_data)
        for tag_name in tags:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            profile.followed_tags.add(tag)

        return user


class CompanyRegistrationSerializer(RegistrationSerializer):
    company = CompanySerializer(write_only=True)

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
