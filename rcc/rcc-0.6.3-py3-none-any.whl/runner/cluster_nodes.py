'''Repeatitly print cluster info

Copyright (c) 2020 Machine Zone, Inc. All rights reserved.
'''
import asyncio
import click

from rcc.client import RedisClient


def getSlotsRange(slots):
    '''I failed the programming interview quizz but the function
       works like redis CLUSTER NODES
    '''

    if len(slots) == 0:
        return ''

    ranges = []

    equal = False
    firstSlot = slots[0]

    for i in range(1, len(slots)):

        if slots[i - 1] + 1 == slots[i]:
            equal = True
            continue
        else:
            equal = False
            ranges.append((firstSlot, slots[i - 1]))
            firstSlot = slots[i]

    if equal:
        ranges.append((firstSlot, slots[i]))

    res = []
    for r in ranges:
        if r[0] == r[1]:
            res.append(str(r[0]))
        else:
            res.append('{}-{}'.format(r[0], r[1]))

    return ' '.join(res)


async def printRedisClusterInfoCoro(redisUrl, role=None):
    redisClient = RedisClient(redisUrl, '')
    nodes = await redisClient.cluster_nodes()

    clients = []
    for node in nodes:
        if role is not None and node.role != role:
            continue

        url = f'redis://{node.ip}:{node.port}'
        client = RedisClient(url, '')
        clients.append((node, client))

        slotRange = getSlotsRange(node.slots)
        print(node.node_id, node.ip + ':' + node.port, node.role, slotRange)


@click.command()
@click.option('--redis_urls', default='redis://localhost:11000')
@click.option('--role', '-r')
def cluster_nodes(redis_urls, role):
    '''Monitor redis metrics

    \b
    rcc cluster-nodes
    '''

    asyncio.run(printRedisClusterInfoCoro(redis_urls, role))
