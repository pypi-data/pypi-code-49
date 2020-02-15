import pickle
import pkg_resources
import sqlite3

sqlite3.register_converter('PICKLE', pickle.loads)

class Database:
    """Manage an in-memory database of structures

    `Database` objects wrap a sqlite database containing structure
    information. Structures can be added to and read from the
    database.

    Databases should only be written to by a single thread at once.

    Currently the only table populated in the database is
    `unit_cells`, with the fields:

      * name (str): Short name of the structure type
      * space_group (int): Integer representation of the space group of the structure
      * size (int): Number of particles in the unit cell
      * structure (:class:`.Structure`): Structure object

    """
    def __init__(self):
        self._connection = sqlite3.connect(
            ':memory:', detect_types=sqlite3.PARSE_DECLTYPES,
            check_same_thread=False)

        self._initialize_db()

    def _initialize_db(self):
        with self._connection as c:
            c.execute(
                'CREATE TABLE IF NOT EXISTS unit_cells( '
                'name STRING, space_group INTEGER, '
                'size INTEGER, structure PICKLE )')

    @property
    def connection(self):
        return self._connection

    def insert_unit_cell(self, name, space_group, structure, cursor=None):
        """Insert a unit cell into this database object

        :param name: Short name of the structure
        :param space_group: Integer representation of the space group for the structure
        :param structure: :class:`.Structure` object to store
        :param cursor: Database connection cursor (optional)
        """
        cursor = cursor or self._connection

        assert isinstance(space_group, int)

        encoded_structure = pickle.dumps(structure)
        size = len(structure.positions)

        cursor.execute(
            'INSERT INTO unit_cells VALUES (?, ?, ?, ?)',
            (name, space_group, size, encoded_structure))

    def query(self, query, *args):
        """Execute a (sqlite) query on the database

        Parameters are the same as for an `sqlite3` database.
        """
        for row in self._connection.execute(query, *args):
            yield row

    @classmethod
    def make_standard(cls):
        """Generate the standard database from all installed packages
        """
        result = cls()

        for entry_point in pkg_resources.iter_entry_points('pyriodic_sources'):
            callback = entry_point.load()
            callback(result)

        return result
