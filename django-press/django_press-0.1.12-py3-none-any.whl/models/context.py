from django.db import models


class Context(models.Model):
    key = models.CharField(max_length=500, unique=True, blank=False, null=False)
    value = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f'{self.key}: {self.value}'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.value:
            self.value = self.key
        super().save(force_insert, force_update, using, update_fields)

