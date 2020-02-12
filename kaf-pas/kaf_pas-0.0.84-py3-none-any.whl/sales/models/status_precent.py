import logging

from bitfield import BitField

from isc_common.bit import IsBitOn
from isc_common.models.base_ref import BaseRef, BaseRefQuerySet, StatusBaseRefManager

logger = logging.getLogger(__name__)


class StatusPrecentQuerySet(BaseRefQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class StatusPrecentManager(StatusBaseRefManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'code': record.code,
            'name': record.name,
            'description': record.description,
            'props': record.props._value,
            'disabled': IsBitOn(record.props, 0),
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return StatusPrecentQuerySet(self.model, using=self._db)


class StatusPrecent(BaseRef):
    props = BitField(flags=(
        ('disabled', 'Неактивная запись в гриде')
    ), default=0, db_index=True)

    objects = StatusPrecentManager()

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = 'Статусы распоряжения'
