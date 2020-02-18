import os
import pytest
import shutil
import tempfile

import fs

from flywheel_cli.bulk_import import db

DATA_ROOT = os.path.join("tests", "data")
DICOM_ROOT = os.path.join(DATA_ROOT, "DICOM")
DEFAULT_DB = ["sqlite"]
CLEANUP_TABLES = [ "ingest_items", "ingest_operations", "scan_queue", "work_queue"]


@pytest.fixture(scope="function")
def dicom_file():
    def get_dicom_file(folder, filename):
        fd, path = tempfile.mkstemp(suffix=".dcm")
        os.close(fd)

        src_path = os.path.join(DICOM_ROOT, folder, filename)
        shutil.copy(src_path, path)

        return path

    return get_dicom_file

@pytest.fixture(scope="function")
def dicom_data():
    def get_dicom_file_data(folder, filename):
        src_path = os.path.join(DICOM_ROOT, folder, filename)
        with open(src_path, "rb") as f:
            data = f.read()

        return data

    return get_dicom_file_data

@pytest.fixture(scope="function")
def temp_fs():
    tempdirs = []

    def make_mock_fs(structure):
        tempdir = tempfile.TemporaryDirectory()
        tempdirs.append(tempdir)

        tmpfs_url = f"osfs://{tempdir.name}"
        tmpfs = fs.open_fs(tmpfs_url)

        for path, files in structure.items():
            with tmpfs.makedirs(path, recreate=True) as subdir:
                for name in files:
                    if isinstance(name, tuple):
                        name, content = name
                    else:
                        content = b"Hello World"

                    with subdir.open(name, "wb") as f:
                        f.write(content)

        return tmpfs, tmpfs_url

    yield make_mock_fs


@pytest.fixture(scope="function")
def ingest_factory(db_connection_string):
    _factories = []

    def create(db_type):
        connection_string = db_connection_string(db_type)
        factory = db.create_ingest_factory(connection_string)
        _factories.append(factory)
        return factory

    yield create

    for factory in _factories:
        # Cleanup any tables that were added
        conn = factory.connect()
        try:
            drop_tables(conn)
        finally:
            conn.close()


@pytest.fixture(scope="function")
def db_connection_string():
    def _get_connection_string(db_type):
        if db_type == "sqlite":
            connection_string = "sqlite:/tmp/sqlite.db"
        elif db_type == "postgres":
            connection_string = "postgresql:" + os.environ["POSTGRES_TEST_DB"]
        return connection_string
    return _get_connection_string


def drop_tables(conn):
    with conn:
        c = conn.cursor()
        for table in CLEANUP_TABLES:
            c.execute(f"DROP TABLE IF EXISTS {table}")


def pytest_addoption(parser):
    parser.addoption("--db", action="append", default=[], help="list of db-modules to pass to test functions")


def pytest_generate_tests(metafunc):
    if "db_type" in metafunc.fixturenames:
        db_opt = metafunc.config.getoption("db")
        if not db_opt:
            db_opt = DEFAULT_DB
        metafunc.parametrize("db_type", db_opt)
