import logging

from django.db.models import DecimalField, FloatField

from isc_common.fields.related import ForeignKeyCascade, ForeignKeyProtect
from isc_common.models.audit import AuditModel, AuditManager, AuditQuerySet
from kaf_pas.ckk.models.ed_izm import Ed_izm
from kaf_pas.planing.models.operations import Operations

logger = logging.getLogger(__name__)


class Operation_valueQuerySet(AuditQuerySet):
    pass


class Operation_valueManager(AuditManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return Operation_valueQuerySet(self.model, using=self._db)


class Operation_value(AuditModel):
    operation = ForeignKeyCascade(Operations)
    edizm = ForeignKeyProtect(Ed_izm)
    value = FloatField()

    objects = Operation_valueManager()

    def __str__(self):
        return f"ID:{self.id}, value: {self.value}, edizm: [{self.edizm}]"

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Кросс таблица значений операции'
