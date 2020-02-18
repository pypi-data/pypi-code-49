"""Provies the IngestItemsMapper class."""

from ..models import IngestItem


class IngestItemsMapper:
    """Creating and controlling ingest items."""
    # The set of columns in this table
    columns = {
        'item_id': 'INT PRIMARY KEY',
        'ingest_id': 'INT',
        'subdir': 'VARCHAR(4096)',
        'files': 'VARCHAR(4096)',
        'item_type': 'VARCHAR(24)',  # file, packfile, metadata
        'context': 'TEXT',
        'size': 'INT',
        'mtime': 'TIMESTAMP',
        'warnings': 'TEXT',
        'errors': 'TEXT',
    }

    def __init__(self, factory):
        """Create an IngestItems

        Args:
            factory: The connection factory
        """
        self._factory = factory

    def connect(self):
        """Get a database connection"""
        return self._factory.connect()

    def initialize(self):
        """Ensures that the table and indexes exist"""
        self._factory.create_autoinc_table('ingest_items', 'item_id', self.columns)

    def insert(self, record):
        """Insert one record, with autoincrement.

        Args:
            record (IngestItem): The item to insert

        Returns:
            int: The inserted row id

        """
        insert_keys = list(self.columns.keys())[1:]
        insert_keys_str = ','.join(insert_keys)
        placeholders = ','.join(['?'] * len(insert_keys))

        command = 'INSERT INTO ingest_items({}) VALUES({})'.format(insert_keys_str, placeholders)

        # Map fields ahead of insert
        params = [IngestItem.map_field(key, getattr(record, key, None)) for key in insert_keys]

        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(command, tuple(params))
            return cursor.lastrowid

    def update(self, item_id, **kwargs):
        """Update one record by item_id.

        Args:
            item_id (int): The id of the record to update.
            **kwargs: The set of fields to update
        """
        updates = []
        params = []

        # Create the update SET clauses
        for key, value in kwargs.items():
            if key not in self.columns:
                raise Exception('Invalid key field')
            updates.append('{} = ?'.format(key))
            params.append(IngestItem.map_field(key, value))

        # WHERE clause argument
        params.append(item_id)

        command = 'UPDATE ingest_items SET {} WHERE item_id = ?'.format(','.join(updates))
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(command, tuple(params))

    def find(self, item_id):
        """Find an item by item_id"""
        return self._find_one("SELECT * FROM ingest_items WHERE item_id = ?", (item_id,))

    def get_unique_count_of_ingest(self, column, ingest_id):
        """Get the count of unique items in the given column of ingest"""
        command = f"SELECT COUNT(DISTINCT {column}) FROM ingest_items WHERE ingest_id = ?"
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(command, (ingest_id,))
            return cursor.fetchone()

    def get_sum_of_sizes(self, ingest_id):
        """Get the sum of ingest item sizes"""
        command = "SELECT SUM(size) from ingest_items WHERE ingest_id= ? "
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(command, (ingest_id,))
            return cursor.fetchone()

    def get_sum_of_completed_sizes(self, ingest_id):
        """Get the sum of completed ingest item sizes"""
        command = ("SELECT SUM(ingest_items.size) FROM ingest_items "
                   "JOIN work_queue ON (ingest_items.item_id = work_queue.item_id) "
                   "AND ingest_items.ingest_id = ? WHERE work_queue.status = 'complete'")
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(command, (ingest_id,))
            return cursor.fetchone()

    def get_count_of_ingest(self, column, ingest_id):
        """Get the count of items in the given column of ingest"""
        command = f"SELECT COUNT({column}) FROM ingest_items WHERE ingest_id = ?"
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(command, (ingest_id,))
            return cursor.fetchone()

    def get_column_of_ingest(self, column, ingest_id):
        """Get items from the given column of ingest"""
        command = f"SELECT {column} FROM ingest_items WHERE ingest_id = ?"
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(command, (ingest_id,))
            return cursor.fetchall()

    def get_all_item_for_ingest(self, ingest_id):
        """Return all item id that releate to the given ingest_id"""
        limit = 1000
        command = "SELECT * FROM ingest_items WHERE ingest_id = ? LIMIT {} OFFSET {}"
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
    def deserialize(cls, row):
        """Deserialize a row into IngestItem"""
        if row is None:
            return None

        columns = cls.columns.keys()
        props = {}
        for idx, colname in enumerate(columns):
            props[colname] = row[idx]

        return IngestItem.from_map(props)
