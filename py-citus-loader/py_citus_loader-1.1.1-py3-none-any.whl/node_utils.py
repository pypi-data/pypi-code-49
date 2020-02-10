import os

def get_nodes_pg_dump_statements(coordinator):
    configuration = coordinator.configuration

    commands = []

    for node in coordinator.nodes:
        commands.append(node.dump_statement)

    return commands


def get_rename_node_shards_statements(node, old=True):
    statements = []

    for shard in node.shards:
        if not shard.old_shard:
            continue

        if old:
            statements.append('ALTER TABLE %s_%d RENAME TO %s_%d_old;\n' % (
                shard.table.name, shard.id,
                shard.table.name, shard.id))
        else:
            statements.append('ALTER TABLE %s_%d RENAME TO %s_%d;\n' % (
                shard.old_shard.table.name,
                shard.old_shard.id,
                shard.table.name,
                shard.id))
            statements.append('DROP TABLE %s_%d_old CASCADE;\n' % (shard.table.name, shard.id))

    return statements

def dump_rename_node_shards_to_old_file(coordinator, configuration):
    for node in coordinator.nodes:
        f = open(os.path.join(configuration.dump_folder, '%s_rename_shard_old.sql' % node.name), "w+")
        statements = get_rename_node_shards_statements(node)
        for statement in statements:
            f.write(statement)


def rename_node_shards(coordinator, configuration, old=True):
    command = 'psql %s  -a -f %s'

    for node in coordinator.nodes:
        if old:
            file_path = os.path.join(configuration.dump_folder, '%s_rename_shard_old.sql' % node.name)
        else:
            file_path = os.path.join(configuration.dump_folder, '%s_rename_shard_new.sql' % node.name)
        os.system(command % (node.connection_string, file_path))


def dump_rename_node_shards_to_new_file(coordinator,  configuration):
    for node in coordinator.nodes:
        f = open(os.path.join(configuration.dump_folder, '%s_rename_shard_new.sql' % node.name), "w+")
        statements = get_rename_node_shards_statements(node, old=False)
        for statement in statements:
            f.write(statement)



def get_nodes_pg_restore_statements(coordinator):
    command = "%(pg_restore)s --no-acl --no-owner -j %(jobs)d -d '%(host)s' %(path)s --disable-triggers"

    commands = []

    for node in coordinator.nodes:
        future_shards = {}

        for shard in node.shards:
            if not shard.future_shard:
                continue

            if shard.future_shard.node not in future_shards:
                future_shards[shard.future_shard.node] = ' -t %s_%d' % (shard.table.name, shard.id)
            else:
                future_shards[shard.future_shard.node] += ' -t %s_%d' % (shard.table.name, shard.id)

        for new_node, shards in future_shards.items():
            commands.append(command % {
                'pg_restore': coordinator.configuration.pg_restore,
                'host': new_node.connection_string,
                'path': node.dump_file,
                'jobs': coordinator.configuration.dump_jobs
            } + shards)

    return commands
