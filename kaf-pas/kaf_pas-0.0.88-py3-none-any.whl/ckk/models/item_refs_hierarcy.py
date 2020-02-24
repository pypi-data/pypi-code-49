import logging

from django.db.models import BigIntegerField
from isc_common.fields.related import ForeignKeyProtect
from isc_common.models.audit import AuditManager, AuditQuerySet
from isc_common.models.base_ref import Hierarcy
from isc_common.models.tree_audit import TreeAuditModelManager

from kaf_pas.ckk.models.item_refs import Item_refs

logger = logging.getLogger(__name__)


class Item_refs_hierarcyQuerySet(AuditQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def update(self, **kwargs):
        return super().update(**kwargs)

    def get_or_create(self, defaults=None, **kwargs):
        return super().get_or_create(defaults, **kwargs)

    def update_or_create(self, defaults=None, **kwargs):
        return super().update_or_create(defaults, **kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Item_refs_hierarcyManager(AuditManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'parent_id': record.parent.id if record.parent else None,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return Item_refs_hierarcyQuerySet(self.model, using=self._db)


class Item_refs_hierarcy(Hierarcy):
    id = BigIntegerField(primary_key=True, verbose_name="Идентификатор")

    item_refs = ForeignKeyProtect(Item_refs)

    objects = TreeAuditModelManager()

    def __str__(self):
        return f'\nID={self.id}, parent_id={self.parent_id}'

    class Meta:
        verbose_name = 'Item_refs_hierarcy'
