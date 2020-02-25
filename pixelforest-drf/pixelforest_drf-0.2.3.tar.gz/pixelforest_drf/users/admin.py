# Imports ##############################################################################################################
from django.contrib import admin
from django.contrib.auth import get_user_model, admin as auth_admin
from django.contrib.auth import forms as auth_forms

from .forms import UserWithCountriesLinkCreationFormMixin, UserWithLinkServiceCreationFormMixin
from .models import CountryUserMixin, CompaniesUserMixin, AbstractEmailUser

User = get_user_model()


# Admin ################################################################################################################

def admin_generator():
    """
    This method will generate a auth_admin.UserAdmin child class to use for your specific configuration
    It is based on your current user_model
    """
    # Get the MRO once
    mro = User.mro()

    # Use default values for a non Custom User
    add_user_form_mixins = []
    permissions_fields = ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)
    country_fieldsets = None
    service_fieldsets = None
    add_fields = ('email', 'first_name', 'last_name', 'password1', 'password2', )
    list_display_fields = ('email', 'first_name', 'last_name', 'is_staff',)
    ro_fields = []

    # If the User has a linked_countries method (aka is linked to the Countries application), modify the required fields
    if CountryUserMixin in mro:
        add_user_form_mixins += [UserWithCountriesLinkCreationFormMixin]
        country_fieldsets = ('Country Objects', {'fields': ('country', 'sub_region', 'region', )})
        add_fields += ('country', 'sub_region', 'region')
        list_display_fields += ('country', 'sub_region', 'region')

    if CompaniesUserMixin in mro:
        add_user_form_mixins += [UserWithLinkServiceCreationFormMixin]
        service_fieldsets = ('Service Objects', {'fields': ('service', )})
        add_fields += ('service', )
        list_display_fields += ('service', )

    if AbstractEmailUser in mro:
        ro_fields = ['created', 'created_by']

    # Create the creation form for this User
    class CreationForm(auth_forms.UserCreationForm, *add_user_form_mixins):
        pass

    class GeneratedUserAdmin(auth_admin.UserAdmin):
        """
        A UserAdmin class generated using the 'admin_generator' method.
        I t will adapt to the current User model and add the necessary fields
        """
        fieldsets = [
            (None, {'fields': ('email', 'password')}),
            ('Personal info', {'fields': ('first_name', 'last_name', 'phone')}),
            ('Permissions', {'fields': permissions_fields}),
            service_fieldsets,
            country_fieldsets,
            ('General Informations', {'fields': ('last_login', 'created', 'created_by')}),
        ]
        fieldsets = [elem for elem in fieldsets if elem is not None]
        limited_fieldsets = (
            (None, {'fields': ('email',)}),
            ('Personal info', {'fields': ('first_name', 'last_name')}),
            ('Important dates', {'fields': ('last_login', 'created')}),
        )
        add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': add_fields}),
        )
        form = auth_forms.UserChangeForm
        add_form = CreationForm
        change_password_form = auth_admin.AdminPasswordChangeForm
        list_display = list_display_fields
        list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
        search_fields = ('first_name', 'last_name', 'email')
        ordering = ('email',)
        filter_horizontal = ('groups', 'user_permissions',)
        readonly_fields = ['last_login'] + ro_fields

    return GeneratedUserAdmin


# Register Admin #######################################################################################################
admin.site.register(User, admin_generator())
