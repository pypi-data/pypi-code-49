'''PubSub commands

Copyright (c) 2020 Machine Zone, Inc. All rights reserved.
'''
import asyncio


class PubSubCommandsMixin:
    async def subscribe(self, key, callback, obj):
        '''Will take over the connection.
           Do not send any other command while this is running.
        '''
        response = await self.send('SUBSCRIBE', None, key)

        try:
            while True:
                response = await self.readResponse(self.connection)
                await callback(obj, response)

        except asyncio.CancelledError:
            await self.send('UNSUBSCRIBE', None, key)

    async def psubscribe(self, key, callback, obj):
        '''Will take over the connection.
           Do not send any other command while this is running.
        '''
        response = await self.send('PSUBSCRIBE', None, key)

        try:
            while True:
                response = await self.readResponse(self.connection)
                await callback(obj, response)

        except asyncio.CancelledError:
            await self.send('PUNSUBSCRIBE', None, key)

    async def publish(self, key, value):
        await self.send('PUBLISH', None, key, value)
