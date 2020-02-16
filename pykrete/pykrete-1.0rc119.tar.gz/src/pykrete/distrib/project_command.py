"""
distutils project-command base
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
from abc import abstractmethod
from distutils.cmd import Command


class ProjectCommand(Command):
    """A custom command base for project commands"""

    more_options = []
    user_options = [('project=', None, 'Project name')] + more_options

    def __init__(self, dist):
        """
        :param dist: distribution
        """
        self._project = None
        super(ProjectCommand, self).__init__(dist)

    def initialize_options(self):
        """Set default values for options"""
        self._project = None

    def finalize_options(self):
        """Post-process received options"""
        assert self._project, 'project name not specified'

    @abstractmethod
    def run(self):
        """Performs the command"""
