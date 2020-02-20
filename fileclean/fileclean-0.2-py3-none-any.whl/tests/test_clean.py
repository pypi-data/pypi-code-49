import os
import pytest
from fileclean import clean
from fileclean.workers import PathNotFoundError


@pytest.fixture
def initFile():
    filename = "file1.txt"
    fromPath = "./tests/data/from/"
    toPath = "./tests/data/to/"
    filepath = os.path.join(fromPath, filename)
    toFilepath = os.path.join(toPath, filename)
    with open(filepath, "w") as f:
        f.write("from")
    if os.path.exists(toFilepath):
        os.remove(toFilepath)
    return fromPath, toPath


def test_cleanwork_move(initFile):
    fromPath, toPath = initFile
    for i in range(2):
        clean.cleanwork(fromPath, toPath, r".*\.txt", "move")
        # asssert not error if task rerun


def test_cleanwork_delete(initFile):
    fromPath, toPath = initFile
    for i in range(2):
        clean.cleanwork(fromPath, None, r".*\.txt", "delete")


def test_cleanwork_copy(initFile):
    fromPath, toPath = initFile
    for i in range(2):
        clean.cleanwork(fromPath, toPath, r".*\.txt", "copy")


def test_cleanwork_copy_error(initFile):
    fromPath, toPath = initFile
    with pytest.raises(PathNotFoundError):
        clean.cleanwork(fromPath, None, r".*\.txt", "copy")
