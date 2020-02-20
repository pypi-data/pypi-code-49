import os
from multiprocessing.pool import ThreadPool

from subprocess import STDOUT, call

from .formation_utils import *
from .coordinator_utils import (dump_schema as dump_coordinator_schema,
                                dump_sequences,
                                lock_tables_before_data_dump)
from .node_utils import *
from .configuration import *



def run(cmd):
    print('run statement %s' % cmd)
    return cmd, os.system(cmd)


def get_dump_statements(coordinator):
    statements = get_nodes_pg_dump_statements(coordinator)

    if coordinator.configuration.dump_coordinator_data:
        statements.append(coordinator.data_dump_statement)

    return statements


def perform_dump(coordinator):
    configuration = coordinator.configuration

    if configuration.dump_schema:
        dump_coordinator_schema(coordinator)

    # Get pg_dump statements for workers and coordinator
    statements = get_dump_statements(coordinator)

    if not os.path.exists(os.path.join(configuration.dump_folder, 'coordinator_schema.sql')):
        raise Exception('Schema dump isn\'t valid')

    # Run pg_dump with n tasks in parallel
    if configuration.dump_data:
        # Try to lock distributed and reference tables, if can't do it, raise error
        # Add option ignore_locks option
        if not configuration.ignore_write_locks:
            print('Locking the tables to ensure no concurrent write is happening')
            lock_tables_before_data_dump(coordinator)

        pool = ThreadPool(configuration.parallel_tasks)
        for cmd, rc in pool.imap_unordered(run, statements):
            print('{cmd} return code: {rc}'.format(**vars()))

        pool.close()
        pool.join()

    # get dump for sequences
    dump_sequences(coordinator)

    print('Finished pg_dump')
