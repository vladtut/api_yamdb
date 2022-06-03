from rest_framework import permissions

# admin


class IsRoleAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        return request.user.is_superuser
# moderator

# user
class IsRoleUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
