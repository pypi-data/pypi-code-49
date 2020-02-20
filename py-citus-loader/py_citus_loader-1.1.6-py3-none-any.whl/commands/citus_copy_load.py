oimport os
from multiprocessing.pool import ThreadPool

from subprocess import STDOUT, call

import click

import psycopg2

from ..formation_utils import *
from ..configuration import *
from ..dump_utils import perform_dump
from ..restore_utils import perform_restore
from ..coordinator_utils import (dump_schema as dump_coordinator_schema)


def run(cmd):
    print('run statement %s' % cmd)
    return cmd, os.system(cmd)


def run(cmds):
    for cmd in cmds:
        print('run statement %s' % cmd)
        result = os.system(cmd)
        print('{cmd} return code: {rc}'.format(cmd, result)
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
@click.option('--dump-jobs', required=False, type=int,
              default=1,
              help='Value for option -j in pg_dump, number of jobs in parallel')
@click.option('--restore-jobs', required=False, type=int,
              default=1,
              help='Value for option -j in pg_dump, number of jobs in parallel')
@click.option('--load-schema', required=False, type=bool,
              default=True,
              help='Restore schema and distribute tables on the future formation')
@click.option('--load-coordinator-data', required=False, type=bool,
              default=True,
              help='Run pg_dump/restore for data on the coordinator')
@click.option('--load-workers-data', required=False, type=bool,
              default=True,
              help='Run COPY for data of distributed tables')
@click.option('--config-file', required=False, type=click.Path(),
              help='YaML file containing the configuration for the command')
def dump_and_restore(host, db, password, port, user,
                     destination_host, destination_db, destination_password,
                     destination_port, destination_user,
                     folder, pg_dump, pg_restore, parallel_tasks,
                     dump_jobs, restore_jobs,
                     load_schema, load_coordinator_data, load_workers_data,
                     config_file):


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
        'load_schema': load_schema,
        'load_coordinator_data': load_coordinator_data,
        'load_workers_data': load_workers_data,
    }

    configuration = Configuration(**config_args)

    print('Connecting to current host')
    conn = configuration.connection()
    print('Connected to host')

    print('Retrieving data for old formation')
    data = retrieve_formation_data(connection=conn)
    coordinator = init_formation(configuration, data)

    # Step 1 - dump and restore schema
    # Step 2 - distribute tables
    if configuration.load_schema:
        dump_coordinator_schema(coordinator)

        print('Connecting to destination host')
        destination_conn = configuration.destination_connection()
        print('Connected to destination host')

        restore_coordinator('postgres://%s:%s@%s:%s/%s?sslmode=require' % (
            configuration.destination_user, configuration.destination_pwd,
            configuration.destination_host, configuration.destination_port,
            configuration.destination_db), configuration)

        data = retrieve_formation_data(connection=destination_conn)
        new_coordinator = init_formation(configuration, data,
                                         destination=True)

    # Step 3 - coordinator data dump/restore, except if configuration.tables only contains distributed tables
    if configuration.load_coordinator_data:
        statements = [coordinator.data_dump_statement,
                      statements.append(coordinator.pg_restore_statement)]
    # Step 4 - COPY data from workers to coordinator
