"""Provides DeidLogMapper class"""

from ..models import DeidLog


class DeidLogMapper:
    """Provides methods to controll deid logs"""

    # The set of columns in this table
    columns = {
        "ingest_id": "INT",
        "path": "VARCHAR(4096)",
        "log_type": "VARCHAR(10)",
        "field_values": "TEXT",
        "created": "TIMESTAMP",
    }

    def __init__(self, factory):
        self._factory = factory

    def connect(self):
        """Get a database connection"""
        return self._factory.connect()

    def initialize(self):
        """Ensures that the table and indexes exist"""
        self._factory.create_table('deid_logs', self.columns)

    def insert(self, record):
        """Insert one record.

        Args:
            record (DeidLog): The item to insert

        """
        insert_keys = list(self.columns.keys())
        insert_keys_str = ','.join(insert_keys)
        placeholders = ','.join(['?'] * len(insert_keys))
        command = 'INSERT INTO deid_logs({}) VALUES({})'.format(insert_keys_str, placeholders)

        # Map fields ahead of insert
        params = [DeidLog.map_field(key, getattr(record, key, None)) for key in insert_keys]

        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(command, tuple(params))

    def get_all_item_for_ingest(self, ingest_id):
        """Return all item id that releate to the given ingest_id"""
        limit = 1000
        command = "SELECT * FROM deid_logs WHERE ingest_id = ? LIMIT {} OFFSET {}"
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

    @classmethod
    def deserialize(cls, row, columns=None):
        """Deserialize a row into DeidLog"""
        if row is None:
            return None

        if columns is None:
            columns = cls.columns.keys()

        props = {}
        for idx, colname in enumerate(columns):
            props[colname] = row[idx]

        return DeidLog.from_map(props)
