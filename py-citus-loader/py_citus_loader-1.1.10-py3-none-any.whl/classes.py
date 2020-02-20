import os.path


class Coordinator:
    def __init__(self, connection_string, nodes, configuration):
        self.nodes = nodes
        self.distributed_tables = None
        self.reference_tables = None
        self.connection_string = connection_string
        self.configuration = configuration

    @property
    def distributed_shards(self):
        if not self.distributed_tables:
            return None
        distributed_shards = []
        for table in self.distributed_tables:
            distributed_shards += table.shards

        return distributed_shards

    @property
    def dump_data_file(self):
        return os.path.join(self.configuration.dump_folder, 'coordinator_data_dump')

    def dump_files_exist(self):
        if (not self.dump_data_file
            and self.configuration.restore_coordinator_data):
            return False

        for node in self.nodes:
            if (self.configuration.restore_nodes_data
                and node.name not in self.configuration.restore_nodes_data):
                continue

            if not node.dump_file_exist():
                return False

        if (not os.path.exists(self.dump_data_file)
            and self.configuration.restore_coordinator_data):
            print('%s does not exist' % self.dump_data_file)
            return False

        return True

    @property
    def distribute_statements(self):
        statements = []

        for table in self.distributed_tables:
            statements.append("SELECT create_distributed_table('%s', '%s');\n"
                              % (table.name,
                                 table.distribution_column))


        return statements

    @property
    def reference_statements(self):
        statements = []

        for table in self.reference_tables:
            statements.append("SELECT create_reference_table('%s');\n"
                              % table.name)

        return statements

    @property
    def schema_dump_path(self):
        return os.path.join(self.configuration.dump_folder, 'coordinator_schema.sql')

    @property
    def distribute_path(self):
        return os.path.join(self.configuration.dump_folder, 'coordinator_distribute.sql')

    @property
    def sequences_dump_path(self):
        return os.path.join(self.configuration.dump_folder, 'coordinator_sequences.sql')

    @property
    def schema_dump_statement(self):
        return '%(pg_dump)s --no-owner --format=plain --schema-only %(ignore_tables)s %(ignore_schemas)s --file=%(file)s %(connection_string)s' % {
            'pg_dump': self.configuration.pg_dump,
            'ignore_tables': ' '.join(['-T %s' % table for table in self.configuration.ignore_tables]),
            'ignore_schemas': ' '.join(['-N %s' % schema for schema in self.configuration.ignore_schemas]),
            'file': self.schema_dump_path,
            'connection_string': self.connection_string
        }

    @property
    def data_dump_statement(self):
        command = "%(pg_dump)s -d '%(connection_string)s' -Fd -j %(dump_jobs)d -f %(file)s --data-only %(ignore_tables)s %(ignore_schemas)s" % {
            'pg_dump': self.configuration.pg_dump,
            'connection_string': self.connection_string,
            'dump_jobs': self.configuration.dump_jobs,
            'file': self.dump_data_file,
            'ignore_tables': ' '.join(['-T %s' % table for table in self.configuration.ignore_tables]),
            'ignore_schemas': ' '.join(['-N %s' % schema for schema in self.configuration.ignore_schemas])
        }

        for distributed_table in self.distributed_tables:
            command += ' -T %s' % distributed_table.name

        return command

    @property
    def pg_restore_statement(self):
        command = "%s --no-acl --no-owner --data-only -j %d -d '%s' %s --disable-triggers"

        return command % (self.configuration.pg_restore, self.configuration.restore_jobs,
                          self.connection_string, self.dump_data_file)


    @property
    def lock_statements(self):
        statements = []

        for table in self.distributed_tables + self.reference_tables:
            statements.append('LOCK TABLE %s IN EXCLUSIVE MODE;' % table.name)

        return statements


class Node:
    def __init__(self, name, port, connection_string):
        self.name = name
        self.port = port
        self.formation = None
        self.coordinator = None
        self.shards = []
        self.connection_string = connection_string

    def set_coordinator(self, coordinator):
        self.coordinator = coordinator

    def set_formation(self, formation):
        self.coordinator = formation

    def set_shards(self, shards):
        self.shards = shards

    def add_shard(self, shard):
        self.shards.append(shard)

    def dump_file_exist(self):
        if not os.path.exists(self.dump_file):
            print('%s does not exist' % self.dump_file)
            return False

        return True

    @property
    def dump_file(self):
        return os.path.join(self.coordinator.configuration.dump_folder,
                            '%s_dump' % (self.name))

    @property
    def dump_statement(self):
        return  "%(pg_dump)s -d '%(host)s' -Fd -j %(jobs)d %(ignore_tables)s %(ignore_schemas)s -f %(path)s" % {
            'pg_dump': self.coordinator.configuration.pg_dump,
            'host': self.connection_string,
            'path': self.dump_file,
            'jobs': self.coordinator.configuration.dump_jobs,
            'ignore_tables': ' '.join(['-T %s' % table for table in self.coordinator.configuration.ignore_tables]),
            'ignore_schemas': ' '.join(['-N %s' % schema for schema in self.coordinator.configuration.ignore_schemas])
        }



class Table:
    def __init__(self, name, is_reference=False,
                 is_distributed=False,
                 distribution_column=None,
                 shards=None):
        self.name = name
        self.is_reference = is_reference
        self.is_distributed = is_distributed
        self.distribution_column = distribution_column
        self.shards = shards

    def set_shards(self, shards):
        self.shards = shards


class Shard:
    def __init__(self, id, node, table, min_value, max_value):
        self.id = id
        self.node = node
        self.table = table
        self.min_value = min_value
        self.max_value = max_value
        self.future_shard = None
        self.old_shard = None

    def set_future_shard(self, shard):
        self.future_shard = shard

    def set_old_shard(self, shard):
        self.old_shard = shard
