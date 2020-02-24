import logging

from django.db.models import BooleanField

from isc_common.managers.common_managet_with_lookup_fields import CommonManagetWithLookUpFieldsManager, CommonManagetWithLookUpFieldsQuerySet
from isc_common.models.base_ref import BaseRefHierarcy
from isc_common.number import DelProps
from kaf_pas.production.models.operations import OperationsManager

logger = logging.getLogger(__name__)


class Operations_viewQuerySet(CommonManagetWithLookUpFieldsQuerySet):
    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Operations_viewManager(CommonManagetWithLookUpFieldsManager):

    @staticmethod
    def getRecord(record):
        res = {
            "id": record.id,
            "code": record.code,
            "name": record.name,
            "full_name": record.full_name,
            "description": record.description,
            "parent_id": record.parent_id,
            "lastmodified": record.lastmodified,
            'isFolder': record.isFolder,
            'editing': record.editing,
            'deliting': record.deliting,
            'props': record.props,
            'made_common_form': record.props.made_common_form,
        }
        return DelProps(res)

    def get_queryset(self):
        return Operations_viewQuerySet(self.model, using=self._db)


class Operations_view(BaseRefHierarcy):
    isFolder = BooleanField()
    props = OperationsManager.get_props()

    objects = Operations_viewManager()

    def _get_planing_operation_type(self, parent):
        if parent:
            if parent.planing_operation_type:
                return parent.planing_operation_type
            else:
                return self._get_planing_operation_type(parent=parent.parent)
        else:
            return None

    def __str__(self):
        return f"ID={self.id}, code={self.code}, name={self.name}, description={self.description}"

    class Meta:
        db_table = 'production_operations_view'
        managed = False
        verbose_name = 'Операции'
