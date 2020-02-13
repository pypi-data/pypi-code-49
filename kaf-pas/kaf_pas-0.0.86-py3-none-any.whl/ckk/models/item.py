import logging

from bitfield import BitField, BitHandler
from django.db import transaction
from django.db.models import PositiveIntegerField, BigIntegerField, UniqueConstraint, Q
from django.forms import model_to_dict

from isc_common import getAttr, setAttr, delAttr
from isc_common.fields.related import ForeignKeyProtect
from isc_common.http.DSRequest import DSRequest
from isc_common.managers.common_managet_with_lookup_fields import CommonManagetWithLookUpFieldsManager, CommonManagetWithLookUpFieldsQuerySet
from isc_common.models.audit import AuditModel
from isc_common.progress import managed_progress
from kaf_pas.ckk.models import get_operations_from_trunsaction
from kaf_pas.kd.models.document_attributes import Document_attributes
from kaf_pas.kd.models.documents import Documents
from kaf_pas.kd.models.lotsman_documents_hierarcy import Lotsman_documents_hierarcy

logger = logging.getLogger(__name__)


class ItemQuerySet(CommonManagetWithLookUpFieldsQuerySet):

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class ItemManager(CommonManagetWithLookUpFieldsManager):

    def createFromRequest(self, request):
        from kaf_pas.ckk.models.item_refs import Item_refs

        request = DSRequest(request=request)
        data = request.get_data()
        _data = data.copy()

        parent = _data.get('parent')
        if parent:
            delAttr(_data, 'parent')
            setAttr(_data, 'parent_id', parent)

        delAttr(_data, 'STMP_1__value_str')
        delAttr(_data, 'STMP_2__value_str')

        props = 0

        props |= Item.props.relevant
        props |= Item.props.man_input

        delAttr(_data, 'relevant')
        delAttr(_data, 'where_from')
        setAttr(_data, 'props', props)

        res = super().create(**_data)
        logger.debug(f'Added: {res}')

        # if not data.get('parent_id'):
        #     raise Exception('Не выбран родительский узел.')

        item_refs, create = Item_refs.objects.get_or_create(parent_id=_data.get('parent_id'), child=res)
        if create:
            logger.debug(f'Added item_ref: {item_refs}')

        res = model_to_dict(res)

        props = getAttr(res, 'props')
        if props and isinstance(props, BitHandler):
            props = getAttr(res, 'props')._value
            setAttr(res, 'props', props)
        setAttr(res, 'isFolder', False)
        data.update(res)
        return data

    @staticmethod
    def delete_recursive(item_id, delete_lines=False, soft_delete=False, user=None):
        with transaction.atomic():
            from isc_common.management.commands.refresh_mat_views import refresh_mat_view
            from kaf_pas.ckk.models.item_image_refs import Item_image_refs
            from kaf_pas.ckk.models.item_line import Item_line
            from kaf_pas.ckk.models.item_refs import Item_refs
            from kaf_pas.production.models.operations_item import Operations_item
            from kaf_pas.production.models.ready_2_launch_detail import Ready_2_launch_detail

            item_lotsman_document_cnt = 0
            cnt = Item_refs.objects.get_descendants_count(id=item_id)

            with managed_progress(
                    id=f'delete_recursive_{item_id}',
                    qty=cnt,
                    user=user,
                    message='Удаление товарной(ых) позиций',
                    title='Выполнено'
            ) as progress:
                item = Item.objects.get(id=item_id)
                if cnt == 0:
                    item.delete()
                    return 1

                progress.setContentsLabel(f'''<h3>Удаление товарной позиции ({item.STMP_1.value_str if item.STMP_1 else ''} : {item.STMP_2.value_str if item.STMP_2 else ''}).</h3>''')
                for item in Item_refs.objects.get_descendants(id=item_id, order_by_clause='order by level desc'):
                    if not soft_delete:
                        Item_image_refs.objects.filter(item_id=item.child_id).delete()

                        if delete_lines:
                            Item_line.objects.filter(parent_id=item.child_id).delete()
                            Item_line.objects.filter(child_id=item.child_id).delete()

                        Item_refs.objects.filter(parent_id=item.child_id).delete()
                        Item_refs.objects.filter(child_id=item.child_id).delete()

                        Operations_item.objects.filter(item=item.child_id).delete()
                        Ready_2_launch_detail.objects.filter(item=item.child_id).delete()

                        Item.objects.filter(id=item.child_id).delete()

                    else:
                        Item_image_refs.objects.filter(item_id=item.child_id).soft_delete()

                        if delete_lines:
                            Item_line.objects.filter(parent_id=item.child_id).soft_delete()
                            Item_line.objects.filter(child_id=item.child_id).soft_delete()

                        Item_refs.objects.filter(parent_id=item.child_id).soft_delete()
                        Item_refs.objects.filter(child_id=item.child_id).soft_delete()
                        Item.objects.filter(id=item.child_id).soft_delete()

                    if progress:
                        progress.step()
                if item_lotsman_document_cnt > 0:
                    refresh_mat_view('kd_lotsman_documents_hierarcy_mview')

    def updateFromRequest(self, request, removed=None, function=None):
        from kaf_pas.ckk.models.item_refs import Item_refs
        from kaf_pas.ckk.models.item_line import Item_line

        if not isinstance(request, DSRequest):
            request = DSRequest(request=request)
        data = request.get_data()

        with transaction.atomic():
            targetRecord = data.get('targetRecord')
            dropRecords = data.get('dropRecords')
            if data.get('mode') == 'move':
                res = 0
                for dropRecord in dropRecords:
                    res += Item_refs.objects.filter(parent_id=dropRecord.get('parent_id'), child_id=dropRecord.get('id')).update(parent_id=targetRecord.get('id'))
                    res += Item_line.objects.filter(parent_id=dropRecord.get('parent_id'), child_id=dropRecord.get('id')).update(parent_id=targetRecord.get('id'))
                return res
            elif data.get('mode') == 'copy':
                res = 0
                for dropRecord in dropRecords:
                    Item_refs.objects.create(parent_id=targetRecord.get('id'), child_id=dropRecord.get('id'))
                    res += 1
                return res
            elif data.get('mode') == 'replace':
                res = 0
                for dropRecord in dropRecords:
                    Item_refs.objects.create(parent_id=targetRecord.get('parent_id'), child_id=dropRecord.get('id'))
                    res += 1

                    item_line = model_to_dict(Item_line.objects.get(parent_id=targetRecord.get('parent_id'), child_id=targetRecord.get('id')))
                    delAttr(item_line, 'id')
                    delAttr(item_line, 'parent')
                    delAttr(item_line, 'child')
                    setAttr(item_line, 'parent_id', targetRecord.get('parent_id'))
                    setAttr(item_line, 'child_id', dropRecord.get('id'))
                    setAttr(item_line, 'SPC_CLM_NAME_id', dropRecord.get('STMP_1_id'))
                    delAttr(item_line, 'SPC_CLM_NAME')
                    setAttr(item_line, 'SPC_CLM_MARK_id', dropRecord.get('STMP_2_id'))
                    delAttr(item_line, 'SPC_CLM_MARK')
                    setAttr(item_line, 'SPC_CLM_FORMAT_id', getAttr(item_line, 'SPC_CLM_FORMAT'))
                    delAttr(item_line, 'SPC_CLM_FORMAT')
                    setAttr(item_line, 'SPC_CLM_ZONE_id', getAttr(item_line, 'SPC_CLM_ZONE'))
                    delAttr(item_line, 'SPC_CLM_ZONE')
                    setAttr(item_line, 'SPC_CLM_POS_id', getAttr(item_line, 'SPC_CLM_POS'))
                    delAttr(item_line, 'SPC_CLM_POS')
                    setAttr(item_line, 'SPC_CLM_COUNT_id', getAttr(item_line, 'SPC_CLM_COUNT'))
                    delAttr(item_line, 'SPC_CLM_COUNT')
                    setAttr(item_line, 'SPC_CLM_NOTE_id', getAttr(item_line, 'SPC_CLM_NOTE'))
                    delAttr(item_line, 'SPC_CLM_NOTE')
                    setAttr(item_line, 'SPC_CLM_MASSA_id', getAttr(item_line, 'SPC_CLM_MASSA'))
                    delAttr(item_line, 'SPC_CLM_MASSA')
                    setAttr(item_line, 'SPC_CLM_MATERIAL_id', getAttr(item_line, 'SPC_CLM_MATERIAL'))
                    delAttr(item_line, 'SPC_CLM_MATERIAL')
                    setAttr(item_line, 'SPC_CLM_USER_id', getAttr(item_line, 'SPC_CLM_USER'))
                    delAttr(item_line, 'SPC_CLM_USER')
                    setAttr(item_line, 'SPC_CLM_KOD_id', getAttr(item_line, 'SPC_CLM_KOD'))
                    delAttr(item_line, 'SPC_CLM_KOD')
                    setAttr(item_line, 'SPC_CLM_FACTORY_id', getAttr(item_line, 'SPC_CLM_FACTORY'))
                    delAttr(item_line, 'SPC_CLM_FACTORY')
                    Item_line.objects.create(**item_line)
                    res += 1

                    Item_refs.objects.filter(parent_id=targetRecord.get('parent_id'), child_id=targetRecord.get('id')).delete()
                    Item_line.objects.filter(parent_id=targetRecord.get('parent_id'), child_id=targetRecord.get('id')).delete()

                    try:
                        Item.objects.filter(id=targetRecord.get('id')).delete()
                    except Exception as ex:
                        logger.debug(ex)

                return res

            else:
                def rec(data):
                    relevant = data.get('relevant')
                    props = data.get('props')

                    if relevant == 'Актуален':
                        props |= Item.props.relevant
                    else:
                        props &= ~Item.props.relevant

                    where_from = data.get('where_from')
                    if where_from == 'Получено из чертежа':
                        props |= Item.props.from_cdw
                    elif where_from == 'Получено из спецификации':
                        props |= Item.props.from_spw
                    elif where_from == 'Получено из бумажного архива':
                        props |= Item.props.from_pdf
                    elif where_from == 'Занесено вручную':
                        props |= Item.props.man_input

                    delAttr(data, 'relevant')
                    delAttr(data, 'where_from')
                    delAttr(data, 'qty_operations')
                    delAttr(data, 'refs_props')
                    delAttr(data, 'icon')
                    setAttr(data, 'props', props)

                    return self.filter(id=data.get('id')).update(**data)

                if isinstance(data, dict):
                    for k, _data in data.items():
                        if isinstance(_data, dict):
                            res = rec(_data)
                        else:
                            res = rec(data.copy())
                else:
                    res = 0

            return res

    def deleteFromRequest(self, request, removed=None, ):
        from kaf_pas.ckk.models.item_refs import Item_refs
        from kaf_pas.ckk.models.item_view import Item_view
        from kaf_pas.ckk.models.item_line import Item_line

        request = DSRequest(request=request)
        data = request.get_data()
        res = 0

        mode = None
        with transaction.atomic():
            operations = get_operations_from_trunsaction(data)
            if isinstance(operations, list):
                for operation in get_operations_from_trunsaction(data):
                    _data = operation.get('data')
                    if _data.get('mode') == 'deleteInner':
                        mode = 'deleteInner'
                        records = _data.get('records')

                        if isinstance(records, list):
                            for record in records:
                                res, _ = Item_refs.objects.filter(child_id=record.get('id'), parent_id=record.get('parent_id')).delete()

                if mode == 'deleteInner':
                    return res
            elif isinstance(data, dict):
                if data.get('mode') == 'deleteInner':
                    records = data.get('records')

                    if isinstance(records, list):
                        for record in records:
                            res, _ = Item_refs.objects.filter(child_id=record.get('id'), parent_id=record.get('parent_id')).delete()
                        return res
                elif data.get('mode') == 'deleteCyclingRefs':
                    records = data.get('records')
                    res = 0
                    if isinstance(records, list):
                        for record in records:
                            id = record.get('id')
                            parent_id = record.get('parent_id')

                            for item in Item_view.objects.raw('''select *
                                                        from ckk_item_view
                                                        where parent_id in (select id
                                                                            from ckk_item_view
                                                                            where parent_id = %s
                                                                              and "isFolder" = true)
                                                          and child_id = %s''', [id, id]):
                                item_refs = Item_refs.objects.get(id=item.refs_id)
                                item_refs.delete()
                                res += 1
                    return res
                elif data.get('mode') == 'reloadRefs':
                    records = data.get('records')
                    res = 0
                    if isinstance(records, list):
                        for record in records:
                            id = record.get('id')
                            parent_id = record.get('parent_id')

                            for item_line in Item_line.objects.filter(parent_id=id):
                                item_refs, _ = Item_refs.objects.get_or_create(parent_id=id, child=item_line.child)
                                res += 1

                    return res

        with transaction.atomic():
            for id, mode in request.get_tuple_ids():
                if mode == 'hide':
                    res = self.delete_recursive(item_id=id, soft_delete=True, delete_lines=True, user=request.user_id)
                else:
                    res = self.delete_recursive(item_id=id, soft_delete=False, delete_lines=True, user=request.user_id)
        return res

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'STMP_1_id': record.STMP_1.id if record.STMP_1 else None,
            'STMP_1__value_str': record.STMP_1.value_str if record.STMP_1 else None,
            'STMP_2_id': record.STMP_2.id if record.STMP_2 else None,
            'STMP_2__value_str': record.STMP_2.value_str if record.STMP_2 else None,
            'lastmodified': record.lastmodified,
            'version': record.version,
            'document_id': record.document.id if record.document else None,
            'document__file_document': record.document.file_document if record.document else None,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return ItemQuerySet(self.model, using=self._db)


