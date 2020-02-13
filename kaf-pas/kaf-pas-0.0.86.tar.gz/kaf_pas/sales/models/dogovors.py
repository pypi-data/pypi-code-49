import logging

from bitfield import BitField
from django.db.models import DateTimeField
from django.forms import model_to_dict
from django.utils import timezone

from crypto.models.crypto_file import Crypto_file, CryptoManager, CryptoQuerySet
from isc_common import delAttr, getAttr, setAttr
from isc_common.fields.code_field import CodeStrictField
from isc_common.fields.description_field import DescriptionField
from isc_common.fields.related import ForeignKeyProtect
from isc_common.http.DSRequest import DSRequest
from isc_common.models.base_ref import BaseHierarcy
from kaf_pas.sales.models.customer import Customer
from kaf_pas.sales.models.dogovor_types import Dogovor_types
from kaf_pas.sales.models.status_dogovor import StatusDogovor

logger = logging.getLogger(__name__)


class DogovorsQuerySet(CryptoQuerySet):
    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class DogovorsManager(CryptoManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'name': record.name,
            'full_name': record.full_name,
            'date': record.date,
            'date_sign': record.date_sign,
            'description': record.description,

            'status_id': record.status.id,
            'status__code': record.status.code,
            'status__name': record.status.name,

            'type_id': record.type.id,
            'type__code': record.type.code,
            'type__name': record.type.name,

            'customer_id': record.customer.id,
            'customer__inn': record.customer.inn,
            'customer__kpp': record.customer.kpp,
            'customer__name': record.customer.name,
            'customer__full_name': record.customer.full_name,
            'customer__description': record.customer.description,

            'format': record.format,
            'mime_type': record.mime_type,
            'size': record.size if not str(record.size).startswith('.') else str(record.size).replace('.', '0.'),
            'real_name': record.real_name,

            'lastmodified': record.lastmodified,
            'editing': record.editing,
            'deliting': record.deliting,
            'parent_id': record.parent.id if record.parent else None,
        }
        return res

    def createFromRequest(self, request, printRequest=False, function=None):
        request = DSRequest(request=request)
        data = request.get_data()
        _data = data.copy()
        delAttr(_data, 'form')
        if data.get('id'):
            delAttr(_data, 'id')
            res = super().filter(id=data.get('id')).update(**_data)
        else:
            res = super().create(**_data)
            res = model_to_dict(res)
            delAttr(res, 'attfile')
            setAttr(res, 'props', getAttr(res, 'props')._value)
            data.update(res)
        return data

    def updateFromRequest(self, request):
        request = DSRequest(request=request)
        data = request.get_data()
        _data = data.copy()
        delAttr(_data, 'form')
        delAttr(_data, 'isFolder')
        delAttr(_data, 'full_name')
        delAttr(_data, 'enabled')
        super().filter(id=request.get_id()).update(**_data)
        return data

    def get_queryset(self):
        return DogovorsQuerySet(self.model, using=self._db)


class Dogovors(Crypto_file, BaseHierarcy):
    name = CodeStrictField()
    description = DescriptionField()

    date = DateTimeField(verbose_name='Дата', db_index=True, default=timezone.now)
    date_sign = DateTimeField(verbose_name='Дата подписания', db_index=True, null=True, blank=True)

    status = ForeignKeyProtect(StatusDogovor)
    customer = ForeignKeyProtect(Customer)
    type = ForeignKeyProtect(Dogovor_types)

    props = BitField(flags=(
        ('real', 'Реальный документ'),
    ), default=1, db_index=True)

    objects = DogovorsManager()

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Договора'
