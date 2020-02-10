from __future__ import absolute_import, unicode_literals

import os
import shutil

import six

from virtualenv.util.path import Path

from .base import PipInstall


class CopyPipInstall(PipInstall):
    def _sync(self, src, dst):
        src_str = six.ensure_text(str(src))
        dest_str = six.ensure_text(str(dst))
        if src.is_dir():
            shutil.copytree(src_str, dest_str)
        else:
            shutil.copy(src_str, dest_str)

    def _generate_new_files(self):
        # create the pyc files
        new_files = super(CopyPipInstall, self)._generate_new_files()
        new_files.update(self._cache_files())
        return new_files

    def _cache_files(self):
        version = self._creator.interpreter.version_info
        py_c_ext = ".{}-{}{}.pyc".format(self._creator.interpreter.implementation.lower(), version.major, version.minor)
        for root, dirs, files in os.walk(six.ensure_text(str(self._image_dir)), topdown=True):
            root_path = Path(root)
            for name in files:
                if name.endswith(".py"):
                    yield root_path / "{}{}".format(name[:-3], py_c_ext)
            for name in dirs:
                yield root_path / name / "__pycache__"

    def _fix_records(self, new_files):
        extra_record_data_str = self._records_text(new_files)
        with open(six.ensure_text(str(self._dist_info / "RECORD")), "ab") as file_handler:
            file_handler.write(extra_record_data_str.encode("utf-8"))
