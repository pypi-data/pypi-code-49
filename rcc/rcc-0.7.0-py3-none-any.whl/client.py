'''Redis client

Copyright (c) 2020 Machine Zone, Inc. All rights reserved.

TODO:
    RESP3 support (start by sending hello3) / then use hash types
'''

import asyncio
import hiredis

from rcc.hash_slot import getHashSlot
from rcc.pool import ConnectionPool

from rcc.commands.cluster import ClusterCommandsMixin
from rcc.commands.pubsub import PubSubCommandsMixin
from rcc.response import ResponseConverterMixin


class RedisClient(ClusterCommandsMixin, PubSubCommandsMixin, ResponseConverterMixin):
    def __init__(self, url: str, password):
        self.url = url
        self.password = password

        self.lock = asyncio.Lock()

        self.pool = ConnectionPool(password)
        self.urls = {}

        self.connection = self.pool.get(self.url)
        self.cluster = False

    @property
    def host(self):
        return self.connection.host

    @property
    def port(self):
        return self.connection.port

    async def connect(self):
        await self.connection.connect()

        info = await self.send('INFO')
        self.cluster = info.get('cluster_enabled') == '1'

        if self.cluster:
            await self.connect_cluster_nodes()

    async def connect_cluster_nodes(self):
        nodes = await self.cluster_nodes()
        for node in nodes:
            if node.role == 'master':
                url = f'redis://{node.ip}:{node.port}'
                await self.setConnection(node.slots, url)

    async def readResponse(self, connection):
        response = await connection.readResponse()
        return response

    def close(self):
        # FIXME
        pass

    async def getConnection(self, key):
        hashSlot = None
        if key is not None:
            hashSlot = getHashSlot(key)

        url = self.urls.get(hashSlot, self.url)
        connection = self.pool.get(url)

        return connection

    async def setConnection(self, slots, url: str):
        connection = self.pool.get(url)
        await connection.connect()

        for slot in slots:
            self.urls[slot] = url

    async def send(self, cmd, *args):
        # FIXME we need a timeout here, and not retry until the end of time
        #       in cluster mode. (like aredis does)

        # We need to extract the key to hash it in cluster mode
        key = None if len(args) == 0 else args[0]

        # key is at different spot than first args for some commands such as STREAMS

        async with self.lock:
            while True:
                # we should optimize this for the common case
                connection = await self.getConnection(key)

                await connection.send(cmd, key, *args)
                response = await self.readResponse(connection)

                responseType = type(response)
                if responseType != hiredis.ReplyError:
                    return self.convert(response, cmd)

                responseStr = str(response)
                if responseStr.startswith('MOVED'):
                    tokens = responseStr.split()
                    slotStr = tokens[1]
                    slot = int(slotStr)
                    url = tokens[2]
                    url = 'redis://' + url

                    await self.setConnection([slot], url)
                else:
                    raise response

    def __repr__(self):
        return f'<RedisClient at {self.host}:{self.port}>'
