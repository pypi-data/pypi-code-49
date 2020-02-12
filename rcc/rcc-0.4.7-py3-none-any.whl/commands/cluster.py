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
