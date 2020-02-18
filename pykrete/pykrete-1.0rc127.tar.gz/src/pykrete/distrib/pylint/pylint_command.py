"""
distutils pylint-command base
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
from re import findall
from abc import abstractmethod
from distutils.errors import DistutilsModuleError
from distutils.log import INFO, ERROR, DEBUG
from ..project_command import ProjectCommand
from ...calls import CheckedCall


class PylintCommand(ProjectCommand):
    """A custom command to run static-test on python files"""

    description = 'Run pylint static analysis on a package'

    def run(self):
        self.__use_pylint_to_verify_each(*self._get_target_python_files_and_folders())

    @abstractmethod
    def _get_target_python_files_and_folders(self):
        """
        :return: a list of paths to python code files/folders
        """

    def __use_pylint_to_verify_each(self, *targets):
        failures = []
        for target in targets:
            cmd = self.__pylint_test_target(target)
            if not cmd.success:
                failures.append(target)
            else:
                self.__announce_target_rating(cmd.get_output())
        if failures:
            raise DistutilsModuleError(f'Static analysis failed on {failures}')

    def __announce_target_rating(self, output):
        self.announce('Rating: ' + '<--'.join(findall(r'\d+\.\d+/\d+', output)), INFO)

    def __pylint_test_target(self, target):
        self.announce(f'Static analysis of: {target}', level=INFO)
        cmd = CheckedCall(f'python -m pylint {target}')
        self.announce(cmd.get_output(), DEBUG if cmd.success else ERROR)
        return cmd
