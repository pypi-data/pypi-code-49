# -*- coding: utf-8 -*-

from nwae.utils.Log import Log
from inspect import getframeinfo, currentframe
import asyncio


class BroadcastHandler:

    def __init__(self):
        return

    async def async_task(self, arg):
        # Do some long IO here
        print('Step 1: ' + str(arg))
        # Let other tasks run
        await asyncio.sleep(0)
        # Do whatever else here
        print('Step 2: ' + str(arg))

    async def handler(self, args):
        atasks = []
        for arg in args:
            atask = asyncio.create_task(self.async_task(arg))
            atasks.append(atask)

        for atask in atasks:
            await atask


if __name__ == '__main__':
    asyncio.run(BroadcastHandler().handler(['jenny','yuna']))

