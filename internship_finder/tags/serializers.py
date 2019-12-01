from rest_framework.serializers import ModelSerializer

from internship_finder.tags.models import Tag


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