class Item_add:
    @staticmethod
    def get_prop_field():
        return BitField(flags=(
            ('relevant', 'Актуальность'),  # 1
            ('from_cdw', 'Получено из чертежа'),  # 2
            ('from_spw', 'Получено из спецификации'),  # 4
            ('for_line', 'Строка спецификации'),  # 8
            ('from_pdf', 'Получено из бумажного архива'),  # 16
            ('man_input', 'Занесено вручную'),  # 32
            ('copied', 'Скопировано'),  # 64
            ('from_lotsman', 'Получено из Лоцмана'),  # 128
        ), default=1, db_index=True)


class Item(AuditModel):
    STMP_1 = ForeignKeyProtect(Document_attributes, verbose_name='Наименование изделия', related_name='STMP_1', null=True, blank=True)
    STMP_2 = ForeignKeyProtect(Document_attributes, verbose_name='Обозначение изделия', related_name='STMP_2', null=True, blank=True)
    version = PositiveIntegerField(null=True, blank=True)

    props = Item_add.get_prop_field()

    document = ForeignKeyProtect(Documents, verbose_name='Документ', null=True, blank=True)
    lotsman_document = ForeignKeyProtect(Lotsman_documents_hierarcy, verbose_name='Документ из Лоцмана', null=True, blank=True)
    lotsman_type_id = BigIntegerField(null=True, blank=True)

    objects = ItemManager()

    @property
    def item_name(self):
        if self.STMP_1 != None and self.STMP_2 != None:
            return f'{self.STMP_1.value_str}: {self.STMP_2.value_str}'
        elif self.STMP_1 == None and self.STMP_2 != None:
            return self.STMP_2.value_str
        elif self.STMP_1 != None and self.STMP_2 == None:
            return self.STMP_1.value_str
        else:
            return 'Неизвестен'

    @staticmethod
    def get_vaslue_str(doc_attr):
        if doc_attr.value_str == None:
            return None
        return doc_attr.value_str.strip() if doc_attr else None

    def save(self, *args, **kwargs):
        if ~self.props.relevant:
            item = Item.objects.filter()
            from django.db.models import Max

            res = item.aggregate(Max('version'))
            self.version = 1 if not res.get('version__max') else res.get('version__max') + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f'ID={self.id} STMP_1=[{self.STMP_1}], STMP_2=[{self.STMP_2}], props={self.props}, version={self.version}'

    def __repr__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Товарная позиция'
        constraints = [
            UniqueConstraint(fields=['props'], condition=Q(STMP_1=None) & Q(STMP_2=None) & Q(lotsman_document_id=None) & Q(lotsman_type_id=None) & Q(version=None), name='Item_unique_constraint_0'),
            UniqueConstraint(fields=['STMP_1', 'props'], condition=Q(STMP_2=None) & Q(lotsman_document_id=None) & Q(lotsman_type_id=None) & Q(version=None), name='Item_unique_constraint_1'),
            UniqueConstraint(fields=['STMP_2', 'props'], condition=Q(STMP_1=None) & Q(lotsman_document_id=None) & Q(lotsman_type_id=None) & Q(version=None), name='Item_unique_constraint_2'),
            UniqueConstraint(fields=['STMP_1', 'STMP_2', 'props'], condition=Q(lotsman_document_id=None) & Q(lotsman_type_id=None) & Q(version=None), name='Item_unique_constraint_3'),
            UniqueConstraint(fields=['props', 'version'], condition=Q(STMP_1=None) & Q(STMP_2=None) & Q(lotsman_document_id=None) & Q(lotsman_type_id=None), name='Item_unique_constraint_4'),
            UniqueConstraint(fields=['STMP_1', 'props', 'version'], condition=Q(STMP_2=None) & Q(lotsman_document_id=None) & Q(lotsman_type_id=None), name='Item_unique_constraint_5'),
            UniqueConstraint(fields=['STMP_2', 'props', 'version'], condition=Q(STMP_1=None) & Q(lotsman_document_id=None) & Q(lotsman_type_id=None), name='Item_unique_constraint_6'),
            UniqueConstraint(fields=['STMP_1', 'STMP_2', 'props', 'version'], condition=Q(lotsman_document_id=None) & Q(lotsman_type_id=None), name='Item_unique_constraint_7'),
            UniqueConstraint(fields=['lotsman_document_id', 'props'], condition=Q(STMP_1=None) & Q(STMP_2=None) & Q(lotsman_type_id=None) & Q(version=None), name='Item_unique_constraint_8'),
            UniqueConstraint(fields=['STMP_1', 'lotsman_document_id', 'props'], condition=Q(STMP_2=None) & Q(lotsman_type_id=None) & Q(version=None), name='Item_unique_constraint_9'),
            UniqueConstraint(fields=['STMP_2', 'lotsman_document_id', 'props'], condition=Q(STMP_1=None) & Q(lotsman_type_id=None) & Q(version=None), name='Item_unique_constraint_10'),
            UniqueConstraint(fields=['STMP_1', 'STMP_2', 'lotsman_document_id', 'props'], condition=Q(lotsman_type_id=None) & Q(version=None), name='Item_unique_constraint_11'),
            UniqueConstraint(fields=['lotsman_document_id', 'props', 'version'], condition=Q(STMP_1=None) & Q(STMP_2=None) & Q(lotsman_type_id=None), name='Item_unique_constraint_12'),
            UniqueConstraint(fields=['STMP_1', 'lotsman_document_id', 'props', 'version'], condition=Q(STMP_2=None) & Q(lotsman_type_id=None), name='Item_unique_constraint_13'),
            UniqueConstraint(fields=['STMP_2', 'lotsman_document_id', 'props', 'version'], condition=Q(STMP_1=None) & Q(lotsman_type_id=None), name='Item_unique_constraint_14'),
            UniqueConstraint(fields=['STMP_1', 'STMP_2', 'lotsman_document_id', 'props', 'version'], condition=Q(lotsman_type_id=None), name='Item_unique_constraint_15'),
            UniqueConstraint(fields=['lotsman_type_id', 'props'], condition=Q(STMP_1=None) & Q(STMP_2=None) & Q(lotsman_document_id=None) & Q(version=None), name='Item_unique_constraint_16'),
            UniqueConstraint(fields=['STMP_1', 'lotsman_type_id', 'props'], condition=Q(STMP_2=None) & Q(lotsman_document_id=None) & Q(version=None), name='Item_unique_constraint_17'),
            UniqueConstraint(fields=['STMP_2', 'lotsman_type_id', 'props'], condition=Q(STMP_1=None) & Q(lotsman_document_id=None) & Q(version=None), name='Item_unique_constraint_18'),
            UniqueConstraint(fields=['STMP_1', 'STMP_2', 'lotsman_type_id', 'props'], condition=Q(lotsman_document_id=None) & Q(version=None), name='Item_unique_constraint_19'),
            UniqueConstraint(fields=['lotsman_type_id', 'props', 'version'], condition=Q(STMP_1=None) & Q(STMP_2=None) & Q(lotsman_document_id=None), name='Item_unique_constraint_20'),
            UniqueConstraint(fields=['STMP_1', 'lotsman_type_id', 'props', 'version'], condition=Q(STMP_2=None) & Q(lotsman_document_id=None), name='Item_unique_constraint_21'),
            UniqueConstraint(fields=['STMP_2', 'lotsman_type_id', 'props', 'version'], condition=Q(STMP_1=None) & Q(lotsman_document_id=None), name='Item_unique_constraint_22'),
            UniqueConstraint(fields=['STMP_1', 'STMP_2', 'lotsman_type_id', 'props', 'version'], condition=Q(lotsman_document_id=None), name='Item_unique_constraint_23'),
            UniqueConstraint(fields=['lotsman_document_id', 'lotsman_type_id', 'props'], condition=Q(STMP_1=None) & Q(STMP_2=None) & Q(version=None), name='Item_unique_constraint_24'),
            UniqueConstraint(fields=['STMP_1', 'lotsman_document_id', 'lotsman_type_id', 'props'], condition=Q(STMP_2=None) & Q(version=None), name='Item_unique_constraint_25'),
            UniqueConstraint(fields=['STMP_2', 'lotsman_document_id', 'lotsman_type_id', 'props'], condition=Q(STMP_1=None) & Q(version=None), name='Item_unique_constraint_26'),
            UniqueConstraint(fields=['STMP_1', 'STMP_2', 'lotsman_document_id', 'lotsman_type_id', 'props'], condition=Q(version=None), name='Item_unique_constraint_27'),
            UniqueConstraint(fields=['lotsman_document_id', 'lotsman_type_id', 'props', 'version'], condition=Q(STMP_1=None) & Q(STMP_2=None), name='Item_unique_constraint_28'),
            UniqueConstraint(fields=['STMP_1', 'lotsman_document_id', 'lotsman_type_id', 'props', 'version'], condition=Q(STMP_2=None), name='Item_unique_constraint_29'),
            UniqueConstraint(fields=['STMP_2', 'lotsman_document_id', 'lotsman_type_id', 'props', 'version'], condition=Q(STMP_1=None), name='Item_unique_constraint_30'),
            UniqueConstraint(fields=['STMP_1', 'STMP_2', 'lotsman_document_id', 'lotsman_type_id', 'props', 'version'], name='Item_unique_constraint_31'),
        ]
        db_constraints = {
            'Item_not_null_STMP1_STMP2': 'CHECK ("STMP_1_id" IS NOT NULL OR "STMP_2_id" IS NOT NULL)',
        }
