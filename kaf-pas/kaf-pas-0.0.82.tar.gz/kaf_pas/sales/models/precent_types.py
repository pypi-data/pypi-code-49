import logging

from bitfield import BitField

from isc_common import setAttr, delAttr
from isc_common.bit import IsBitOn, TurnBitOn
from isc_common.fields.related import ForeignKeyProtect
from isc_common.http.DSRequest import DSRequest
from isc_common.models.base_ref import BaseRefManager, BaseRefQuerySet, BaseRef
from kaf_pas.sales.models.precent_item_types import Precent_item_types

logger = logging.getLogger(__name__)


class Precent_typesQuerySet(BaseRefQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Precent_typesManager(BaseRefManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'code': record.code,
            'name': record.name,
            'precent_item_type_id': record.precent_item_type.id,
            'precent_item_type__code': record.precent_item_type.code,
            'precent_item_type__name': record.precent_item_type.name,
            'description': record.description,
            'props': record.props._value,
            'enableDogovor': IsBitOn(record.props, 0),
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return Precent_typesQuerySet(self.model, using=self._db)

    def createFromRequest(self, request):
        _request = DSRequest(request=request)
        data = _request.get_data()
        _data = data.copy()

        props = 0
        if _data.get('enableDogovor'):
            props = TurnBitOn(props, 0)

        delAttr(_data, 'enableDogovor')
        delAttr(_data, 'precent_item_type__name')
        setAttr(_data, 'props', props)
        res = super().create(**_data)
        return data

    def updateFromRequest(self, request):
        request = DSRequest(request=request)
        data = request.get_data()
        id = data.get('id')

        props = 0
        if data.get('enableDogovor'):
            props = TurnBitOn(props, 0)

        delAttr(data, 'id')
        delAttr(data, 'enableDogovor')
        delAttr(data, 'precent_item_type__code')
        delAttr(data, 'precent_item_type__name')
        setAttr(data, 'props', props)
        res = super().filter(id=id).update(**data)
        return res


class Precent_types(BaseRef):
    precent_item_type = ForeignKeyProtect(Precent_item_types)
    props = BitField(flags=(
        ('enableDogovor', 'Наличие договора'),
    ), default=1, db_index=True)

    objects = Precent_typesManager()

    def __str__(self):
        return f"ID:{self.id}, code: {self.code}, name: {self.name}, description: {self.description}"

    class Meta:
        verbose_name = 'Типы распоряжений'
