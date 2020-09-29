from rest_framework import permissions

from bothub.common.models import Repository
from .. import READ_METHODS
from .. import WRITE_METHODS


class RepositoryPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        authorization = obj.get_user_authorization(request.user)
        if request.method in READ_METHODS and not request.user.is_authenticated:
            return authorization.can_read

        if request.user.is_authenticated:
            if request.method in READ_METHODS:
                return authorization.can_read
            if request.method in WRITE_METHODS:
                return authorization.can_write
            return authorization.is_admin
        return False


class RepositoryInfoPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        authorization = obj.repository.get_user_authorization(request.user)
        if request.method in READ_METHODS and not request.user.is_authenticated:
            return authorization.can_read

        if request.user.is_authenticated:
            if request.method in READ_METHODS:
                return authorization.can_read
            if request.method in WRITE_METHODS:
                return authorization.can_write
            return authorization.is_admin
        return False


class RepositoryAdminManagerAuthorization(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        authorization = obj.repository.get_user_authorization(request.user)
        return authorization.is_admin


class RepositoryExamplePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        authorization = obj.repository_version_language.repository_version.repository.get_user_authorization(
            request.user
        )
        if request.method in READ_METHODS:
            return authorization.can_read
        return authorization.can_contribute


class RepositoryExampleTranslatorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            repository = Repository.objects.get(
                pk=request.auth.repository_version_language.repository_version.repository.pk
            )
            authorization = repository.get_user_authorization(request.user)

            if request.method in READ_METHODS:
                return authorization.can_read
            return authorization.can_contribute
        except Repository.DoesNotExist:
            return False
        except AttributeError:
            return False


class RepositoryEntityHasPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        authorization = obj.repository_version.repository.get_user_authorization(
            request.user
        )
        if request.method in READ_METHODS:
            return authorization.can_read
        if request.user.is_authenticated:
            if request.method in WRITE_METHODS:
                return authorization.can_write
            return authorization.is_admin
        return False


class RepositoryIntentPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        authorization = obj.repository_version.repository.get_user_authorization(
            request.user
        )
        if request.method in READ_METHODS:
            return authorization.can_read
        return authorization.can_contribute
