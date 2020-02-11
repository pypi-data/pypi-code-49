import logging

from django.db.models import DecimalField, TextField
from django.forms import model_to_dict

from isc_common import delAttr, setAttr
from isc_common.auth.models.user import User
from isc_common.fields.code_field import ColorField
from isc_common.fields.related import ForeignKeyProtect
from isc_common.http.DSRequest import DSRequest
from isc_common.managers.common_managet_with_lookup_fields import CommonManagetWithLookUpFieldsManager, CommonManagetWithLookUpFieldsQuerySet
from isc_common.models.audit import AuditModel
from isc_common.models.standard_colors import Standard_colors
from isc_common.number import DelProps
from kaf_pas.ckk.models.ed_izm import Ed_izm
from kaf_pas.ckk.models.item import Item
from kaf_pas.ckk.models.locations import Locations

logger = logging.getLogger(__name__)


class Tmp_bufferQuerySet(CommonManagetWithLookUpFieldsQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Tmp_bufferManager(CommonManagetWithLookUpFieldsManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'location_id': record.location.id,
            'location__code': record.location.code,
            'location__name': record.location.name,
            'location__full_name': record.location.full_name,
            'item_id': record.item.id,
            'item__STMP_1_id': record.item.STMP_1.id if record.item.STMP_1 else None,
            'item__STMP_1__value_str': record.item.STMP_1.value_str if record.item.STMP_1 else None,
            'item__STMP_2_id': record.item.STMP_2.id if record.item.STMP_2 else None,
            'item__STMP_2__value_str': record.item.STMP_2.value_str if record.item.STMP_2 else None,
            'edizm_id': record.edizm.id,
            'edizm__code': record.edizm.code,
            'edizm__name': record.edizm.name,
            'editing': record.editing,
            'deliting': record.deliting,
            'description': record.description,
            'value': record.value,
            'color_id': record.color.id if record.color else None,
            'color__color': record.color.color if record.color else None,
            'color__name': record.color.name if record.color else None,
            'value_off': record.value_off,
        }
        return res

    def createFromRequest(self, request, removed=None):
        request = DSRequest(request=request)
        data = request.get_data()
        _data = data.copy()
        delAttr(_data, 'dataSource')
        delAttr(_data, 'operationType')
        delAttr(_data, 'textMatchStyle')
        delAttr(_data, 'form')
        _data.setdefault('user_id', request.user_id)
        self._remove_prop(_data, removed)

        res = super().create(**_data)
        try:
            full_name = res.full_name
        except:
            full_name = None
        res = model_to_dict(res)
        if full_name:
            setAttr(res, 'full_name', full_name)

        setAttr(res, 'isFolder', False)
        data.update(DelProps(res))
        return data

    def updateFromRequest(self, request, removed=None, function=None):
        if not isinstance(request, DSRequest):
            request = DSRequest(request=request)
        data = request.get_data()

        _data = data.copy()
        if _data.get('value_off'):
            if _data.get('value') < _data.get('value_off'):
                raise Exception(f'Превышен лимит.')

        delAttr(_data, 'id')
        delAttr(_data, 'item')
        delAttr(_data, 'location')
        delAttr(_data, 'user')
        delAttr(_data, 'edizm')
        res, _ = super().update_or_create(id=request.get_id(), defaults=_data)

        _data.setdefault('id', res.id)
        return _data

    def get_queryset(self):
        return Tmp_bufferQuerySet(self.model, using=self._db)


class Tmp_buffer(AuditModel):
    item = ForeignKeyProtect(Item)
    location = ForeignKeyProtect(Locations)
    user = ForeignKeyProtect(User)
    edizm = ForeignKeyProtect(Ed_izm)
    value = DecimalField(max_digits=19, decimal_places=4)
    value_off = DecimalField(max_digits=19, decimal_places=4, null=True, blank=True)
    description = TextField(null=True, blank=True)
    color = ForeignKeyProtect(Standard_colors, null=True, blank=True)

    objects = Tmp_bufferManager()

    def __str__(self):
        return f'ID:{self.id}'

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Временное хранилищи данных для буферов'
