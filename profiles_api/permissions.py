from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit thier own profile"""
        if request.method in permission.SAFE_METHODS:
            return True

        return obj.id == request.user.id
