import logging

from django.db.models import TextField

from isc_common.fields.related import ForeignKeyCascade
from isc_common.models.audit import AuditModel, AuditManager, AuditQuerySet
from kaf_pas.ckk.models.item import Item
from kaf_pas.production.models.ready_2_launch import Ready_2_launch

logger = logging.getLogger(__name__)


class Ready_2_launch_detailQuerySet(AuditQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Ready_2_launch_detailManager(AuditManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'item_id': record.item.id,
            'item__STMP_1_id': record.item.STMP_1.id if record.item.STMP_1 else None,
            'item__STMP_1__value_str': record.item.STMP_1.value_str if record.item.STMP_1 else None,
            'item__STMP_2_id': record.item.STMP_2.id if record.item.STMP_2 else None,
            'item__STMP_2__value_str': record.item.STMP_2.value_str if record.item.STMP_2 else None,
            'notes': record.notes,
            'ready_id': record.ready.id,
            'ready__lastmodified': record.ready.lastmodified,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return Ready_2_launch_detailQuerySet(self.model, using=self._db)


class Ready_2_launch_detail(AuditModel):
    item = ForeignKeyCascade(Item)
    ready = ForeignKeyCascade(Ready_2_launch)
    notes = TextField(null=True, blank=True)
    objects = Ready_2_launch_detailManager()

    def __str__(self):
        return f"ID:{self.id}"

    class Meta:
        verbose_name = 'Детализация готовности к запуску'
