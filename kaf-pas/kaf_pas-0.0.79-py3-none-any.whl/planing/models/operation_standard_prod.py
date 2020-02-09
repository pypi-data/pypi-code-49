from django.utils.translation import ugettext_lazy as _

import logging

from isc_common.fields.related import ForeignKeyProtect, ForeignKeyCascade
from isc_common.models.audit import AuditModel, AuditManager, AuditQuerySet
from kaf_pas.ckk.models.materials import Materials
from kaf_pas.planing.models.operations import Operations

logger = logging.getLogger(__name__)


class Operation_standard_prodQuerySet(AuditQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Operation_standard_prodManager(AuditManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return Operation_standard_prodQuerySet(self.model, using=self._db)


class Operation_standard_prod(AuditModel):
    operation = ForeignKeyCascade(Operations)
    material = ForeignKeyProtect(Materials)

    objects = Operation_standard_prodManager()

    def __str__(self):
        return f"ID:{self.id}"

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Кросс таблица стандартнх изделий'
