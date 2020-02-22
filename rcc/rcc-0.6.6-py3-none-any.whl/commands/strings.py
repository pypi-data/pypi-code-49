'''String commands

Copyright (c) 2020 Machine Zone, Inc. All rights reserved.
'''


class StringsCommandsMixin:
    async def set(self, key, value):
        return await self.send('SET', key, key, value)

    async def get(self, key):
        return await self.send('GET', key, key)
