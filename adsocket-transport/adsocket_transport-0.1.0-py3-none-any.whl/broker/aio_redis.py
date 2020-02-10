import json

from . import BaseBroker
import aioredis


class Redis(BaseBroker):

    _r = None

    def __init__(self, channel='adsocket', host=None, port=6379, db=0,
                 max_connections=5, **kwargs):
        self._host = host
        self._port = port
        self._db = db
        self._max_connections = max_connections
        self._channel = channel
        self._loop = kwargs.get('loop')

    @property
    async def _redis(self) -> aioredis.Redis:
        if not self._r:
            self._r = await aioredis.create_redis(
                self._host,
                db=self._db,
                loop=self._loop)
        return self._r

    async def publish(self, message):
        r = await self._redis
        await r.publish(self._channel, message.to_json())

    async def store_credentials(self, key, data, ttl=None):
        """
        Store user authentication token to redis
        :param key:
        :param data:
        :param ttl:
        :return:
        """
        r = await self._redis
        await r.set(key, json.dumps(data), expire=ttl)


broker = Redis
