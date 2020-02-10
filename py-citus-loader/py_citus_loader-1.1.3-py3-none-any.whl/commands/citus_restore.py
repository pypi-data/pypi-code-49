import click


from ..configuration import *
from ..restore_utils import perform_restore
from ..formation_utils import retrieve_formation_data, init_formation


@click.command()
@click.option('--host', required=False, type=str, help='host of your current coordinator')
@click.option('--db', required=False, type=str, help='database of your current coordinator')
@click.option('--password', required=False, type=str, help='password to citus current coordinator')
@click.option('--port', required=False, type=str, help='port of citus current coordinator')
@click.option('--user', required=False, type=str, help='user for current coordinator')
@click.option('--folder', required=False, type=click.Path(),
              help='Path to the folder for your pg_dump')
@click.option('--pg-restore', required=False, type=click.Path(),
              help='Path to the pg_restore')
@click.option('--parallel-tasks', required=False, type=int,
              default=1,
              help='Number of pg_dump/restore running in parallel')
@click.option('--restore-data', required=False, type=bool,
              default=True,
              help='Restore data')
@click.option('--restore-schema', required=False, type=bool,
              default=True,
              help='Restore schema and distribute tables on the future formation')
@click.option('--restore-jobs', required=False, type=int,
              default=1,
              help='Value for option -j in pg_dump, number of jobs in parallel')
@click.option('--config-file', required=False, type=click.Path(),
              help='JSON file containing the configuration for the command')
def citus_restore(host, db, password, port, user,
                  folder, pg_restore, parallel_tasks,
                  restore_data, restore_schema,
                  restore_jobs, config_file):


    config_args = {
        'destination': {
            'host': host,
            'db': db,
            'pwd': password,
            'port': port,
            'user': user
        },
        'dump_folder': folder,
        'pg_restore': pg_restore,
        'parallel_tasks': parallel_tasks,
        'pg_restore_jobs': restore_jobs,
        'config_file': config_file,
        'restore_data': restore_data,
        'restore_schema': restore_schema,
        'restore_only': True
    }

    configuration = Configuration(**config_args)

    path_metadata_file = os.path.join(configuration.dump_folder,
                                      'source_coordinator_metadata.yml')

    print('Retrieving data for old formation')
    data = retrieve_formation_data(from_file=path_metadata_file)
    coordinator = init_formation(configuration, data)


    perform_restore(coordinator)
