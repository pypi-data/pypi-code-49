#
#  setup_scmversion - Builds a pythonic version number sbased on scm tags and branches.
#
#  Copyright (C) 2019 Jorge M. Faleiro Jr.
#
#  This program is free software: you can redistribute it and/or modify
#
#  it under the terms of the GNU Affero General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os
from distutils.cmd import Command

from setuptools.command.develop import develop
from setuptools.command.install import install
from setuptools.command.sdist import sdist

from . import PARSERS, version, tag_version


class TagVersionCommand(Command):
    description = "Tags <package>/version.py with the version number"
    user_options = [
        ('package=', None,
            'name of the main package where the version file will be overwritten'),
        ('file', '_version', 'name of the file'),
    ]

    def initialize_options(self):
        self.package = package
        self.scm = 'git'

    def finalize_options(self):
        assert os.path.exists(
            self.package), 'package does not exist: %s' % self.package
        assert self.scm in PARSERS.keys()

    def run(self):
        tag_version(package=self.package, file=self.file, scm=self.scm)


def command_classes(package, scm='git'):

    class SdistCommand(sdist):

        def run(self):
            tag_version(package, version(scm))
            sdist.run(self)

    class DevelopCommand(develop):

        def run(self):
            tag_version(package, version(scm))
            develop.run(self)

    class InstallCommand(install):

        def run(self):
            tag_version(package, version(scm))
            install.run(self)

    commands = dict(
        tag_version=TagVersionCommand,
        sdist=SdistCommand,
        develop=DevelopCommand,
        install=InstallCommand,
    )

    return commands
