'''Generic commands

Copyright (c) 2020 Machine Zone, Inc. All rights reserved.
'''


class GenericCommandsMixin:
    async def unknown_command(self):
        '''for testing'''
        return await self.send('UNKNOWN')

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

    async def migrate(self, host, port, db, timeout, *keys):
        '''
        https://redis.io/commands/migrate
        redis-cli -p 5000 del foo ; redis-cli set foo bar ; redis-cli migrate 127.0.0.1 5000 "" 0 5000 KEYS foo  # noqa
        '''
        return await self.send(
            'MIGRATE', None, host, port, "", db, timeout, "KEYS", *keys
        )
