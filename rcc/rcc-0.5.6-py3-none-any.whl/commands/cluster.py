'''Cluster commands

Copyright (c) 2020 Machine Zone, Inc. All rights reserved.
'''

import collections
import hiredis


ClusterNode = collections.namedtuple(
    'ClusterNode', ['node_id', 'address', 'ip', 'port', 'role', 'slots']
)


class ClusterCommandsMixin:
    async def cluster_nodes(self):
        response = await self.send('CLUSTER', None, 'NODES')

        # ERR This instance has cluster support disabled'
        responseType = type(response)
        if responseType == hiredis.ReplyError:
            return []

        response = response.decode()

        nodes = []
        for line in response.splitlines():
            tokens = line.split()
            node_id = tokens[0]

            address = tokens[1]
            url, _, _ = address.partition('@')
            ip, _, port = url.partition(':')

            role = tokens[2]
            role = role.replace('myself,', '')
            role = role.replace('myself,', '')

            slots = []
            for token in tokens[8:]:
                if '-' in token:
                    start, _, end = token.partition('-')
                    start = int(start)
                    end = int(end)
                    for i in range(start, end + 1):
                        slots.append(i)
                else:
                    slots.append(token)

            nodes.append(ClusterNode(node_id, address, ip, port, role, slots))

        return nodes

    async def cluster_set_slots(self, slot, mode, node_id):
        '''
        https://redis.io/commands/cluster-setslot
        '''
        raise ValueError('Not implemented')

    async def cluster_get_keys_in_slot(self, slot: int, count: int):
        '''
        https://redis.io/commands/cluster-getkeysinslot

        redis-cli -p 10002 CLUSTER GETKEYSINSLOT 12182 10
        '''
        return await self.send('CLUSTER', None, 'GETKEYSINSLOT', str(slot), str(count))
