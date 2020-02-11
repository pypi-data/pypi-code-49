import logging

from asyncpg import create_pool

from .base import Producer


LOG = logging.getLogger(__name__)


class TimescaleProducer(Producer):
    '''
    Uses connections from a shared connection pool to connect to a timescale database.

    Exposes a number of methods for ease of use implementation by a client.
    TODO: Document interface.
    '''
    async def _setup(self) -> None:
        await super()._setup()
        self.pool = await create_pool(
            host=self.hosts,
            database=self.database,
            user=self.username,
            password=self.password,
            loop=self.loop,
            min_size=10,
            max_size=100,
        )

    async def connect(self) -> None:
        self.connected = True

    async def disconnect(self) -> None:
        await self.producer.stop()
        self.connected = False

    async def produce_data(self, data: dict, target: str = None) -> None:
        '''
        Produces the values in the passed data dict in corresponding given order.
        '''
        async with self.pool.acquire() as connection:
            async with connection.transaction():
                await connection.execute(data)
