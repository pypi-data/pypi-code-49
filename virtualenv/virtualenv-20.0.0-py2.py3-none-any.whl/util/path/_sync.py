from __future__ import absolute_import, unicode_literals

import logging
import os
import shutil

from six import PY2, PY3, ensure_text

from virtualenv.info import IS_CPYTHON, IS_WIN

if PY3:
    from os import link as os_link

if PY2 and IS_CPYTHON and IS_WIN:  # CPython2 on Windows supports unicode paths if passed as unicode
    norm = lambda src: ensure_text(str(src))  # noqa
else:
    norm = str


def ensure_dir(path):
    if not path.exists():
        logging.debug("create folder %s", ensure_text(str(path)))
        os.makedirs(norm(path))


def ensure_safe_to_do(src, dest):
    if src == dest:
        raise ValueError("source and destination is the same {}".format(src))
    if not dest.exists():
        return
    if dest.is_dir() and not dest.is_symlink():
        shutil.rmtree(norm(dest))
        logging.debug("remove directory %s", dest)
    else:
        logging.debug("remove file %s", dest)
        dest.unlink()


def symlink(src, dest):
    ensure_safe_to_do(src, dest)
    logging.debug("symlink %s", _Debug(src, dest))
    dest.symlink_to(src, target_is_directory=src.is_dir())


def copy(src, dest):
    ensure_safe_to_do(src, dest)
    is_dir = src.is_dir()
    method = shutil.copytree if is_dir else shutil.copy2
    logging.debug("copy %s", _Debug(src, dest))
    method(norm(src), norm(dest))


def link(src, dest):
    ensure_safe_to_do(src, dest)
    logging.debug("hard link %s", _Debug(src, dest.name))
    os_link(norm(src), norm(dest))


class _Debug(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def __str__(self):
        return "{}{} to {}".format(
            "directory " if self.src.is_dir() else "", ensure_text(str(self.src)), ensure_text(str(self.dest))
        )


__all__ = ("ensure_dir", "symlink", "copy", "link", "symlink", "link")
