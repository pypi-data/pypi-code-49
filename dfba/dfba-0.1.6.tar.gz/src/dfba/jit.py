# Copyright (C) 2018, 2019 Columbia University Irving Medical Center,
#     New York, USA
# Copyright (C) 2019 Novo Nordisk Foundation Center for Biosustainability,
#     Technical University of Denmark

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


"""JIT compilation of functionlib.cpp.

Adapted from
<https://github.com/jakeret/hope>. Copyright (c) 2013 ETH Zurich, Institute
of Astronomy, Lukas Gamper <lukas.gamper@usystems.ch>.
"""


import logging
import sys
from os.path import basename, isfile, join, splitext
from sysconfig import get_config_var, get_config_vars
from tempfile import NamedTemporaryFile

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext


logger = logging.getLogger(__name__)


CXX_FLAGS = {
    "clang": [
        "-Wall",
        "-Wno-unused-variable",
        "-march=native",
        "-stdlib=libc++",
        "-std=c++11",
    ],
    "icc": [
        "-Wall",
        "-Wno-unused-variable",
        "-march=native",
        "-stdlib=libc++",
        "-std=c++11",
    ],
    "gcc-mac": ["-Wall", "-Wno-unused-variable", "-std=c++11", "-msse4.2"],
    "gcc-linux": ["-Wall", "-Wno-unused-variable", "-std=c++11"],
}


class UnsupportedCompilerException(Exception):
    """Raise exceptions on unsuported compilers."""

    pass


class BuildExtWithoutPlatformSuffix(build_ext):
    """Class for building library functionlib WithoutPlatformSuffix."""

    def get_ext_filename(self, ext_name):
        """Relies onf ext_name."""
        filename = super().get_ext_filename(ext_name)
        return get_ext_filename_without_platform_suffix(filename)


def get_ext_filename_without_platform_suffix(filename):
    """File name without platform suffix.

    Returns
    -------
    filename
        Name of shared library without platform suffix.

    """

    name, ext = splitext(filename)
    ext_suffix = get_config_var("EXT_SUFFIX")

    if ext_suffix == ext:
        return filename

    ext_suffix = ext_suffix.replace(ext, "")
    idx = name.find(ext_suffix)

    if idx == -1:
        return filename
    else:
        return name[:idx] + ext


def get_cxxflags():
    """CXX FLAGS.

    JIT compilation of functionlib.cpp adapted from
    <https://github.com/jakeret/hope>. Copyright (c) 2013 ETH Zurich, Institute
    of Astronomy, Lukas Gamper <lukas.gamper@usystems.ch>

    Returns
    -------
    flags
        The appropriate CXX FLAGS for compilation of functionlib.cpp on
        supported platform. Requires compilation with c++11 features enabled.

    """
    from distutils.ccompiler import new_compiler
    from distutils.sysconfig import customize_compiler
    from platform import system

    system_ = system()
    if system_ == "Darwin":
        CXX_FLAGS["gcc"] = CXX_FLAGS["gcc-mac"]
        CXX_FLAGS["cc"] = CXX_FLAGS["clang"]
        CXX_FLAGS["c++"] = CXX_FLAGS["clang"]
    elif system_ == "Linux":
        CXX_FLAGS["gcc"] = CXX_FLAGS["gcc-linux"]
        CXX_FLAGS["cc"] = CXX_FLAGS["gcc"]
        CXX_FLAGS["c++"] = CXX_FLAGS["gcc"]
    else:
        raise RuntimeError(f"{system_} is currently not supported.")

    get_config_vars()
    compiler = new_compiler()
    customize_compiler(compiler)
    compiler_name = basename(compiler.compiler[0])

    # Since we test for the presence of these names in the current compiler name,
    # for example, 'cc' must be tested before 'gcc'.
    for name in ("clang", "icc", "gcc-mac", "gcc-linux", "gcc", "c++", "cc"):
        if name in compiler_name:
            return CXX_FLAGS[name]
    raise UnsupportedCompilerException(f"Unknown compiler: {compiler_name}")


def compile(directory):
    """Compile library.

    JIT compilation of functionlib.cpp adapted from
    <https://github.com/jakeret/hope>. Copyright (c) 2013 ETH Zurich, Institute
    of Astronomy, Lukas Gamper <lukas.gamper@usystems.ch>

    Parameters
    -------
    directory : string
        Path to temporary directory containing library.

    """

    stdout = sys.stdout
    sys.stdout = NamedTemporaryFile(mode="w", suffix=".log", delete=False)
    argv, target, localfilename, so_filename = (
        sys.argv,
        directory,
        "functionlib",
        "functionlib.so",
    )
    sources = join(target, f"{localfilename}.cpp")
    sys.argv = ["", "build_ext", "-b", target, "-t", "/"]
    cfg_vars = get_config_vars()
    if "CFLAGS" in cfg_vars:
        cfg_vars["CFLAGS"] = cfg_vars["CFLAGS"].replace("-Wstrict-prototypes", "")
    if "OPT" in cfg_vars:
        cfg_vars["OPT"] = cfg_vars["OPT"].replace("-Wstrict-prototypes", "")
    try:
        setup(
            name=localfilename,
            ext_modules=[
                Extension(
                    localfilename, sources=[sources], extra_compile_args=get_cxxflags(),
                )
            ],
            cmdclass={"build_ext": BuildExtWithoutPlatformSuffix},
        )
    except SystemExit as err:
        logger.critical(
            "Dynamic compilation failed. You can find more information in %r.",
            sys.stdout.name,
            exc_info=err,
        )
        sys.stdout.flush(), sys.stderr.flush()
    finally:
        sys.argv = argv
        sys.stdout.close()
        sys.stdout = stdout

    so_path = join(target, so_filename)
    if not isfile(so_path):
        raise RuntimeError("Error compiling function library!")
    return so_path
