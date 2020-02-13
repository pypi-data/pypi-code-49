#  
#      setup_headers - Sets a standard header in all source files
#  
#      Copyright (C) 2019 Jorge M. Faleiro Jr.
#  
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU Affero General Public License as published
#      by the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#  
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU Affero General Public License for more details.
#  
#      You should have received a copy of the GNU Affero General Public License
#      along with this program.  If not, see <http://www.gnu.org/licenses/>.
#  
from setuptools import Command
import glob
import os
import logging
from ._version import __version__


def process_lines(header_lines, lines, comment_prefix):
    result = []
    phases = ('adding_hashbangs',
              'removing_previous_comments',
              'adding_header',
              'adding_source')
    phase = phases[0]
    for line in lines:
        line = line.strip('\n')
        assert phase in phases, '%s not in %s' % (phase, phases)
        if phase == phases[0]:
            if line.startswith('#!'):
                result.append(line)
            else:
                phase = phases[1]
        if phase == phases[1]:
            if line.startswith(comment_prefix[0]):
                pass
            else:
                phase = phases[2]
        if phase == phases[2]:
            result.extend([comment_prefix + l.strip('\n')
                           for l in header_lines])
            phase = phases[3]
        if phase == phases[3]:
            result.append(line)
    return result


class LicenseHeaderCommand(Command):
    """
    adds a standard copyright header to all source files
    """
    description = __doc__.strip()
    user_options = [
        ('header-file=', 'f', 'header license file'),
        ('extensions=', 'e', 'source file extensions'),
        ('comment-prefix=', 'c', 'comment line prefix'),
        ('dry-run=', 'd', 'dry run'),
    ]

    def initialize_options(self):
        self.header_file = 'HEADER'
        self.extensions = 'py, cfg'
        self.comment_prefix = '# '

    def finalize_options(self):
        assert self.header_file is not None, 'header_file is required'
        assert self.extensions is not None, 'extension is required'
        assert self.comment_prefix is not None, 'comment line prefix is required'

    def run(self):
        if not os.path.isfile(self.header_file):
            raise Exception("header file '%s' is not a file" %
                            self.header_file)
        with open(self.header_file) as header:
            header_lines = header.readlines()
        for extension in self.extensions.split(','):
            extension = extension.strip()
            for filename in glob.iglob("**/*%s" % extension, recursive=True):
                logging.debug(filename)
                with open(filename, 'r') as file:
                    lines = file.readlines()
                output = process_lines(
                    header_lines, lines, self.comment_prefix)
                with open(filename, 'w') as file:
                    for line in output:
                        file.write(line + '\n')
