from rest_framework.permissions import BasePermission

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsAdminOrReadOnly(BasePermission):
    """
    Permission for Read-only or ManagerGroup
    """
    def has_permission(self, request, view):
        return bool(
            (request.user and request.user.is_authenticated)
            and (request.user.is_superuser or request.method in SAFE_METHODS)
        )
