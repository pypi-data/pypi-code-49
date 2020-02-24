"""
distutils pylint project-test command
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
from os import path
from .pylint_command import PylintCommand


class ProjectTestCommand(PylintCommand):
    """A custom command to run static-test on all python files in a package"""

    def _get_target_python_files_and_folders(self):
        """:return: The project's directory
        """
        return [path.join('src', self.project)]
