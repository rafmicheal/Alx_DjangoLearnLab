from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: only owners (author) can edit or delete. Read-only for others.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS are read-only
        if request.method in permissions.SAFE_METHODS:
            return True

        # write permissions only to the author
        return getattr(obj, 'author', None) == request.user
