import logging

from bitfield import BitField
from django.db.models import DateTimeField, BigIntegerField, TextField, BooleanField

from isc_common.bit import IsBitOff
from isc_common.fields.code_field import CodeField
from isc_common.fields.description_field import DescriptionField
from isc_common.fields.name_field import NameField
from isc_common.fields.related import ForeignKeyProtect
from isc_common.models.audit import AuditModel, AuditManager, AuditQuerySet
from isc_common.models.base_ref import BaseHierarcy
from kaf_pas.sales.models.customer import Customer
from kaf_pas.sales.models.dogovor_types import Dogovor_types
from kaf_pas.sales.models.status_dogovor import StatusDogovor

logger = logging.getLogger(__name__)


class Dogovors_viewQuerySet(AuditQuerySet):
    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Dogovors_viewManager(AuditManager):

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
            'isFolder': record.isFolder,
            'parent_id': record.parent.id if record.parent else None,
            'enabled': IsBitOff(record.status.props, 0),
        }
        return res

    def get_queryset(self):
        return Dogovors_viewQuerySet(self.model, using=self._db)


class Dogovors_view(AuditModel, BaseHierarcy):
    name = CodeField()
    isFolder = BooleanField()
    description = DescriptionField()

    size = BigIntegerField(verbose_name='Размер фала', default=0)
    real_name = TextField(verbose_name='Первоначальное имя файла', null=True, blank=True, default=None)
    mime_type = NameField(verbose_name='MIME тип файла файла', null=True, blank=True, default=None)
    format = NameField(verbose_name='Формат файла')

    date = DateTimeField(verbose_name='Дата', db_index=True)
    date_sign = DateTimeField(verbose_name='Дата подписания', db_index=True, null=True, blank=True)

    status = ForeignKeyProtect(StatusDogovor)
    customer = ForeignKeyProtect(Customer)
    type = ForeignKeyProtect(Dogovor_types)

    props = BitField(flags=(
        ('real', 'Реальный документ'),
    ), default=1, db_index=True)

    objects = Dogovors_viewManager()

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Документы'
        db_table = 'sales_dogovors_view'
        managed = False
