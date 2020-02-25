import socket

from django_ical.views import ICalFeed
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from huscy.appointments import models, services


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_feed_url(request):
    token, _ = models.Token.objects.get_or_create(user=request.user)
    return Response({'feed': f'/feed/{token.key}'})


class AppointmentFeed(ICalFeed):
    timezone = 'UTC'
    file_name = "appointments.ics"

    def __call__(self, request, *args, **kwargs):
        try:
            self.user = models.Token.objects.get(key=kwargs['token']).user
        except models.Token.DoesNotExist:
            self.user = None

        return super(AppointmentFeed, self).__call__(request, *args, **kwargs)

    def items(self):
        if self.user and self.user.is_superuser:
            return services.get_appointments()
        elif self.user:
            return services.get_appointments(owner=self.user)
        return []

    def item_guid(self, item):
        return f'{item.id}@{socket.getfqdn()}'

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_start_datetime(self, item):
        return item.start

    def item_end_datetime(self, item):
        return item.end

    def item_link(self, item):
        return ''
