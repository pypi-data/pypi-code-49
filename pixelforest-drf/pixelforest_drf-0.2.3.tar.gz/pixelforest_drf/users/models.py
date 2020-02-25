# Imports ##############################################################################################################
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.postgres.fields import CIEmailField, CICharField

from phonenumber_field.modelfields import PhoneNumberField

from ..countries.models import Country, SubRegion, Region
from ..companies.models import Service
from .managers import UserAndDownIsActiveManager
from ..utils.models_mixins import UpAndDownIsActiveMixinWithoutManager


# Models ###############################################################################################################
class CompaniesUserMixin(models.Model):
    """
    Add a link to a company object to the user
    He must be linked to one service
    """
    service = models.ForeignKey(to=Service, blank=False, null=False, on_delete=models.PROTECT)

    class Meta:
        abstract = True


class CountryUserMixin(models.Model):
    """
    Add a link to a country object to the user
    He can be linked to zero or one Country, SubRegion or Region.
    """
    country = models.ForeignKey(to=Country, blank=True, null=True, on_delete=models.PROTECT)
    sub_region = models.ForeignKey(to=SubRegion, blank=True, null=True, on_delete=models.PROTECT)
    region = models.ForeignKey(to=Region, blank=True, null=True, on_delete=models.PROTECT)

    class Meta:
        abstract = True

    def clean(self):
        """ Override the base clean to verify that the User links to Country objects is ok """
        super().clean()
        linked_objects = [field for field in ["country", "sub_region", "region"]
                          if hasattr(self, field) and getattr(self, field) is not None]
        if len(linked_objects) > 1:
            raise ValidationError("The user {} must be linked to one Countries object (but is linked to {})".format(
                self, ", ".join(linked_objects)))

    @property
    def _country_fields(self):
        if self.country:
            return self.country
        if self.sub_region:
            return self.sub_region
        if self.region:
            return self.region
        return None

    @property
    def linked_countries(self):
        return self._country_fields.linked_countries if self._country_fields is not None else Country.objects.all()


class AbstractEmailUser(AbstractBaseUser, PermissionsMixin, UpAndDownIsActiveMixinWithoutManager):
    """
    Custom User class created in order to use the email as the username field, and add the phone number

    Reference documentation:
    https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#abstractbaseuser
    Used to implement the custom specification as detailed in the page 3 of the following document:
    https://docs.google.com/document/d/1J9LITylvflWHTifQ1Tn1_lyxhdGsd3vpEtv_3KFCPtw/edit
    """
    email = CIEmailField(unique=True, blank=False, null=False)
    first_name = CICharField(max_length=64, blank=False, null=False)
    last_name = CICharField(max_length=64, blank=False, null=False)
    phone = PhoneNumberField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.PROTECT)

    objects = UserAndDownIsActiveManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', ]

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        abstract = True

    def get_full_name(self):
        """ Returns the last name followed by the first name, with a space in between """
        return (self.last_name + ' ' + self.first_name).strip()

    def get_short_name(self):
        """ Returns the short name for the user """
        return self.first_name


class PFUser(CompaniesUserMixin, CountryUserMixin, AbstractEmailUser):
    pass
