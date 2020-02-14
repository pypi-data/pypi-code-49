"""Base Implementation of a Delivery Backend."""

import abc
from json import dumps
import six
import channels.layers
from asgiref.sync import async_to_sync

from django.contrib.auth import get_user_model

from . import default_settings as settings


@six.add_metaclass(abc.ABCMeta)
class BaseNotificationChannel():
    """Base channel for sending notifications."""

    def __init__(self, **kwargs):
        self.notification_kwargs = kwargs

    @abc.abstractmethod
    def construct_message(self):
        """Constructs a message from notification details."""
        pass

    @abc.abstractmethod
    def notify(self, message):
        """Sends the notification."""
        pass


class ConsoleChannel(BaseNotificationChannel):
    """Dummy channel that prints to the console."""

    def construct_message(self):
        """Stringify the notification kwargs."""
        return str(self.notification_kwargs)

    def notify(self, message):
        print(message)


class BasicWebSocketChannel(BaseNotificationChannel):
    """It creates a Redis user for each user (based on their username)."""

    def _connect(self):

        channel_layer = channels.layers.get_channel_layer()
        return channel_layer

    def construct_message(self):
        """Construct message from notification details."""

        return self.notification_kwargs

    def notify(self, message):
        """
        Puts a new message on the queue.
        
        The queue is named based on the username (for Uniqueness)
        """
        uri = self.notification_kwargs['uri']

        if not uri:
            return

        channel_layer = self._connect()
        # add this moment work only with user, not guest
        async_to_sync(channel_layer.group_send)(
            uri,
            {
                "type": "send_data",
                'data': message,
            }
        )

       # # Get user instance
        # User = get_user_model()
        # source = User.objects.get(id=message['source'])
        # recipient = User.objects.get(id=message['recipient'])
        #
        # channel.queue_declare(queue=source.username)
        #
        # jsonified_messasge = dumps(message)
        # channel.basic_publish(
        #     exchange='', routing_key=recipient.username,
        #     body=jsonified_messasge
        # )
