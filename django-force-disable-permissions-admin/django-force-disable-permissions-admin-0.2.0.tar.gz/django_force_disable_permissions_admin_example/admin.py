from django.contrib import admin
from .models import Category
from .models import Book
from django_force_disable_permissions_admin.admin import DjagnoForceDisablePermissionsAdminMixin

class BookInline(admin.TabularInline):
    model = Book

class CategoryAdmin(DjagnoForceDisablePermissionsAdminMixin, admin.ModelAdmin):
    add_permission_enable_for_superuser = False
    delete_permission_enable_for_superuser = False
    change_permission_enable_for_superuser = False
    view_permission_enable_for_superuser = False
    force_disable_add_permission = True
    force_disable_delete_permission = True
    force_disable_change_permission = True
    force_disable_view_permission = False

    list_display = ["name"]
    inlines = [
        BookInline,
    ]

admin.site.register(Category, CategoryAdmin)
