import logging

from django.db.models import DecimalField, Model

from isc_common.fields.related import ForeignKeyProtect
from isc_common.http.DSRequest import DSRequest
from isc_common.models.audit import Manager
from isc_common.models.standard_colors import Standard_colors
from kaf_pas.ckk.models.ed_izm import Ed_izm
from kaf_pas.ckk.models.item import Item
from kaf_pas.ckk.models.locations import Locations

logger = logging.getLogger(__name__)


class BuffersManager(Manager):

    @staticmethod
    def getRecord(record):
        res = {
            'location_id': record.location.id,
            'location__code': record.location.code,
            'location__name': record.location.name,
            'location__full_name': record.location.full_name,
            'item_id': record.item.id,
            'value': record.value,
            'color_id': record.color.id if record.color else None,
            'color__color': record.color.color if record.color else None,
            'color__name': record.color.name if record.color else None,
            'item__STMP_1_id': record.item.STMP_1.id if record.item.STMP_1 else None,
            'item__STMP_1__value_str': record.item.STMP_1.value_str if record.item.STMP_1 else None,
            'item__STMP_2_id': record.item.STMP_2.id if record.item.STMP_2 else None,
            'item__STMP_2__value_str': record.item.STMP_2.value_str if record.item.STMP_2 else None,
            'edizm_id': record.edizm.id,
            'edizm__code': record.edizm.code,
            'edizm__name': record.edizm.name,
        }
        return res


class Buffers(Model):
    item = ForeignKeyProtect(Item)
    location = ForeignKeyProtect(Locations)
    edizm = ForeignKeyProtect(Ed_izm)
    value = DecimalField(max_digits=19, decimal_places=4)
    color = ForeignKeyProtect(Standard_colors, null=True, blank=True)

    objects = BuffersManager()

    def __str__(self):
        return f'ID:{self.id}'

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Буферы'
        managed = False
        db_table = 'accounting_buffers_view'
