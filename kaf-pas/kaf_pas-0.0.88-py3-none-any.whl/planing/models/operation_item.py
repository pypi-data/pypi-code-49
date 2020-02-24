import logging

from django.contrib.postgres.fields import JSONField
from django.db.models import TextField

from isc_common.fields.related import ForeignKeyProtect, ForeignKeyCascade
from isc_common.models.audit import AuditModel, AuditManager, AuditQuerySet
from kaf_pas.ckk.models.item import Item
from kaf_pas.planing.models.operations import Operations

logger = logging.getLogger(__name__)


class Operation_itemQuerySet(AuditQuerySet):
    pass


class Operation_itemManager(AuditManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return Operation_itemQuerySet(self.model, using=self._db)


class Operation_item(AuditModel):
    operation = ForeignKeyCascade(Operations)
    item = ForeignKeyProtect(Item)
    item_full_name = TextField()
    item_full_name_obj = JSONField(default=dict)

    objects = Operation_itemManager()

    def __str__(self):
        return f"ID:{self.id}, operation: [{self.operation}], item: [{self.item}], item_full_name: {self.item_full_name}, item_full_name_obj: {self.item_full_name_obj}"

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Кросс таблица'
        unique_together = (('operation', 'item'),)
