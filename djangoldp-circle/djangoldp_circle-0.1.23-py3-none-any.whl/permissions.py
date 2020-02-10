from djangoldp.permissions import LDPPermissions
from django.db.models.base import ModelBase


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class CirclePermissions(LDPPermissions):
    def user_permissions(self, user, obj_or_model, obj=None):
        if not user.is_anonymous:
            if not isinstance(obj_or_model, ModelBase):
                obj = obj_or_model
            if obj:
                if obj.members.filter(user=user).exists():
                    if obj.members.filter(user=user).get().is_admin:
                        return ['view', 'add', 'change', 'delete']
                    else:
                        return ['view']
                elif obj.status != 'Public':
                    return []
                else:
                    return ['view', 'add']
            else:
                return ['view', 'add']

        return []
    
    def has_permission(self, request, view):
        if(get_client_ip(request) == '51.15.243.248'):
            return True

        return super().has_permission(request, view)
    
    def has_object_permission(self, request, view, obj):
        if(get_client_ip(request) == '51.15.243.248'):
            return True

        return super().has_object_permission(request, view, obj)


class CircleMemberPermissions(LDPPermissions):
    def user_permissions(self, user, obj_or_model, obj=None):

        if not user.is_anonymous:
            if not isinstance(obj_or_model, ModelBase):
                obj = obj_or_model
            if obj:
                if not hasattr(obj, 'user'):
                    return ['view', 'add']
                elif obj.user == user:
                    if obj.is_admin and obj.circle.members.filter(is_admin=True).count() == 1:
                        return ['view']
                    else:
                        if obj.circle.status == 'Public':
                            return ['view', 'add', 'delete']
                        else:
                            return ['view', 'delete']
                else:
                    if obj.circle.members.filter(user=user).exists():
                        if obj.circle.members.filter(user=user).get().is_admin:
                            if obj.is_admin:
                                return ['view', 'add']
                            else:
                                return ['view', 'add', 'delete']
                        else:
                            return ['view', 'add']
                    elif obj.circle.status != 'Public':
                        return []
                    else:
                        return ['view', 'add']
            else:
                return ['view', 'add']

        return []
    
    def has_permission(self, request, view):
        if(get_client_ip(request) == '51.15.243.248'):
            return True

        return super().has_permission(request, view)
    
    def has_object_permission(self, request, view, obj):
        if(get_client_ip(request) == '51.15.243.248'):
            return True

        return super().has_object_permission(request, view, obj)
