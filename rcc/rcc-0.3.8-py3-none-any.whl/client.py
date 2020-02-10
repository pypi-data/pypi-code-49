'''Redis client

Copyright (c) 2020 Machine Zone, Inc. All rights reserved.

TODO:
    RESP3 support (start by sending hello3) / then use hash types
'''

import asyncio
import hiredis

from rcc.connection import Connection
from rcc.hash_slot import getHashSlot

from rcc.commands.streams import StreamsCommandsMixin
from rcc.commands.cluster import ClusterCommandsMixin
from rcc.commands.generic import GenericCommandsMixin
from rcc.commands.strings import StringsCommandsMixin


class RedisClient(
    StreamsCommandsMixin,
    ClusterCommandsMixin,
    StringsCommandsMixin,
    GenericCommandsMixin,
):
    connections = {}
    urls = {}

    def __init__(self, url: str, password):
        self.password = password

        self.lock = asyncio.Lock()
        self.connectionsLock = asyncio.Lock()

        self.connection = Connection(url, password)

    @property
    def host(self):
        return self.connection.host

    @property
    def port(self):
        return self.connection.port

    async def connect(self):
        await self.connection.connect()

        nodes = await self.cluster_nodes()
        for node in nodes:
            url = f'redis://{node.ip}:{node.port}'
            await self.setConnection(node.slots, url)

    async def readResponse(self, connection):
        response = await connection.readResponse()
        return response

    def close(self):
        pass

    async def getConnection(self, key):
        hashSlot = None
        if key is not None:
            hashSlot = getHashSlot(key)

        async with self.connectionsLock:
            url = RedisClient.urls.get(hashSlot)
            connection = RedisClient.connections.get(url, self.connection)
            return connection

    async def setConnection(self, slots, url):
        async with self.connectionsLock:
            connection = Connection(url, self.password)
            await connection.connect()

            for slot in slots:
                RedisClient.urls[slot] = url

            RedisClient.connections[url] = connection

            self.connection = connection

    async def send(self, cmd, key=None, *args):
        # FIXME we need a timeout here, and not retry until the end of time

        while True:
            connection = await self.getConnection(key)

            await connection.send(cmd, key, *args)
            response = await self.readResponse(connection)

            responseType = type(response)
            if responseType != hiredis.ReplyError:
                return response

            responseStr = str(response)
            if responseStr.startswith('MOVED'):
                tokens = responseStr.split()
                slotStr = tokens[1]
                slot = int(slotStr)
                url = tokens[2]
                url = 'redis://' + url

                await self.setConnection([slot], url)
            else:
                return response

    def __repr__(self):
        return f'RedisClient at {self.host}:{self.port}'


async def create_redis_publisher(host, port, password, verbose=False):
    client = RedisClient(host, port, password, verbose)
    await client.connect()
    return client
