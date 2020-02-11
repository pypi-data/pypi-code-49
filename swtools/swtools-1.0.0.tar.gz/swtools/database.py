#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A simple interface for SQLite database connections.

Creating an instance of the `Database` class will immediately attempt
to connect to the database and create a cursor. When using a context
manager, the connection will close automatically. If not, a `close()`
method is provided and must be called to close all database objects.

Notes
-----
When trying to connect to a database, SQLite will attempt to create
the file if it doesn't exist. In this case, instantiation will not
cause an exception. However, subsequent attempts to use the generated
cursor will cause a `sqlite3.OperationalError`. This is because the
SQL will be called on a new empty database. This error, as well as other
typical file system access exceptions, should be caught by the class.

Examples
--------
.. code-block:: python
    :caption: Create an instance using a context manager (recommended)

    with Database(database_full_path) as db:
        db.cursor.execute(sql)

.. code-block:: python
    :caption: Create an instance directly. Calling the close() method is required.

    db = Database(database_full_path)
    db.cursor.execute(sql)
    db.close()

"""

import sqlite3


class Database():
    """A simple interface for SQLite database connections."""

    def __init__(self, database=None):
        try:
            self.db = database
            self.conn = sqlite3.connect(self.db)
            self.conn.row_factory = sqlite3.Row
            self.cursor = self.conn.cursor()
        except Exception as e:
            print('\n Database Error:', e, '\n')
            self.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is sqlite3.OperationalError:
            print('\n Database Error:', exc_value, '\n')
            return False
        self.close()

    def close(self):
        """Close all database objects."""
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None
