"""Reaper utility functions"""

from __future__ import print_function
import hashlib
import string
import six

import pytz
import tzlocal
import pydicom

from dateutil import relativedelta


try:
    DEFAULT_TZ = tzlocal.get_localzone()
except pytz.exceptions.UnknownTimeZoneError:
    print('Could not determine timezone, defaulting to UTC')
    DEFAULT_TZ = pytz.utc


def localize_timestamp(timestamp, timezone=None):
    # pylint: disable=missing-docstring
    timezone = DEFAULT_TZ if timezone is None else timezone
    return timezone.localize(timestamp)


def parse_sort_info(sort_info, default_subject=''):
    # pylint: disable=missing-docstring
    subject, _, group_project = sort_info.strip(string.whitespace).rpartition('@')
    delimiter = next((char for char in '/:' if char in group_project), '^')
    group, _, project = group_project.partition(delimiter)
    return subject or default_subject.strip(string.whitespace), group, project


def is_seekable(fp):
    """Check if the given file-like object is seekable"""
    seekable_fn = fp.getattr('seekable', None)
    if seekable_fn:
        return seekable_fn()

    seek_fn = fp.getattr('seek', None)
    return callable(seek_fn)


if six.PY3:
    def hash_value(value, algorithm='sha256', output_format='hex', salt=None):
        """Hash a string using the given algorithm and salt, and return in the requested output_format.

        Arguments:
            value (str): The value to hash
            algorithm (str): The algorithm to use (default is sha256)
            output_format (str): The output format, one of 'hex', 'dec', or None
            salt (str): The optional salt string
        """
        hasher = hashlib.new(algorithm)
        # Work in bytes
        if salt:
            hasher.update(salt.encode('utf-8'))
        hasher.update(value.encode('utf-8'))
        if output_format == 'hex':
            result = hasher.hexdigest()
        elif output_format == 'dec':
            digest = hasher.digest()
            result = ''
            for atom in digest:
                result += str(atom)
        else:
            result = hasher.digest
        return result
else:
    def hash_value(value, algorithm='sha256', output_format='hex', salt=None):
        """Hash a string using the given algorithm and salt, and return in the requested output_format.

        Arguments:
            value (str): The value to hash
            algorithm (str): The algorithm to use (default is sha256)
            output_format (str): The output format, one of 'hex', 'dec', or None
            salt (str): The optional salt string
        """
        hasher = hashlib.new(algorithm)
        # Work in bytes
        if salt:
            hasher.update(salt)
        hasher.update(value)
        if output_format == 'hex':
            result = hasher.hexdigest()
        elif output_format == 'dec':
            digest = hasher.digest()
            result = ''
            for atom in digest:
                result += str(ord(atom))
        else:
            result = hasher.digest
        return result


def date_delta(d1, d2, desired_unit=None, max_value=None):
    """Calculate difference between two dates in days, months or years.

    Returns the lowest resolution that fits below max_value, and the units used
    """
    rt = None

    units = ['D', 'M', 'Y']
    if desired_unit in units:
        units = units[units.index(desired_unit):]

    if d1 > d2:  # Ensure that d2 > d1
        d1, d2 = d2, d1

    unit = ''
    for unit in units:
        # Use timedelta for days
        if unit == 'D':
            value = (d2 - d1).days
        else:
            # Use relativedelta for months and years
            if rt is None:
                rt = relativedelta.relativedelta(d2, d1)

            if unit == 'M':
                value = 12 * rt.years + rt.months
            else:
                value = rt.years

        if not max_value or value < max_value:
            break

    if max_value and value > max_value:
        value = max_value

    return value, unit


def walk_wild_sequence(dcm, tag_list):
    """Returns a nested dictionary according to all element in dcm matching tag_list

    Args:
        dcm (pydicom.FileDataset): A pydicom DataElement
        tag_list (list): List of keys or index to get to a specific dicom element (e.g.
            ['SequenceKeyWord', '*', 'OtherKeyword'])

    Returns:
        dict: Wild card expanded nested dictionary matching tag_list for dcm record

    Example:
        .. code-block:: python
        tag_list = ['SequenceKeyWord', '*', 'OtherKeyword']
        walk_wild_sequence(dcm, tag_list)
        > {'SequenceKeyWord': {0: 'OtherKeyword', 1: 'OtherKeyword'}}   # assuming SequenceKeyword has length 2
    """

    if not len(tag_list) == 1:
        if tag_list[0] == '*' and isinstance(dcm.value, pydicom.sequence.Sequence):
            tmp = {}
            for i in range(len(dcm.value)):
                tmp[i] = walk_wild_sequence(dcm[i], tag_list[1:])
            return tmp
        return {tag_list[0]: walk_wild_sequence(dcm[tag_list[0]], tag_list[1:])}
    return tag_list[0]


def dict_paths(tree, cur=None):
    """Convert nested dictionary to a list of list of keys to traverse the dictionary

    Args:
        tree (dict): A dictionary
        cur (list): list of current keys to get to current tree

    Return:
        list: List of lists of keys to traverse the dictionary tree

    Example:
        .. code-block:: python
        tree = {'SequenceKeyWord': {0: 'OtherKeyword', 1: 'OtherKeyword'}}
        dict_paths(tree)
        > [['SequenceKeyword', 0, 'OtherKeyword'], ['SequenceKeyword', 1, 'OtherKeyword']]
    """
    cur = cur if cur else []
    if not isinstance(tree, dict):
        yield cur + [tree]
    else:
        for k, v in tree.items():
            for path in dict_paths(v, cur + [k]):
                yield path


def matches_byte_sig(input_bytes, offset, byte_sig):
    """Checks bytes for a file signature

    If the input_bytes contain the byte_sig at the offset, return True, otherwise, False

    Args:
        input_bytes (bytes): byte data to check for signature
        offset (int): the starting byte of the byte signature
        byte_sig (bytes): the byte signature to check

    Returns:
        bool: True if signature match, False otherwise
    """
    # Calculate the location of the last byte to grab
    byte_end = offset + len(byte_sig)
    return input_bytes[offset:byte_end] == byte_sig


def is_dicom(src_fs, filepath):
    """Determines if a file is a dicom only by checking for the dicom byte signature"""
    offset = 128
    byte_sig = b'DICM'
    with src_fs.open(filepath, 'rb') as f:
        file_bytes = f.read(offset + len(byte_sig))
        return matches_byte_sig(file_bytes, offset, byte_sig)


def is_jpg(src_fs, filepath):
    """Determines if a file is a jpg only by checking for the jpg byte signature"""
    offset = 0
    byte_sig = b'\xFF\xD8\xFF'
    with src_fs.open(filepath, 'rb') as f:
        file_bytes = f.read(offset + len(byte_sig))
        return matches_byte_sig(file_bytes, offset, byte_sig)


def is_png(src_fs, filepath):
    """Determines if a file is a png only by checking for the dicom byte signature"""
    offset = 0
    byte_sig = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'
    with src_fs.open(filepath, 'rb') as f:
        file_bytes = f.read(offset + len(byte_sig))
        return matches_byte_sig(file_bytes, offset, byte_sig)
