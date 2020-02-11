# Imports ##############################################################################################################
from django.db import models
from django.db.models import ForeignKey


# Querysets ############################################################################################################

class ActiveQuerySet(models.QuerySet):
    """ Add simple shortcuts for the filter queryset to keep only the active/inactive objects """
    def active(self):
        return self.filter(is_active=True)

    def inactive(self):
        return self.filter(is_active=False)


class DownIsActiveMixinQuerySet(ActiveQuerySet):

    def _deactivate_children(self, pkd):
        """
        Deactive related downward is_active field of all instances recursively.
        Can be call by update or save.
        """
        # return all Many to One relation
        for field in self.get_downward_related_fields():
            if hasattr(field.related_model, 'is_active'):
                # get the foreignkey name field
                field_pk = field.remote_field.name + "__pk__in"
                # Queryset of all objects that have to be modify
                field.related_model.objects.filter(is_active=True).filter(**{field_pk: pkd}).update(is_active=False)

    # add deactivate private method in the manager
    _deactivate_children.queryset_only = False

    def get_downward_related_fields(self):
        """ Return ManytoOnefield related to self"""
        return [field for field in self.model._meta.get_fields() if field.get_internal_type() == "ForeignKey" and not
                isinstance(field, ForeignKey)]

    def update(self, **kwargs):
        # get the list of the pks from the Query (pk_list), We need to get it before update, otherwise the query becomes
        # Null. pk_list is set to [] if the Query is empty.
        pk_list = list(self.values_list("pk", flat=True)) if 'is_active' in kwargs and not kwargs['is_active'] else []
        super().update(**kwargs)
        if pk_list:
            self._deactivate_children(pk_list)


class DownIsActiveMixinManager(models.Manager.from_queryset(DownIsActiveMixinQuerySet)):
    use_in_migration = True

