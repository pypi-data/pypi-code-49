import logging

from django.db.models import BooleanField, PositiveIntegerField

from isc_common import delAttr
from isc_common.fields.name_field import NameField
from isc_common.fields.related import ForeignKeyProtect
from isc_common.http.DSRequest import DSRequest
from isc_common.models.audit import AuditQuerySet, AuditManager
from isc_common.models.base_ref import Hierarcy
from kaf_pas.ckk.models.item import Item_add
from kaf_pas.kd.models.document_attributes import Document_attributes
from kaf_pas.kd.models.documents import Documents
from kaf_pas.kd.models.lotsman_documents_hierarcy import Lotsman_documents_hierarcy
from kaf_pas.planing.models.operations_view import Operations_view

logger = logging.getLogger(__name__)


class Item_flat_viewQuerySet(AuditQuerySet):

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)

    def get_infoPlan(self, request, *args):
        request = DSRequest(request=request)
        data = request.get_data()
        item_ids = [item.get('item_id') for item in Operations_view.objects.filter(
            launch_id=data.get('launch_id'),
            operation_level_id=data.get('level_id'),
            resource_id=data.get('resource_id'),
            resource__location_id=data.get('location_id'),
        ).values('item_id').distinct()]

        delAttr(request.json.get('data'), 'full_name')
        delAttr(request.json.get('data'), 'launch_id')
        delAttr(request.json.get('data'), 'level_id')
        delAttr(request.json.get('data'), 'resource_id')
        delAttr(request.json.get('data'), 'location_id')

        # criteria = self.get_criteria(json=request.json)
        cnt = super().filter(id__in=item_ids).count()
        cnt_all = super().filter().count()
        return dict(qty_rows=cnt, all_rows=cnt_all)


class Item_flat_viewManager(AuditManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'STMP_1_id': record.STMP_1.id if record.STMP_1 else None,
            'STMP_1__value_str': record.STMP_1.value_str if record.STMP_1 else None,
            'STMP_2_id': record.STMP_2.id if record.STMP_2 else None,
            'STMP_2__value_str': record.STMP_2.value_str if record.STMP_2 else None,
            'lastmodified': record.lastmodified,
            'document_id': record.document.id if record.document else None,
            'document__file_document': record.document.file_document if record.document else None,
            'lotsman_document_id': record.lotsman_document.id if record.lotsman_document else None,
            'editing': record.editing,
            'deliting': record.deliting,
            'isFolder': record.isFolder,
            'relevant': record.relevant,
            'where_from': record.where_from,
            'version': record.version,
            'props': int(record.props),
        }
        # print(res)
        return res

    def get_queryset(self):
        return Item_flat_viewQuerySet(self.model, using=self._db)


class Item_flat_view(Hierarcy):
    STMP_1 = ForeignKeyProtect(Document_attributes, verbose_name='Наименование изделия', related_name='STMP_1_flat_view', null=True, blank=True)
    STMP_2 = ForeignKeyProtect(Document_attributes, verbose_name='Обозначение изделия', related_name='STMP_2_flat_view', null=True, blank=True)
    document = ForeignKeyProtect(Documents, verbose_name='Документ', null=True, blank=True)
    lotsman_document = ForeignKeyProtect(Lotsman_documents_hierarcy, verbose_name='Документ', null=True, blank=True)
    relevant = NameField()
    where_from = NameField()
    props = Item_add.get_prop_field()
    version = PositiveIntegerField(null=True, blank=True)

    isFolder = BooleanField()

    objects = Item_flat_viewManager()

    @property
    def item(self):
        from kaf_pas.ckk.models.item import Item
        return Item.objects.get(id=self.id)

    def __str__(self):
        return f"ID={self.id} STMP_1=[{self.STMP_1}], STMP_2=[{self.STMP_2}], props={self.props}"

    class Meta:
        managed = False
        db_table = 'ckk_item_flat_view'
        verbose_name = 'Товарная позиция'
