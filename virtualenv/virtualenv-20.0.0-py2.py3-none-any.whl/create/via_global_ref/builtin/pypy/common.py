from __future__ import absolute_import, unicode_literals

import abc

import six

from virtualenv.create.via_global_ref.builtin.ref import PathRefToDest
from virtualenv.util.path import Path

from ..via_global_self_do import ViaGlobalRefVirtualenvBuiltin


@six.add_metaclass(abc.ABCMeta)
class PyPy(ViaGlobalRefVirtualenvBuiltin):
    @classmethod
    def can_describe(cls, interpreter):
        return interpreter.implementation == "PyPy" and super(PyPy, cls).can_describe(interpreter)

    @classmethod
    def _executables(cls, interpreter):
        host = Path(interpreter.system_executable)
        targets = sorted("{}{}".format(name, PyPy.suffix) for name in cls.exe_names(interpreter))
        yield host, targets

    @classmethod
    def exe_names(cls, interpreter):
        return {
            cls.exe_stem(),
            "python",
            "python{}".format(interpreter.version_info.major),
        }

    @classmethod
    def sources(cls, interpreter):
        for src in super(PyPy, cls).sources(interpreter):
            yield src
        for host in cls._add_shared_libs(interpreter):
            yield PathRefToDest(host, dest=lambda self, s: self.bin_dir / s.name)

    @classmethod
    def _add_shared_libs(cls, interpreter):
        # https://bitbucket.org/pypy/pypy/issue/1922/future-proofing-virtualenv
        python_dir = Path(interpreter.system_executable).parent
        for libname in cls._shared_libs():
            src = python_dir / libname
            if src.exists():
                yield src

    @classmethod
    def _shared_libs(cls):
        raise NotImplementedError
