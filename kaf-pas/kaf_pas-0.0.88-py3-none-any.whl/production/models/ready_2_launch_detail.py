import logging

from django.contrib.postgres.fields import JSONField
from django.db.models import TextField

from isc_common.fields.code_field import CodeField
from isc_common.fields.related import ForeignKeyCascade
from isc_common.models.audit import AuditModel, AuditManager, AuditQuerySet
from kaf_pas.production.models.ready_2_launch import Ready_2_launch

logger = logging.getLogger(__name__)


class Ready_2_launch_detailQuerySet(AuditQuerySet):
    def delete(self):
        super().delete()


class Ready_2_launch_detailManager(AuditManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'item_full_name': record.item_full_name,
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
    ready = ForeignKeyCascade(Ready_2_launch)
    item_full_name = TextField(null=True, blank=True)
    item_full_name_obj = JSONField(default=dict)
    notes = TextField(null=True, blank=True)

    objects = Ready_2_launch_detailManager()

    def __str__(self):
        return f"ID:{self.id}"

    class Meta:
        verbose_name = 'Детализация готовности к запуску'
