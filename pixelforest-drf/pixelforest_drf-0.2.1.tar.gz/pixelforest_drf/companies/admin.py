# Imports ##############################################################################################################
from django.contrib import admin

from .models import CompanyGroup, Company, Subsidiary, Service


# Admin generator ######################################################################################################

def inline_generator(cls):
    """ Generate a simple administration inline with the correct model """
    class GenericInlineAdmin(admin.TabularInline):
        model = cls
        extra = 0

    return GenericInlineAdmin


def admin_generator(cls):
    """ Generate an administration panel  """
    inline_class = None
    fk_links = []

    if cls == CompanyGroup:
        inline_class = inline_generator(Company)
    elif cls == Company:
        inline_class = inline_generator(Subsidiary)
        fk_links = [
            'company_group',
        ]
    elif cls == Subsidiary:
        inline_class = inline_generator(Service)
        fk_links = [
            'company',
            'company__company_group',
        ]
    elif cls == Service:
        fk_links = [
            'subsidiary',
            'subsidiary__company',
            'subsidiary__company__company_group',
        ]

    class Admin(admin.ModelAdmin):
        inlines = [inline_class] if inline_class else []

        list_display = [
            'name',
            'abbreviation',
            ] + ([fk_links[0]] if fk_links else []) + [
            'logo',
            'is_active',
            'last_update',
            'created_at',
        ]

        list_filter = ['is_active'] + fk_links

    return Admin


# Register models ######################################################################################################
admin.site.register(CompanyGroup, admin_generator(CompanyGroup))
admin.site.register(Company, admin_generator(Company))
admin.site.register(Subsidiary, admin_generator(Subsidiary))
admin.site.register(Service, admin_generator(Service))
