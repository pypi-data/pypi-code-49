'''Simple client for redis

Copyright (c) 2020 Machine Zone, Inc. All rights reserved.

TODO:
    RESP3 support (start by sending hello3) / then use hash types
'''

import asyncio
import collections
import hiredis

from rcc.connection import Connection
from rcc.hash_slot import getHashSlot


ClusterNode = collections.namedtuple(
    'ClusterNode', ['node_id', 'address', 'ip', 'port', 'role', 'slots']
)


class RedisClient(object):
    connections = {}
    urls = {}

    def __init__(self, url: str, password):
        self.password = password

        self.lock = asyncio.Lock()
        self.connectionsLock = asyncio.Lock()

        self.connection = Connection(url, password)

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

    async def auth(self, password):
        async with self.lock:
            return await self.send('AUTH', None, password)

    async def ping(self):
        async with self.lock:
            return await self.send('PING')

    async def delete(self, key):
        async with self.lock:
            return await self.send('DEL', key, key)

    async def set(self, key, value):
        async with self.lock:
            return await self.send('SET', key, key, value)

    async def get(self, key):
        async with self.lock:
            return await self.send('GET', key, key)

    async def exists(self, key):
        async with self.lock:
            return await self.send('EXISTS', key, key)

    async def xinfo(self, key, stream=True):
        async with self.lock:
            return await self.send('XINFO', key, 'STREAM', key)

    async def xadd(self, key: str, attrName: str, attrValue: str, maxLen: int):
        async with self.lock:
            return await self.send(
                'XADD',
                key,
                key,
                b'MAXLEN',
                b'~',
                str(maxLen).encode(),
                b'*',
                attrName,
                attrValue,
            )

    async def xread(self, key, latest_id):
        '''
        Result set is a list
        [[b'1580684995724-0', [b'temperature', b'10']]]
        '''
        async with self.lock:
            response = await self.send(
                'XREAD', key, b'BLOCK', b'0', b'STREAMS', key, latest_id
            )

            items = []
            for item in response[0][1]:
                position = item[0]
                array = item[1]
                entries = {}

                for i in range(len(array) // 2):
                    key = array[2 * i]
                    value = array[2 * i + 1]
                    entries[key] = value

                items.append((position, entries))

            return items

    async def xrevrange(self, key, end, start, count):
        '''
        > XREVRANGE foo + - COUNT 1
        1) 1) "1580792642251-0"
           2) 1) "json"
              2) "{}"
        '''
        async with self.lock:
            response = await self.send(
                'XREVRANGE', key, key, end, start, b'COUNT', str(count)
            )

            items = []
            for item in response:
                position = item[0]
                array = item[1]
                entries = {}

                for i in range(len(array) // 2):
                    key = array[2 * i]
                    value = array[2 * i + 1]
                    entries[key] = value

                items.append((position, entries))

            return items

    async def cluster_nodes(self):
        async with self.lock:
            response = await self.send('CLUSTER', None, 'NODES')

            # ERR This instance has cluster support disabled'
            responseType = type(response)
            if responseType == hiredis.ReplyError:
                return []

            response = response.decode()

            nodes = []
            for line in response.splitlines():
                tokens = line.split()
                node_id = tokens[0]

                address = tokens[1]
                url, _, _ = address.partition('@')
                ip, _, port = url.partition(':')

                role = tokens[2]
                role = role.replace('myself,', '')
                role = role.replace('myself,', '')

                slots = []
                for token in tokens[8:]:
                    if '-' in token:
                        start, _, end = token.partition('-')
                        start = int(start)
                        end = int(end)
                        for i in range(start, end + 1):
                            slots.append(i)
                    else:
                        slots.append(token)

                nodes.append(ClusterNode(node_id, address, ip, port, role, slots))

            return nodes

    def __repr__(self):
        return f'RedisClient at {self.connection.host}:{self.connection.port}'


async def create_redis_publisher(host, port, password, verbose=False):
    client = RedisClient(host, port, password, verbose)
    await client.connect()
    return client
