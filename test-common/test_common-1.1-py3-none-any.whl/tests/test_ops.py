"""
Tests for ops module.
"""
import os
import pytest
import tempfile

import test_common.fs.ops as ops


@pytest.mark.ops
def test_delete_file():
    _, temp_file_pathname = tempfile.mkstemp()
    assert os.path.exists(temp_file_pathname)
    ops.delete_file(temp_file_pathname)
    assert not os.path.exists(temp_file_pathname)


@pytest.mark.ops
def test_delete_existing_files():
    temp_file_pathnames = [tempfile.mkstemp()[1] for _ in range(2)]
    for temp_file_pathname in temp_file_pathnames:
        assert os.path.exists(temp_file_pathname)
    ops.delete_files(temp_file_pathnames, False)
    for temp_file_pathname in temp_file_pathnames:
        assert not os.path.exists(temp_file_pathname)


@pytest.mark.ops
def test_deleting_non_existing_files():
    _, temp_file_pathname = tempfile.mkstemp()
    assert os.path.exists(temp_file_pathname)
    unexisting_file = "/tmp/123456789.nex"
    files_to_delete = [temp_file_pathname, unexisting_file]
    # Check non-existing files are detected when ignore_missing is False.
    with pytest.raises(FileNotFoundError):
        ops.delete_files(files_to_delete, False)
    # Check non-existing files don't raise any exception when ignore_missing
    # is true.
    _, temp_file_pathname = tempfile.mkstemp()
    files_to_delete = [temp_file_pathname, unexisting_file]
    assert os.path.exists(temp_file_pathname)
    ops.delete_files(files_to_delete, True)
    assert not os.path.exists(temp_file_pathname)


@pytest.mark.ops
def test_copy_file():
    temp_file_pathname = tempfile.mkstemp()[1]
    temp_file_name = os.path.basename(temp_file_pathname)
    with tempfile.TemporaryDirectory() as temp_dir:
        expected_file_pathname = os.path.join(temp_dir, temp_file_name)
        assert not os.path.exists(expected_file_pathname)
        ops.copy_file(temp_file_pathname, expected_file_pathname)
        assert os.path.exists(expected_file_pathname)


@pytest.mark.ops
def test_copy_files():
    temp_file_pathnames = [tempfile.mkstemp()[1] for _ in range(2)]
    with tempfile.TemporaryDirectory() as temp_dir:
        ops.copy_files(temp_file_pathnames, temp_dir)
        assert all(True
                   if os.path.exists(os.path.join(temp_dir,
                                                  os.path.basename(file)))
                   else False
                   for file in temp_file_pathnames)
