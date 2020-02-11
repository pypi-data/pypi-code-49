"""Provides the SqliteIngestFactory class."""

from ..abstract_ingest_factory import AbstractIngestFactory
from .discover_queue_mapper import DiscoverQueueMapper
from .scan_queue_mapper import ScanQueueMapper
from .work_queue_mapper import WorkQueueMapper
from .subjects_mapping_mapper import SubjectsMappingMapper


class SqliteIngestFactory(AbstractIngestFactory):
    """Sqlite specific implementation of AbstractIngestFactory class."""

    def __init__(self, connection_string):
        self._connection_string = connection_string

    def connect(self):
        """Create a database connection object"""
        import sqlite3  # pylint: disable=import-outside-toplevel
        return sqlite3.connect(self._connection_string, detect_types=sqlite3.PARSE_DECLTYPES)

    def create_discover_queue_mapper(self):
        """Create a DiscoverQueueMapper object"""
        return DiscoverQueueMapper(self)

    def create_scan_queue_mapper(self):
        """Create a ScanQueueMapper object"""
        return ScanQueueMapper(self)

    def create_work_queue_mapper(self):
        """Create a WorkQueueMapper object"""
        return WorkQueueMapper(self)

    def create_subjects_mapping_mapper(self):
        """Create a SubjectsMappingMapper object"""
        return SubjectsMappingMapper(self)

    def autoinc_column(self):
        """Get the autoincrementing id type for this database"""
        return 'INTEGER PRIMARY KEY'
