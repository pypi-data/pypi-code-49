"""Provides the PostgresIngestFactory class."""

import logging

from ..abstract_ingest_factory import AbstractIngestFactory
from .discover_queue_mapper import DiscoverQueueMapper
from .connection_wrapper import ConnectionWrapper
from .scan_queue_mapper import ScanQueueMapper
from .subjects_mapping_mapper import SubjectsMappingMapper
from .work_queue_mapper import WorkQueueMapper

log = logging.getLogger(__name__)


class PostgresIngestFactory(AbstractIngestFactory):
    """Postgres specific implementation of AbstractIngestFactory class."""

    def __init__(self, connection_string):
        self._connection_string = connection_string

    def connect(self):
        """Create a database connection object"""
        import psycopg2  # pylint: disable=import-outside-toplevel
        conn = psycopg2.connect(self._connection_string)
        return ConnectionWrapper(conn)

    def create_discover_queue_mapper(self):
        """Create a DiscoverQueueMapper object"""
        return DiscoverQueueMapper(self)

    def create_scan_queue_mapper(self):
        """Create an ScanQueueMapper object"""
        return ScanQueueMapper(self)

    def create_work_queue_mapper(self):
        """Create an WorkQueueMapper object"""
        return WorkQueueMapper(self)

    def create_subjects_mapping_mapper(self):
        """Create a SubjectsMappingMapper object"""
        return SubjectsMappingMapper(self)

    def autoinc_column(self):
        """Get the autoincrementing id type for this database"""
        return 'SERIAL PRIMARY KEY'
