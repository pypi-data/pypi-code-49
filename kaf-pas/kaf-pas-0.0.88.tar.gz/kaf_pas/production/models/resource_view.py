import logging

from django.db.models import BooleanField

from clndr.models.calendars import Calendars
from isc_common.fields.related import ForeignKeyProtect
from isc_common.managers.common_managet_with_lookup_fields import CommonManagetWithLookUpFieldsQuerySet, CommonManagetWithLookUpFieldsManager
from isc_common.models.base_ref import BaseRefHierarcy, BaseRef
from isc_common.number import DelProps
from kaf_pas.ckk.models.locations import Locations
from kaf_pas.production.models.resource import ResourceManager

logger = logging.getLogger(__name__)


class Resource_viewQuerySet(CommonManagetWithLookUpFieldsQuerySet):
    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Resource_viewManager(CommonManagetWithLookUpFieldsManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'code': record.code,
            'name': record.name,
            'full_name': record.name,
            'description': record.description,
            'isFolder': record.isFolder,
            # "location_id": record.location.id,
            # "location__code": record.location.code,
            # "location__name": record.location.name,
            # "location__full_name": record.location.full_name,
            'calendar_id': record.calendar.id if record.calendar else None,
            'calendar__full_name': record.calendar.full_name if record.calendar else None,
            'isWorkshop': record.props.isWorkshop,
            'props': record.props,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return DelProps(res)

    def get_queryset(self):
        return Resource_viewQuerySet(self.model, using=self._db)

    @property
    def full_name(self):
        return f'{self.location.full_name}/{super().full_name}'


class Resource_view(BaseRef):
    location = ForeignKeyProtect(Locations)
    calendar = ForeignKeyProtect(Calendars, null=True, blank=True)
    isFolder = BooleanField()
    props = ResourceManager.props()

    objects = Resource_viewManager()

    def __str__(self):
        return f"{self.id}"

    class Meta:
        db_table = 'production_resource_view'
        managed = False
        verbose_name = 'Ресурсы'
