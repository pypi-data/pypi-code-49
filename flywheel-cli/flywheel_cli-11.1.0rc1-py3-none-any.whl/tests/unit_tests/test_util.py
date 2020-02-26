from datetime import datetime
from unittest import mock

import pytest

from flywheel_cli import util

@pytest.fixture
def mocked_files():
    class TestFile:
        def __init__(self, name):
            self.name = name
            self.size = len(self.name)

    files = [TestFile(name) for name in (
        'a/b/c',
        'a/b/d',
        'a/e',
        'f',
    )]
    return files


def test_is_dicom_file():
    assert util.is_dicom_file('test.dcm')
    assert util.is_dicom_file('test.DCM')
    assert util.is_dicom_file('test.dicom')
    assert util.is_dicom_file('test.DICOM')
    assert util.is_dicom_file('test.dcm.gz')
    assert util.is_dicom_file('test.DCM.GZ')
    assert util.is_dicom_file('test.dicom.gz')
    assert util.is_dicom_file('test.DICOM.GZ')
    assert util.is_dicom_file('/full/path/to/test.dcm')

    assert not util.is_dicom_file('')
    assert not util.is_dicom_file('/')
    assert not util.is_dicom_file('/test.txt')
    assert not util.is_dicom_file('/dcm.test')
    assert not util.is_dicom_file('test.dcmisnt')
    assert not util.is_dicom_file('test.dcm.zip')


def test_key_with_options():
    # Raises key error if key is missing
    with pytest.raises(KeyError):
        util.KeyWithOptions({})

    # String value
    opts = util.KeyWithOptions('value')
    assert opts.key == 'value'
    assert opts.config == {}

    # Other value types
    opts = util.KeyWithOptions(4.2)
    assert opts.key == 4.2
    assert opts.config == {}

    # Dictionary with options
    opts = util.KeyWithOptions({
        'name': 'Test Name',
        'option': 8.0
    })
    assert opts.key == 'Test Name'
    assert opts.config == {'option': 8.0}

    # Dictionary with key override
    opts = util.KeyWithOptions({
        'pattern': 'Test Pattern',
    }, key='pattern')
    assert opts.key == 'Test Pattern'
    assert opts.config == {}


def test_str_to_filename():
    assert util.str_to_filename('test ?_.dicom.zip') == 'test _.dicom.zip'
    assert util.str_to_filename('test ?/.dicom.zip') == 'test _.dicom.zip'
    assert util.str_to_filename('test-1?/**test.dicom.zip') == 'test-1_test.dicom.zip'


def test_get_filepath_dir_exists(mocker):
    mocker.patch("flywheel_cli.util.os.path.isdir", side_effect=[True])
    mocked_datetime = mocker.patch("flywheel_cli.util.datetime.datetime")
    mocked_datetime.utcnow.return_value = datetime(1900, 1, 1, 0, 0, 0)
    assert util.get_filepath("foo/") == "foo/log-19000101-000000.csv"


def test_get_filepath_dir_not_exists(mocker):
    mocker.patch("flywheel_cli.util.os.path.isdir", side_effect=[False])
    with pytest.raises(FileNotFoundError):
        util.get_filepath("foo/")


def test_get_incremental_filename(mocker):
    mocker.patch("flywheel_cli.util.os.path.isfile", side_effect=[True, False, True, False])
    assert util.get_incremental_filename("foo") == "foo(1)"
    assert util.get_incremental_filename("foo/bar(1).txt")
