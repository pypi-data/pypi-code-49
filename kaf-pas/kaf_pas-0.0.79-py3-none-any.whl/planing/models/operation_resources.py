import logging

from isc_common.fields.related import ForeignKeyProtect, ForeignKeyCascade
from isc_common.models.audit import AuditManager, AuditModel, AuditQuerySet
from kaf_pas.planing.models.operations import Operations
from kaf_pas.production.models.resource import Resource

logger = logging.getLogger(__name__)


class Operation_resourcesQuerySet(AuditQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Operation_resourcesManager(AuditManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return Operation_resourcesQuerySet(self.model, using=self._db)


class Operation_resources(AuditModel):
    operation = ForeignKeyCascade(Operations, related_name='planing_operation_res')
    resource = ForeignKeyProtect(Resource, related_name='planing_resource_res')

    objects = Operation_resourcesManager()

    def __str__(self):
        return f"ID:{self.id}"

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Кросс таблица'
