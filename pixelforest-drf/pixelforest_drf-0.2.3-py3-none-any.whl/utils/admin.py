# Imports ##############################################################################################################
from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin


# Admin Mixins #########################################################################################################

class NoCreateModelAdminMixin(admin.ModelAdmin):
    """ Remove the create ability of the admin interface """
    def has_add_permission(self, request, obj=None):
        return False


class NoChangeModelAdminMixin(admin.ModelAdmin):
    """ Remove the change ability of the admin interface """
    def has_change_permission(self, request, obj=None):
        return False


class NoDeleteModelAdminMixin(admin.ModelAdmin):
    """ Remove the delete ability of the admin interface """
    def has_delete_permission(self, request, obj=None):
        return False


# Inline Mixins ########################################################################################################

class NoCreateInlineModelAdminMixin(InlineModelAdmin):
    """ Remove the create ability of the admin interface """
    def has_add_permission(self, request, obj=None):
        return False


class NoChangeInlineModelAdminMixin(InlineModelAdmin):
    """ Remove the change ability of the admin interface """
    def has_change_permission(self, request, obj=None):
        return False


# Admin models #########################################################################################################

class ReadOnlyModelAdmin(NoCreateModelAdminMixin, NoChangeModelAdminMixin, NoDeleteModelAdminMixin):
    """ Remove all abilities (create/change/delete) of the admin interface, making it readonly """
    pass
