"""Provides the AbstractIngestFactory class."""

import copy
from abc import ABC, abstractmethod

from .mappers import AuditLogMapper, DeidLogMapper, IngestItemsMapper, IngestOperationsMapper, PrivateTagsMapper


class AbstractIngestFactory(ABC):
    """Abstract class to create ingest mappers."""

    @abstractmethod
    def connect(self):
        """Create a database connection object"""

    @abstractmethod
    def create_discover_queue_mapper(self):
        """Create a DiscoverQueueMapper object"""

    @abstractmethod
    def create_scan_queue_mapper(self):
        """Create an ScanQueueMapper object"""

    @abstractmethod
    def create_work_queue_mapper(self):
        """Create an WorkQueueMapper object"""

    @abstractmethod
    def create_subjects_mapping_mapper(self):
        """Create an SubjectsMappingMapper object"""

    @abstractmethod
    def autoinc_column(self):
        """Get the autoincrementing id type for this database"""

    def create_autoinc_table(self, table_name, primary_key, columns):
        """Create an auto-incrementing table.

        Args:
            table_name (str): The name of the table to create
            primary_key (str): The name of the primary key column
            columns (dict): The set of columns to create
        """
        columns = copy.deepcopy(columns)
        columns[primary_key] = self.autoinc_column()

        cols = ','.join(['{} {}'.format(name, spec) for name, spec in columns.items()])

        command = 'CREATE TABLE IF NOT EXISTS {}({})'.format(table_name, cols)
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(command)

    def create_table(self, table_name, columns):
        """Create a table.

        Args:
            table_name (str): The name of the table to create
            columns (dict): The set of columns to create

        """
        cols = ','.join(['{} {}'.format(name, spec) for name, spec in columns.items()])

        command = 'CREATE TABLE IF NOT EXISTS {}({})'.format(table_name, cols)
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(command)

    def create_mapper(self):
        """Create an IngestOperationMapper object"""
        return IngestOperationsMapper(self)

    def create_ingest_items_mapper(self):
        """Create an IngestItemsMapper object"""
        return IngestItemsMapper(self)

    def create_audit_log_mapper(self):
        """Create an AuditLogMapper object"""
        return AuditLogMapper(self)

    def create_private_tags_mapper(self):
        """Create a PrivateTagsMapper object"""
        return PrivateTagsMapper(self)

    def create_deid_log_mapper(self):
        """Create a DeidLogMapper object"""
        return DeidLogMapper(self)
