import logging
import sys

from django.db import transaction

from isc_common import setAttr
from isc_common.http.DSRequest import DSRequest
from kaf_pas.kd.models.document_attributes import Document_attributes, Document_attributesManager
from kaf_pas.kd.models.document_attrs_view import Document_attrs_view, Document_attrs_viewManager, Document_attrs_viewQuerySet

logger = logging.getLogger(__name__)


class Spw_attrsQuerySet(Document_attrs_viewQuerySet):
    def __str__(self):
        return self.query

    def filter(self, *args, **kwargs):
        setAttr(kwargs, 'attr_type__code__contains', 'SPC')
        return super().filter(*args, **kwargs)

    @staticmethod
    def make_specification(queryResult):
        res = []
        attr_typee_id = sys.maxsize
        id = None
        r = None
        max_position_in_raw_document = None

        index = queryResult.count()
        for record in queryResult:
            if attr_typee_id > record.attr_type.id:
                if r:
                    setAttr(r, 'id', id)
                    setAttr(r, 'max_position_in_raw_document', max_position_in_raw_document)
                    res.append(r.copy())
                id = None
                r = dict()
            attr_typee_id = record.attr_type.id
            setAttr(r, f'{record.attr_type.code}_ID', record.id)
            setAttr(r, record.attr_type.code, record.value_str)
            setAttr(r, 'document_id', record.document.id)
            setAttr(r, 'section', record.section)
            setAttr(r, 'subsection', record.subsection)
            setAttr(r, f'{record.attr_type.code}_position_in_document', record.position_in_document)
            max_position_in_raw_document = record.position_in_document
            setAttr(r, f'{record.attr_type.code}_cross_id', record.cross_id)
            setAttr(r, 'editing', True)
            setAttr(r, 'deliting', True)
            if id == None:
                id = str(record.id)
            else:
                id += f'${record.id}'
            index -= 1
            if index == 0:
                setAttr(r, 'id', id)
                res.append(r.copy())

        # for item in res:
        #     logger.debug(item)
        return res

    def get_range_rows1(self, request, function=None):
        request = DSRequest(request=request)
        self.alive_only = request.alive_only
        criteria = self.get_criteria(json=request.json)
        queryResult = self.filter(*[], criteria).order_by(*['position_in_document'])
        res = Spw_attrsQuerySet.make_specification(queryResult)
        return res


