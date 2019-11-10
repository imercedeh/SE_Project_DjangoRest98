from rest_framework.permissions import BasePermission


class IsLeaderOrReadOnly(BasePermission):
    def has_object_permission(self,request,view,obj):
        return obj.leader == request.user