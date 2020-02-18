"""Provides the AbstractScanQueueMapper class."""

from abc import ABC, abstractmethod

from ..models import ScanTask, TaskStatus


class AbstractScanQueueMapper(ABC):
    """Abstract class to create and control the scan queue."""
    # The set of columns in this table
    columns = {
        'task_id': 'INT PRIMARY KEY',
        'ingest_id': 'INT',
        'path': 'VARCHAR(4096)',
        'context': 'TEXT',
        'scanner_type': 'VARCHAR(24)',
        'actor_id': 'VARCHAR(256)',
        'status': 'VARCHAR(24)',
    }

    # The set of indexes to create for this table
    indexes = [
        ('status_idx', ['status']),
        ('actor_idx', ['actor_id']),
    ]

    @abstractmethod
    def _get(self, actor_id):
        """Get the next item from the queue"""

    def __init__(self, factory):
        """Create factory instance"""
        self._factory = factory

    def connect(self):
        """Get a database connection"""
        return self._factory.connect()

    def initialize(self):
        """Ensures that the table and indexes exist"""
        self._factory.create_autoinc_table('scan_queue', 'task_id', self.columns)
        self.create_indexes()

    def insert(self, record):
        """Insert one record, with autoincrement.

        Args:
            record (ScanTask): The item to insert

        Returns:
            int: The inserted row id

        """
        insert_keys = list(self.columns.keys())[1:]
        insert_keys_str = ','.join(insert_keys)
        placeholders = ','.join(['?'] * len(insert_keys))

        command = 'INSERT INTO scan_queue({}) VALUES({})'.format(insert_keys_str, placeholders)
        record.status = TaskStatus.waiting
        # Map fields ahead of insert
        params = [ScanTask.map_field(key, getattr(record, key, None)) for key in insert_keys]
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(command, tuple(params))
            return cursor.lastrowid

    def update(self, task_id, **kwargs):
        """Update one record by task_id.

        Args:
            task_id (int): The id of the record to update.
            **kwargs: The set of fields to update
        """
        updates = []
        params = []

        # Create the update SET clauses
        for key, value in kwargs.items():
            if key not in self.columns:
                raise Exception('Invalid key field')
            updates.append('{} = ?'.format(key))
            params.append(ScanTask.map_field(key, value))

        # WHERE clause argument
        params.append(task_id)

        command = 'UPDATE scan_queue SET {} WHERE task_id = ?'.format(','.join(updates))
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(command, tuple(params))

    def find(self, task_id):
        """Find a task by task_id"""
        command = "SELECT * FROM scan_queue WHERE task_id=? LIMIT 1"
        return self._find_one(command, task_id)

    def create_indexes(self):
        """Create necessary indexes"""
        for index_name, columns in self.indexes:
            command = 'CREATE INDEX IF NOT EXISTS {} on scan_queue({})'.format(index_name, ','.join(columns))
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute(command)

    def get(self, actor_id):
        """Get the next item off the work queue"""
        return self._get(actor_id)

    def is_complete(self):
        """Check that the scan queue has uncomplete items, items with status waiting or processing."""
        command = "SELECT * FROM scan_queue WHERE (status='waiting' OR status='processing') LIMIT 1"
        return not bool(self._find_one(command))

    def is_complete_ingest(self, ingest_id):
        """Check that the scan queue has uncomplete items for a given ingest id, items with status waiting or processing."""
        command = "SELECT * FROM scan_queue WHERE (status='waiting' OR status='processing') AND ingest_id=? LIMIT 1"
        return not bool(self._find_one(command, ingest_id))

    def _find_one(self, command, *args):
        """Find one with the given query / args"""
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(command, tuple(args))
            try:
                row = next(cursor)
            except StopIteration:
                row = None

        return self.deserialize(row)

    @classmethod
    def deserialize(cls, row):
        """Deserialize a row into ScanTask"""
        if row is None:
            return None

        columns = cls.columns.keys()

        props = {}
        for idx, colname in enumerate(columns):
            props[colname] = row[idx]

        return ScanTask.from_map(props)
