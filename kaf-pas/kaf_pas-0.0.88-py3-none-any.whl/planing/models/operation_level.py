import logging

from isc_common.fields.related import ForeignKeyCascade
from isc_common.models.audit import AuditModel, AuditManager, AuditQuerySet
from kaf_pas.planing.models.levels import Levels
from kaf_pas.planing.models.operations import Operations

logger = logging.getLogger(__name__)


class Operation_levelQuerySet(AuditQuerySet):
    pass


class Operation_levelManager(AuditManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return Operation_levelQuerySet(self.model, using=self._db)


class Operation_level(AuditModel):
    operation = ForeignKeyCascade(Operations, related_name='planing_operation_1')
    level = ForeignKeyCascade(Levels, related_name='planing_lev_1')

    objects = Operation_levelManager()

    def __str__(self):
        return f"ID:{self.id}, level: [{self.level}] , operation: [{self.operation}]"

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Кросс-таблица'
        unique_together = (('operation', 'level'),)
