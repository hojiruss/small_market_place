from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == 'POST':
            return (
                    request.user.is_authenticated
                    and hasattr(request.user, 'profile')
                    and request.user.profile.role == 'seller'
            )
        return request.user and request.user.is_authenticated

    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.seller == request.user
