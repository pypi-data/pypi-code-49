import logging

from django.db import connection
from django.db.models import BigIntegerField, BooleanField, PositiveIntegerField, TextField

from isc_common.fields.name_field import NameField
from isc_common.fields.related import ForeignKeyProtect
from isc_common.http.DSRequest import DSRequest
from isc_common.models.audit import AuditManager, AuditQuerySet, AuditModel
from isc_common.models.tree_audit import TreeAuditModelManager
from isc_common.number import DelProps
from kaf_pas.ckk.models.attr_type import Attr_type
from kaf_pas.kd.models.document_attributes import Document_attributes
from kaf_pas.kd.models.documents import Documents
from kaf_pas.kd.models.lotsman_documents_hierarcy import Lotsman_documents_hierarcyManager

logger = logging.getLogger(__name__)


class Lotsman_documents_hierarcy_viewQuerySet(AuditQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)

    def get_range_rows5(self, start=None, end=None, function=None, json=None, distinct_field_names=None, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute(f'''select min(level)
            from kd_lotsman_documents_hierarcy_recurs_view
            where document_id = {kwargs.get('document_id')}''')
            level_min = cursor.fetchone()[0]

            cursor.execute(f'''SELECT 'SELECT case when a.level = {level_min} then null
                                       else a.parent_id
                                       end as parent_id, ' || array_to_string(ARRAY(SELECT 'a' || '."' || c.column_name || '"'
                                                                                    FROM information_schema.columns As c
                                                                                    WHERE table_name = 'kd_lotsman_documents_hierarcy_recurs_view'
                                                                                      AND c.column_name NOT IN ('parent_id')
                                                                                         ), ',') || ' FROM kd_lotsman_documents_hierarcy_recurs_view as a where a.document_id={kwargs.get('document_id')}' as sqlstmt''')

            sqlstmt = cursor.fetchone()[0]

            m_view_recurs_doc_name = f'''kd_lotsman_documents_hierarcy_recurs_{kwargs.get('document_id')}_view'''

            sqlstmt = f'''DROP VIEW IF EXISTS {m_view_recurs_doc_name};
                          CREATE VIEW {m_view_recurs_doc_name} AS {sqlstmt};'''
            cursor.execute(sqlstmt)

            parent_str = f'parent_id is null'
            if kwargs.get('parent_id') != None:
                parent_str = f'''parent_id={kwargs.get('parent_id')}'''

            sqlstmt = f'''select * from {m_view_recurs_doc_name} 
                           where {parent_str}   
                             limit %s offset %s'''

        queryResult = Lotsman_documents_hierarcy_view.objects.raw(raw_query=sqlstmt, params=[end - start, start])
        return [function(record) for record in queryResult]

    def get_range_rows4(self, request, function=None, distinct_field_names=None):
        request = DSRequest(request=request)
        criteria = request.get_criteria()
        criteria_dict = dict()

        for criterion in criteria:
            if isinstance(criterion, dict):
                criteria_dict.setdefault(criterion.get('fieldName'), criterion.get('value'))

        self.alive_only = request.alive_only
        self.enabledAll = request.enabledAll
        res = self.get_range_rows5(start=request.startRow, end=request.endRow, function=function, distinct_field_names=distinct_field_names, json=request.json, **criteria_dict)
        return res


class Lotsman_documents_hierarcy_viewManager(AuditManager):

    @staticmethod
    def getIcon(record):
        if record.attr_name != None:
            _section = record.attr_name.lower()
            if _section == 'документация':
                return 'documentation.png'
            elif _section == 'спецификация':
                return 'documentation.png'
            elif _section == 'изделие':
                return 'product.png'
            elif _section == 'чертеж':
                return 'documentation.png'
            elif _section == 'комплексы':
                return 'complexes.png'
            elif _section == 'сборочная единица':
                return 'assembly.png'
            elif _section == 'деталь':
                return 'part.png'
            elif _section == 'стандартные изделия':
                return 'standard_prod.png'
            elif _section == 'прочие изделия':
                return 'other.png'
            elif _section == 'материалы':
                return 'materials.png'
            elif _section == 'комплекты':
                return 'kits.png'
            elif _section == 'папка':
                return 'folder_256.png'
            elif _section == 'материал':
                return 'material.png'
            elif _section == 'ведомость':
                return 'templates.png'
            else:
                return 'question.png'
        else:
            return 'question.png'

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'parent': record.parent_id,
            'editing': record.editing,
            'deliting': record.deliting,
            'document_id': record.document.id,

            'STMP_120_id': record.STMP_120.id if record.STMP_120 else None,
            'STMP_120__value_str': record.STMP_120.value_str if record.STMP_120 else None,

            'SPC_CLM_FORMAT_id': record.SPC_CLM_FORMAT.id if record.SPC_CLM_FORMAT else None,
            'SPC_CLM_FORMAT__value_str': record.SPC_CLM_FORMAT.value_str if record.SPC_CLM_FORMAT else None,
            'SPC_CLM_ZONE_id': record.SPC_CLM_ZONE.id if record.SPC_CLM_ZONE else None,
            'SPC_CLM_ZONE__value_str': record.SPC_CLM_ZONE.value_str if record.SPC_CLM_ZONE else None,
            'SPC_CLM_POS_id': record.SPC_CLM_POS.id if record.SPC_CLM_POS else None,
            'SPC_CLM_POS__value_int': record.SPC_CLM_POS.value_int if record.SPC_CLM_POS else None,
            'SPC_CLM_MARK_id': record.SPC_CLM_MARK.id if record.SPC_CLM_MARK else None,
            'SPC_CLM_MARK__value_str': record.SPC_CLM_MARK.value_str if record.SPC_CLM_MARK else None,
            'SPC_CLM_NAME_id': record.SPC_CLM_NAME.id if record.SPC_CLM_NAME else None,
            'SPC_CLM_NAME__value_str': record.SPC_CLM_NAME.value_str if record.SPC_CLM_NAME else None,
            'SPC_CLM_COUNT_id': record.SPC_CLM_COUNT.id if record.SPC_CLM_COUNT else None,
            'SPC_CLM_COUNT__value_str': record.SPC_CLM_COUNT.value_str if record.SPC_CLM_COUNT else None,
            'SPC_CLM_NOTE_id': record.SPC_CLM_NOTE.id if record.SPC_CLM_NOTE else None,
            'SPC_CLM_NOTE__value_str': record.SPC_CLM_NOTE.value_str if record.SPC_CLM_NOTE else None,
            'SPC_CLM_MASSA_id': record.SPC_CLM_MASSA.id if record.SPC_CLM_MASSA else None,
            'SPC_CLM_MASSA__value_str': record.SPC_CLM_MASSA.value_str if record.SPC_CLM_MASSA else None,
            'SPC_CLM_MATERIAL_id': record.SPC_CLM_MATERIAL.id if record.SPC_CLM_MATERIAL else None,
            'SPC_CLM_MATERIAL__value_str': record.SPC_CLM_MATERIAL.value_str if record.SPC_CLM_MATERIAL else None,
            'SPC_CLM_USER_id': record.SPC_CLM_USER.id if record.SPC_CLM_USER else None,
            'SPC_CLM_USER__value_str': record.SPC_CLM_USER.value_str if record.SPC_CLM_USER else None,
            'SPC_CLM_KOD_id': record.SPC_CLM_KOD.id if record.SPC_CLM_KOD else None,
            'SPC_CLM_KOD__value_str': record.SPC_CLM_KOD.value_str if record.SPC_CLM_KOD else None,
            'SPC_CLM_FACTORY_id': record.SPC_CLM_FACTORY.id if record.SPC_CLM_FACTORY else None,
            'SPC_CLM_FACTORY__value_str': record.SPC_CLM_FACTORY.value_str if record.SPC_CLM_FACTORY else None,
            'Наименование_материала_id': record.Наименование_материала.id if record.Наименование_материала else None,
            'Наименование_материала__value_str': record.Наименование_материала.value_str if record.Наименование_материала else None,
            'Документ_на_материал_id': record.Документ_на_материал.value_str if record.Документ_на_материал else None,
            'Наименование_сортамента__value_str': record.Наименование_сортамента.value_str if record.Наименование_сортамента else None,
            'Документ_на_сортамент_id': record.Документ_на_сортамент.value_str if record.Документ_на_сортамент else None,
            'Документ_на_сортамент__value_str': record.Документ_на_сортамент.value_str if record.Документ_на_сортамент else None,
            '_Version_id': record._Version.value_int if record._Version else None,
            '_Version__value_int': record._Version.value_int if record._Version else None,
            # '_Type_id': record.__Type.value_int if record._Type else None,
            # '_Type__value_int': record._Type.value_int if record._Type else None,

            'section': record.section,
            'subsection': record.subsection,
            'attr_code': record.attr_code,
            'attr_name': record.attr_name,
            'isFolder': record.isFolder,
            'icon': Lotsman_documents_hierarcy_viewManager.getIcon(record)
        }
        return DelProps(res)

    def get_queryset(self):
        return Lotsman_documents_hierarcy_viewQuerySet(self.model, using=self._db)


