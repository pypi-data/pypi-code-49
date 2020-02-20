'''Tools to reshard a redis cluster

Copyright (c) 2020 Machine Zone, Inc. All rights reserved.
'''

import click

from rcc.cluster.reshard import binPackingReshard


@click.command()
@click.option('--port', default=6379)
@click.option('--redis_urls', default='redis://localhost:10000')
@click.option('--weight', '-w', required=True)
def binpacking_reshard(port, redis_urls, weight):
    '''Reshard using the bin-packing technique
    '''

    binPackingReshard(redis_urls, weight)
