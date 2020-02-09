import logging

from clndr.models.calendars import Calendars
from isc_common.fields.related import ForeignKeyProtect
from isc_common.managers.common_managet_with_lookup_fields import CommonManagetWithLookUpFieldsQuerySet, CommonManagetWithLookUpFieldsManager
from isc_common.models.base_ref import BaseRefHierarcy, BaseRefQuerySet
from kaf_pas.ckk.models.locations import Locations

logger = logging.getLogger(__name__)


class ResourceQuerySet(CommonManagetWithLookUpFieldsQuerySet, BaseRefQuerySet):
    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class ResourceManager(CommonManagetWithLookUpFieldsManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'code': record.code,
            'name': record.name,
            'full_name': record.full_name,
            'description': record.description,
            'parent_id': record.parent.id if record.parent else None,
            'calendar_id': record.calendar.id if record.calendar else None,
            'calendar__full_name': record.calendar.full_name if record.calendar else None,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return ResourceQuerySet(self.model, using=self._db)


class Resource(BaseRefHierarcy):
    location = ForeignKeyProtect(Locations)
    calendar = ForeignKeyProtect(Calendars, null=True, blank=True)

    objects = ResourceManager()

    def _get_calendar(self, parent):
        if parent:
            if parent.calendar:
                return parent.calendar
            else:
                return self._get_calendar(parent=parent.parent)
        else:
            return None

    @property
    def get_calendar(self):
        if self.calendar:
            return self.calendar

        return self._get_calendar(parent=self.parent)

    def __str__(self):
        return f"ID: {self.id}, code: {self.code}, name: {self.name}, full_name: {self.full_name}, description: {self.description}, location: [{self.location}]"

    def __repr__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Ресурсы'
