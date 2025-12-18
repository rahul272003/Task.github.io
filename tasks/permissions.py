from rest_framework.permissions import BasePermission

class IsAdminOrOwner(BasePermission):
    """
    Admin users can access all tasks.
    Normal users can access only their own tasks.
    """

    def has_object_permission(self, request, view, obj):
        # Admin group users
        if request.user.groups.filter(name='Admin').exists():
            return True

        # Owner can access own task
        return obj.owner == request.user
