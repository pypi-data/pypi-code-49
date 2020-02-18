"""Provides the AbstractSubjectMappingMapper class."""

import json
from abc import ABC, abstractmethod

from ..models import SubjectMap


class AbstractSubjectMappingMapper(ABC):
    """Abstract class to manage subject codes"""


    columns = {
        "ingest_id": "INT",
        "subject_id": "INT",
        "subject_code": "VARCHAR(1024)",
        "field_values": "TEXT",
    }

    # The set of indexes to create for this table
    indexes = [
        ("ingest_idx", ["ingest_id"]),
    ]

    def __init__(self, factory):
        self._factory = factory

    @abstractmethod
    def _get(self, ingest_id, field_values, format_code=None):
        """Get/generate a subject code based on the given field values.
        The scope is the given ingest id.

        Args:
            ingest_id (int): Ingest id
            field_values (str): Values of the input fields

        Returns: SubjectMap
        """

    def connect(self):
        """Get a database connection"""
        return self._factory.connect()

    def initialize(self):
        """Ensures that the table and indexes exist"""
        self._factory.create_table("subjects_mapping", self.columns)
        self.create_indexes()


    def create_indexes(self):
        """Create necessary indexes"""
        for index_name, columns in self.indexes:
            command = 'CREATE INDEX IF NOT EXISTS {} on work_queue({})'.format(index_name, ','.join(columns))
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute(command)

    def get(self, ingest_id, field_values, format_code=None):
        """Get the next subject map."""
        field_values = json.dumps(field_values)
        return self._get(ingest_id, field_values, format_code)

    def get_all_item_for_ingest(self, ingest_id):
        """Return all subjects map that relate to the given ingest_id"""
        command = "SELECT * FROM subjects_mapping WHERE ingest_id = ? ORDER BY subject_code"
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(command, (ingest_id,))
            rows = cursor.fetchall()
        return list(map(self.deserialize, rows))

    def insert(self, record):
        """Insert one record.

        Args:
            record (SubjectMap): The item to insert
        """
        insert_keys = list(self.columns.keys())
        insert_keys_str = ','.join(insert_keys)
        placeholders = ','.join(['?'] * len(insert_keys))

        command = 'INSERT INTO subjects_mapping({}) VALUES({})'.format(insert_keys_str, placeholders)
        # Map fields ahead of insert
        params = [SubjectMap.map_field(key, getattr(record, key, None)) for key in insert_keys]
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(command, tuple(params))

    @classmethod
    def deserialize(cls, row, columns=None):
        """Deserialize a row into ScanTask"""
        if row is None:
            return None

        if columns is None:
            columns = cls.columns.keys()

        props = {}
        for idx, colname in enumerate(columns):
            props[colname] = row[idx]

        return SubjectMap.from_map(props)
