'''String commands

Copyright (c) 2020 Machine Zone, Inc. All rights reserved.
'''


class StringsCommandsMixin:
    async def set(self, key, value):
        async with self.lock:
            return await self.send('SET', key, key, value)

    async def get(self, key):
        async with self.lock:
            return await self.send('GET', key, key)
