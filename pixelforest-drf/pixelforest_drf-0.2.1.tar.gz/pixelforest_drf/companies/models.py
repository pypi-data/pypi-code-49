# Imports ##############################################################################################################
from django.db import models
from django.contrib.postgres.fields import CICharField

from ..utils.models_mixins import AbrModelMixin, UpAndDownIsActiveMixin


# Models ###############################################################################################################

class AbstractCompanyModel(AbrModelMixin, UpAndDownIsActiveMixin):
    """
    Common fields to all models in this application.
    Note that the logo isn't here because it uses different folders for the storage of images.
    """
    name = CICharField(max_length=256, null=False, blank=False)
    last_update = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """ Add the validation save """
        self.full_clean()
        return super().save(*args, **kwargs)

    @property
    def linked_services(self):
        """ Returns a queryset containing all Companies objects linked to this object """
        raise NotImplementedError("This method needs to be implemented")

    class Meta:
        abstract = True


class AbstractCompanyGroup(AbstractCompanyModel):
    """
    Highest level object, not mandatory.
    Example: ACME Group
    """
    logo = models.ImageField(upload_to='companies/groups/', null=True, blank=True)

    @property
    def linked_services(self):
        return Service.objects.filter(subsidiary__company__company_group=self.pk)

    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'
        abstract = True
        constraints = [
            models.UniqueConstraint(fields=['name', ],
                                    name="Two groups cannot share the same name, case insensitive"),
            models.UniqueConstraint(fields=['abbreviation'],
                                    name="Two groups cannot share the same abbreviation, case insensitive"),
        ]


class CompanyGroup(AbstractCompanyGroup):
    pass


class AbstractCompany(AbstractCompanyModel):
    """
    Highest mandatory object.
    Example: ACME
    """
    company_group = models.ForeignKey(to=CompanyGroup, null=True, blank=True, on_delete=models.PROTECT)
    logo = models.ImageField(upload_to='companies/companies/', null=True, blank=True)

    @property
    def linked_services(self):
        return Service.objects.filter(subsidiary__company=self.pk)

    def __str__(self):
        if self.company_group is None:
            return self.get_name_or_abbreviation()
        return '%s - %s' % (self.company_group.__str__(), self.get_name_or_abbreviation())

    class Meta:
        verbose_name_plural = 'companies'
        abstract = True
        constraints = [
            models.UniqueConstraint(fields=['company_group', 'name'],
                                    name="Two companies cannot share the same name and the same group."),
            models.UniqueConstraint(fields=['company_group', 'abbreviation'],
                                    name="Two companies cannot share the same abbreviation and group"),
        ]


class Company(AbstractCompany):
    pass


class AbstractSubsidiary(AbstractCompanyModel):
    """
    Example: ACME France
    """
    company = models.ForeignKey(to=Company, null=False, blank=False, on_delete=models.PROTECT)
    logo = models.ImageField(upload_to='companies/subsidiaries', null=True, blank=True)

    @property
    def linked_services(self):
        return Service.objects.filter(subsidiary=self.pk)

    def __str__(self):
        return '%s - %s' % (self.company.__str__(), self.get_name_or_abbreviation())

    class Meta:
        verbose_name_plural = 'subsidiaries'
        abstract = True
        constraints = [
            models.UniqueConstraint(fields=['company', 'name'],
                                    name="Two subsidiaries cannot share the same name and company."),
            models.UniqueConstraint(fields=['company', 'abbreviation'],
                                    name="Two subsidiaries cannot share the same abbreviation and company"),
        ]


class Subsidiary(AbstractSubsidiary):
    pass


class AbstractService(AbstractCompanyModel):
    """
    Example: Dev Team
    """
    subsidiary = models.ForeignKey(to=Subsidiary, null=False, blank=False, on_delete=models.PROTECT)
    logo = models.ImageField(upload_to='companies/services', null=True, blank=True)

    @property
    def linked_services(self):
        return Service.objects.filter(pk=self.pk)

    def __str__(self):
        return '%s - %s' % (self.subsidiary.__str__(), self.get_name_or_abbreviation())

    class Meta:
        abstract = True
        constraints = [
            models.UniqueConstraint(fields=['subsidiary', 'name'],
                                    name="Two services cannot share the same name and subsidiary"),
            models.UniqueConstraint(fields=['subsidiary', 'abbreviation'],
                                    name="Two services cannot share the same abbreviation and subsidiary"),
        ]


class Service(AbstractService):
    pass
