import logging

from django.db import transaction, connection
from django.db.models import PositiveIntegerField, OneToOneField, CASCADE
from django.forms import model_to_dict

from isc_common import delAttr, setAttr
from isc_common.fields.related import ForeignKeyProtect
from isc_common.http.DSRequest import DSRequest
from isc_common.managers.common_managet_with_lookup_fields import CommonManagetWithLookUpFieldsManager, CommonManagetWithLookUpFieldsQuerySet
from isc_common.models.audit import AuditModel
from kaf_pas.ckk.models.locations import Locations
from kaf_pas.production.models.operations_item import Operations_item
from kaf_pas.production.models.resource import Resource

logger = logging.getLogger(__name__)


class Operation_resourcesQuerySet(CommonManagetWithLookUpFieldsQuerySet):
    def create(self, **kwargs):
        if kwargs.get('resource'):
            setAttr(kwargs, 'resource_id', kwargs.get('resource').id)
            delAttr(kwargs, 'resource')

        if kwargs.get('location'):
            setAttr(kwargs, 'location_id', kwargs.get('location').id)
            delAttr(kwargs, 'location')

        if not kwargs.get('resource_id') and not kwargs.get('location_id'):
            raise Exception('Необходим хотябы один выпбранный параметр.')
        delAttr(kwargs, 'resource__full_name')
        delAttr(kwargs, 'location__full_name')

        resource_id = kwargs.get('resource_id')
        if resource_id:
            setAttr(kwargs, 'location_id', Resource.objects.get(id=resource_id).location.id)

        setAttr(kwargs, '_operation', 'create')
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Operation_resourcesManager(CommonManagetWithLookUpFieldsManager):

    @staticmethod
    def refresh_resource(apps=None, schema_editor=None):
        sql_text = '''select  operationitem_id, count(*)
                    from production_operation_resources
                    group by operationitem_id
                    having count(*) > 1'''

        sql_items = f'''select id
            from production_operation_resources
            where operationitem_id = %s'''

        with transaction.atomic():
            with connection.cursor() as cursor:
                cursor.execute(sql_text)
                rows = cursor.fetchall()
                for row in rows:
                    operationitem_id, count = row
                    # print(f'launch_operationitem_id: {launch_operationitem_id}')
                    cursor.execute(sql_items, [operationitem_id])
                    rows_item = cursor.fetchall()

                    first_step = True
                    for item in rows_item:
                        id, = item
                        if not first_step:
                            # print(f'id: {id}')
                            res = Operation_resources.objects.filter(id=id).delete()
                            # print(res)
                        else:
                            first_step = False

    def createFromRequest(self, request):
        request = DSRequest(request=request)
        data = request.get_data()
        _data = data.copy()
        operationitem_id = _data.get('operationitem_id')

        res = []
        if isinstance(operationitem_id, list):
            delAttr(_data, 'operationitem_id')
            with transaction.atomic():
                for operationitem in operationitem_id:
                    setAttr(_data, 'operationitem_id', operationitem)
                    delAttr(_data, 'location__full_name')
                    delAttr(_data, 'resource__full_name')
                    operation_resource, created = super().get_or_create(**_data)
                    if created:
                        _res = model_to_dict(operation_resource)
                        setAttr(_res, 'location__full_name', operation_resource.location.full_name if operation_resource.location else None)
                        setAttr(_res, 'resource__full_name', operation_resource.resource.full_name if operation_resource.resource else None)
                        res.append(_res)
        else:
            delAttr(_data, 'location__full_name')
            delAttr(_data, 'resource__full_name')
            operation_resource, created = super().get_or_create(**_data)
            if created:
                _res = model_to_dict(operation_resource)
                setAttr(_res, 'location__full_name', operation_resource.location.full_name if operation_resource.location else None)
                setAttr(_res, 'resource__full_name', operation_resource.resource.full_name if operation_resource.resource else None)
                res.append(_res)
        return res

    def updateFromRequest(self, request, removed=None, function=None):
        if not isinstance(request, DSRequest):
            request = DSRequest(request=request)
        data = request.get_data()

        self._remove_prop(data, removed)
        _data = self.clone_data(data)
        delAttr(_data, 'id')
        res = super().filter(id=data.get('id')).update(**_data)
        return res

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'operationitem_id': record.operationitem.id if record.operationitem else None,
            'resource_id': record.resource.id if record.resource else None,
            'resource__code': record.resource.code if record.resource else None,
            'resource__name': record.resource.name if record.resource else None,
            'resource__full_name': record.resource.full_name if record.resource else None,
            'location_id': record.location.id if record.location else None,
            'location__code': record.location.code if record.location else None,
            'location__name': record.location.name if record.location else None,
            'location__full_name': record.location.full_name if record.location else None,
            'complex_name': record.complex_name,
            'batch_size': record.batch_size,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return Operation_resourcesQuerySet(self.model, using=self._db)


class Operation_resources(AuditModel):
    operationitem = OneToOneField(Operations_item, on_delete=CASCADE)
    resource = ForeignKeyProtect(Resource, null=True, blank=True)
    location = ForeignKeyProtect(Locations, null=True, blank=True)
    batch_size = PositiveIntegerField(default=1)

    @property
    def complex_name(self):
        return f'{self.resource.location.full_name}{self.resource.full_name}' if self.resource else None

    objects = Operation_resourcesManager()

    def __str__(self):
        return f"{self.id}, operationitem: [{self.operationitem}], resource: [{self.resource}], location: [{self.location}]"

    def __repr__(self):
        return str(self.resource) if self.resource else str(self.location)

    class Meta:
        verbose_name = 'Кросс таблица'
