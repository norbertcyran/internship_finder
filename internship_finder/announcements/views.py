from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from internship_finder.accounts import permissions
from .serializers import AnnouncementSerializer, ApplicationSerializer
from .models import Announcement, Application


class AnnouncementViewSet(viewsets.ModelViewSet):

    def get_serializer_class(self):
        if self.action == 'apply':
            return ApplicationSerializer
        return AnnouncementSerializer

    def get_queryset(self):
        if self.action == 'recommended':
            return self.request.user.profile.get_recommended_announcements()
        return Announcement.objects.all()

    @action(detail=True, methods=['post'])
    def apply(self, request, pk=None):
        announcement = self.get_object()
        user = self.request.user
        user = user if user.is_authenticated else None

        application_serializer = self.get_serializer(data=self.request.data)
        application_serializer.is_valid(raise_exception=True)
        application_serializer.save(announcement=announcement)

        headers = self.get_success_headers(application_serializer.data)
        return Response(application_serializer.data, status=201, headers=headers)

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsStudent])
    def recommended(self, request, **kwargs):
        return self.list(request, **kwargs)


class ApplicationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        return Application.objects.filter(announcement=self.kwargs['announcement_pk'])
