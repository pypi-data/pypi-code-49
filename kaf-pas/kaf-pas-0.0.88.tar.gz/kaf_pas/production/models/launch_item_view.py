import logging

from django.db.models import BigIntegerField, BooleanField, PositiveIntegerField

from isc_common.fields.code_field import CodeField
from isc_common.fields.name_field import NameField
from isc_common.fields.related import ForeignKeyProtect
from isc_common.http.DSRequest import DSRequest
from isc_common.models.audit import AuditManager
from isc_common.models.base_ref import Hierarcy
from isc_common.models.tree_audit import TreeAuditModelManager, TreeAuditModelQuerySet
from isc_common.number import DelProps
from kaf_pas.ckk.models.item import Item_add
from kaf_pas.ckk.models.item_line import Item_lineManager
from kaf_pas.kd.models.document_attributes import Document_attributes
from kaf_pas.kd.models.documents import Documents
from kaf_pas.production.models.launches import Launches

logger = logging.getLogger(__name__)


class Launch_item_viewQuerySet(TreeAuditModelQuerySet):
    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Launch_item_viewManager(AuditManager):

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
            'parent_id': record.parent_id,
            'launch_id': record.launch.id,
            'item_refs_id': record.item_refs_id,
            'editing': record.editing,
            'deliting': record.deliting,
            'isFolder': record.isFolder,
            'relevant': record.relevant,
            'version': record.version,
            'where_from': record.where_from,
            'props': record.props,
            'used': record.used,
            'icon': Item_lineManager.getIcon(record),
        }
        return DelProps(res)

    def updateFromRequest(self, request, removed=None, function=None):
        from kaf_pas.production.models.launch_item_refs import Launch_item_refs
        request = DSRequest(request=request)
        data = request.get_data()
        _data = data.copy()

        used = data.get('used', False)
        if used == True:
            Launch_item_refs.objects.update_or_create(id=data.get('item_refs_id'), defaults=dict(props=Launch_item_refs.props.enabled))
        else:
            Launch_item_refs.objects.update_or_create(id=data.get('item_refs_id'), defaults=dict(props=~Launch_item_refs.props.enabled))

        return data

    def get_queryset(self):
        return Launch_item_viewQuerySet(self.model, using=self._db)


class Launch_item_view(Hierarcy):
    STMP_1 = ForeignKeyProtect(Document_attributes, verbose_name='Наименование изделия', related_name='STMP_1_view_launch', null=True, blank=True)
    STMP_2 = ForeignKeyProtect(Document_attributes, verbose_name='Обозначение изделия', related_name='STMP_2_view_launch', null=True, blank=True)
    document = ForeignKeyProtect(Documents, verbose_name='Документ', null=True, blank=True)
    relevant = NameField()
    where_from = NameField()
    props = Item_add.get_prop_field()
    version = PositiveIntegerField(null=True, blank=True)
    section = CodeField(null=True, blank=True)
    item_refs_id = BigIntegerField()
    launch = ForeignKeyProtect(Launches, related_name='production_launch')

    isFolder = BooleanField()
    used = BooleanField()

    objects = Launch_item_viewManager()
    tree_objects = TreeAuditModelManager()

    def __str__(self):
        return f"ID: {self.id} STMP_1: [{self.STMP_1}], STMP_2: [{self.STMP_2}], props: {self.props}"

    class Meta:
        managed = False
        db_table = 'production_launch_item_view'
        verbose_name = 'Товарная позиция в производственной спецификации'
