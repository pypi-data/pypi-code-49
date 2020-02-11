import unittest
import warnings

from sheraf.testing.utils import (
    close_database,
    create_blob_directory,
    create_database,
    create_temp_directory,
    delete_temp_directory,
    start_postgresql_server,
    start_zeo_server,
    stop_postgresql_server,
    stop_zeo_server,
)


class DatabaseTestCase(unittest.TestCase):
    """This :class:`~unittest.TestCase` creates a database and let the user
    access it through ``self.database``.

    One can pass database arguments by surcharging
    :func:`~sheraf.testing.unittest_fixtures.DatabaseTestCase.database_args`.
    By default, a in-memory database is created with
    :class:`~ZODB.DemoStorage.DemoStorage`.

    >>> class MyTest(sheraf.testing.unittest_fixtures.DatabaseTestCase):
    ...    def test_something(self):
    ...        with sheraf.connection(commit=True):
    ...            MyModel.create()
    ...
    >>> class MyOtherTest(sheraf.testing.unittest_fixtures.DatabaseTestCase):
    ...    def database_args(self):
    ...        base_args = super(MyOtherTest, self).database_args()
    ...        base_args["database_name"] = "foobar_db"
    ...        return base_args
    ...
    ...    def test_something(self):
    ...        assert "foobar_db" == self.database.name
    """

    def setUp(self):
        super(DatabaseTestCase, self).setUp()
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            self.database = create_database(
                self.database_args() or self.default_pool_kwargs()
            )

    def database_args(self):
        return {}

    def default_pool_kwargs(self):
        return {}

    def tearDown(self):
        close_database(self.database)
        super(DatabaseTestCase, self).tearDown()


class ConnectedTestCase(DatabaseTestCase):
    """This :class:`~sheraf.testing.unittest_fixtures.TestCase` opens a
    connection on a database and let the user access it through
    ``self.connection``.

    >>> class MyTest(sheraf.testing.unittest_fixtures.ConnectedTestCase):
    ...     def test_something(self):
    ...         assert self.connection
    ...         MyModel.create()
    """

    def setUp(self):
        super(ConnectedTestCase, self).setUp()
        self.connection = self.database.connection_open()

    def tearDown(self):
        self.connection.transaction_manager.abort()
        self.connection.close()
        super(ConnectedTestCase, self).tearDown()


class FileStorageTestCase(DatabaseTestCase):
    """This :class:`~sheraf.testing.unittest_fixtures.TestCase` creates a
    database using a :class:`~ZODB.FileStorage.FileStorage`."""

    def database_args(self):
        return {"uri": "file:///{}/Data.fs".format(self.persistent_dir_path)}

    def setUp(self):
        self.persistent_dir_path, self._old_files_root_dir = create_temp_directory()
        super(FileStorageTestCase, self).setUp()

    def tearDown(self):
        super(FileStorageTestCase, self).tearDown()
        delete_temp_directory(self.persistent_dir_path, self._old_files_root_dir)


class ZeoTestCase(DatabaseTestCase):
    """This :class:`~sheraf.testing.unittest_fixtures.TestCase` launches a ZEO
    server, and then creates a database using a :class:`~ZEO.ClientStorage`."""

    def setUp(self):
        self.persistent_dir_path, self._old_files_root_dir = create_temp_directory()
        self.blob_dir = create_blob_directory(self.persistent_dir_path)
        self.zeo_process, self.zeo_port = start_zeo_server(
            self.persistent_dir_path, self.blob_dir
        )
        super(ZeoTestCase, self).setUp()

    def database_args(self):
        return {
            "uri": "zeo://localhost:{}".format(self.zeo_port),
            "blob_dir": self.blob_dir,
            "shared_blob_dir": True,
        }

    def tearDown(self):
        super(ZeoTestCase, self).tearDown()
        stop_zeo_server(self.zeo_process)
        delete_temp_directory(self.persistent_dir_path, self._old_files_root_dir)


class PostgreSQLRelStorageTestCase(DatabaseTestCase):
    """This :class:`~sheraf.testing.unittest_fixtures.TestCase` launches a
    PostgreSQL server, and then creates a database using a
    :class:`~relstorage.storage.RelStorage`."""

    AFTER_PSQL_SERVER_LAUNCH_SLEEP_TIME = 1

    def setUp(self):
        self.persistent_dir_path, self._old_files_root_dir = create_temp_directory()
        (
            self.pg_process,
            self.pg_user,
            self.pg_port,
            self.pg_error,
        ) = start_postgresql_server(self.persistent_dir_path)
        if self.pg_error:  # pragma: no cover
            raise Exception(self.pg_error)
        super(PostgreSQLRelStorageTestCase, self).setUp()

    def database_args(self):
        return {
            "uri": "postgres://{}@localhost:{}/zodb".format(self.pg_user, self.pg_port)
        }

    def tearDown(self):
        super(PostgreSQLRelStorageTestCase, self).tearDown()
        stop_postgresql_server(self.pg_process)
        delete_temp_directory(self.persistent_dir_path, self._old_files_root_dir)


TestCase = DatabaseTestCase
