# Import ##############################################################################################################
from django.db import models
from django.core.validators import MinLengthValidator

from pixelforest_drf.utils.models_mixins import AbrModelMixin, NotModifiableFieldsModelMixin, UpAndDownIsActiveMixin


# Mixins ###############################################################################################################

class LocBaseAbstractModel(UpAndDownIsActiveMixin):
    """
    Shared Fields/Methods to all models in the Countries application
    """
    name = models.CharField(max_length=256, null=False, blank=False, unique=True)
    last_update = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """ Add the validation to save """
        self.full_clean()
        return super().save(*args, **kwargs)

    @property
    def linked_countries(self):
        """ Returns a queryset containing all Countries object linked to this object """
        raise NotImplementedError("This method needs to be implemented")

    class Meta:
        abstract = True


# Abstract Models ######################################################################################################

# Regions
class AbstractRegion(LocBaseAbstractModel, AbrModelMixin):
    """
    A Region is a group of Sub Regions. It is mostly used with continents, but can be customized.
    Examples: Asia, Africa, Oceania, Europe, Americas ...
    """
    class Meta:
        abstract = True
        constraints = [
            models.UniqueConstraint(fields=['name'],
                                    name="Two regions cannot share the same name"),
            models.UniqueConstraint(fields=['abbreviation'],
                                    name="Two regions cannot share the same abbreviation")
        ]

    @property
    def linked_countries(self):
        return Country.objects.filter(sub_region__region=self.pk)


class Region(AbstractRegion):
    pass


# SubRegions
class AbstractSubRegion(LocBaseAbstractModel, AbrModelMixin):
    """
    A SubRegion is a group of Countries. It is mostly used for geographical areas, but can be customized.
    Example : Northern Africa
    """
    region = models.ForeignKey(to=Region, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True
        constraints = [
            models.UniqueConstraint(fields=['region', 'name'],
                                    name="Two sub regions cannot share the same name and region."),
            models.UniqueConstraint(fields=['region', 'abbreviation'],
                                    name="Two sub regions cannot share the same abbreviation and region."),
        ]

    @property
    def linked_countries(self):
        return Country.objects.filter(sub_region=self.pk)


class SubRegion(AbstractSubRegion):
    pass


class AbstractCountry(LocBaseAbstractModel, NotModifiableFieldsModelMixin):
    """
    A country, as defined by the ISO 3166 standard.
    Example : Algeria
    """
    name = models.CharField(max_length=256, null=False, blank=False, unique=True)
    iso_alpha_2 = models.CharField(null=False, blank=False, unique=True,
                                   max_length=2, validators=[MinLengthValidator(2)])
    iso_alpha_3 = models.CharField(null=False, blank=False, unique=True,
                                   max_length=3, validators=[MinLengthValidator(3)])
    iso_num = models.IntegerField(null=False, blank=False, unique=True)
    sub_region = models.ForeignKey(to=SubRegion, on_delete=models.SET_NULL, null=True, blank=True)
    flag = models.ImageField(upload_to='pixelforest_drf/flags/', blank=True, null=True)

    not_modifiable_fields = ['name', 'iso_alpha_2', 'iso_alpha_3', 'iso_num']

    class Meta:
        abstract = True
        verbose_name_plural = 'Countries'
        constraints = [
            models.UniqueConstraint(fields=['sub_region', 'name'],
                                    name="Two countries cannot share the same name and sub_region"),
        ]

    def __str__(self):
        return self.name

    @property
    def linked_countries(self):
        return Country.objects.filter(pk=self.pk)


class Country(AbstractCountry):
    pass
