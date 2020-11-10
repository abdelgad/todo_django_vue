from rest_framework import permissions


class IsOwnerOrRefuse(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to CRUD it.
    """

    def has_object_permission(self, request, view, obj):
        if not bool(request.user and request.user.is_authenticated):
            return False
        return obj.owner == request.user
