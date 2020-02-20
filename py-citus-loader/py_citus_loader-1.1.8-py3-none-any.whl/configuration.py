import os
import yaml
import psycopg2

from .exceptions import ConfigurationException


class Configuration:
    def __init__(self, **kwargs):
        file_path = kwargs.get('config_file', None)
        if file_path:
            self.init_from_file(file_path)

            if not self.dump_only and bool(kwargs.get('dump_only', False)):
                self.dump_only = True
                self.destination_host = None
                self.destination_db = None
                self.destination_pwd = None
                self.destination_port = None
                self.destination_user = None

            if not self.restore_only and bool(kwargs.get('restore_only', False)):
                self.restore_only = True
                self.host = None
                self.db = None
                self.pwd = None
                self.port = None
                self.user = None

        else:
            self.init_configuration(**kwargs)
            self.nodes_hosts = {}
            self.destination_nodes_hosts = {}

        self.validate_configuration()

    def init_from_file(self, path):
        with open(path) as yaml_file:
            data = yaml.load(yaml_file, Loader=yaml.FullLoader)
            self.init_configuration(**data)

        # Dictionary for workers connection string / ip in pg_dist_nodes
        # Optional (useful for Hyperscale azure)
        # Example : {'10.0.0.1': 'psql://citus:pwd:test-w0.azure:5432/citus'}
        source = data.get('source', {})
        self.nodes_hosts = source.get('nodes', {})
        destination = data.get('destination', {})
        self.destination_nodes_hosts = destination.get('nodes', {})

    def init_configuration(self, **kwargs):

        source = kwargs.get('source', {})
        self.host = source.get('host', None)
        self.db = source.get('db', None)
        self.pwd = source.get('pwd', None)
        self.port = str(source.get('port', '5432'))
        self.user = source.get('user', None)

        destination = kwargs.get('destination', {})

        self.destination_host = destination.get('host', None)
        self.destination_db = destination.get('db', None)
        self.destination_pwd = destination.get('pwd', None)
        self.destination_port = str(destination.get('port', '5432'))
        self.destination_user = destination.get('user', None)

        self.dump_folder = kwargs.get('dump_folder', None)
        self.pg_dump = kwargs.get('pg_dump', 'pg_dump')
        self.pg_restore = kwargs.get('pg_restore', 'pg_restore')

        self.parallel_tasks = kwargs.get('parallel_tasks', 1)
        self.dump_jobs = kwargs.get('pg_dump_jobs', 1)
        self.restore_jobs = kwargs.get('pg_restore_jobs', 1)

        self.restore_only = bool(kwargs.get('restore_only', False))
        self.dump_only = bool(kwargs.get('dump_only', False))
        self.dump_schema = bool(kwargs.get('dump_schema', True))
        self.dump_data = bool(kwargs.get('dump_data', True))
        self.restore_schema = bool(kwargs.get('restore_schema', True))
        self.restore_data = bool(kwargs.get('restore_data', True))

        # We want to be able to filter nodes to be able to dump/restore subset of nodes
        # Can be useful if we have a 25 nodes cluster
        self.dump_coordinator_data = bool(kwargs.get('dump_coordinator_data', True))
        self.restore_coordinator_data = bool(kwargs.get('dump_coordinator_data', True))
        self.dump_nodes_data = kwargs.get('dump_nodes_data', [])
        self.restore_nodes_data = kwargs.get('restore_nodes_data', [])

        # Make sure we don't get any data from metadata tables
        self.ignore_tables = kwargs.get('ignore_tables', []) + ['pg_catalog.*']


        self.ignore_schemas = kwargs.get('ignore_schemas', []) + ['cron', 'partman']

        self.ignore_write_locks = bool(kwargs.get('ignore_write_locks', False))


    def validate_configuration(self):
        missing_fields = []

        if self.dump_only:
            fields = ('host', 'db', 'port', 'user', 'dump_folder')
        if self.restore_only:
            fields = ('destination_host', 'destination_db', 'destination_port',
                      'destination_user', 'dump_folder')
        if not self.dump_only and not self.restore_only:
            fields = ('host', 'db', 'port', 'user',
                      'destination_host', 'destination_db',
                      'destination_port', 'destination_user',
                      'dump_folder')

        for field in fields:
            if not getattr(self, field, None):
                missing_fields.append(field)

        if missing_fields:
            raise ConfigurationException(
                'The configuration is missing the attribute(s) %s' % ', '.join(missing_fields)
            )

    def connection(self):
        return psycopg2.connect(dbname=self.db,
                                user=self.user,
                                host=self.host,
                                password=self.pwd,
                                port=self.port,
                                sslmode='require')


    def destination_connection(self):
        return psycopg2.connect(dbname=self.destination_db,
                                user=self.destination_user,
                                host=self.destination_host,
                                password=self.destination_pwd,
                                port=self.destination_port,
                                sslmode='require')
