from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin

from internship_finder.tags.models import Tag
from internship_finder.tags.serializers import TagSerializer


class TagViewSet(viewsets.ReadOnlyModelViewSet, CreateModelMixin):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
