import logging

from django.db import IntegrityError
from django.db.models import Model, PositiveIntegerField, QuerySet, Manager, Max

from isc_common.fields.related import ForeignKeyCascade, ForeignKeyProtect
from kaf_pas.kd.models.document_attributes import Document_attributes
from kaf_pas.kd.models.lotsman_documents_hierarcy import Lotsman_documents_hierarcy

logger = logging.getLogger(__name__)


class Lotsman_document_attr_cross1QuerySet(QuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def update(self, **kwargs):
        return super().create(**kwargs)

    def update_or_create(self, defaults=None, **kwargs):
        return super().update_or_create(**kwargs, defaults=defaults)

    def get_or_create(self, defaults=None, **kwargs):
        return super().get_or_create(**kwargs, defaults=defaults)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Lotsman_document_attr_cross1Manager(Manager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return Lotsman_document_attr_cross1QuerySet(self.model, using=self._db)


class Lotsman_document_attr_cross(Model):
    document = ForeignKeyCascade(Lotsman_documents_hierarcy)
    attribute = ForeignKeyProtect(Document_attributes)

    objects = Lotsman_document_attr_cross1Manager()

    def __str__(self):
        return f"{self.id}, document: [{self.document}], attribute: [{self.attribute}]"

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Кросс таблица'
        # unique_together = (('document', 'position_in_document'),)
