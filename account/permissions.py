from rest_framework import permissions

class UserPermission(permissions.BasePermission):
    
    def has_permission(self, request, view):
        user = request.user

        if user.is_owner:
            print(user.is_owner)
            return True
        else:
            return False