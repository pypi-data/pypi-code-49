import logging

from django.db.models import TextField, Model

from isc_common.fields.related import ForeignKeyProtect
from one_c.models.param_type import Param_type

logger = logging.getLogger(__name__)


class Documents_param_1c(Model):
    type = ForeignKeyProtect(Param_type)
    value = TextField(db_index=True)

    def __str__(self):
        return f"(id: {self.id}, document: type: {self.type}, value: {self.value})"

    class Meta:
        verbose_name = 'Параметры документов 1С'
        unique_together = (('type', 'value'),)
