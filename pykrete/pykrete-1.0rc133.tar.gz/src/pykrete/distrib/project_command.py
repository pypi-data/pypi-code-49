"""
distutils project-command base
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
from abc import abstractmethod
from distutils.cmd import Command


class ProjectCommand(Command):
    """A custom command base for project commands"""

    _project_option = ('project=', None, 'Project name')
    user_options = [_project_option]

    def __init__(self, dist):
        """
        :param dist: distribution
        """
        self.project = None
        super(ProjectCommand, self).__init__(dist)

    def initialize_options(self):
        """Set default values for options"""
        self.project = None

    def finalize_options(self):
        """Post-process received options"""
        assert self.project, 'project name not specified'

    @abstractmethod
    def run(self):
        """Performs the command"""
