import logging

from django.db.models import Model, PositiveIntegerField, Manager, QuerySet, Max

from isc_common.fields.code_field import CodeField
from isc_common.fields.related import ForeignKeyCascade, ForeignKeyProtect
from kaf_pas.kd.models.document_attributes import Document_attributes
from kaf_pas.kd.models.documents import Documents

logger = logging.getLogger(__name__)


class Document_attr_cross1QuerySet(QuerySet):
    def delete(self):
        return super().delete()

    def _position_in_document(self, **kwargs):
        position_in_document = kwargs.get('position_in_document')
        document = kwargs.get('document')
        if document != None:
            if position_in_document == None:
                position_in_document_dict = Document_attr_cross.objects.filter(document=document).aggregate(Max('position_in_document'))
                position_in_document = position_in_document_dict.get('position_in_document__max')
                if position_in_document == None:
                    position_in_document = 1
                else:
                    position_in_document += 1
                kwargs.setdefault('position_in_document', position_in_document)
                return kwargs
            else:
                return kwargs
        else:
            raise Exception(f'Not have a document paremetr.')

    def create(self, **kwargs):
        return super().create(**self._position_in_document(**kwargs))

    def update(self, **kwargs):
        return super().create(**self._position_in_document(**kwargs))

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Document_attr_cross1Manager(Manager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return Document_attr_cross1QuerySet(self.model, using=self._db)


class Document_attr_cross(Model):
    document = ForeignKeyCascade(Documents)
    attribute = ForeignKeyProtect(Document_attributes)
    position_in_document = PositiveIntegerField()

    section = CodeField(verbose_name="Раздел", null=True, blank=True)
    subsection = CodeField(verbose_name="Подраздел", null=True, blank=True)

    objects = Document_attr_cross1Manager()

    def save(self, *args, **kwargs):
        if self.attribute.attr_type.code == 'STMP_1' or self.attribute.attr_type.code == 'STMP_2':
            try:
                Document_attr_cross.objects.get(attribute=self.attribute, document=self.document)
                raise Exception(f'Попытка записи дубликата: {self.attribute}')
            except Document_attr_cross.DoesNotExist:
                ...
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = 'Кросс таблица'
        unique_together = (('document', 'position_in_document'),)