class Spw_attrsManager(Document_attrs_viewManager):

    @staticmethod
    def rec_document_attr(document_id, attr_type_id, code, attr_type__code, value_str, position, section, subsection):
        from kaf_pas.kd.models.document_attr_cross import Document_attr_cross
        from kaf_pas.kd.models.documents import Documents

        if attr_type_id == None:
            if code != None and attr_type__code != None:
                attr_type, _ = Document_attributesManager.get_or_create_attribute(attr_codes=code, value_str=attr_type__code)
                attr_type_id = attr_type.id

        if attr_type_id != None:
            value_int = None
            try:
                value_int = int(value_str)
            except:
                pass

            document = Documents.objects.get(id=document_id)
            document_attribute_old = Document_attributes.objects.get(id=attr_type_id)

            document_attr_cross_old = None
            try:
                document_attr_cross_old = Document_attr_cross.objects.get(
                    document=document,
                    attribute=document_attribute_old,
                    position_in_document=position
                )
            except Document_attr_cross.DoesNotExist:
                pass

            document_attribute, ctreated = Document_attributes.objects.get_or_create(
                attr_type=document_attribute_old.attr_type,
                value_str=value_str,
                value_int=value_int
            )

            position_in_document = None
            if document_attr_cross_old != None:
                position_in_document = document_attr_cross_old.position_in_document
                document_attr_cross_old.delete()

            res, created = Document_attr_cross.objects.get_or_create(
                attribute=document_attribute,
                document=document,
                position_in_document=position_in_document,
                section=section,
                subsection=subsection,
            )
            return res

    @staticmethod
    def update_rec_spesification(data):
        with transaction.atomic():
            attr_type__code = 'SPC_CLM_FORMAT'
            Spw_attrsManager.rec_document_attr(
                document_id=data.get('document_id'),
                code=attr_type__code,
                attr_type__code=data.get(attr_type__code),
                attr_type_id=data.get(f'{attr_type__code}_ID'),
                value_str=data.get(attr_type__code),
                position=data.get(f'{attr_type__code}_position_in_document'),
                section=data.get('section'),
                subsection=data.get('subsection'),
            )

            attr_type__code = 'SPC_CLM_ZONE'
            Spw_attrsManager.rec_document_attr(
                document_id=data.get('document_id'),
                code=attr_type__code,
                attr_type__code=data.get(attr_type__code),
                attr_type_id=data.get(f'{attr_type__code}_ID'),
                value_str=data.get(attr_type__code),
                position=data.get(f'{attr_type__code}_position_in_document'),
                section=data.get('section'),
                subsection=data.get('subsection'),
            )

            attr_type__code = 'SPC_CLM_POS'
            Spw_attrsManager.rec_document_attr(
                document_id=data.get('document_id'),
                code=attr_type__code,
                attr_type__code=data.get(attr_type__code),
                attr_type_id=data.get(f'{attr_type__code}_ID'),
                value_str=data.get(attr_type__code),
                position=data.get(f'{attr_type__code}_position_in_document'),
                section=data.get('section'),
                subsection=data.get('subsection'),
            )

            attr_type__code = 'SPC_CLM_MARK'
            Spw_attrsManager.rec_document_attr(
                document_id=data.get('document_id'),
                code=attr_type__code,
                attr_type__code=data.get(attr_type__code),
                attr_type_id=data.get(f'{attr_type__code}_ID'),
                value_str=data.get(attr_type__code),
                position=data.get(f'{attr_type__code}_position_in_document'),
                section=data.get('section'),
                subsection=data.get('subsection'),
            )

            attr_type__code = 'SPC_CLM_NAME'
            Spw_attrsManager.rec_document_attr(
                document_id=data.get('document_id'),
                code=attr_type__code,
                attr_type__code=data.get(attr_type__code),
                attr_type_id=data.get(f'{attr_type__code}_ID'),
                value_str=data.get(attr_type__code),
                position=data.get(f'{attr_type__code}_position_in_document'),
                section=data.get('section'),
                subsection=data.get('subsection'),
            )

            attr_type__code = 'SPC_CLM_COUNT'
            Spw_attrsManager.rec_document_attr(
                document_id=data.get('document_id'),
                code=attr_type__code,
                attr_type__code=data.get(attr_type__code),
                attr_type_id=data.get(f'{attr_type__code}_ID'),
                value_str=data.get(attr_type__code),
                position=data.get(f'{attr_type__code}_position_in_document'),
                section=data.get('section'),
                subsection=data.get('subsection'),
            )

            attr_type__code = 'SPC_CLM_NOTE'
            Spw_attrsManager.rec_document_attr(
                document_id=data.get('document_id'),
                code=attr_type__code,
                attr_type__code=data.get(attr_type__code),
                attr_type_id=data.get(f'{attr_type__code}_ID'),
                value_str=data.get(attr_type__code),
                position=data.get(f'{attr_type__code}_position_in_document'),
                section=data.get('section'),
                subsection=data.get('subsection'),
            )

            attr_type__code = 'SPC_CLM_MASSA'
            Spw_attrsManager.rec_document_attr(
                document_id=data.get('document_id'),
                code=attr_type__code,
                attr_type__code=data.get(attr_type__code),
                attr_type_id=data.get(f'{attr_type__code}_ID'),
                value_str=data.get(attr_type__code),
                position=data.get(f'{attr_type__code}_position_in_document'),
                section=data.get('section'),
                subsection=data.get('subsection'),
            )

            attr_type__code = 'SPC_CLM_MATERIAL'
            Spw_attrsManager.rec_document_attr(
                document_id=data.get('document_id'),
                code=attr_type__code,
                attr_type__code=data.get(attr_type__code),
                attr_type_id=data.get(f'{attr_type__code}_ID'),
                value_str=data.get(attr_type__code),
                position=data.get(f'{attr_type__code}_position_in_document'),
                section=data.get('section'),
                subsection=data.get('subsection'),
            )

            attr_type__code = 'SPC_CLM_USER'
            Spw_attrsManager.rec_document_attr(
                document_id=data.get('document_id'),
                code=attr_type__code,
                attr_type__code=data.get(attr_type__code),
                attr_type_id=data.get(f'{attr_type__code}_ID'),
                value_str=data.get(attr_type__code),
                position=data.get(f'{attr_type__code}_position_in_document'),
                section=data.get('section'),
                subsection=data.get('subsection'),
            )

            attr_type__code = 'SPC_CLM_KOD'
            Spw_attrsManager.rec_document_attr(
                document_id=data.get('document_id'),
                code=attr_type__code,
                attr_type__code=data.get(attr_type__code),
                attr_type_id=data.get(f'{attr_type__code}_ID'),
                value_str=data.get(attr_type__code),
                position=data.get(f'{attr_type__code}_position_in_document'),
                section=data.get('section'),
                subsection=data.get('subsection'),
            )

            attr_type__code = 'SPC_CLM_FACTORY'
            Spw_attrsManager.rec_document_attr(
                document_id=data.get('document_id'),
                code=attr_type__code,
                attr_type__code=data.get(attr_type__code),
                attr_type_id=data.get(f'{attr_type__code}_ID'),
                value_str=data.get(attr_type__code),
                position=data.get(f'{attr_type__code}_position_in_document'),
                section=data.get('section'),
                subsection=data.get('subsection'),
            )

    def updateFromRequest(self, request, removed=None, function=None):
        request = DSRequest(request=request)
        data = request.get_data()
        Spw_attrsManager.update_rec_spesification(data)
        return data

    def get_queryset(self):
        return Spw_attrsQuerySet(self.model, using=self._db)

    @staticmethod
    def getRecord(record):
        res = {
            "id": record.id,
            "document_id": record.document.id,
            "attr_type_id": record.attr_type.id,
            "attr_type__code": record.attr_type.code,
            "attr_type__name": record.attr_type.name,
            "attr_type__description": record.attr_type.description if record.attr_type else None,
            "section": record.section,
            "subsection": record.subsection,
            "position_in_document": record.position_in_document,
            "cross_id": record.cross_id,
            "value_str": record.value_str,
            "lastmodified": record.lastmodified,
            "editing": record.editing,
            "deliting": record.deliting,
        }
        return res

    @staticmethod
    def try_delete_attribute(id):
        Document_attributes.objects.filter(id=id).delete()


class Spw_attrs(Document_attrs_view):
    objects = Spw_attrsManager()

    class Meta:
        verbose_name = 'Аттрибуты Спецификаций'
        proxy = True
        managed = False
