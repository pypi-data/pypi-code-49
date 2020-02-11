import logging
import json
from typing import (
    Tuple,
    Any,
)

from gmqtt import Client as GMQTTClient, Subscription
from gmqtt.mqtt.constants import MQTTv311

from .base import Client


LOG = logging.getLogger(__name__)


class MQTTClient(Client):
    ''' Client for subscribing to a broker and pipe incomming messages to configured producer. '''
    def __init__(
            self,
            **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self._inner_client = GMQTTClient(None)

        self._inner_client.on_connect = self.on_connect
        self._inner_client.on_message = self.on_message
        self._inner_client.on_disconnect = self.on_disconnect
        self._inner_client.on_subscribe = self.on_subscribe
        self._inner_client.pipe_message = self.pipe_message

        if not self.username is None:
            self._inner_client.set_auth_credentials(self.username, self.password)


    async def connect(self, topics: Tuple[str, int]) -> None:
        ''' Connects to broker. '''
        LOG.debug('Connecting to MQTT broker.')
        try:
            await self._inner_client.connect(self.uri, 1883, keepalive=60, version=MQTTv311)
            subscriptions = [Subscription(t[0], qos=t[1]) for t in topics]
            self._inner_client.subscribe(subscriptions, subscription_identifier=1)

            await self.producer.connect()

            self.connected = True
        except:
            self.connected = False


async def serialize(data):
    ''' Decodes recieved data to utf-8 and returns it as a dict. '''
    data = data.decode('utf-8')
    try:
        return json.loads(data)
    except json.decoder.JSONDecodeError:
        return data
