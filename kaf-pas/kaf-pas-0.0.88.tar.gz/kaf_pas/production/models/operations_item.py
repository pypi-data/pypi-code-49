import logging

from django.db import transaction, connection
from django.db.models import PositiveIntegerField
from django.forms import model_to_dict

from isc_common import delAttr, setAttr
from isc_common.fields.description_field import DescriptionField
from isc_common.fields.related import ForeignKeyProtect
from isc_common.http.DSRequest import DSRequest
from isc_common.managers.common_managet_with_lookup_fields import CommonManagetWithLookUpFieldsQuerySet, CommonManagetWithLookUpFieldsManager
from isc_common.models.base_ref import Hierarcy
from kaf_pas.ckk.models.ed_izm import Ed_izm
from kaf_pas.ckk.models.item import Item
from kaf_pas.production.models.operations import Operations

logger = logging.getLogger(__name__)


class Operations_itemQuerySet(CommonManagetWithLookUpFieldsQuerySet):
    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Operations_itemManager(CommonManagetWithLookUpFieldsManager):

    @staticmethod
    def refresh_num1():
        sql = '''select item_id,
                           count(*) 
                    from production_operations_item
                    group by item_id
                    having count(*) = 1'''

        sql_max = f'''select num
                        from production_operations_item
                        where item_id = %s'''

        with transaction.atomic():
            cnt = 0
            with connection.cursor() as cursor:
                cursor.execute(sql)
                rows = cursor.fetchall()
                for row in rows:
                    item_id, count = row
                    cursor.execute(sql_max, [item_id])
                    rows1 = cursor.fetchall()

                    for row_num in rows1:
                        num, = row_num
                        if num == None:
                            cnt1 = Operations_item.objects.filter(item_id=item_id).count()
                            if cnt1 == 1:
                                operations_item = Operations_item.objects.get(item_id=item_id)
                                operations_item.num = 1
                                operations_item.save()
                                cnt += 1
            print(f'Corected: {cnt} operations.')
        return cnt

    @staticmethod
    def refresh_num(apps, schema_editor):
        sql = '''select num,
                       item_id,
                       count(*) 
                from production_operations_item
                where num is not null
                group by num,
                         item_id
                having count(*) > 1'''

        sql_max = f'''select max(num)
                                from production_operations_item
                                where item_id = %s'''

        with transaction.atomic():
            with connection.cursor() as cursor:
                cursor.execute(sql)
                rows = cursor.fetchall()
                for row in rows:
                    num, item_id, count = row
                    cursor.execute(sql_max, [item_id])
                    row_max = cursor.fetchone()

                    num_max, = row_max

                    for operations_item in Operations_item.objects.filter(num=num, item_id=item_id):
                        num_max += 1
                        operations_item.num = num_max
                        operations_item.save()

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'operation_id': record.operation.id,
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
            'parent_id': record.parent.id if record.parent else None,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return Operations_itemQuerySet(self.model, using=self._db)

    def _rec_def_resources(self, operationitem):
        from kaf_pas.production.models.operation_def_resources import Operation_def_resources
        from kaf_pas.production.models.operation_resources import Operation_resources
        for operation_def_resource in Operation_def_resources.objects.filter(operation=operationitem.operation):
            Operation_resources.objects.get_or_create(
                operationitem=operationitem,
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
                            __res = model_to_dict(_res)
                            setAttr(__res, 'operation__full_name', _res.operation.full_name)
                            res.append(__res)
                elif isinstance(item_id, list):
                    delAttr(_data, 'item_id')
                    for oparation in oparations:
                        for item in item_id:
                            setAttr(_data, 'operation_id', oparation)
                            setAttr(_data, 'item_id', item)
                            _res, created = super().get_or_create(**_data)
                            if created:
                                self._rec_def_resources(_res)
                                __res = model_to_dict(_res)
                                setAttr(__res, 'operation__full_name', _res.operation.full_name)
                                res.append(__res)

        return res

    def updateFromRequest(self, request):
        request = DSRequest(request=request)
        data = request.get_data()
        _data = data.copy()

        if isinstance(_data, dict):
            for k, v in _data.items():
                data1 = dict()
                if isinstance(v, dict):
                    delAttr(v, 'operation__full_name')
                    for k1, v1 in v.items():
                        if k1.find('_') == -1:
                            data1.setdefault(k1, v1)
                    data1.setdefault('_operation', 'update')
                    res = super().filter(id=v.get('id')).update(**data1)
                else:
                    delAttr(_data, 'operation__full_name')
                    res = super().filter(id=data.get('id')).update(**_data)
                    break
        else:
            delAttr(_data, 'operation__full_name')
            res = super().filter(id=data.get('id')).update(**_data)

        return res


class Operations_item(Hierarcy):
    description = DescriptionField()
    ed_izm = ForeignKeyProtect(Ed_izm, default=None, null=True, blank=True)
    item = ForeignKeyProtect(Item)
    num = PositiveIntegerField(default=None, null=True, blank=True)
    operation = ForeignKeyProtect(Operations)
    qty = PositiveIntegerField(default=None, null=True, blank=True)

    objects = Operations_itemManager()

    def __str__(self):
        return f"ID:{self.id}, item: [{self.item}], id_izm: [{self.ed_izm}], qty: {self.qty}, num: {self.num}"

    class Meta:
        verbose_name = 'Кросс таблица'
        unique_together = (('item', 'operation'),)
