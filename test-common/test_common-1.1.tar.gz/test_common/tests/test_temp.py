"""Tests for fs.temp module."""
import os
import tempfile

from test_common.fs.temp import temp_dir

tmp_folder = tempfile.gettempdir()
tmp_contents_before = os.listdir(tmp_folder)


def test_temp_dir(temp_dir):
    assert os.path.dirname(temp_dir) == tmp_folder
    tmp_contents_now = os.listdir(tmp_folder)
    assert os.path.basename(temp_dir) in tmp_contents_now
