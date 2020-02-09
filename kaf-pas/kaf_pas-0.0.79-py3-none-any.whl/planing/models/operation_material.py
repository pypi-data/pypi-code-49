import logging

from isc_common.fields.related import ForeignKeyProtect, ForeignKeyCascade
from isc_common.models.audit import AuditModel, AuditManager, AuditQuerySet
from kaf_pas.ckk.models.material_askon import Material_askon
from kaf_pas.planing.models.operations import Operations

logger = logging.getLogger(__name__)


class Operation_materialQuerySet(AuditQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Operation_materialManager(AuditManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return Operation_materialQuerySet(self.model, using=self._db)


class Operation_material(AuditModel):
    operation = ForeignKeyCascade(Operations, related_name='planing_operation')
    material = ForeignKeyProtect(Material_askon, related_name='planing_material')

    objects = Operation_materialManager()

    def __str__(self):
        return f"ID:{self.id}"

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Кросс таблица'
