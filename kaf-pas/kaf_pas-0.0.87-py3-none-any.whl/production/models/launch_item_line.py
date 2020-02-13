import logging

from bitfield import BitField
from django.db.models import PositiveIntegerField

from isc_common.bit import IsBitOn
from isc_common.fields.code_field import CodeStrictField
from isc_common.fields.description_field import DescriptionField
from isc_common.fields.name_field import NameField
from isc_common.fields.related import ForeignKeyProtect, ForeignKeySetNull
from isc_common.models.audit import AuditModel, AuditManager, AuditQuerySet
from isc_common.models.tree_audit import TreeAuditModelManager
from kaf_pas.ckk.models.item import Item
from kaf_pas.ckk.models.item_line import Item_line
from kaf_pas.kd.models.document_attributes import Document_attributes
from kaf_pas.production.models.launches import Launches

logger = logging.getLogger(__name__)


class Launch_item_lineQuerySet(AuditQuerySet):

    def create(self, **kwargs):
        return super().create(**kwargs)

    def get_or_create(self, defaults=None, **kwargs):
        return super().get_or_create(defaults, **kwargs)

    def update(self, **kwargs):
        return super().update(**kwargs)

    def update_or_create(self, defaults=None, **kwargs):
        return super().get_or_create(defaults, **kwargs)


class Launch_item_lineManager(TreeAuditModelManager):
    @staticmethod
    def props():
        return  BitField(flags=(
        ('enabled', 'Доступность в данной производственной спецификации'),  # 1
    ), default=1, db_index=True)

    def get_queryset(self):
        return Launch_item_lineQuerySet(self.model, using=self._db)

    @staticmethod
    def section_num(section):
        sorted_section = {"Документация": 0, "Комплексы": 1, "Сборочные единицы": 2, "Детали": 3, "Стандартные изделия": 4, "Прочие изделия": 5, "Материалы": 6, "Комплекты": 7}
        return sorted_section.get(section)

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'child_id': record.child.id if record.child else None,
            'parent_id': record.parent.id,
            'SPC_CLM_FORMAT_id': record.SPC_CLM_FORMAT.id if record.SPC_CLM_FORMAT else None,
            'SPC_CLM_FORMAT__value_str': record.SPC_CLM_FORMAT.value_str if record.SPC_CLM_FORMAT else None,
            'SPC_CLM_ZONE_id': record.SPC_CLM_ZONE.id if record.SPC_CLM_ZONE else None,
            'SPC_CLM_ZONE__value_str': record.SPC_CLM_ZONE.value_str if record.SPC_CLM_ZONE else None,
            'SPC_CLM_POS_id': record.SPC_CLM_POS.id if record.SPC_CLM_POS else None,
            'SPC_CLM_POS__value_str': record.SPC_CLM_POS.value_str if record.SPC_CLM_POS else None,
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
            "launch_id": record.launch.id,
            "item_line_id": record.item_line.id,
            'section': record.section,
            'section_num': record.section_num,
            'subsection': record.subsection,
            'lastmodified': record.lastmodified,
            'editing': record.editing,
            'deliting': record.deliting,
            'props': record.props._value,
            'enabled': IsBitOn(record.props, 0),
        }
        return res

    @staticmethod
    def getIcon(record):
        if record.isFolder:
            return 'folder_256.png'
        elif record.section:
            _section = record.section.lower()
            if _section == 'документация':
                return 'documentation.png'
            elif _section == 'комплексы':
                return 'complexes.png'
            elif _section == 'сборочные единицы':
                return 'assembly.png'
            elif _section == 'детали':
                return 'part.png'
            elif _section == 'стандартные изделия':
                return 'standard_prod.png'
            elif _section == 'прочие изделия':
                return 'other.png'
            elif _section == 'материалы':
                return 'materials.png'
            elif _section == 'комплекты':
                return 'kits.png'
            else:
                return 'folder_256.png'


