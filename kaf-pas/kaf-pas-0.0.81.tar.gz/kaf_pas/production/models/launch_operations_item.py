import logging

from bitfield import BitField
from django.db import transaction
from django.db.models import PositiveIntegerField
from django.forms import model_to_dict

from isc_common import delAttr, setAttr
from isc_common.bit import IsBitOn
from isc_common.fields.description_field import DescriptionField
from isc_common.fields.related import ForeignKeyProtect, ForeignKeySetNull
from isc_common.http.DSRequest import DSRequest
from isc_common.managers.common_managet_with_lookup_fields import CommonManagetWithLookUpFieldsQuerySet, CommonManagetWithLookUpFieldsManager
from isc_common.models.base_ref import Hierarcy
from isc_common.number import DelProps
from kaf_pas.ckk.models.ed_izm import Ed_izm
from kaf_pas.ckk.models.item import Item
from kaf_pas.production.models.launches import Launches
from kaf_pas.production.models.operations import Operations
from kaf_pas.production.models.operations_item import Operations_item

logger = logging.getLogger(__name__)


class Launch_operations_itemQuerySet(CommonManagetWithLookUpFieldsQuerySet):
    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Launch_operations_itemManager(CommonManagetWithLookUpFieldsManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'launch_id': record.launch.id,
            'operation_id': record.operation.id,
            'operationitem_id': record.operationitem.id if record.operationitem else None,
            'operation__code': record.operation.code,
            'operation__name': record.operation.name,
            'operation__full_name': record.operation.full_name,
            'operation__description': record.operation.description,
            'ed_izm_id': record.ed_izm.id if record.ed_izm else None,
            'ed_izm__code': record.ed_izm.code if record.ed_izm else None,
            'ed_izm__name': record.ed_izm.name if record.ed_izm else None,
            'ed_izm__description': record.ed_izm.description if record.ed_izm else None,
            'qty': record.qty,
            'num': record.num,
            'description': record.description,
            'item_id': record.item.id,
            'parent_id': record.parent.id if record.parent else None,
            'props': record.props._value,
            'enabled': IsBitOn(record.props, 0),
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return Launch_operations_itemQuerySet(self.model, using=self._db)

    def _rec_def_resources(self, launch_operationitem):
        from kaf_pas.production.models.operation_def_resources import Operation_def_resources
        from kaf_pas.production.models.launch_operation_resources import Launch_operation_resources

        for operation_def_resource in Operation_def_resources.objects.filter(operation=launch_operationitem.operation):
            Launch_operation_resources.objects.get_or_create(
                launch_operationitem=launch_operationitem,
                resource=operation_def_resource.resource,
                location=operation_def_resource.location,
            )

    def createFromRequest(self, request):
        request = DSRequest(request=request)
        data = request.get_data()
        _data = data.copy()
        delAttr(_data, 'operation__full_name')

        oparations = _data.get('operation')
        item_id = _data.get('item_id')
        delAttr(_data, 'operation')
        res = []
        if isinstance(oparations, list):
            with transaction.atomic():
                if isinstance(item_id, int):
                    for oparation in oparations:
                        setAttr(_data, 'operation_id', oparation)
                        _res, created = super().get_or_create(**_data)
                        if created:
                            self._rec_def_resources(_res)
                            res1 = model_to_dict(_res)
                            setAttr(res1, 'operation__full_name', _res.operation.full_name)
                            res.append(DelProps(res1))
                elif isinstance(item_id, list):
                    delAttr(_data, 'item_id')
                    for oparation in oparations:
                        for item in item_id:
                            setAttr(_data, 'operation_id', oparation)
                            setAttr(_data, 'item_id', item)
                            _res, created = super().get_or_create(**_data)
                            if created:
                                self._rec_def_resources(_res)
                                res1 = model_to_dict(_res)
                                setAttr(res1, 'operation__full_name', _res.operation.full_name)
                                res.append(DelProps(res1))

        return res

    def updateFromRequest(self, request, removed=None, function=None):
        request = DSRequest(request=request)
        data = request.get_data()
        _data = data.copy()

        delAttr(_data, 'operation__full_name')
        delAttr(_data, 'enabled')
        delAttr(_data, 'id')
        res = super().filter(id=data.get('id')).update(**_data)

        return data


class Launch_operations_item(Hierarcy):
    description = DescriptionField()
    ed_izm = ForeignKeyProtect(Ed_izm, null=True, blank=True)
    item = ForeignKeyProtect(Item)
    launch = ForeignKeyProtect(Launches)
    num = PositiveIntegerField(null=True, blank=True)
    operation = ForeignKeyProtect(Operations)
    operationitem = ForeignKeySetNull(Operations_item, null=True, blank=True)
    qty = PositiveIntegerField(null=True, blank=True)
    props = BitField(flags=(
        ('enabled', 'Доступность в данной производственной спецификации'),  # 1
    ), default=1, db_index=True)

    objects = Launch_operations_itemManager()

    def __str__(self):
        return f"ID:{self.id}, item: [{self.item}], id_izm: [{self.ed_izm}], qty: {self.qty}, num: {self.num}"

    def __repr__(self):
        return self.operation.full_name

    class Meta:
        verbose_name = 'Кросс таблица'
        unique_together = (('item', 'launch', 'operation'),)
