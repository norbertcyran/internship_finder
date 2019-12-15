from rest_framework import permissions

from internship_finder.accounts.models import User


class OwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser is True or obj.user == request.user


class CanEditUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser is True or obj == request.user


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_anonymous and request.user.user_type == User.STUDENT_TYPE
