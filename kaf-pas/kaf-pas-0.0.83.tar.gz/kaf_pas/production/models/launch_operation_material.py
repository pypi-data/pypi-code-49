import logging

from bitfield import BitField
from django.db import transaction
from django.db.models import DecimalField, UniqueConstraint, Q
from django.forms import model_to_dict

from isc_common import setAttr, delAttr
from isc_common.bit import IsBitOn
from isc_common.fields.related import ForeignKeyProtect, ForeignKeyCascade, ForeignKeySetNull
from isc_common.http.DSRequest import DSRequest
from isc_common.managers.common_managet_with_lookup_fields import CommonManagetWithLookUpFieldsManager, CommonManagetWithLookUpFieldsQuerySet
from isc_common.models.audit import AuditModel
from isc_common.number import DelProps
from kaf_pas.ckk.models.ed_izm import Ed_izm
from kaf_pas.ckk.models.material_askon import Material_askon
from kaf_pas.ckk.models.materials import Materials
from kaf_pas.production.models.launch_operations_item import Launch_operations_item
from kaf_pas.production.models.operation_material import Operation_material

logger = logging.getLogger(__name__)


class Launch_operations_materialQuerySet(CommonManagetWithLookUpFieldsQuerySet):
    def create(self, **kwargs):
        if kwargs.get('material'):
            setAttr(kwargs, 'material_id', kwargs.get('material').id)
            delAttr(kwargs, 'material')

        if kwargs.get('material_askon'):
            setAttr(kwargs, 'material_askon_id', kwargs.get('material_askon').id)
            delAttr(kwargs, 'material_askon')

        if not kwargs.get('material_id') and not kwargs.get('material_askon_id'):
            raise Exception('Необходим хотябы один выпбранный параметр.')
        setAttr(kwargs, '_operation', 'create')
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Launch_operations_materialManager(CommonManagetWithLookUpFieldsManager):

    def createFromRequest(self, request):
        request = DSRequest(request=request)
        data = request.get_data()
        _data = data.copy()
        launch_operationitem_id = _data.get('launch_operationitem_id')

        res = []
        if isinstance(launch_operationitem_id, list):
            delAttr(_data, 'launch_operationitem_id')
            with transaction.atomic():
                for launch_operationitem in launch_operationitem_id:
                    setAttr(_data, 'launch_operationitem_id', launch_operationitem)
                    operation_material, created = super().get_or_create(**_data)
                    if created:
                        _res = model_to_dict(operation_material)
                        setAttr(_res, 'material_askon__field0', operation_material.material_askon.field0 if operation_material.material_askon else None)
                        setAttr(_res, 'complex_name', operation_material.complex_name)
                        setAttr(_res, 'complex_gost', operation_material.complex_gost)
                        setAttr(_res, 'edizm__code', operation_material.edizm.code)
                        res.append(DelProps(_res))
        else:
            operation_material, created = super().get_or_create(**_data)
            if created:
                _res = model_to_dict(operation_material)
                setAttr(_res, 'material_askon__field0', operation_material.material_askon.field0 if operation_material.material_askon else None)
                setAttr(_res, 'complex_name', operation_material.complex_name)
                setAttr(_res, 'complex_gost', operation_material.complex_gost)
                setAttr(_res, 'edizm__code', operation_material.edizm.code)
                res.append(DelProps(_res))
        return res

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'operation_material_id': record.operation_material.id if record.operation_material else None,
            'launch_operationitem_id': record.launch_operationitem.id,
            'material_askon_id': record.material_askon.id if record.material_askon else None,
            'material_askon__field0': record.material_askon.field0 if record.material_askon else '',
            'material_id': record.material.id if record.material else None,
            'material__name': record.material.name if record.material else '',
            'complex_name': record.complex_name,
            'complex_gost': record.complex_gost,
            'edizm_id': record.edizm.id,
            'edizm__code': record.edizm.code,
            'edizm__name': record.edizm.name,
            'qty': record.qty,
            'props': record.props._value,
            'enabled': IsBitOn(record.props, 0),
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return Launch_operations_materialQuerySet(self.model, using=self._db)


class Launch_operations_material(AuditModel):
    operation_material = ForeignKeySetNull(Operation_material, null=True, blank=True)
    launch_operationitem = ForeignKeyCascade(Launch_operations_item)
    material = ForeignKeyProtect(Materials, null=True, blank=True)
    material_askon = ForeignKeyProtect(Material_askon, null=True, blank=True)
    edizm = ForeignKeyProtect(Ed_izm)
    qty = DecimalField(max_digits=10, decimal_places=4, default=0.0)

    props = BitField(flags=(
        ('enabled', 'Доступность в данной производственной спецификации'),  # 1
    ), default=1, db_index=True)

    @property
    def complex_name(self):
        if self.material:
            return f'{self.material.materials_type.full_name}{self.material.full_name}'
        else:
            return ''

    @property
    def complex_gost(self):
        if self.material:
            if self.material.materials_type.gost:
                return f'{self.material.materials_type.gost} / {self.material.gost}'
            else:
                return self.material.gost if self.material else ''
        else:
            return ''

    objects = Launch_operations_materialManager()

    def __str__(self):
        return f"{self.complex_name}"

    class Meta:
        verbose_name = 'Кросс таблица'
        constraints = [
            UniqueConstraint(fields=['launch_operationitem'], condition=Q(material=None) & Q(material_askon=None), name='Launch_operations_material_unique_constraint_0'),
            UniqueConstraint(fields=['launch_operationitem', 'material'], condition=Q(material_askon=None), name='Launch_operations_material_unique_constraint_1'),
            UniqueConstraint(fields=['launch_operationitem', 'material_askon'], condition=Q(material=None), name='Launch_operations_material_unique_constraint_2'),
            UniqueConstraint(fields=['launch_operationitem', 'material', 'material_askon'], name='Launch_operations_material_unique_constraint_3'),
        ]

