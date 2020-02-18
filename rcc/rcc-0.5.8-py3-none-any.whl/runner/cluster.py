'''Tools to work with redis-cluster

Copyright (c) 2020 Machine Zone, Inc. All rights reserved.
'''

import asyncio
import os
import json
import logging

import click
import tabulate
try:
    import binpacking  # This could be more lightweight
except ImportError:
    pass

from rcc.client import RedisClient
from rcc.hash_slot import getHashSlot


ACTIONS = ['get_endpoints', 'redis_cluster_init', 'info', 'binpacking_reshard']


def getEndpointsIps(service):
    '''
    kubectl get endpoints -o json redis-cluster
    '''

    content = os.popen(f'kubectl get endpoints -o json {service}').read()
    data = json.loads(content)

    assert len(data['subsets']) == 1
    assert 'addresses' in data['subsets'][0]
    addresses = data['subsets'][0]['addresses']

    ips = []
    for address in addresses:
        ip = address.get('ip')
        ips.append(ip)

    return ips


def printEndpoints(service, port):
    ips = getEndpointsIps(service)

    endpoints = []
    for ip in ips:
        endpoints.append(f'redis://{ip}:{port}')

    print(';'.join(endpoints))


def printRedisClusterInitCommand(service, port):
    cmd = 'redis-cli --cluster create '

    ips = getEndpointsIps(service)

    for ip in ips:
        cmd += f'{ip}:{port} '

    cmd += ' --cluster-replicas 1'

    print(cmd)


async def printRedisClusterInfoCoro(redisClient, stats, role=None):
    nodes = await redisClient.cluster_nodes()

    clients = []
    for node in nodes:
        if role is not None and node.role != role:
            continue

        url = f'redis://{node.ip}:{node.port}'
        client = RedisClient(url, '')
        clients.append((node, client))

    while True:
        rows = [['node', 'role', *stats]]

        for node, client in clients:
            info = await client.info()

            row = [node.ip + ':' + node.port, node.role]
            for stat in stats:
                row.append(info[stat])

            rows.append(row)

        click.clear()
        print(tabulate.tabulate(rows, tablefmt="simple", headers="firstrow"))
        await asyncio.sleep(1)


def printRedisClusterInfo(redis_urls, stats, role):
    redisClient = RedisClient(redis_urls, '')
    asyncio.run(printRedisClusterInfoCoro(redisClient, stats, role))


def makeClientfromNode(node):
    url = f'redis://{node.ip}:{node.port}'
    return RedisClient(url, '')  # FIXME password


async def migrate(nodes, slot, sourceNode, destinationNode):
    '''Migrate a slot to a node'''
    logging.info(
        f'migrate from {sourceNode.node_id} to {destinationNode.node_id} slot [{slot}]'
    )

    sourceClient = makeClientfromNode(sourceNode)
    destinationClient = makeClientfromNode(destinationNode)

    # await sourceClient.cluster_set_slot(slot, 'STABLE', None)
    # await destinationClient.cluster_set_slot(slot, 'STABLE', None)

    # 1. Set the destination node slot to importing state using CLUSTER SETSLOT
    #    <slot> IMPORTING <source-node-id>.
    try:
        await destinationClient.cluster_set_slot(slot, 'IMPORTING', sourceNode.node_id)
    except Exception as e:
        logging.error(f'error with SETSLOT IMPORTING command: {e}')
        return False

    # 2. Set the source node slot to migrating state using CLUSTER SETSLOT
    #    <slot> MIGRATING <destination-node-id>.
    try:
        await sourceClient.cluster_set_slot(slot, 'MIGRATING', destinationNode.node_id)
    except Exception as e:
        logging.error(f'error with SETSLOT MIGRATING command: {e}')
        return False

    # 3. Get keys from the source node with CLUSTER GETKEYSINSLOT command and
    #    move them into the destination node using the MIGRATE command.
    # FIXME / we need to repeat this process / make this scalable etc...
    keys = await sourceClient.cluster_get_keys_in_slot(slot, 1000)

    timeout = 5000  # 5 seconds
    if len(keys) > 0:
        print('migrating', len(keys), 'keys')
        await sourceClient.migrate(
            destinationNode.ip, destinationNode.port, 0, timeout, *keys
        )

    # 4. Use CLUSTER SETSLOT <slot> NODE <destination-node-id> in the source or
    #    destination.
    try:
        # do we need to do both ? / probably not
        await sourceClient.cluster_set_slot(slot, 'NODE', destinationNode.node_id)
        await destinationClient.cluster_set_slot(slot, 'NODE', destinationNode.node_id)
    except Exception as e:
        logging.error(f'error with SETSLOT NODE command: {e}')
        return False

    # 5. Make it stable ?
    # try:
    #     await destinationClient.cluster_set_slot(slot, 'STABLE', None)
    # except Exception as e:
    #     logging.error(f'error with SETSLOT stable command: {e}')
    #     return False

    return True


async def binPackingReshardCoroutine(redis_urls, weights):
    redisClient = RedisClient(redis_urls, '')
    nodes = await redisClient.cluster_nodes()

    # There will be as many bins as there are master nodes
    masterNodes = [node for node in nodes if node.role == 'master']
    binCount = len(masterNodes)

    # We need to know where each slots lives
    slotToNodes = {}
    for node in masterNodes:
        for slot in node.slots:
            slotToNodes[slot] = node

    # Run the bin packing algorithm
    bins = binpacking.to_constant_bin_number(weights, binCount)

    slots = []

    for binIdx, b in enumerate(bins):
        binSlots = []

        for key in b:
            slot = getHashSlot(key)
            binSlots.append(slot)

        slots.append(binSlots)

    for binSlots, node in zip(slots, masterNodes):
        print(f'== {node.node_id} / {node.ip}:{node.port} ==')

        for slot in binSlots:
            sourceNode = slotToNodes[slot]
            if sourceNode.node_id != node.node_id:
                ret = await migrate(nodes, slot, sourceNode, node)
                if not ret:
                    return

        print()


def binPackingReshard(redis_urls, weightPath):
    if not os.path.exists(weightPath):
        logging.error(f'{weightPath} does not exists')
        return

    with open(weightPath) as f:
        content = f.read()
        weights = json.loads(content)

    asyncio.run(binPackingReshardCoroutine(redis_urls, weights))


@click.command()
@click.option('--action', default='get_endpoints', type=click.Choice(ACTIONS))
@click.option('--service', default='redis-cluster')
@click.option('--port', default=6379)
@click.option('--redis_urls', default='redis://localhost:10000')
@click.option('--stats', '-s', default=['redis_version'], multiple=True)
@click.option('--role', '-r')
@click.option('--weight', '-w', required=True)
def cluster(action, service, port, redis_urls, stats, role, weight):
    '''Help with redis cluster operations

    \brcc redis-cluster --service redis-cluster --action redis_cluster_init

    instantaneous_input_kbps
    instantaneous_output_kbps
    connected_clients
    used_memory_rss_human
    '''

    if action == 'get_endpoints':
        printEndpoints(service, port)
    elif action == 'redis_cluster_init':
        printRedisClusterInitCommand(service, port)
    elif action == 'info':
        printRedisClusterInfo(redis_urls, stats, role)
    elif action == 'binpacking_reshard':
        binPackingReshard(redis_urls, weight)
