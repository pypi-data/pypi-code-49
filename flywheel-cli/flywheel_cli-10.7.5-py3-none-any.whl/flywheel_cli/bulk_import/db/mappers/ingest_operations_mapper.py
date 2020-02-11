"""Provide the IngestOperationMapper class."""

from ..models import IngestOperation


class IngestOperationsMapper:
    """Provides methods to create and controll IngestOperations."""

    # The set of columns in this table
    columns = {
        'ingest_id': 'INT PRIMARY KEY',
        'name': 'VARCHAR(256)',
        'created': 'TIMESTAMP',
        'fs_path': 'VARCHAR(4096)',
        'config': 'TEXT',
        'stage': 'VARCHAR(24)',
        'version': 'VARCHAR(24)',
        'processing_start': 'TIMESTAMP',
        'processing_end': 'TIMESTAMP',
    }

    def __init__(self, factory):
        """Create factory instance"""
        self._factory = factory

    def connect(self):
        """Get a database connection"""
        return self._factory.connect()

    def initialize(self):
        """Ensures that the table and indexes exist, for all tables"""
        # Create ingest_operations table
        self._factory.create_autoinc_table('ingest_operations', 'ingest_id', self.columns)

        # Create ingest_items table
        items_mapper = self._factory.create_ingest_items_mapper()
        items_mapper.initialize()

        # Create scan_queue table
        scan_queue_mapper = self._factory.create_scan_queue_mapper()
        scan_queue_mapper.initialize()

        # Create work_queue table
        work_queue_mapper = self._factory.create_work_queue_mapper()
        work_queue_mapper.initialize()

        # Create audit_log table
        audit_log_mapper = self._factory.create_audit_log_mapper()
        audit_log_mapper.initialize()

        # Create private_tags table
        private_tags_mapper = self._factory.create_private_tags_mapper()
        private_tags_mapper.initialize()

        # initialize subjects_mapping table
        subjects_mapping_mapper = self._factory.create_subjects_mapping_mapper()
        subjects_mapping_mapper.initialize()

        # initialize deid_logs table
        deid_log_mapper = self._factory.create_deid_log_mapper()
        deid_log_mapper.initialize()

        # initialize discover_queue table
        discover_queue_mapper = self._factory.create_discover_queue_mapper()
        discover_queue_mapper.initialize()

    def insert(self, record):
        """Insert one record, with autoincrement.

        Args:
            record (IngestOperation): The item to insert

        Returns:
            int: The inserted row id

        """
        insert_keys = list(self.columns.keys())[1:]
        insert_keys_str = ','.join(insert_keys)
        placeholders = ','.join(['?'] * len(insert_keys))

        command = 'INSERT INTO ingest_operations({}) VALUES({})'.format(insert_keys_str, placeholders)

        # Map fields ahead of insert
        params = [IngestOperation.map_field(key, getattr(record, key, None)) for key in insert_keys]

        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(command, tuple(params))
            return cursor.lastrowid

    def update(self, ingest_id, **kwargs):
        """Update one record by ingest_id.

        Args:
            ingest_id (int): The id of the record to update.
            **kwargs: The set of fields to update
        """
        updates = []
        params = []

        # Create the update SET clauses
        for key, value in kwargs.items():
            if key not in self.columns:
                raise Exception('Invalid key field')
            updates.append('{} = ?'.format(key))
            params.append(IngestOperation.map_field(key, value))

        # WHERE clause argument
        params.append(ingest_id)

        command = 'UPDATE ingest_operations SET {} WHERE ingest_id = ?'.format(','.join(updates))
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(command, tuple(params))

    def find(self, ingest_id):
        """Find an item by item_id"""
        return self._find_one("SELECT * FROM ingest_operations WHERE ingest_id = ?", (ingest_id,))

    def _find_one(self, command, *args):
        """Find one with the given query / args"""
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(command, *args)
            try:
                row = next(cursor)
            except StopIteration:
                row = None

        return self.deserialize(row)

    @classmethod
    def deserialize(cls, row):
        """Deserialize a row into IngestOperation"""
        if row is None:
            return None

        columns = cls.columns.keys()
        props = {}
        for idx, colname in enumerate(columns):
            props[colname] = row[idx]

        return IngestOperation.from_map(props)
