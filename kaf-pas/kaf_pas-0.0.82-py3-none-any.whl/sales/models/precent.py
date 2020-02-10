import logging

from django.db import transaction
from django.db.models import DateTimeField
from django.forms import model_to_dict
from django.utils import timezone

from crypto.models.crypto_file import Crypto_file, CryptoManager, CryptoQuerySet
from isc_common import delAttr, setAttr, getAttr
from isc_common.fields.code_field import CodeField
from isc_common.fields.description_field import DescriptionField
from isc_common.fields.related import ForeignKeyProtect
from isc_common.http.DSRequest import DSRequest
from kaf_pas.sales.models.precent_item_types import Precent_item_types
from kaf_pas.sales.models.precent_types import Precent_types
from kaf_pas.sales.models.status_precent import StatusPrecent

logger = logging.getLogger(__name__)


class PrecentQuerySet(CryptoQuerySet):
    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class PrecentManager(CryptoManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'code': record.code,
            'date': record.date,
            'date_sign': record.date_sign,
            'description': record.description,

            'status_id': record.status.id,
            'status__code': record.status.code,
            'status__name': record.status.name,

            'format': record.format,
            'mime_type': record.mime_type,
            'size': record.size if not str(record.size).startswith('.') else str(record.size).replace('.', '0.'),
            'real_name': record.real_name,

            'lastmodified': record.lastmodified,
            'editing': record.editing,
            'deliting': record.deliting,
            'parent_id': record.parent.id if record.parent else None,

            'precent_item_type_id': record.precent_item_type.id,
            'precent_item_type__code': record.precent_item_type.code,
            'precent_item_type__name': record.precent_item_type.name,

            'precent_type_id': record.precent_type.id,
            'precent_type__code': record.precent_type.code,
            'precent_type__name': record.precent_type.name,
        }
        return res

    def createFromRequest(self, request, printRequest=False, function=None):
        from kaf_pas.sales.models.precent_dogovors import Precent_dogovors
        from kaf_pas.sales.models.status_dogovor import StatusDogovor
        from kaf_pas.sales.models.dogovor_types import Dogovor_types
        from kaf_pas.sales.models.customer import Customer
        from kaf_pas.sales.models.dogovors import Dogovors

        request = DSRequest(request=request)
        data = request.get_data()
        _data = data.copy()
        for key in data:
            if key.find('__') != -1:
                delAttr(_data, key)
        delAttr(_data, 'form')

        with transaction.atomic():
            document = data.get('document')
            if not isinstance(document, list):
                status, _ = StatusDogovor.objects.get_or_create(code='virtual', props=0)
                customer, _ = Customer.objects.get_or_create(name='virtual', props=0)
                dogovor_type, _ = Dogovor_types.objects.get_or_create(code='virtual', props=0)
                dogovor, _ = Dogovors.objects.get_or_create(name='virtual', status=status, customer=customer, type=dogovor_type, props=0, deliting=False, editing=False)
                document = [dogovor.id]

            else:
                delAttr(_data, 'document')
            for document_id in document:
                if data.get('id') or not data.get('real_name'):
                    delAttr(_data, 'id')
                    setAttr(_data, 'precent_item_type', Precent_types.objects.get(id=getAttr(_data, 'precent_type_id')).precent_item_type)
                    res, _ = super().get_or_create(id=data.get('id'), defaults=_data)

                    Precent_dogovors.objects.get_or_create(dogovor_id=document_id, precent=res)
                    res = model_to_dict(res)
                    delAttr(res, 'attfile')
                    delAttr(res, 'form')
                    data.update(res)

        return data

    def updateFromRequest(self, request):
        request = DSRequest(request=request)
        data = request.get_data()
        _data = data.copy()
        # data.update(dict(type))
        delAttr(_data, 'status__code')
        delAttr(_data, 'status__name')
        delAttr(_data, 'precent_item_type__code')
        delAttr(_data, 'precent_item_type__name')
        delAttr(_data, 'type__name')
        delAttr(_data, 'ifFolder')
        delAttr(_data, 'form')
        super().filter(id=request.get_id()).update(**_data)
        return data

    def get_queryset(self):
        return PrecentQuerySet(self.model, using=self._db)


class Precent(Crypto_file):
    code = CodeField()
    description = DescriptionField()
    parent = ForeignKeyProtect('self', null=True, blank=True, related_name='parent_p')

    date = DateTimeField(verbose_name='Дата', db_index=True, default=timezone.now)
    date_sign = DateTimeField(verbose_name='Дата подписания', db_index=True, null=True, blank=True)

    status = ForeignKeyProtect(StatusPrecent)
    precent_item_type = ForeignKeyProtect(Precent_item_types)
    precent_type = ForeignKeyProtect(Precent_types)

    objects = PrecentManager()

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Распоряжение'
