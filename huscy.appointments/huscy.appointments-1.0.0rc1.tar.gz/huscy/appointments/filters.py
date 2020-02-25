from django_filters import rest_framework as filters

from huscy.appointments.models import Appointment


class AppointmentFilter(filters.FilterSet):
    # Note: from_time and to_time express a time range within the appointment starts
    from_time = filters.DateTimeFilter(field_name="start", lookup_expr='gte')
    to_time = filters.DateTimeFilter(field_name="start", lookup_expr='lte')

    class Meta:
        model = Appointment
        fields = (
            'from_time',
            'owner',
            'resource',
            'title',
            'to_time',
        )
