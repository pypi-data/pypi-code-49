import os
import click
import yaml

from ..configuration import *
from ..dump_utils import perform_dump
from ..formation_utils import retrieve_formation_data, init_formation


@click.command()
@click.option('--host', required=False, type=str, help='host of your current coordinator')
@click.option('--db', required=False, type=str, help='database of your current coordinator')
@click.option('--password', required=False, type=str, help='password to citus current coordinator')
@click.option('--port', required=False, type=str, help='port of citus current coordinator')
@click.option('--user', required=False, type=str, help='user for current coordinator')
@click.option('--folder', required=False, type=click.Path(),
              help='Path to the folder for your pg_dump')
@click.option('--pg-dump', required=False, type=click.Path(),
              help='Path to the pg_dump')
@click.option('--parallel-tasks', required=False, type=int,
              default=1,
              help='Number of pg_dump/restore running in parallel')
@click.option('--dump-schema', required=False, type=bool,
              default=True,
              help='Dump schema from coordinator')
@click.option('--dump-data', required=False, type=bool,
              default=True,
              help='Dump data from coordinator and workers')
@click.option('--dump-jobs', required=False, type=int,
              default=1,
              help='Value for option -j in pg_dump, number of jobs in parallel')
@click.option('--ignore-write-locks', required=False, type=bool,
              default=False,
              help='''If this option is to true, it won\'t execute LOCK TABLE statements,
              Especially useful to test process on your production.''')
@click.option('--config-file', required=False, type=click.Path(),
              help='JSON file containing the configuration for the command')
def citus_dump(host, db, password, port, user,
               folder, pg_dump, parallel_tasks,
               dump_schema, dump_data,
               dump_jobs, ignore_write_locks,
               config_file):


    config_args = {
        'source': {
            'host': host,
            'db': db,
            'pwd': password,
            'port': port,
            'user': user
        },
        'dump_folder': folder,
        'pg_dump': pg_dump,
        'parallel_tasks': parallel_tasks,
        'pg_dump_jobs': dump_jobs,
        'config_file': config_file,
        'dump_schema': dump_schema,
        'dump_data': dump_data,
        'ignore_write_locks': ignore_write_locks,
        'dump_only': True
    }

    configuration = Configuration(**config_args)

    print('Connecting to current host')
    conn = configuration.connection()
    print('Connected to host')

    print('Retrieving data for old formation')
    data = retrieve_formation_data(connection=conn)
    coordinator = init_formation(configuration, data)

    if not os.path.exists(configuration.dump_folder):
        os.makedirs(configuration.dump_folder)

    # Write metadata to file to be later used during restore
    path_metadata_file = os.path.join(configuration.dump_folder,
                                      'source_coordinator_metadata.yml')
    f = open(path_metadata_file, "w")
    yaml.dump(data, f)
    f.close()

    perform_dump(coordinator)
