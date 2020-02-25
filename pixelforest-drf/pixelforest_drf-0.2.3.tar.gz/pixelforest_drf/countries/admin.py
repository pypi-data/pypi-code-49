# Import ###############################################################################################################
from django.contrib import admin
from django.utils.html import mark_safe

from pixelforest_drf.utils.admin import NoDeleteModelAdminMixin, NoCreateModelAdminMixin, NoCreateInlineModelAdminMixin

from .models import Region, SubRegion, Country


# Inlines ##############################################################################################################

class CountryInline(admin.TabularInline, NoCreateInlineModelAdminMixin):
    model = Country
    can_delete = False

    fields = [
        'name',
        'iso_num',
        'iso_alpha_2',
        'iso_alpha_3',
        'is_active',
    ]

    readonly_fields = [
        'name',
        'iso_num',
        'iso_alpha_2',
        'iso_alpha_3',
    ]


class SubRegionInline(admin.TabularInline, NoCreateInlineModelAdminMixin):
    model = SubRegion

    fields = [
        'name',
        'abbreviation',
        'is_active',
    ]


# Admin classes ########################################################################################################

class RegionAdmin(admin.ModelAdmin):
    # Individual View
    inlines = [
        SubRegionInline
    ]

    fields = [
        ('name', 'abbreviation',),
        ('created_at', 'last_update',),
        'is_active',
    ]

    readonly_fields = [
        'last_update',
        'created_at',
    ]

    # List View
    list_display = [
        'name',
        'abbreviation',
        'is_active',
    ]

    list_filter = [
        'is_active',
    ]

    search_fields = [
        'name',
        'abbreviation',
    ]


class SubRegionAdmin(admin.ModelAdmin):
    # Individual View
    inlines = [
        CountryInline
    ]

    fields = [
        ('name', 'abbreviation',),
        'region',
        ('created_at', 'last_update',),
        'is_active',
    ]

    readonly_fields = [
        'last_update',
        'created_at',
    ]

    # List View
    list_display = [
        'name',
        'abbreviation',
        'region',
        'is_active',
    ]

    list_filter = [
        'region',
        'is_active',
    ]

    list_select_related = [
        'region',
    ]

    search_fields = [
        'name',
        'abbreviation',
    ]


class CountriesAdmin(NoDeleteModelAdminMixin, NoCreateModelAdminMixin):
    # Custom fields
    def flag_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(url=obj.flag.url,
                                                                                      width=100,
                                                                                      height=70))

    # Individual View
    fields = [
        ('name', 'iso_alpha_2', 'iso_alpha_3', 'iso_num',),
        'sub_region',
        ('flag_image', 'flag',),
        ('created_at', 'last_update',),
        'is_active',
    ]

    readonly_fields = [
        'name',
        'flag_image',
        'iso_num',
        'iso_alpha_2',
        'iso_alpha_3',
        'last_update',
        'created_at',
    ]

    # List View
    list_display = [
        'name',
        'iso_alpha_2',
        'sub_region',
        'is_active',
    ]

    list_filter = [
        'sub_region__region',
        'sub_region',
        'is_active',
    ]

    list_select_related = [
        'sub_region__region',
        'sub_region',
    ]

    search_fields = [
        'name',
        'iso_num',
        'iso_alpha_2',
        'iso_alpha_3',
    ]


# Admin registering ####################################################################################################

admin.site.register(Region, RegionAdmin)
admin.site.register(SubRegion, SubRegionAdmin)
admin.site.register(Country, CountriesAdmin)
