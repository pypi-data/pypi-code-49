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

import logging
from subprocess import CalledProcessError

from .. import ScmParser
from ..util import execute_command


class GitParser(ScmParser):
    def _branch(self):
        return execute_command('git rev-parse --abbrev-ref HEAD')

    def _commits(self):
        return execute_command('git rev-list --count %s' % self.branch)

    def _tag(self):
        try:
            return execute_command('git describe --tags --exact-match')
        except CalledProcessError as _:
            return None
