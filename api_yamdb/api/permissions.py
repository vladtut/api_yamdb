from rest_framework import permissions


class IsRoleAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.is_admin or request.user.is_superuser)


class IsRoleModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.is_moderator)


class IsRoleUser(permissions.BasePermission):

    def has_permission(self, request, view, obj):
        return (request.user.is_authenticated and request.user.is_user)


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS

        # return obj.author == request.user
