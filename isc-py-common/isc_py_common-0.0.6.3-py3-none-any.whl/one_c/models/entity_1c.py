import logging

from django.db.models import Model

from isc_common.fields.code_field import CodeField

logger = logging.getLogger(__name__)


class Entity_1c(Model):
    code = CodeField(unique=True)
    def __str__(self):
        return f"(id: {self.id}, code: {self.code})"

    class Meta:
        verbose_name = 'Сущность 1С'
