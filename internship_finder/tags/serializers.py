import json

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from internship_finder.tags.models import Tag


class TagSerializerField(serializers.ListField):
    child = serializers.CharField()

    def to_representation(self, data):
        if not isinstance(data, list):
            tags = data.all()
            data = [tag.name for tag in tags]
        return data


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
