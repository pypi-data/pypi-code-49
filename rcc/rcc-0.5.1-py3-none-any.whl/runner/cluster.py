'''Tools to work with redis-cluster

Copyright (c) 2020 Machine Zone, Inc. All rights reserved.
'''

import asyncio
import os
import json

import click
import tabulate

from rcc.client import RedisClient


ACTIONS = ['get_endpoints', 'redis_cluster_init', 'info']


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


async def printRedisClusterInfoCoro(redisClient, stats):
    nodes = await redisClient.cluster_nodes()

    rows = [['node', *stats]]

    for node in nodes:
        url = f'redis://{node.ip}:{node.port}'
        nodeClient = RedisClient(url, '')
        info = await nodeClient.info()

        row = [node.ip + ':' + node.port]
        for stat in stats:
            row.append(info[stat])

        rows.append(row)

    print(tabulate.tabulate(rows, tablefmt="simple", headers="firstrow"))


def printRedisClusterInfo(redis_urls, stats):
    redisClient = RedisClient(redis_urls, '')
    asyncio.run(printRedisClusterInfoCoro(redisClient, stats))


@click.command()
@click.option('--action', default='get_endpoints', type=click.Choice(ACTIONS))
@click.option('--service', default='redis-cluster')
@click.option('--port', default=6379)
@click.option('--redis_urls', default='redis://localhost:10000')
@click.option('--stats', default=['redis_version'], multiple=True)
def cluster(action, service, port, redis_urls, stats):
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
        printRedisClusterInfo(redis_urls, stats)
