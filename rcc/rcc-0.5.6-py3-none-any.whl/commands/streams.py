class StreamsCommandsMixin:
    async def xinfo(self, key, stream=True):
        return await self.send('XINFO', key, 'STREAM', key)

    async def xadd(self, key: str, attrName: str, attrValue: str, maxLen: int):
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
