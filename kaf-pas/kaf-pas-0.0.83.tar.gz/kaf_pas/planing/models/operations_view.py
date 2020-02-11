import logging

from django.db.models import TextField, DecimalField, PositiveIntegerField, BooleanField, DateTimeField

from isc_common.auth.models.user import User
from isc_common.fields.code_field import ColorField
from isc_common.fields.related import ForeignKeyProtect
from isc_common.models.audit import AuditManager, AuditModel, AuditQuerySet
from isc_common.models.standard_colors import Standard_colors
from kaf_pas.ckk.models.ed_izm import Ed_izm
from kaf_pas.ckk.models.item import Item
from kaf_pas.ckk.models.locations import Locations
from kaf_pas.planing.models.operation_types import Operation_types
from kaf_pas.planing.models.status_operation_types import Status_operation_types

logger = logging.getLogger(__name__)


class Operations_viewQuerySet(AuditQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Operations_viewManager(AuditManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'date': record.date,
            'opertype_id': record.opertype.id,
            'opertype__full_name': record.opertype.full_name,
            'status_id': record.status.id if record.status else None,
            'status__code': record.status.code if record.status else None,
            'status__name': record.status.name if record.status else None,
            'location_id': record.location.id if record.location else None,
            'location__code': record.location.code if record.location else None,
            'location__name': record.location.name if record.location else None,
            'location__full_name': record.location.full_name if record.location else None,
            'item_id': record.item.id if record.item else None,
            'value': record.value,
            'color_id': record.color.id if record.color else None,
            'color__color': record.color.color if record.color else None,
            'color__name': record.color.name if record.color else None,
            'parent_id': record.parent_id,
            'isFolder': record.isFolder,
            'description': record.description,
            'item__STMP_1_id': record.item.STMP_1.id if record.item and record.item.STMP_1 and record.item.STMP_1 else None,
            'item__STMP_1__value_str': record.item.STMP_1.value_str if record.item and record.item.STMP_1 and record.item.STMP_1 else None,
            'item__STMP_2_id': record.item.STMP_2.id if record.item and record.item.STMP_2 and record.item.STMP_2 else None,
            'item__STMP_2__value_str': record.item.STMP_2.value_str if record.item and record.item.STMP_2 and record.item.STMP_2 else None,
            'edizm_id': record.edizm.id if record.edizm else None,
            'edizm__code': record.edizm.code if record.edizm else None,
            'edizm__name': record.edizm.name if record.edizm else None,
            'creator_id': record.creator.id,
            'creator__short_name': record.creator.get_short_name,
        }
        return res

    def get_queryset(self):
        return Operations_viewQuerySet(self.model, using=self._db)


class Operations_view(AuditModel):
    date = DateTimeField()
    opertype = ForeignKeyProtect(Operation_types)
    status = ForeignKeyProtect(Status_operation_types, null=True, blank=True)
    item = ForeignKeyProtect(Item, null=True, blank=True)
    location = ForeignKeyProtect(Locations, null=True, blank=True)
    edizm = ForeignKeyProtect(Ed_izm, null=True, blank=True)
    value = DecimalField(max_digits=19, decimal_places=4, null=True, blank=True)
    color = ForeignKeyProtect(Standard_colors, null=True, blank=True)
    description = TextField(null=True, blank=True)
    parent_id = PositiveIntegerField(null=True, blank=True)
    isFolder = BooleanField()
    creator = ForeignKeyProtect(User)

    objects = Operations_viewManager()

    def __str__(self):
        return f"ID:{self.id}, opertype: [{self.opertype}], status: [{self.status}]"

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Опреации системные'
        managed = False
        db_table = 'planing_operations_view'