class Lotsman_documents_hierarcy_view(AuditModel):
    id = BigIntegerField(primary_key=True, verbose_name="Идентификатор")
    attr_type = ForeignKeyProtect(Attr_type, verbose_name='Тип документа')
    parent_id = BigIntegerField(null=True, blank=True)
    document = ForeignKeyProtect(Documents)

    STMP_120 = ForeignKeyProtect(Document_attributes, related_name='STMP_120_Lotsman_documents_hierarcy_view', null=True, blank=True)

    SPC_CLM_KOD = ForeignKeyProtect(Document_attributes, related_name='SPC_CLM_KOD_Lotsman_documents_hierarcy_view', null=True, blank=True)
    SPC_CLM_FORMAT = ForeignKeyProtect(Document_attributes, related_name='SPC_CLM_FORMAT_Lotsman_documents_hierarcy_view', null=True, blank=True)
    SPC_CLM_COUNT = ForeignKeyProtect(Document_attributes, related_name='SPC_CLM_COUNT_Lotsman_documents_hierarcy_view', null=True, blank=True)
    SPC_CLM_ZONE = ForeignKeyProtect(Document_attributes, related_name='SPC_CLM_ZONE_Lotsman_documents_hierarcy_view', null=True, blank=True)
    SPC_CLM_MASSA = ForeignKeyProtect(Document_attributes, related_name='SPC_CLM_MASSA_Lotsman_documents_hierarcy_view', null=True, blank=True)
    SPC_CLM_POS = ForeignKeyProtect(Document_attributes, related_name='SPC_CLM_POS_Lotsman_documents_hierarcy_view', null=True, blank=True)
    SPC_CLM_NAME = ForeignKeyProtect(Document_attributes, related_name='SPC_CLM_NAME_Lotsman_documents_hierarcy_view', null=True, blank=True)
    SPC_CLM_MARK = ForeignKeyProtect(Document_attributes, related_name='SPC_CLM_MARK_Lotsman_documents_hierarcy_view', null=True, blank=True)
    SPC_CLM_NOTE = ForeignKeyProtect(Document_attributes, related_name='SPC_CLM_NOTE_Lotsman_documents_hierarcy_view', null=True, blank=True)
    SPC_CLM_USER = ForeignKeyProtect(Document_attributes, related_name='SPC_CLM_USER_Lotsman_documents_hierarcy_view', null=True, blank=True)
    SPC_CLM_FACTORY = ForeignKeyProtect(Document_attributes, related_name='SPC_CLM_FACTORY_Lotsman_documents_hierarcy_view', null=True, blank=True)
    SPC_CLM_MATERIAL = ForeignKeyProtect(Document_attributes, related_name='SPC_CLM_MATERIAL_Lotsman_documents_hierarcy_view', null=True, blank=True)

    Документ_на_материал = ForeignKeyProtect(Document_attributes, related_name='Документ_на_материал_Lotsman_documents_hierarcy_view', null=True, blank=True)
    Наименование_материала = ForeignKeyProtect(Document_attributes, related_name='Наименование_материала_Lotsman_documents_hierarcy_view', null=True, blank=True)
    Документ_на_сортамент = ForeignKeyProtect(Document_attributes, related_name='Документ_на_сортамент_Lotsman_documents_hierarcy_view', null=True, blank=True)
    Наименование_сортамента = ForeignKeyProtect(Document_attributes, related_name='Наименование_сортамента_Lotsman_documents_hierarcy_view', null=True, blank=True)
    _Version = ForeignKeyProtect(Document_attributes, related_name='_Version_Lotsman_documents_hierarcy_view', null=True, blank=True)
    _Type = ForeignKeyProtect(Document_attributes, related_name='_Type_id_Lotsman_documents_hierarcy_view', null=True, blank=True)

    section = NameField(null=True, blank=True)
    subsection = NameField(null=True, blank=True)
    attr_code = NameField(null=True, blank=True)
    attr_name = NameField(null=True, blank=True)
    isFolder = BooleanField(null=True, blank=True)
    props = Lotsman_documents_hierarcyManager.get_props()

    objects = Lotsman_documents_hierarcy_viewManager()
    objects_tree = TreeAuditModelManager()

    def __str__(self):
        return f'ID:{self.id}, \n' \
               f'attr_type: [{self.attr_type}], \n' \
               f'document: [{self.document}], \n' \
               f'STMP_120: [{self.STMP_120}], \n' \
               f'SPC_CLM_KOD: [{self.SPC_CLM_KOD}], \n' \
               f'SPC_CLM_FORMAT: [{self.SPC_CLM_FORMAT}], \n' \
               f'SPC_CLM_COUNT: [{self.SPC_CLM_COUNT}], \n' \
               f'SPC_CLM_ZONE: [{self.SPC_CLM_ZONE}], \n' \
               f'SPC_CLM_MASSA: [{self.SPC_CLM_MASSA}], \n' \
               f'SPC_CLM_POS: [{self.SPC_CLM_POS}], \n' \
               f'SPC_CLM_NAME: [{self.SPC_CLM_NAME}], \n' \
               f'SPC_CLM_MARK: [{self.SPC_CLM_MARK}], \n' \
               f'SPC_CLM_NOTE: [{self.SPC_CLM_NOTE}], \n' \
               f'SPC_CLM_USER: [{self.SPC_CLM_USER}], \n' \
               f'SPC_CLM_FACTORY: [{self.SPC_CLM_FACTORY}], \n' \
               f'SPC_CLM_MATERIAL: [{self.SPC_CLM_MATERIAL}], \n' \
               f'Документ_на_материал: [{self.Документ_на_материал}], \n' \
               f'Наименование_материала: [{self.Наименование_материала}], \n' \
               f'Документ_на_сортамент: [{self.Документ_на_сортамент}], \n' \
               f'Наименование_сортамента: [{self.Наименование_сортамента}], \n' \
               f'_Version: [{self._Version}], \n' \
               f'_Type: [{self._Type}], \n' \
               f'section: {self.section}, \n' \
               f'subsection: {self.subsection}, \n' \
               f'attr_code: {self.attr_code}, \n' \
               f'attr_name: {self.attr_name}, \n' \
               f'isFolder: {self.isFolder}, \n' \
               f'props: {self.props} \n' \

    def __repr__(self):
        return self.__str__()

    def get_mat(selfname, name, doc):
        if name != None and doc != None:
            return f'{name}/{doc}'
        elif name != None and doc == None:
            return name
        elif name == None and doc != None:
            return doc
        else:
            return None

    @property
    def SPC_CLM_MATERIAL_NAME_DOC(self):
        name = f'{self.Наименование_материала.value_str if self.Наименование_материала.value_str else None}'
        doc = f'{self.Документ_на_материал.value_str if self.Документ_на_материал.value_str else None}'

        return self.get_mat(name=name, doc=doc)

    @property
    def SPC_CLM_MATERIAL_SORT_DOC(self):
        name = f'{self.Наименование_сортамента.value_str if self.Наименование_сортамента.value_str else None}'
        doc = f'{self.Документ_на_сортамент.value_str if self.Документ_на_сортамент.value_str else None}'

        return self.get_mat(name=name, doc=doc)\

    class Meta:
        verbose_name = 'Иерархия документа из Лоцмана'
        managed = False
        db_table = 'kd_lotsman_documents_hierarcy_mview'
