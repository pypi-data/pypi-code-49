import logging

from bitfield import BitField

from isc_common.fields.related import ForeignKeyProtect
from isc_common.models.base_ref import BaseRefManager, BaseRefQuerySet, BaseRef
from isc_common.number import DelProps
from kaf_pas.planing.models.operation_types import Operation_types

logger = logging.getLogger(__name__)


class Status_operation_typesQuerySet(BaseRefQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Status_operation_typesManager(BaseRefManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'code': record.code,
            'name': record.name,
            'description': record.description,
            'editing': record.editing,
            'deliting': record.deliting,
            'disabled': record.props.disabled,
            'props': record.props._value,
            'opertype': record.opertype.id,
        }
        return DelProps(res)

    def get_queryset(self):
        return Status_operation_typesQuerySet(self.model, using=self._db)


class Status_operation_types(BaseRef):
    opertype = ForeignKeyProtect(Operation_types)

    props = BitField(flags=(
        ('disabled', 'Неактивная запись в гриде')
    ), default=0, db_index=True)

    objects = Status_operation_typesManager()

    def __str__(self):
        return f"ID:{self.id}, code: {self.code}, name: {self.name}, description: {self.description}, props: {self.props}"

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Статусы запусков'
