import logging
import asyncio
from typing import (
    Callable,
    List,
)
from pipeline.producers import get_producer


LOG = logging.getLogger(__name__)


def _on_connect(client, *args, **kwargs):
    LOG.debug('%s: CONNECTED', client._client_id)


async def _on_message(client, msg, *args, **kwargs):
    LOG.debug('RECV: %s', msg)


def _on_disconnect(client, *args, **kwargs):
    LOG.debug('%s: DISCONNECTED', client._client_id)


def _on_subscribe(client, *args, **kwargs):
    LOG.debug('%s: SUBSCRIBED TO TOPICS.', client._client_id)


class Client:
    ''' Base class for consumers.'''
    def __init__(
            self,
            uri: str,
            username: str = None,
            password: str = None,
            connected: bool = False,
            on_connect: Callable = _on_connect,
            on_message: Callable = _on_message,
            on_disconnect: Callable = _on_disconnect,
            on_subscribe: Callable = _on_subscribe,
    ):
        self.uri = uri
        self.username = username
        self.password = password
        self.connected = connected

        self.on_connect = on_connect
        self.on_message = on_message
        self.on_disconnect = on_disconnect
        self.on_subscribe = on_subscribe

        self.loop = asyncio.get_event_loop()

    async def _setup(self):
        self.producer = await get_producer()

    async def pipe_message(self, data: dict, target: str) -> None:
        ''' Pipes mesage to configured producer. '''
        await self.producer.produce_data(
            data=data,
            target=target,
        )

    async def connect(self, topics: List) -> None:
        raise NotImplementedError("No driver specified")

    async def disconnect(self) -> None:
        raise NotImplementedError("No driver specified")
