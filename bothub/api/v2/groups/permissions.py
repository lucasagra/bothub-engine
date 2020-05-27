from rest_framework import permissions

from .. import READ_METHODS, WRITE_METHODS


class RepositoryEntityGroupHasPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        authorization = obj.repository_version.repository.get_user_authorization(
            request.user
        )
        if request.method in READ_METHODS:
            return authorization.can_read  # pragma: no cover
        if request.user.is_authenticated:
            if request.method in WRITE_METHODS:
                return authorization.can_write
            return authorization.is_admin  # pragma: no cover
        return False  # pragma: no cover
