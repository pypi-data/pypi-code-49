import logging

from bitfield import BitField
from django.db.models import UniqueConstraint, Q

from clndr.models.calendars import Calendars
from isc_common.fields.related import ForeignKeyProtect
from isc_common.managers.common_managet_with_lookup_fields import CommonManagetWithLookUpFieldsQuerySet, CommonManagetWithLookUpFieldsManager
from isc_common.models.base_ref import BaseRefQuerySet, BaseRef
from isc_common.number import DelProps
from kaf_pas.ckk.models.locations import Locations

logger = logging.getLogger(__name__)


class ResourceQuerySet(CommonManagetWithLookUpFieldsQuerySet, BaseRefQuerySet):
    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class ResourceManager(CommonManagetWithLookUpFieldsManager):

    @staticmethod
    def props():
        return BitField(flags=(
            ('isWorkshop', 'Уровень цеха'),  # 1
        ), default=0, db_index=True)

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'code': record.code,
            'name': record.name,
            'description': record.description,
            'calendar_id': record.calendar.id if record.calendar else None,
            'calendar__full_name': record.calendar.full_name if record.calendar else None,
            'editing': record.editing,
            'deliting': record.deliting,
            'isWorkshop': record.props.isWorkshop,
            'props': record.props,
        }
        return DelProps(res)

    def get_queryset(self):
        return ResourceQuerySet(self.model, using=self._db)


class Resource(BaseRef):
    location = ForeignKeyProtect(Locations)
    calendar = ForeignKeyProtect(Calendars, null=True, blank=True)
    props = ResourceManager.props()

    objects = ResourceManager()

    @property
    def get_calendar(self):
        return self.calendar

    def __str__(self):
        return f"ID: {self.id}, code: {self.code}, name: {self.name}, description: {self.description}, location: [{self.location}]"

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = 'Ресурсы'
        constraints = [
            UniqueConstraint(fields=['location', 'props'], condition=Q(calendar=None), name='Resource_unique_constraint_0'),
            UniqueConstraint(fields=['calendar', 'location', 'props'], name='Resource_unique_constraint_1'),
        ]
