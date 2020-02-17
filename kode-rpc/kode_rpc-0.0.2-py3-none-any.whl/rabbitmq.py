import asyncio
import logging
from typing import Optional

from aio_pika import connect_robust, Connection
from aiormq import IncompatibleProtocolError

logger = logging.getLogger(__name__)


class RabbitMQ:
    def __init__(self, host: str, user: str, password: str):
        self._host = host
        self._user = user
        self._password = password
        self._connection = None

    async def connect(self):
        assert self._connection is None, 'Connection has already established'

        try:
            self._connection = await connect_robust(
                host=self._host,
                login=self._user,
                password=self._password,
            )
            logger.info(f'Connected to RabbitMQ {self._connection.__repr__()}')
        except (IncompatibleProtocolError, ConnectionError):
            logger.warning('Could not connect to RabbitMQ, going to retry in 5 seconds')
            await asyncio.sleep(5)
            await self.connect()

    @property
    def connection(self) -> Optional[Connection]:
        return self._connection

    async def disconnect(self):
        async def _closer():
            try:
                for channel in tuple(self.connection.connection.channels.values()):
                    await channel.close()
            finally:
                await self.connection.close()

        if self.connection:
            await asyncio.shield(_closer())
