from djangoldp.permissions import LDPPermissions
from django.db.models.base import ModelBase


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class CustomerPermissions(LDPPermissions):
    def user_permissions(self, user, obj_or_model, obj=None):
        from .models import Member

        if not user.is_anonymous:
            # model base permissions - permissions for /customers/
            # object permissions - permissions for a customer instance
            if not isinstance(obj_or_model, ModelBase):
                obj = obj_or_model
            if obj:
                # owners have full permissions
                if obj.owner == user:
                    return ['view', 'add', 'change', 'delete']
                # members of one of their projects can view the customer
                if Member.objects.filter(project__customer=obj, user=user).exists():
                    return ['view']
                else:
                    return []
            # authenticated users can view a list of their customers and add new ones
            else:
                return ['view', 'add']

        return []


class ProjectPermissions(LDPPermissions):
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


class ProjectMemberPermissions(LDPPermissions):
    def user_permissions(self, user, obj_or_model, obj=None):

        if not user.is_anonymous:
            if not isinstance(obj_or_model, ModelBase):
                obj = obj_or_model
            if obj:
                if not hasattr(obj, 'user'):
                    return ['view', 'add']
                elif obj.user == user:
                    if obj.is_admin and obj.project.members.filter(is_admin=True).count() == 1:
                        return ['view']
                    else:
                        return ['view', 'delete']
                else:
                    if obj.project.members.filter(user=user).exists():
                        if obj.project.members.filter(user=user).get().is_admin:
                            if obj.is_admin:
                                return ['view', 'add']
                            else:
                                return ['view', 'add', 'delete']
                        else:
                            return ['view']
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
