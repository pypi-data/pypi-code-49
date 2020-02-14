'''Tools to work with redis-cluster

Copyright (c) 2020 Machine Zone, Inc. All rights reserved.
'''

import asyncio
import os
import json
import logging

import click
import tabulate

from rcc.client import RedisClient


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


def binPackingReshard(redis_urls, weightPath):
    if not os.path.exists(weightPath):
        logging.error(f'{weightPath} does not exists')
        return

    with open(weightPath) as f:
        content = f.read()
        weights = json.loads(content)

    print(weights)

    import binpacking

    bins = binpacking.to_constant_bin_number(weights, 4)

    # Print the result. Excuse the ugly uppercase Bin, but bin is a reserved function in Python
    for b in bins:
        # We will print the sum of all the weights in the bin, along with the bin itself
        print(sum(b.values()), b)

    # 1. Set the destination node slot to importing state using CLUSTER SETSLOT
    #    <slot> IMPORTING <source-node-id>.
    #
    # 2. Set the source node slot to migrating state using CLUSTER SETSLOT
    #    <slot> MIGRATING <destination-node-id>.
    #
    # 3. Get keys from the source node with CLUSTER GETKEYSINSLOT command and
    #    move them into the destination node using the MIGRATE command.
    #
    # 4. Use CLUSTER SETSLOT <slot> NODE <destination-node-id> in the source or
    #    destination.


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
