'''Generic commands

Copyright (c) 2020 Machine Zone, Inc. All rights reserved.
'''


class GenericCommandsMixin:
    async def auth(self, password):
        async with self.lock:
            return await self.send('AUTH', None, password)

    async def ping(self):
        async with self.lock:
            return await self.send('PING')

    async def delete(self, key):
        async with self.lock:
            return await self.send('DEL', key, key)

    async def exists(self, key):
        async with self.lock:
            return await self.send('EXISTS', key, key)
