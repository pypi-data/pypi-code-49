import logging

from isc_common.fields.code_field import ColorField
from isc_common.fields.related import ForeignKeyCascade, ForeignKeyProtect
from isc_common.models.audit import AuditModel, AuditManager, AuditQuerySet
from isc_common.models.standard_colors import Standard_colors
from kaf_pas.planing.models.operations import Operations

logger = logging.getLogger(__name__)


class Operation_colorQuerySet(AuditQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Operation_colorManager(AuditManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'editing': record.editing,
            'deliting': record.deliting,
            'color_id': record.color.id,
            'color__color': record.color.color,
            'color__name': record.color.name,
        }
        return res

    def get_queryset(self):
        return Operation_colorQuerySet(self.model, using=self._db)


class Operation_color(AuditModel):
    operation = ForeignKeyCascade(Operations)
    color = ForeignKeyProtect(Standard_colors)

    objects = Operation_colorManager()

    def __str__(self):
        return f"ID:{self.id}"

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Кросс таблица значений операции'
