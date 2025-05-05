from rest_framework import permissions

class OwnerPermission(permissions.BasePermission):
    
    def has_permission(self, request, view):
        user = request.user

        if user.is_owner:
            return True
        else:
            return False

class AdminPermission(permissions.BasePermission):
    
    def has_permission(self, request, view):
        user = request.user
        
        if user.is_owner or user.is_admin:
            return True
        else:
            return False