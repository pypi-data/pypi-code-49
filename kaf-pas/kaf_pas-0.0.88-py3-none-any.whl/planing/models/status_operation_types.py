import logging

from bitfield import BitField
from django.db import transaction

from isc_common import delAttr, setAttr
from isc_common.fields.related import ForeignKeyProtect
from isc_common.http.DSRequest import DSRequest
from isc_common.managers.common_managet_with_lookup_fields import CommonManagetWithLookUpFieldsManager, CommonManagetWithLookUpFieldsQuerySet
from isc_common.models.base_ref import BaseRefManager, BaseRefQuerySet, BaseRef
from isc_common.number import DelProps
from kaf_pas.planing.models.operation_types import Operation_types

logger = logging.getLogger(__name__)


class Status_operation_typesQuerySet(BaseRefQuerySet):
    pass


class Status_operation_typesManager(BaseRefManager):

    def updateFromRequest(self, request, removed=None, function=None):
        if not isinstance(request, DSRequest):
            request = DSRequest(request=request)
        data = request.get_data()

        _data = data.copy()

        if self._dataIsArray(data):
            data = list(data.values())
            for data_item in data:
                self._remove_prop(data_item, removed)
                data_item = self._remove_prop_(data_item)
                if isinstance(data_item, dict):
                    if function:
                        function(data, data_item)
                    else:
                        cloned_data = self.clone_data(data)
                        if data_item.get('id'):
                            super().update_or_create(id=data_item.get('id'), defaults=cloned_data)
                        else:
                            super().create(**cloned_data)
        else:
            self._remove_prop(data, removed)
            data = self._remove_prop_(data)
            if function:
                function(data)
            else:
                cloned_data = self.clone_data(data)
                if request.get_id():
                    delAttr(cloned_data, 'id')
                    super().update_or_create(id=request.get_id(), defaults=cloned_data)
                else:
                    new_item = super().create(**cloned_data)
                    setAttr(_data, 'id', new_item.id)
        return _data

    @staticmethod
    def make_statuses(opertype, status_map):
        res = dict()
        with transaction.atomic():
            for key_value in status_map:
                status, _ = Status_operation_types.objects.update_or_create(
                    opertype=opertype,
                    code=key_value.get('code'),
                    defaults=dict(
                        name=key_value.get('name'),
                        deliting=False,
                        editing=False,
                    ))
                res.setdefault(key_value.get('code'), status)
        return res

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
        return f"ID:{self.id}, code: {self.code}, name: {self.name}, description: {self.description}, props: {self.props}, opertype: [{self.opertype}]"

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Статусы запусков'
