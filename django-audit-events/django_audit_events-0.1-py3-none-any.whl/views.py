from django.db.models import ForeignObject, ManyToManyField
from rest_framework import viewsets

from django_audit_events.filters import AuditEventFilterSet
from django_audit_events.models import get_audit_event_model
from django_audit_events.serializers import EventSerializer

AuditEvent = get_audit_event_model()


class AuditEventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AuditEvent.objects.all()
    filter_class = AuditEventFilterSet

    def __new__(cls, *args, **kwargs):
        obj = super(AuditEventViewSet, cls).__new__(cls, *args, **kwargs)
        obj.filter_class.Meta.model = AuditEvent
        return obj

    # noinspection PyMethodMayBeStatic
    def get_serializer_class(self, *args, **kwargs):
        EventSerializer.Meta.model = AuditEvent
        return EventSerializer

    def get_queryset(self):
        # noinspection PyProtectedMember
        fields = AuditEvent._meta.local_fields
        select_related = []
        prefetch_related = []

        for field in fields:
            if isinstance(field, ForeignObject):
                select_related.append(field.name)
            elif isinstance(field, ManyToManyField):
                prefetch_related.append(field.name)

        queryset = super(AuditEventViewSet, self).get_queryset()
        return queryset.select_related(*select_related).prefetch_related(
            *prefetch_related
        )