class Launch_item_line(AuditModel):
    parent = ForeignKeyProtect(Item, related_name='Launch_item_parent')
    added_parent = ForeignKeyProtect('self', related_name='Launch_item_added_parent', null=True, blank=True)
    child = ForeignKeyProtect(Item, related_name='Launch_item_child')
    item_line = ForeignKeySetNull(Item_line, null=True, blank=True)
    launch = ForeignKeyProtect(Launches)

    SPC_CLM_FORMAT = ForeignKeyProtect(Document_attributes, verbose_name='Формат', related_name='Launch_SPC_CLM_FORMAT', null=True, blank=True)
    SPC_CLM_ZONE = ForeignKeyProtect(Document_attributes, verbose_name='Зона', related_name='Launch_SPC_CLM_ZONE', null=True, blank=True)
    SPC_CLM_POS = ForeignKeyProtect(Document_attributes, verbose_name='Позиция', related_name='Launch_SPC_CLM_POS', null=True, blank=True)
    SPC_CLM_MARK = ForeignKeyProtect(Document_attributes, verbose_name='Обозначение', related_name='Launch_SPC_CLM_MARK', null=True, blank=True)
    SPC_CLM_NAME = ForeignKeyProtect(Document_attributes, verbose_name='Наименование', related_name='Launch_SPC_CLM_NAME', null=True, blank=True)
    SPC_CLM_COUNT = ForeignKeyProtect(Document_attributes, verbose_name='Количество', related_name='Launch_SPC_CLM_COUNT', null=True, blank=True)
    SPC_CLM_NOTE = ForeignKeyProtect(Document_attributes, verbose_name='Примечание', related_name='Launch_SPC_CLM_NOTE', null=True, blank=True)
    SPC_CLM_MASSA = ForeignKeyProtect(Document_attributes, verbose_name='Масса', related_name='Launch_SPC_CLM_MASSA', null=True, blank=True)
    SPC_CLM_MATERIAL = ForeignKeyProtect(Document_attributes, verbose_name='Материал', related_name='Launch_SPC_CLM_MATERIAL', null=True, blank=True)
    SPC_CLM_USER = ForeignKeyProtect(Document_attributes, verbose_name='Пользовательская', related_name='Launch_SPC_CLM_USER', null=True, blank=True)
    SPC_CLM_KOD = ForeignKeyProtect(Document_attributes, verbose_name='Код', related_name='Launch_SPC_CLM_KOD', null=True, blank=True)
    SPC_CLM_FACTORY = ForeignKeyProtect(Document_attributes, verbose_name='Предприятие - изготовитель', related_name='Launch_SPC_CLM_FACTORY', null=True, blank=True)
    section = CodeStrictField()
    section_num = PositiveIntegerField(null=True, blank=True)
    subsection = NameField()
    description = DescriptionField()
    props = Launch_item_lineManager.props()


    objects = Launch_item_lineManager()

    @property
    def item_name(self):
        if self.SPC_CLM_NAME != None and self.SPC_CLM_MARK != None:
            return f'{self.SPC_CLM_NAME.value_str}: {self.SPC_CLM_MARK.value_str}'
        elif self.SPC_CLM_NAME == None and self.SPC_CLM_MARK != None:
            return self.SPC_CLM_MARK.value_str
        elif self.SPC_CLM_NAME != None and self.SPC_CLM_MARK == None:
            return self.SPC_CLM_NAME.value_str
        else:
            return 'Неизвестен'

    def save(self, *args, **kwargs):
        if self.parent:
            if self.parent.id == self.child.id:
                raise Exception(f'Attempt to record with parent.id ({self.parent.id}) == child.id ({self.child.id})')

        if self.SPC_CLM_MARK == None and self.SPC_CLM_NAME == None:
            raise Exception(f'SPC_CLM_MARK and SPC_CLM_NAME not been Null together. ({self})')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'\n\nchild=[{self.child}]\n' \
               f'\nparent=[{self.parent}]\n' \
               f'\nSPC_CLM_FORMAT=[{self.SPC_CLM_FORMAT}]' \
               f'\nSPC_CLM_ZONE=[{self.SPC_CLM_ZONE}]' \
               f'\nSPC_CLM_POS=[{self.SPC_CLM_POS}]' \
               f'\nSPC_CLM_MARK=[{self.SPC_CLM_MARK}]' \
               f'\nSPC_CLM_NAME=[{self.SPC_CLM_NAME}]' \
               f'\nSPC_CLM_COUNT=[{self.SPC_CLM_COUNT}]' \
               f'\nSPC_CLM_NOTE=[{self.SPC_CLM_NOTE}]' \
               f'\nSPC_CLM_MASSA=[{self.SPC_CLM_MASSA}]' \
               f'\nSPC_CLM_MATERIAL=[{self.SPC_CLM_MATERIAL}]' \
               f'\nSPC_CLM_USER=[{self.SPC_CLM_USER}]' \
               f'\nSPC_CLM_KOD=[{self.SPC_CLM_KOD}' \
               f'\nSPC_CLM_FACTORY={self.SPC_CLM_FACTORY}]\n' \
               f'section={self.section}\n' \
               f'subsection={self.subsection}\n\n'

    class Meta:
        verbose_name = 'Строка состава изделия'
        unique_together = (('parent', 'child', 'launch'),)
        ordering = ['section']
