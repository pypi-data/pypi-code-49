import io
from unittest.mock import Mock

import pytest

from flywheel_cli.util import (KeyWithOptions, is_dicom_file, print_tree,
                               str_to_filename)

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
    assert is_dicom_file('test.dcm')
    assert is_dicom_file('test.DCM')
    assert is_dicom_file('test.dicom')
    assert is_dicom_file('test.DICOM')
    assert is_dicom_file('test.dcm.gz')
    assert is_dicom_file('test.DCM.GZ')
    assert is_dicom_file('test.dicom.gz')
    assert is_dicom_file('test.DICOM.GZ')
    assert is_dicom_file('/full/path/to/test.dcm')

    assert not is_dicom_file('')
    assert not is_dicom_file('/')
    assert not is_dicom_file('/test.txt')
    assert not is_dicom_file('/dcm.test')
    assert not is_dicom_file('test.dcmisnt')
    assert not is_dicom_file('test.dcm.zip')


def test_key_with_options():
    # Raises key error if key is missing
    with pytest.raises(KeyError):
        KeyWithOptions({})

    # String value
    opts = KeyWithOptions('value')
    assert opts.key == 'value'
    assert opts.config == {}

    # Other value types
    opts = KeyWithOptions(4.2)
    assert opts.key == 4.2
    assert opts.config == {}

    # Dictionary with options
    opts = KeyWithOptions({
        'name': 'Test Name',
        'option': 8.0
    })
    assert opts.key == 'Test Name'
    assert opts.config == {'option': 8.0}

    # Dictionary with key override
    opts = KeyWithOptions({
        'pattern': 'Test Pattern',
    }, key='pattern')
    assert opts.key == 'Test Pattern'
    assert opts.config == {}


def test_str_to_filename():
    assert str_to_filename('test ?_.dicom.zip') == 'test _.dicom.zip'
    assert str_to_filename('test ?/.dicom.zip') == 'test _.dicom.zip'
    assert str_to_filename('test-1?/**test.dicom.zip') == 'test-1_test.dicom.zip'


def test_print_tree_with_simple_hierarchy(mocked_files):
    tree = io.StringIO()
    print_tree(mocked_files, 'fw://test', fh=tree)
    assert tree.getvalue() == (
        'fw://test (14 bytes / 4 files)'.ljust(80) + '\n'
        '`- a (3 bytes / 1 file)\n'
        '   `- b (10 bytes / 2 files)\n'
    )

def test_print_tree_with_leaves(mocked_files):
    tree = io.StringIO()
    print_tree(mocked_files, 'fw://test', verbose=True, fh=tree)
    assert tree.getvalue() == (
        'fw://test (14 bytes / 4 files)'.ljust(80) + '\n'
        '`- f (1 byte)\n'
        '`- a\n'
        '   |- e (3 bytes)\n'
        '   `- b\n'
        '      |- c (5 bytes)\n'
        '      `- d (5 bytes)\n'
    )

def test_print_tree_with_leaves_utf8(mocked_files):
    tree = Mock(wraps=io.StringIO(), encoding='UTF-8')
    print_tree(mocked_files, 'fw://test', verbose=True, fh=tree)
    assert tree.getvalue() == (
        'fw://test (14 bytes / 4 files)'.ljust(80) + '\n'
        '└─ f (1 byte)\n'
        '└─ a\n'
        '   ├─ e (3 bytes)\n'
        '   └─ b\n'
        '      ├─ c (5 bytes)\n'
        '      └─ d (5 bytes)\n'
    )
