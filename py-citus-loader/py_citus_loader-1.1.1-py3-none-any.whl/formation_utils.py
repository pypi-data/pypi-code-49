import yaml

from .classes import *


def retrieve_formation_data(connection=None, from_file=None):
    if from_file:
        with open(from_file) as yaml_file:
            return yaml.load(yaml_file, Loader=yaml.FullLoader)

    nodes_query = '''SELECT nodename, nodeport FROM pg_dist_node WHERE 
    noderole='primary';
    '''

    distributed_tables_query = '''SELECT logicalrelid, pg_attribute.attname
    FROM pg_dist_partition
    INNER JOIN pg_attribute ON (logicalrelid=attrelid)
    WHERE partmethod='h'
    AND attnum=substring(partkey from '%:varattno #"[0-9]+#"%' for '#')::int
    '''

    reference_tables_query = '''SELECT logicalrelid FROM pg_dist_partition 
    WHERE partmethod = 'n' ORDER BY logicalrelid
    '''

    shards_query = '''SELECT logicalrelid::text, sp.nodename, sp.shardid,
    shardminvalue, shardmaxvalue
    FROM pg_dist_shard_placement sp
    INNER JOIN pg_dist_shard
    ON pg_dist_shard.shardid=sp.shardid
    WHERE shardminvalue IS NOT NULL;
    '''

    cursor = connection.cursor()

    print('retrieving data from coordinator')
    cursor.execute(nodes_query)
    nodes_data = cursor.fetchall()

    cursor.execute(distributed_tables_query)
    distributed_tables_data = cursor.fetchall()

    cursor.execute(reference_tables_query)
    reference_tables_data = cursor.fetchall()

    cursor.execute(shards_query)
    shards_data = cursor.fetchall()

    shards_dict = {}

    for shard in shards_data:
        if shard[0] not in shards_dict:
            shards_dict[shard[0]] = {shard[1]: [[shard[2], shard[3], shard[4]]]}
        else:
            if shard[1] not in shards_dict[shard[0]]:
                shards_dict[shard[0]][shard[1]] = [[shard[2], shard[3], shard[4]]]
            else:
                shards_dict[shard[0]][shard[1]].append([shard[2], shard[3], shard[4]])


    return {'nodes': nodes_data,
            'distributed_tables': distributed_tables_data,
            'reference_tables': reference_tables_data,
            'shards': shards_dict}


def init_formation(configuration, data,
                   destination=False):

    if destination:
        nodes_hosts = configuration.destination_nodes_hosts
        user = configuration.destination_user
        host = configuration.destination_host
        db = configuration.destination_db
        password = configuration.destination_pwd
        port = configuration.destination_port
    else:
        nodes_hosts = configuration.nodes_hosts
        user = configuration.user
        host = configuration.host
        db = configuration.db
        password = configuration.pwd
        port = configuration.port

    nodes = []
    for dat in data['nodes']:
        connection_string = nodes_hosts.get(dat[0], None) or 'postgres://%s:%s@%s:%s/%s?sslmode=require' % (user, password,
                                                                                                             dat[0], dat[1],
                                                                                                             db)
        nodes.append(Node(dat[0], dat[1],connection_string))

    coordinator = Coordinator('postgres://%s:%s@%s:%s/%s?sslmode=require' % (user, password,
                                                                             host, port,
                                                                             db),
                              nodes,
                              configuration)


    for node in nodes:
        node.coordinator = coordinator

    # Get distributed tables
    tables = []
    for dat in data['distributed_tables']:
        table = Table(dat[0], is_distributed=True,
                      distribution_column=dat[1])

        shards = []
        for node in nodes:
            if node.name not in data['shards'][table.name]:
                # A table might not have been rebalanced and in one node
                # there is no shard.
                continue

            shard_data = data['shards'][table.name][node.name]
            for s_data in shard_data:
                shard = Shard(s_data[0], node, table, s_data[1], s_data[2])
                shards.append(shard)
                node.add_shard(shard)

        table.set_shards(shards)
        tables.append(table)

    coordinator.distributed_tables = tables

    # Get reference tables
    tables = []
    for dat in data['reference_tables']:
        tables.append(Table(dat[0], is_reference=True))

    coordinator.reference_tables = tables

    return coordinator


def find_equivalent_shards(shards, shard):
    for s in shards:
        if (s.table.name == shard.table.name
            and s.min_value == shard.min_value
            and s.max_value == shard.max_value):
            return s

    return None

def set_future_shards(new_coordinator, old_coordinator):
    for shard in new_coordinator.distributed_shards:
        old_shard = find_equivalent_shards(old_coordinator.distributed_shards, shard)
        if not old_shard:
            continue

        old_shard.set_future_shard(shard)
        shard.set_old_shard(old_shard)
