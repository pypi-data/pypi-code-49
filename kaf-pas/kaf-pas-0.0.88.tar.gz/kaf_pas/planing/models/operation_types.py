import logging

from bitfield import BitField

from isc_common.models.base_ref import BaseRefManager, BaseRefQuerySet, BaseRefHierarcy
from isc_common.number import DelProps

logger = logging.getLogger(__name__)


class Operation_typesQuerySet(BaseRefQuerySet):
    pass


class Operation_typesManager(BaseRefManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'code': record.code,
            'name': record.name,
            'full_name': record.full_name,
            'description': record.description,
            'parent_id': record.parent.id if record.parent else None,
            'editing': record.editing,
            'deliting': record.deliting,
            'props': record.props,
            'plus': record.props.plus,
            'minus': record.props.minus,
        }
        return DelProps(res)

    def get_queryset(self):
        return Operation_typesQuerySet(self.model, using=self._db)


class Operation_types(BaseRefHierarcy):
    props = BitField(flags=(
        ('plus', 'Приходная операция'),  # 2
        ('minus', 'Расходная операция'),  # 2
    ), default=0, db_index=True)

    objects = Operation_typesManager()

    def __str__(self):
        return f"ID:{self.id}, code: {self.code}, name: {self.name}, full_name: {self.full_name}, parent_id: {self.parent_id}, props: {self.props}, description: {self.description}"

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Типы системных операций'

