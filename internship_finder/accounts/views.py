from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .permissions import CanEditUser
from .serializers import UserSerializer, StudentRegistrationSerializer, CompanyRegistrationSerializer
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (CanEditUser,)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def me(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed


class StudentRegistrationAPIView(CreateAPIView):
    serializer_class = StudentRegistrationSerializer
    queryset = User.objects.all()


class CompanyRegistrationAPIView(CreateAPIView):
    serializer_class = CompanyRegistrationSerializer
    queryset = User.objects.all()
