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

import argparse
import logging
import subprocess
import sys
from abc import ABC, abstractmethod
from enum import Enum
from functools import lru_cache
from subprocess import CalledProcessError
from typing import Optional, Tuple

from setuptools import find_packages

from ._version import __version__


class Tags(Enum):
    RELEASE = 1
    RELEASE_BRANCH = 2
    FEATURE_BRANCH = 3
    OTHER = 4


def execute_command(command):
    return subprocess.check_output(command.split()).strip().decode('ascii')


class ScmParser(ABC):

    @property
    @lru_cache()
    def branch(self) -> str:
        return self._branch()

    @property
    @lru_cache()
    def commits(self) -> str:
        return self._commits()

    @property
    @lru_cache()
    def tag(self) -> str:
        return self._tag()

    @staticmethod
    def is_valid_version(v: str) -> bool:
        return v.startswith('master') or v.startswith(
            'unversioned') or v[0].isnumeric()

    @staticmethod
    def is_valid_version_type(t: str) -> bool:
        return t in [vt.name for vt in Tags]

    @staticmethod
    def build_version(branch: str, commits: str, tag: str) -> Tuple[str, str]:
        if branch in ['master', 'HEAD']:
            if tag is None or len(tag.strip()) == 0:
                return Tags.OTHER.name, 'master.dev%s' % commits
            else:
                return Tags.RELEASE.name, tag
        elif branch.startswith('release/'):
            return Tags.RELEASE_BRANCH.name, branch.split('/')[-1] + '.dev%s' % commits
        elif branch.startswith('feature/'):
            return Tags.FEATURE_BRANCH.name, branch.split('/')[-1] + '.feature%s' % commits
        else:
            return Tags.OTHER.name, 'unversioned.dev%s' % commits

    def version(self) -> str:
        return ScmParser.build_version(self.branch, self.commits, self.tag)[1]

    def version_type(self) -> str:
        return ScmParser.build_version(self.branch, self.commits, self.tag)[0]

    @abstractmethod
    def _branch(self) -> str:
        pass

    @abstractmethod
    def _tag(self) -> str:
        pass

    @abstractmethod
    def _commits(self) -> str:
        pass


class GitParser(ScmParser):
    def _branch(self):
        return execute_command('git rev-parse --abbrev-ref HEAD')

    def _commits(self):
        return execute_command('git rev-list --count %s' % self.branch)

    def _tag(self):
        try:
            tag = execute_command('git describe --tags --abbrev=0')
            # check for tag out of the ordinary, i.e.
            # fatal: No names found, cannot describe anything.
            if tag.startswith('fatal:'):
                logging.info('no tags (release branch?): %s' % tag)
                tag = None
        except subprocess.CalledProcessError as _:
            logging.info('cannot describe tag, will use None')
            tag = None
        return tag


PARSERS = dict(
    git=GitParser(),
)


def version(scm: str = 'git') -> str:
    """builds a version number based on information on the scm"""
    if scm not in PARSERS:
        raise ValueError("scm '%s' invalid (options: %s)" %
                         (scm, PARSERS.keys()))
    return PARSERS[scm].version()


def version_type(scm: str = 'git') -> str:
    """finds the version type based on information on the scm"""
    if scm not in PARSERS:
        raise ValueError("scm '%s' invalid (options: %s)" %
                         (scm, PARSERS.keys()))
    return PARSERS[scm].version_type()


def parsers():
    return str(list(PARSERS.keys()))


def tag_version(package: Optional[str], file: Optional[str], scm: str = 'git') -> str:
    """ based on
    https://stackoverflow.com/questions/458550/standard-way-to-embed-version-into-python-package"""
    def detect_package():
        packages = find_packages(exclude=['test*'])
        packages = [p for p in packages if '.' not in p]  # remove sub-packages
        if len(packages) == 0:
            raise ValueError('no default package detected')
        elif len(packages) > 1:
            raise ValueError('multiple packages detected: %s' % str(packages))
        else:
            return packages[0]

    package = package if package is not None else detect_package()
    file = file if file is not None else '_version'
    file_name = '%s.py' % file
    with open('%s/%s' % (package, file_name), 'w') as f:
        f.write('# \n')
        f.write('# automatically generated by setup_scmversion\n')
        f.write('# - do not overwrite\n')
        f.write('# - do not add to source control\n')
        f.write('# \n')
        f.write('__version__ = "%s"\n' % version(scm))
    return 'generated %s/%s' % (package, file_name)


def main(args=sys.argv[1:]):
    commands = {
        'version': lambda _: version(),
        'version-type': lambda _: version_type(),
        'parsers': lambda _: parsers(),
        'tag-version': lambda args: tag_version(args.package, args.file),
    }

    parser = argparse.ArgumentParser(description='Version parser from scm')
    sub_parsers = parser.add_subparsers(required=True, dest='command')

    sub_parsers.add_parser('version',
                           help='displays the version')

    sub_parsers.add_parser('version-type',
                           help=str('displays the version type %s' % [e.name for e in Tags]).replace("'", ''))
    sub_parsers.add_parser('parsers',
                           help='lists all parsers available')

    tag_parser = sub_parsers.add_parser('tag-version',
                                        help='tag the package with the version')
    group = tag_parser.add_mutually_exclusive_group()
    group.add_argument('--auto',
                       help='autodetect package name', action='store_true')
    group.add_argument('package', nargs='?',
                       help='name of the package')
    tag_parser.add_argument('file',
                            help='name of the file',
                            nargs='?',
                            default='_version')
    args = parser.parse_args(args)
    print(commands[args.command](args))


if __name__ == "__main__":
    main(sys.argv[1:])
