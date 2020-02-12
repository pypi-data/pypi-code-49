import logging

from bitfield import BitField

from isc_common.models.base_ref import BaseRefManager, BaseRefQuerySet, BaseRef
from isc_common.number import DelProps

logger = logging.getLogger(__name__)


class Status_launchQuerySet(BaseRefQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Status_launchManager(BaseRefManager):

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
        }
        return DelProps(res)

    def get_queryset(self):
        return Status_launchQuerySet(self.model, using=self._db)


class Status_launch(BaseRef):
    props = BitField(flags=(
        ('disabled', 'Неактивная запись в гриде')
    ), default=0, db_index=True)

    objects = Status_launchManager()

    def __str__(self):
        return f"ID:{self.id}, code: {self.code}, name: {self.name}, description: {self.description}, props: {self.props}"

    class Meta:
        verbose_name = 'Статусы запусков'
