from django.contrib import admin
from django.contrib.admin.options import BaseModelAdmin

class DjagnoForceDisablePermissionsAdminMixin(BaseModelAdmin):
    add_permission_enable_for_superuser = False
    delete_permission_enable_for_superuser = False
    change_permission_enable_for_superuser = False
    view_permission_enable_for_superuser = False
    force_disable_add_permission = False
    force_disable_delete_permission = False
    force_disable_change_permission = False
    force_disable_view_permission = False

    @classmethod
    def is_superuser(cls, request):
        if request.user and request.user.is_superuser:
            return True
        else:
            return False

    def has_add_permission(self, request):
        real_perm = super().has_add_permission(request)
        if self.add_permission_enable_for_superuser and self.is_superuser(request):
            return real_perm
        if self.force_disable_add_permission:
            return False
        else:
            return real_perm

    def has_delete_permission(self, request, obj=None):
        real_perm = super().has_delete_permission(request)
        if self.delete_permission_enable_for_superuser and self.is_superuser(request):
            return real_perm
        if self.force_disable_delete_permission:
            return False
        else:
            return real_perm

    def has_change_permission(self, request, obj=None):
        real_perm = super().has_change_permission(request)
        if self.change_permission_enable_for_superuser and self.is_superuser(request):
            return real_perm
        if self.force_disable_change_permission:
            return False
        else:
            return real_perm

    def has_view_permission(self, request, obj=None):
        real_perm = super().has_view_permission(request)
        if self.view_permission_enable_for_superuser and self.is_superuser(request):
            return real_perm
        if self.force_disable_view_permission:
            return False
        else:
            return real_perm
