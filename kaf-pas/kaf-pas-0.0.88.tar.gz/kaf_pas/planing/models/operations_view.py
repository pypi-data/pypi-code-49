import logging

from django.db.models import TextField, DecimalField, PositiveIntegerField, BooleanField, DateTimeField

from isc_common.auth.models.user import User
from isc_common.fields.code_field import CodeField
from isc_common.fields.related import ForeignKeyProtect, ForeignKeySetNull
from isc_common.models.base_ref import Hierarcy
from isc_common.models.standard_colors import Standard_colors
from isc_common.models.tree_audit import TreeAuditModelQuerySet, TreeAuditModelManager
from isc_common.number import DelProps
from kaf_pas.ckk.models.ed_izm import Ed_izm
from kaf_pas.ckk.models.item import Item
from kaf_pas.ckk.models.material_askon import Material_askon
from kaf_pas.ckk.models.materials import Materials
from kaf_pas.planing.models.levels import Levels
from kaf_pas.planing.models.operation_refs import Operation_refsManager
from kaf_pas.planing.models.operation_types import Operation_types
from kaf_pas.planing.models.operation_value import Operation_value
from kaf_pas.planing.models.status_operation_types import Status_operation_types
from kaf_pas.production.models.launches import Launches
from kaf_pas.production.models.operations import Operations
from kaf_pas.production.models.resource import Resource

logger = logging.getLogger(__name__)


class Operations_viewQuerySet(TreeAuditModelQuerySet):
    pass


class Operations_viewManager(TreeAuditModelManager):

    @staticmethod
    def getRecord(record):
        res = {
            'color__color': record.color.color if record.color else None,
            'color__name': record.color.name if record.color else None,
            'color_id': record.color.id if record.color else None,
            'creator__short_name': record.creator.get_short_name,
            'creator_id': record.creator.id,
            'date': record.date,
            'description': record.description,
            'edizm__code': record.value.edizm.code if record.value and record.value.edizm else None,
            'edizm__name': record.value.edizm.name if record.value and record.value.edizm else None,
            'edizm_id': record.value.edizm.id if record.value and record.value.edizm else None,
            'id': record.id,
            'isFolder': record.isFolder,
            'item__STMP_1__value_str': record.item.STMP_1.value_str if record.item and record.item.STMP_1 and record.item.STMP_1 else None,
            'item__STMP_1_id': record.item.STMP_1.id if record.item and record.item.STMP_1 and record.item.STMP_1 else None,
            'item__STMP_2__value_str': record.item.STMP_2.value_str if record.item and record.item.STMP_2 and record.item.STMP_2 else None,
            'item__STMP_2_id': record.item.STMP_2.id if record.item and record.item.STMP_2 and record.item.STMP_2 else None,
            'item_full_name': record.item_full_name,
            'item_id': record.item.id if record.item else None,
            'item_item_name': record.item.item_name if record.item else None,
            'launch_id': record.launch.id if record.launch else None,
            'location__code': record.resource.location.code if record.resource and record.resource else None,
            'location__full_name': record.resource.location.full_name if record.resource and record.resource else None,
            'location__name': record.resource.location.name if record.resource and record.resource else None,
            'location_id': record.resource.location.id if record.resource else None,
            'mark': record.mark,
            'opertype__full_name': record.opertype.full_name,
            'opertype_id': record.opertype.id,
            'operation_level__name': record.operation_level.name if record.operation_level else None,
            'operation_level__code': record.operation_level.code if record.operation_level else None,
            'operation_level_id': record.operation_level.id if record.operation_level else None,
            'parent_id': record.parent_id,
            'production_operation__full_name': record.production_operation.full_name if record.production_operation else None,
            'production_operation__name': record.production_operation.name if record.production_operation else None,
            'production_operation_edizm__name': record.production_operation_edizm.name if record.production_operation_edizm else None,
            'production_operation_edizm_id': record.production_operation_edizm.id if record.production_operation_edizm else None,
            'production_operation_id': record.production_operation.id if record.production_operation else None,
            'production_operation_num': record.production_operation_num,
            'production_operation_qty': record.production_operation_qty,
            'resource__code': record.resource.code if record.resource and record.resource else None,
            'resource__name': record.resource.name if record.resource and record.resource else None,
            'resource__description': record.resource.description if record.resource and record.resource else None,
            'resource_id': record.resource.id if record.resource else None,
            'status__code': record.status.code if record.status else None,
            'status__name': record.status.name if record.status else None,
            'status_id': record.status.id if record.status else None,
            'value': record.value.value if record.value else None,
        }
        return DelProps(res)

    def get_queryset(self):
        return Operations_viewQuerySet(self.model, using=self._db)


class Operations_view(Hierarcy):
    color = ForeignKeySetNull(Standard_colors, null=True, blank=True)
    creator = ForeignKeyProtect(User, default=None)
    date = DateTimeField(default=None)
    description = TextField(null=True, blank=True)
    isFolder = BooleanField(default=None)
    item = ForeignKeySetNull(Item, null=True, blank=True)
    item_full_name = TextField(null=True, blank=True)
    launch = ForeignKeySetNull(Launches, null=True, blank=True)
    operation_level = ForeignKeySetNull(Levels, null=True, blank=True)
    opertype = ForeignKeyProtect(Operation_types, default=None)
    production_operation = ForeignKeySetNull(Operations, null=True, blank=True)
    production_operation_edizm = ForeignKeySetNull(Ed_izm, null=True, blank=True, related_name='Operations_view_ed_izm')
    production_operation_qty = DecimalField(decimal_places=4, max_digits=19, null=True, blank=True)
    production_operation_num = PositiveIntegerField(null=True, blank=True)
    resource = ForeignKeySetNull(Resource, null=True, blank=True)
    status = ForeignKeySetNull(Status_operation_types, null=True, blank=True)
    material = ForeignKeySetNull(Material_askon, null=True, blank=True)
    value = ForeignKeySetNull(Operation_value, null=True, blank=True)
    std_material = ForeignKeySetNull(Materials, null=True, blank=True)
    mark = CodeField()
    props = Operation_refsManager.props()

    objects = Operations_viewManager()

    def __str__(self):
        return f"ID:{self.id}, \n" \
               f"props: {self.props}, \n" \
               f"creator: [{self.creator}], \n" \
               f"date: {self.date}, \n" \
               f"description: {self.description}, \n" \
               f"opertype: [{self.opertype}], \n" \
               f"status: [{self.status}], \n" \
               f"isFolder: [{self.isFolder}], \n" \
               f"opertype: [{self.opertype}], \n" \
               f"item: [{self.item}], \n" \
               f"parent_id: {self.parent}, \n" \
               f"item_full_name: {self.item_full_name}, \n" \
               f"production_operation: [{self.production_operation}], \n" \
               f"launch: [{self.launch}], \n" \
               f"resource: [{self.resource}], \n" \
               f"operation_level: [{self.operation_level}], \n" \
               f"edizm: [{self.value.edizm}], \n" \
               f"material: [{self.material}], \n" \
               f"std_material: [{self.std_material}], \n" \
               f"value: {self.value.value}"

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Опреации системные'
        managed = False
        db_table = 'planing_operations_view'
