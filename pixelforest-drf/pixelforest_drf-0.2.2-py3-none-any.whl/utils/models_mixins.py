# Imports ##############################################################################################################
from django.db import models
from django.forms.models import model_to_dict
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import CICharField
from django.db.models.fields.reverse_related import ManyToOneRel
from .querysets import DownIsActiveMixinManager


# Static UpIsActiveMixin Private Method ###############################################################################

def _switch_instances_is_active(instances, new_state):
    """ For all objects in the 'instances' list, if 'is_active' is present set it to new_state"""
    for inst in instances:
        if hasattr(inst, 'is_active') and inst.is_active is not new_state:
            inst.is_active = new_state
            inst.save()


# Model Mixins #########################################################################################################

class NotModifiableFieldsModelMixin(models.Model):
    """
    This mixin add the ability to create fields that can only be changed before the object is added in database

    It was created because we expected 'editable=False' to have this behaviour, but this field option only remove the
    field from any ModelForm (such as the admin) AND also remove validation on it
    (https://docs.djangoproject.com/en/2.2/ref/models/fields/#editable).

    Note that this doesn't alter the behaviour of the manager, so fields can still be updated by a bulk_update
    Note that this mixin does not overwrite .save() to call .full_clean() at the save stage for compatibility

    To add a field to the list of fields that cannot be modified, add the name of your field in the
    'not_modifiable_fields' list of your model.
    """
    @classmethod
    def nm_fields(cls):
        if hasattr(cls, "not_modifiable_fields"):
            return cls.not_modifiable_fields
        return []

    def __init__(self, *args, **kwargs):
        """ Override the init to keep the original value """
        # Call the init from the model
        super().__init__(*args, **kwargs)

        # Verify that all fields in not_modifiable_fields are fields of your model
        not_a_field = [f for f in self.nm_fields() if f not in [f.name for f in self._meta.fields]]
        if not_a_field:
            raise ValidationError("One or more field names in not_modifiable_fields do not exists in the {} model ({})"
                                  .format(self.__class__.__name__, not_a_field))

        # Keep the original values of the fields
        self.original_fields = model_to_dict(self, fields=[f for f in self.nm_fields()])

    def clean_fields(self, exclude=None):
        """
        For all fields in not_modifiable_fields, if the call to .save() is not an insert, do the validation
        """
        # If you are not creating a new object
        errors = {}
        if not self._state.adding:
            # Change exclude to empty list if None
            exclude = [] if exclude is None else exclude
            for f in self.nm_fields():
                if f in exclude:
                    continue
                if getattr(self, f) != self.original_fields[f]:
                    error = "This field cannot be modified"
                    errors[f] = errors[f] + [error] if f in errors.keys() else [error]

        # Get a dictionary of errors from clean_fields
        try:
            super().clean_fields(exclude=exclude)
        except ValidationError as e:
            errors = e.update_error_dict(errors)

        if errors:
            raise ValidationError(errors)

    class Meta:
        abstract = True


class AbrModelMixin(models.Model):
    """ Augmented model mixin with an abbreviation field """
    abbreviation = CICharField(max_length=10, null=True, blank=True)

    def get_name_or_abbreviation(self):
        """ Either return the abbreviation (if specified), the name (if specified), or None """
        if self.abbreviation:
            return self.abbreviation
        if hasattr(self, "name") and self.name:
            return self.name
        return None

    def __str__(self):
        str_repr = self.get_name_or_abbreviation()
        return str_repr if str_repr is not None else ""

    class Meta:
        abstract = True

# Is_Active Upward Mixin ##############################################################################################


class _UpIsActiveMixin(models.Model):
    """
    Set is_active to True for upward related instances
    If a series of instances with an is_active field is interrupted by an instance without an is_active field,
    the modification stops right before the object without the is_active field. Example :

          +-----------+      +----------+      +-----------+
          | is_active +--/-->+ no field +----->+ is_active |
          +-----------+      +----------+      +-----------+

    """

    def _get_upward_related_instances(self):
        return [getattr(self, field.name) for field in self._meta.get_fields() if
                field.get_internal_type() == "ForeignKey" and not isinstance(field, ManyToOneRel)]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_is_active = getattr(self, "is_active", None)

    def save(self, *args, **kwargs):
        if hasattr(self, 'is_active') and self.is_active:
            # If is_active was False before and set to True or the object is new
            if not self.original_is_active or self._state.adding:
                # Modify all related instances is_active to True
                _switch_instances_is_active(self._get_upward_related_instances(), True)
            # If is_active was already True before
            elif not self._state.adding and self.is_active:
                # Modify all related instances that were not linked to self before is_active to True
                diff_instances = set(self._get_upward_related_instances()).symmetric_difference(
                    set(self.__class__.objects.get(pk=self.pk)._get_upward_related_instances()))
                _switch_instances_is_active(diff_instances, True)
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class UpIsActiveMixin(_UpIsActiveMixin):
    """
    Set is_active to True for upward related instances
    The is_active field is already created
    """
    is_active = models.BooleanField(default=False, null=False, blank=True)

    class Meta:
        abstract = True

# Is_Active Downward Mixin #############################################################################################


class _DownIsActiveMixin(models.Model):
    """
    Set is_active to False for downward related instances
    If a series of instances with an is_active field is interrupted by an instance without an is_active field,
    the modification stops right before the object without the is_active field. Example :

          +-----------+      +----------+      +-----------+
          | is_active +--/-->+ no field +----->+ is_active |
          +-----------+      +----------+      +-----------+

    """
    objects = DownIsActiveMixinManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if hasattr(self, 'is_active') and not self.is_active and not self._state.adding:
            self.__class__.objects._deactivate_children([self.pk])

    class Meta:
        abstract = True


class DownIsActiveMixin(_DownIsActiveMixin):
    """
    Set is_active to False for downward related instances
    The is_active field is already created
    """
    is_active = models.BooleanField(default=False, null=False, blank=True)

    class Meta:
        abstract = True


class _UpAndDownIsActiveMixin(_DownIsActiveMixin, _UpIsActiveMixin):
    """
    Private Mixin class that inherit Up and Down mixin.
    Set is_active to False for downward related instances and to True for upward related instances.
    """
    pass

    class Meta:
        abstract = True


class UpAndDownIsActiveMixin(_UpAndDownIsActiveMixin):
    """
    Public Mixin class that inherit Up and Down mixin.
    Set is_active to False for downward related instances and to True for upward related instances.
    The is_active field is already created
    """
    is_active = models.BooleanField(default=False, null=False, blank=True)

    class Meta:
        abstract = True
