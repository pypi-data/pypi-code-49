import logging

from django.db.models import PositiveIntegerField

import kaf_pas
from isc_common.fields.related import ForeignKeyCascade, ForeignKeyProtect
from isc_common.models.audit import AuditManager, AuditQuerySet, AuditModel
from kaf_pas import planing, production
from kaf_pas.ckk.models.ed_izm import Ed_izm
from kaf_pas.planing.models.operations import Operations
from kaf_pas.production.models.operations import Operations

logger = logging.getLogger(__name__)


class Operation_operationQuerySet(AuditQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Operation_operationManager(AuditManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return Operation_operationQuerySet(self.model, using=self._db)


class Operation_operation(AuditModel):
    operation = ForeignKeyCascade(kaf_pas.planing.models.operations.Operations, related_name='planing_operation_2')
    production_operation = ForeignKeyCascade(kaf_pas.production.models.operations.Operations, related_name='production_operation_2')
    num = PositiveIntegerField()
    qty = PositiveIntegerField(null=True, blank=True)
    ed_izm = ForeignKeyProtect(Ed_izm, null=True, blank=True)

    objects = Operation_operationManager()

    def __str__(self):
        return f'ID:{self.id}, operation: [{self.operation}], production_operation: [{self.production_operation}]'

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Кросс-таблица'
