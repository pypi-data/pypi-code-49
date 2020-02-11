import logging

from bitfield import BitField
from django.db import transaction

from isc_common.fields.code_field import CodeField
from isc_common.fields.name_field import NameField
from isc_common.fields.related import ForeignKeyProtect
from isc_common.http.DSRequest import DSRequest
from isc_common.models.audit import AuditManager
from isc_common.models.base_ref import BaseRef
from isc_common.progress import managed_progress

logger = logging.getLogger(__name__)


class AttrManager(AuditManager):
    def deleteFromRequest(self, request, removed=None, ):
        from kaf_pas.kd.models.document_attributes import Document_attributes
        from kaf_pas.kd.models.document_attr_cross import Document_attr_cross
        from kaf_pas.kd.models.lotsman_document_attr_cross import Lotsman_document_attr_cross

        request = DSRequest(request=request)
        res = 0
        tuple_ids = request.get_tuple_ids()
        for id, mode in tuple_ids:
            if mode == 'hide':
                super().filter(id=id).soft_delete()
            else:
                cnt = Document_attributes.objects.filter(attr_type_id=id).count()
                with managed_progress(id=f'delete_{id}', qty=Document_attributes.objects.filter(attr_type_id=id).count(), user=request.user_id, title='Удаление атрибута(ов)') as progress:
                    with transaction.atomic():
                        progress.setContentsLabel(f'<b>Удаляю: {Attr_type.objects.get(id=id)}, вхождений: {cnt}</b>')
                        for attribute in Document_attributes.objects.filter(attr_type_id=id):
                            qty, _ = Document_attr_cross.objects.select_related('attribute').filter(attribute=attribute).delete()
                            res += qty

                            qty, _ = Lotsman_document_attr_cross.objects.select_related('attribute').filter(attribute=attribute).delete()
                            res += qty

                            attribute.delete()
                            progress.step()

                        qty, _ = super().filter(id=id).delete()

            res += qty
        return res

    @staticmethod
    def getRecord(record):
        res = {
            "id": record.id,
            "code": record.code,
            "name": record.name,
            "description": record.description,
            "parent_id": record.parent_id,
            "lastmodified": record.lastmodified,
            "editing": record.editing,
            "deliting": record.deliting,
        }
        return res

    @staticmethod
    def get_or_create_attr(attr_codes, attr_names=None, logger=None):
        attr_codes = attr_codes.split('.')
        attr_names = attr_names.split('.') if attr_names != None else []
        attr_type = None
        parent_attr_type = None
        i = 0
        for attr_code in attr_codes:
            attr_name = None
            try:
                attr_name = attr_names[i]
            except:
                attr_name = attr_codes[i]

            attr_type, create = Attr_type.objects.get_or_create(
                code=attr_code,
                defaults=dict(
                    name=attr_name,
                    parent=parent_attr_type,
                ))
            i += 1

            # if create and logger:
            #     logger.logging(f'Added Parent Attr_type: {attr_type}', 'debug')

            parent_attr_type = attr_type

        if attr_type == None:
            raise Exception(f'Failed to create type with code {attr_codes}.')
        return attr_type

    def get_attr(self, code, name=None, default=None):
        try:
            if name:
                return super().get_queryset().get(code=code, name=name)
            else:
                return super().get_queryset().get(code=code)
        except Attr_type.DoesNotExist as e:
            if default:
                return default
            else:
                raise e


class Attr_type(BaseRef):
    code = CodeField(verbose_name="Код", db_index=True, unique=True)
    name = NameField(verbose_name="Наименование", db_index=True)
    props = BitField(flags=(
        ('relevant', 'Актуальность'),
    ), default=1, db_index=True)
    parent = ForeignKeyProtect("self", null=True, blank=True)

    relevent_label = "Действует"
    not_relevent_label = "Не действует"

    objects = AttrManager()

    def __str__(self):
        return f"ID={self.id}, code={self.code} name={self.name} props={self.props}"

    class Meta:
        verbose_name = 'Тип атрибута'
