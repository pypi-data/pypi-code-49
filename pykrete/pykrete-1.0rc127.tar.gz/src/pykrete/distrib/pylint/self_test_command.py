"""
distutils pylint project-test command
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
from sys import argv
from .pylint_command import PylintCommand


class SelfTestCommand(PylintCommand):
    """A custom command to run static-test on setup.py"""

    def finalize_options(self):
        """Post-process received options"""
        assert 'bypass', 'project name not specified'

    def _get_target_python_files_and_folders(self):
        """provide called script and built.py as targets

        :return: Called script and build.py
        """
        return [argv[0], 'build.py']
