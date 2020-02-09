import logging

from isc_common.fields.related import ForeignKeyProtect, ForeignKeyCascade
from isc_common.models.audit import AuditModel, AuditManager, AuditQuerySet
from kaf_pas.ckk.models.locations import Locations
from kaf_pas.planing.models.operations import Operations

logger = logging.getLogger(__name__)


class Operation_locationsQuerySet(AuditQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Operation_locationsManager(AuditManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'editing': record.editing,
            'deliting': record.deliting,
            'location_id': record.location.id,
            'location__code': record.location.code,
            'location__name': record.location.name,
            'location__full_name': record.location.full_name,
        }
        return res

    def get_queryset(self):
        return Operation_locationsQuerySet(self.model, using=self._db)


class Operation_locations(AuditModel):
    operation = ForeignKeyCascade(Operations, related_name='planing_operation_loc')
    location = ForeignKeyProtect(Locations, related_name='planing_resource_loc')

    objects = Operation_locationsManager()

    def __str__(self):
        return f"ID:{self.id}"

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Кросс таблица с место-положением'
