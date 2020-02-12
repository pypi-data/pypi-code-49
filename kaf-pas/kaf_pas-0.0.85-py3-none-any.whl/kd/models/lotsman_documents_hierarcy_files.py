import logging

from django.db.models import TextField

from isc_common.fields.related import ForeignKeyProtect
from isc_common.models.audit import AuditModel, AuditManager, AuditQuerySet
from kaf_pas.kd.models.lotsman_documents_hierarcy import Lotsman_documents_hierarcy

logger = logging.getLogger(__name__)


class Lotsman_documents_hierarcy_filesQuerySet(AuditQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Lotsman_documents_hierarcy_filesManager(AuditManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return Lotsman_documents_hierarcy_filesQuerySet(self.model, using=self._db)


class Lotsman_documents_hierarcy_files(AuditModel):
    lotsman_document = ForeignKeyProtect(Lotsman_documents_hierarcy)
    path = TextField()

    objects = Lotsman_documents_hierarcy_filesManager()

    def __str__(self):
        return f'ID:{self.id}'

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Файлы обрабатанные для данной позиции'
        unique_together = (('lotsman_document', 'path'),)
