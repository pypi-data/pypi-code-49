import logging

from django.db.models import PositiveIntegerField

from isc_common.fields.related import ForeignKeyProtect, ForeignKeyCascade
from isc_common.managers.common_managet_with_lookup_fields import CommonManagetWithLookUpFieldsQuerySet, CommonManagetWithLookUpFieldsManager
from isc_common.models.audit import AuditModel
from kaf_pas.ckk.models.item import Item
from kaf_pas.sales.models.precent_dogovors import Precent_dogovors

logger = logging.getLogger(__name__)


class Precent_items_viewQuerySet(CommonManagetWithLookUpFieldsQuerySet):
    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Precent_items_viewManager(CommonManagetWithLookUpFieldsManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'item_id': record.item.id,
            'item__STMP_1_id': record.item.STMP_1.id if record.item.STMP_1 else None,
            'item__STMP_1__value_str': record.item.STMP_1.value_str if record.item.STMP_1 else None,
            'item__STMP_2_id': record.item.STMP_2.id if record.item.STMP_2 else None,
            'item__STMP_2__value_str': record.item.STMP_2.value_str if record.item.STMP_2 else None,
            'precent_dogovor_id': record.precent_dogovor.id,
            'qty': record.qty,
            'used_qty': record.used_qty,
            'tail_qty': record.tail_qty,
            'lastmodified': record.lastmodified,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return Precent_items_viewQuerySet(self.model, using=self._db)


class Precent_items_view(AuditModel):
    item = ForeignKeyProtect(Item)
    precent_dogovor = ForeignKeyCascade(Precent_dogovors)
    qty = PositiveIntegerField()
    used_qty = PositiveIntegerField()
    tail_qty = PositiveIntegerField()

    objects = Precent_items_viewManager()

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Комплектация распоряжения'
        db_table = 'sales_precent_items_view'
        managed = False
