import os
import shutil
import tempfile

import fs
import pytest

TESTS_ROOT = os.path.dirname(os.path.dirname(__file__))
DATA_ROOT = os.path.join(TESTS_ROOT, "data")
DICOM_ROOT = os.path.join(DATA_ROOT, "DICOM")
DEFAULT_DB = ["sqlite"]
CLEANUP_TABLES = [ "ingest_items", "ingest_operations", "scan_queue", "work_queue"]


@pytest.fixture(scope="session")
def test_data_dir():
    return DATA_ROOT


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
