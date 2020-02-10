'''Publish to a channel

Copyright (c) 2020 Machine Zone, Inc. All rights reserved.
'''

import asyncio

import click
from rcc.client import RedisClient


async def pub(redis_url, redis_password, channel, msg, batch):
    client = RedisClient(redis_url, redis_password)
    await client.connect()

    maxLen = 100

    if batch:
        while True:
            streamId = await client.xadd(channel, 'json', msg, maxLen)
    else:
        streamId = await client.xadd(channel, 'json', msg, maxLen)
        print('Stream id:', streamId)


@click.command()
@click.option('--redis_url', default='redis://localhost')
@click.option('--redis_password')
@click.option('--channel', default='foo')
@click.option('--msg', default='{"bar": "baz"}')
@click.option('--batch', is_flag=True)
def publish(redis_url, redis_password, channel, msg, batch):
    '''Publish to a channel
    '''

    asyncio.get_event_loop().run_until_complete(
        pub(redis_url, redis_password, channel, msg, batch)
    )
