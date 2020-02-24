"""
distutils pylint-command base
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
from os import path
from distutils.log import ERROR
from distutils.errors import DistutilsModuleError
from .project_command import ProjectCommand
from ..calls import CheckedCall
from ..packages import PythonPackage


class TwineCommand(ProjectCommand):
    """A custom command to upload the package to pypi"""

    description = 'Upload the project to pypi'
    user_options = [ProjectCommand._project_option,
                    ('index=', None, 'Index server (optional, defaults to pipy)'),
                    ('config=', None, 'pypirc location (optional, defaults to local file)')]

    def __init__(self, dist):
        """
        :param dist: distribution
        """
        self.__package = None
        self.index = None
        self.config = None
        super(TwineCommand, self).__init__(dist)

    def initialize_options(self):
        """Set default values for options"""
        self.index = 'pypi'
        self.config = 'pypirc'

    def finalize_options(self):
        """Post-process received options"""
        self.__package = path.join(
            'dist',
            f'{self.project}-{PythonPackage(self.project).version}.tar.gz')

    def run(self):
        """Register and upload the package

        :exception OSError: upload failed
        """
        self._twine('upload')

    def _twine(self, command):
        """Run a twine command

        :param command: A twine command
        :exception OSError: command failed
        """
        cmd = CheckedCall(['twine', command, '--config-file', self.config,
                           '-r', self.index, self.__package])
        if not cmd.success:
            self.announce(cmd.get_output(), ERROR)
            raise DistutilsModuleError(f'Twine {command} failed.')
