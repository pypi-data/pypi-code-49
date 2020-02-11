"""Provides AuditLogMapper class."""

import logging

from ..models import AuditLog

log = logging.getLogger(__name__)


class AuditLogMapper:
    """Creating and controlling audit log entries."""
    columns = {
        "log_id": "INT PRIMARY KEY",
        "ingest_id": "INT",
        "src_path": "VARCHAR(4096)",
        "fw_path": "VARCHAR(4096)",
        "failed": "BOOLEAN",
        "message": "TEXT",
    }

    def __init__(self, factory):
        """Create an AuditLog

        Args:
            factory: The connection factory
        """
        self._factory = factory

    def connect(self):
        """Get a database connection"""
        return self._factory.connect()

    def initialize(self):
        """Ensures that the table and indexes exist"""
        self._factory.create_autoinc_table("audit_logs", "log_id", self.columns)

    def insert(self, record, no_audit_log):
        """Insert one record, with autoincrement.

        Args:
            record (AuditLog): The audit log entry to insert

        Returns:
            int: The inserted row id
        """
        if no_audit_log:
            return None

        insert_keys = list(self.columns.keys())[1:]
        insert_keys_str = ",".join(insert_keys)
        placeholders = ",".join(["?"] * len(insert_keys))

        command = f"INSERT INTO audit_logs({insert_keys_str}) VALUES({placeholders})"

        # Map fields ahead of insert
        params = [AuditLog.map_field(key, getattr(record, key, None)) for key in insert_keys]

        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(command, tuple(params))
            return cursor.lastrowid

    def update(self, log_id, **kwargs):
        """Update one record by log_id.

        Args:
            log_id (int): The id of the record to update.
            **kwargs: The set of fields to update.
        """
        updates = []
        params = []

        # Create the update SET clauses
        for key, value in kwargs.items():
            if key not in self.columns:
                raise Exception("Invalid key field")
            updates.append(f"{key} = ?")
            params.append(AuditLog.map_field(key, value))

        # WHERE clause argument
        params.append(log_id)

        command = "UPDATE audit_logs SET {','.join(updates)} WHERE log_id = ?"
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(command, tuple(params))

    def get_logs(self, ingest_id):
        """Save logs for an ingest_id to a file"""
        limit = 1000
        command = "SELECT * FROM audit_logs WHERE ingest_id = ? LIMIT {} OFFSET {}"
        offset = 0
        while True:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute(command.format(limit, offset), (ingest_id,))
                rows = cursor.fetchall()
            for item in map(self.deserialize, rows):
                yield item
            if len(rows) < limit:
                break
            offset += len(rows)

    def find(self, log_id):
        """Find an item by log_id"""
        return self._find_one("SELECT * FROM audit_logs WHERE log_id = ?", (log_id,))

    def _find_one(self, command, *args):
        """Find one with the given query / args"""
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(command, *args)
            try:
                row = next(cursor)
            except StopIteration:
                return None
        return self.deserialize(row)

    @classmethod
    def deserialize(cls, row, columns=None):
        """Deserialize a row into AuditLog"""
        if row is None:
            return None

        if columns is None:
            columns = cls.columns.keys()

        props = {}
        for idx, colname in enumerate(columns):
            props[colname] = row[idx]

        return AuditLog.from_map(props)
