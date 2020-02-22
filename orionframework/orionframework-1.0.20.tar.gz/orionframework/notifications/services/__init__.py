import json

from orionframework.utils.reflection import get_class

from orionframework.notifications import settings
from orionframework.notifications.models import DeviceNotification


class NotificationService(object):
    enabled = settings.NOTIFICATION_ENABLED
    debug = settings.NOTIFICATION_DEBUG

    engines = {}

    def get_engine(self, service):
        if service not in self.engines:
            class_name = settings.NOTIFICATION_SERVICES.get(service)
            factory = get_class(class_name)

            self.engines[service] = factory()

        return self.engines.get(service)

    def push(self, device, recipient, title, description=None, data={}, **kwargs):
        notification = DeviceNotification(device=device,
                                          recipient=recipient,
                                          sender=device.user,
                                          title=title,
                                          description=description,
                                          data=data)

        if self.debug:
            print("Pushing notification: " + str(notification))

        if self.enabled:

            engine = self.get_engine(device.service)

            engine.send(notification, **kwargs)

        elif self.debug:
            print("NotificationService is currently disabled.")
            print("To enable, make sure to set ORION_NOTIFICATION_ENABLE='yes' on your .env file.")

        notification.save()

        return notification
