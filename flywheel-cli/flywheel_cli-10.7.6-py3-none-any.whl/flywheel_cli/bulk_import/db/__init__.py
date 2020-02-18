"""Provides database specific ingest factory classes and a factory method."""

import logging

from .sqlite import SqliteIngestFactory
from .postgres import PostgresIngestFactory

log = logging.getLogger(__name__)

# Map db_type to factory
FACTORY_MAP = {
    'sqlite': SqliteIngestFactory,
    'sqlite3': SqliteIngestFactory,
    'postgres': PostgresIngestFactory,
}


def create_ingest_factory(dbstr):
    """Create the appropriate ingest factory for the given connection string"""
    db_type, _, connection_string = dbstr.partition(':')

    factory_class = FACTORY_MAP.get(db_type)
    if not factory_class:
        raise Exception('Unknown db provider: {}'.format(db_type))
    log.debug(f"Using {db_type}")
    return factory_class(connection_string)
