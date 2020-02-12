'''Generic commands

Copyright (c) 2020 Machine Zone, Inc. All rights reserved.
'''


class GenericCommandsMixin:
    async def auth(self, password):
        return await self.send('AUTH', None, password)

    async def ping(self):
        return await self.send('PING')

    async def delete(self, key):
        return await self.send('DEL', key, key)

    async def exists(self, key):
        return await self.send('EXISTS', key, key)

    async def info(self):
        response = await self.send('INFO', None)
        s = response.decode()

        attributes = {}
        for line in s.splitlines():
            if line.startswith('#'):
                continue

            key, _, val = line.partition(':')
            attributes[key] = val

        return attributes
