import os
from multiprocessing.pool import ThreadPool

from subprocess import STDOUT, call

import click

import psycopg2


from ..formation_utils import *
from ..configuration import *
from ..dump_utils import perform_dump
from ..restore_utils import perform_restore


def run(cmd):
    print('run statement %s' % cmd)
    return cmd, os.system(cmd)


@click.command()
@click.option('--host', required=False, type=str, help='host of your current coordinator')
@click.option('--db', required=False, type=str, help='database of your current coordinator')
@click.option('--password', required=False, type=str, help='password to citus current coordinator')
@click.option('--port', required=False, type=str, help='port of citus current coordinator')
@click.option('--user', required=False, type=str, help='user for current coordinator')
@click.option('--destination-host', required=False, type=str, help='host of your future coordinator')
@click.option('--destination-db', required=False, type=str, help='database of your future coordinator')
@click.option('--destination-password', required=False, type=str, help='password to citus future coordinator')
@click.option('--destination-port', required=False, type=str, help='port of citus future coordinator')
@click.option('--destination-user', required=False, type=str, help='user for future coordinator')
@click.option('--folder', required=False, type=click.Path(),
              help='Path to the folder for your pg_dump')
@click.option('--pg-dump', required=False, type=click.Path(),
              help='Path to the pg_dump')
@click.option('--pg-restore', required=False, type=click.Path(),
              help='Path to the pg_restore')
@click.option('--parallel-tasks', required=False, type=int,
              default=1,
              help='Number of pg_dump/restore running in parallel')
@click.option('--restore-only', required=False, type=bool,
              default=False,
              help='Only restore data')
@click.option('--restore-data', required=False, type=bool,
              default=True,
              help='Restore data')
@click.option('--dump-only', required=False, type=bool,
              default=False,
              help='Only dump data - will do the restore of schema to match shards')
@click.option('--dump-schema', required=False, type=bool,
              default=True,
              help='Dump schema from coordinator')
@click.option('--dump-data', required=False, type=bool,
              default=True,
              help='Dump data from coordinator and workers')
@click.option('--restore-schema', required=False, type=bool,
              default=True,
              help='Restore schema and distribute tables on the future formation')
@click.option('--dump-jobs', required=False, type=int,
              default=1,
              help='Value for option -j in pg_dump, number of jobs in parallel')
@click.option('--restore-jobs', required=False, type=int,
              default=1,
              help='Value for option -j in pg_dump, number of jobs in parallel')
@click.option('--ignore-write-locks', required=False, type=bool,
              default=False,
              help='''If this option is to true, it won\'t execute LOCK TABLE statements,
              Especially useful to test process on your production.''')
@click.option('--config-file', required=False, type=click.Path(),
              help='JSON file containing the configuration for the command')
def dump_and_restore(host, db, password, port, user,
                     destination_host, destination_db, destination_password,
                     destination_port, destination_user,
                     folder, pg_dump, pg_restore, parallel_tasks,
                     restore_only, restore_data, dump_only, dump_schema,
                     dump_data, restore_schema,
                     dump_jobs, restore_jobs, ignore_write_locks, config_file):


    config_args = {
        'source': {
            'host': host,
            'db': db,
            'pwd': password,
            'port': port,
            'user': user
        },
        'destination': {
            'host': destination_host,
            'db': destination_db,
            'pwd': destination_password,
            'port': destination_port,
            'user': destination_user
        },
        'dump_folder': folder,
        'pg_dump': pg_dump,
        'pg_restore': pg_restore,
        'parallel_tasks': parallel_tasks,
        'pg_dump_jobs': dump_jobs,
        'pg_restore_jobs': restore_jobs,
        'config_file': config_file,
        'dump_schema': dump_schema,
        'dump_data': dump_data,
        'restore_data': restore_data,
        'restore_schema': restore_schema,
        'restore_only': restore_only,
        'dump_only': dump_only,
        'ignore_write_locks': ignore_write_locks,
    }

    configuration = Configuration(**config_args)

    print('Connecting to current host')
    conn = configuration.connection()
    print('Connected to host')

    print('Retrieving data for old formation')
    data = retrieve_formation_data(connection=conn)
    coordinator = init_formation(configuration, data)


    if not configuration.restore_only:
        perform_dump(coordinator)

    if configuration.dump_only:
        return None

    perform_restore(coordinator)
