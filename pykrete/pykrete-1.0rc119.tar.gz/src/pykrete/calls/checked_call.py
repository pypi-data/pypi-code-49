"""
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
from subprocess import Popen, PIPE

from ._parse_command_into_call_vector import parse_command_into_call_vector


class CheckedCall:
    """Used to execute shell commands and hold the execution results

    Properties:
    stdout (string): command's standard output
    stderr (string): command's standard error
    success (bool): True if exit-code was 0, False otherwise
    """

    def __init__(self, cmd):
        """Initializes this instance with the specified command

        :param cmd: (string/list) shell command
        """
        print(f'Running command: \n> {cmd}')
        command_vector = self.__get_vector_from_command(cmd)
        self.process = Popen(command_vector,
                             shell=True,
                             stdout=PIPE,
                             stderr=PIPE)
        (self.stdout, self.stderr) = self._run_and_get_streams()
        self.success = self.process.returncode == 0

    def get_output(self):
        """Gets the command's output

        :return: stdout + stderr
        """
        return f'{self.stdout}\n{self.stderr}'

    def __str__(self):
        return f'{self.process.args}\n{self.get_output()}'

    def _run_and_get_streams(self):
        """
        :return (string, string): (stdout, stderr) strings
        """
        return tuple([stream.decode('ascii') for stream in self.process.communicate()])

    @staticmethod
    def __get_vector_from_command(cmd):
        return cmd if isinstance(cmd, list) else parse_command_into_call_vector(str(cmd))
