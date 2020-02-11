# Imports ##############################################################################################################
from django.db import models


# TestCase #############################################################################################################

class CountSaveModelMixin(models.Model):
    """
    This class will count the number of time an object was saved.
    It is used for unit-testing purposes
    """
    @property
    def save_count(self):
        return self._save_count

    def __init__(self, *args, **kwargs):
        """ Add a save counter to the model """
        super().__init__(*args, **kwargs)
        self._save_count = 0

    def save(self, *args, **kwargs):
        """ Increment the save counter on every call """
        super().save(*args, **kwargs)
        self._save_count += 1

    class Meta:
        abstract = True
