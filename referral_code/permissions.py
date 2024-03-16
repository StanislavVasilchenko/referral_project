from rest_framework import permissions


class IsReferralCodeOwner(permissions.BasePermission):
    message = 'You don\'t have permission to perform this action'

    def has_object_permission(self, request, view, obj):
        return obj.user_owner == request.user
