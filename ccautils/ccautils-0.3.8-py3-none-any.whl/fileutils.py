# Copyright (c) 2018, Christopher Allison
#
#     This file is part of ccautils.
#
#     ccautils is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     ccautils is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with ccautils.  If not, see <http://www.gnu.org/licenses/>.
"""Miscellaneous file utility functions.

a set of file based utilities for python programmes and scripts
"""
import hashlib
import os
from pathlib import Path
import sys

from ccautils.errors import errorRaise
import ccautils.utils as UT


def fileExists(fqfn):
    """Tests for the existance of a file.

    Args:
        fqfn: str fully-qualified file name

    Returns:
        Bool: True or False
    """
    try:
        return Path(fqfn).is_file()
    except Exception as e:
        fname = sys._getframe().f_code.co_name
        errorRaise(fname, e)


def dirExists(fqdn):
    """Tests for the existance of a directory.

    Args:
        fqdn: fully-qualified directory name

    Returns:
        Bool: True or False
    """
    try:
        return Path(fqdn).is_dir()
    except Exception as e:
        fname = sys._getframe().f_code.co_name
        errorRaise(fname, e)


def dfExists(fqdfn):
    """Tests for the existance of a directory or file.

    Args:
        fqdfn: fully-qualified directory or file name

    Returns:
        Bool: True or False
    """
    try:
        ret = fileExists(fqdfn)
        if not ret:
            ret = dirExists(fqdfn)
        return ret
    except Exception as e:
        fname = sys._getframe().f_code.co_name
        errorRaise(fname, e)


def makePath(pn):
    """Makes the path.

    Args:
        pn: the fully-qualified path to make
    """
    try:
        if not dfExists(pn):
            p = Path(pn)
            p.mkdir(mode=0o755, parents=True, exist_ok=True)
    except Exception as e:
        fname = sys._getframe().f_code.co_name
        errorRaise(fname, e)


def makeFilePath(fqfn):
    """Makes the path for the file.

    Args:
        fqfn: fully-qualified file name
    """
    try:
        pfn = os.path.basename(fqfn)
        makePath(pfn)
    except Exception as e:
        fname = sys._getframe().f_code.co_name
        errorRaise(fname, e)


def absPath(fn):
    """Transforms the filename into a fully-qualified file name.

    Args:
        fn: file name containing possible unix filesystem 'markers'

    Returns:
        str:
    """
    try:
        return os.path.abspath(os.path.expanduser(fn))
    except Exception as e:
        fname = sys._getframe().f_code.co_name
        errorRaise(fname, e)


def rename(src, dest):
    """Renames src to dest.

    Args:
        src: source file name
        dest: destination file name

    Raises:
        Exception: if source filename does not exist
    """
    try:
        if dfExists(src):
            p = Path(src)
            p.rename(dest)
        else:
            raise Exception(f"src file does not exist: {src}")
    except Exception as e:
        fname = sys._getframe().f_code.co_name
        errorRaise(fname, e)


def fileDelete(fqfn):
    """Deletes the named file.

    Args:
        fqfn: - fully-qualified filename to delete
    """
    try:
        if fileExists(fqfn):
            os.unlink(fqfn)
    except Exception as e:
        fname = sys._getframe().f_code.co_name
        errorRaise(fname, e)


def fileSize(fqfn):
    """Retrieves the size of the file in bytes.

    Args:
        fqfn: str fully-qualified filename

    Returns:
        int: the size of the file
    """
    try:
        if fileExists(fqfn):
            return os.stat(fqfn).st_size
    except Exception as e:
        fname = sys._getframe().f_code.co_name
        errorRaise(fname, e)


def sizeof_fmt(num, suffix="B"):
    """Displays the size of num in human readable units.

    from article by Fred Cirera:
    https://web.archive.org/web/20111010015624/http://blogmag.net/ \
            blog/read/38/Print_human_readable_file_size
    and stackoverflow:
    https://stackoverflow.com/questions/1094841/ \
            reusable-library-to-get-human-readable-version-of-file-size

    Args:
        num: int a number (e.g. the size of a file)
        suffix: str a suffix to append to the output string

    Returns:
        str: num expressed in human readable units
    """
    try:
        for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
            if abs(num) < 1024.0:
                return f"{num:3.1f}{unit}{suffix}"
            num /= 1024.0
    except Exception as e:
        fname = sys._getframe().f_code.co_name
        errorRaise(fname, e)


def getFileHash(fqfn, blocksize=65536):
    """Compute the file sha256 hash and size.

    Args:
        fqfn: str fully-qualified file name
        blocksize: int the block size to pass to the hashing function

    Returns:
        tuple: (hash: str, filesize: int)
    """
    try:
        fnsize = fileSize(fqfn)
        sha = hashlib.sha256()
        with open(fqfn, "rb") as ifn:
            fbuf = ifn.read(blocksize)
            while len(fbuf) > 0:
                sha.update(fbuf)
                fbuf = ifn.read(blocksize)
        return (sha.hexdigest(), fnsize)
    except Exception as e:
        fname = sys._getframe().f_code.co_name
        errorRaise(fname, e)


def fileTouch(fqfn, truncate=True):
    """Creates an empty file, or truncates an existing one as required.

    it is truncated if `truncate` is True and
    the file exists already, otherwise the
    access timestamp is just updated

    Args:
        fqfn: str fully-qualified filename
        truncate: Bool
    """
    try:
        if fileExists(fqfn) and truncate:
            open(fqfn, "w").close()
        elif fileExists(fqfn):
            open(fqfn, "r").close()
        else:
            open(fqfn, "w").close()
    except Exception as e:
        fname = sys._getframe().f_code.co_name
        errorRaise(fname, e)


def readFile(fqfn):
    """Reads the file into the output string.

    Args:
        fqfn: str fully-qualified filename

    Returns:
        str: or None if file does not exist
    """
    try:
        if os.path.exists(fqfn):
            with open(fqfn, "r") as ifn:
                lines = ifn.readlines()
            return UT.addToString("", lines)
    except Exception as e:
        fname = sys._getframe().f_code.co_name
        errorRaise(fname, e)
