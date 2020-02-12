#!/usr/bin/env python

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
# along with this program. If not, see <https://www.gnu.org/licenses/>.


"""Set up the Dynamic FBA package."""


import os
import pathlib

import versioneer
from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext


try:
    DEFAULT_NPROC = len(os.sched_getaffinity(0))
except (OSError, AttributeError):
    DEFAULT_NPROC = 1


class CMakeExtension(Extension):
    """Override the default setuptools extension building."""

    def __init__(self, name, sources=(), **kwargs):
        """Pass everything to `Extension`."""
        super().__init__(name=name, sources=list(sources), **kwargs)


class CMakeBuild(build_ext):
    """Override `build_ext` to then register it in the command classes."""

    def run(self):
        """Call Cmake and build every extension. Overrides parent's method."""
        for ext in self.extensions:
            self.build_extension(ext)
        super().run()

    def build_extension(self, extension):
        """Configure `extension` with CMake and build modules."""
        print("*" * 79)
        cwd = pathlib.Path().absolute()

        # These directories will be created in `build_py`, so if you don't have
        # any Python sources to bundle, the directories will be missing.
        build_temp = pathlib.Path(self.build_temp)
        build_temp.mkdir(parents=True, exist_ok=True)
        ext_dir = pathlib.Path(self.get_ext_fullpath(extension.name))

        # example of cmake args
        config = "Debug" if self.debug else "Release"
        cmake_args = [
            f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={ext_dir.parent.absolute()}",
            f"-DCMAKE_BUILD_TYPE={config}",
        ]

        # example of build args
        num_proc = int(os.getenv("NPROC", DEFAULT_NPROC))
        build_args = ["--config", config, "--", "-j", str(num_proc)]

        os.chdir(str(build_temp))
        self.spawn(["cmake", str(cwd)] + cmake_args)
        if not self.dry_run:
            self.spawn(["cmake", "--build", "."] + build_args)
        os.chdir(str(cwd))
        print("*" * 79)


# Insert the new command class to build extensions.
command_class = versioneer.get_cmdclass()
command_class["build_ext"] = CMakeBuild


# All other arguments are defined in `setup.cfg`.
setup(
    version=versioneer.get_version(),
    cmdclass=command_class,
    ext_modules=[CMakeExtension("dfba/dfba_utils")],
)
