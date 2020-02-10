import logging

from isc_common.auth.models.user import User
from isc_common.fields.code_field import ColorField
from isc_common.fields.related import ForeignKeyCascade, ForeignKeyProtect
from isc_common.models.audit import AuditModel, AuditManager, AuditQuerySet
from isc_common.models.standard_colors import Standard_colors
from kaf_pas.planing.models.operations import Operations

logger = logging.getLogger(__name__)


class Operation_executorQuerySet(AuditQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Operation_executorManager(AuditManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'editing': record.editing,
            'deliting': record.deliting,
            'executor_id': record.executor.id,
        }
        return res

    def get_queryset(self):
        return Operation_executorQuerySet(self.model, using=self._db)


class Operation_executor(AuditModel):
    operation = ForeignKeyCascade(Operations)
    executor = ForeignKeyProtect(User)

    objects = Operation_executorManager()

    def __str__(self):
        return f"ID:{self.id}"

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Кросс таблица значений операции'
        unique_together = (('operation', 'executor'),)
