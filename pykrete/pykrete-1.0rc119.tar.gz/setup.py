"""
Pykrete module build script
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
from sys import argv
from os import path
from enum import Enum
from abc import abstractmethod
from re import findall
from subprocess import Popen, PIPE
from distutils.cmd import Command
from distutils.log import INFO, ERROR, DEBUG
from distutils.errors import DistutilsModuleError
from setuptools import setup, find_packages
import pkg_resources


class _CallVector:
    """Parses a command line into a vector of it's arguments, with support for quote marks

    Properties:
    cmd (string): the source command
    """
    def __init__(self, cmd):
        """Initializes this instance to parse the specified command

        :param cmd: the command to be parsed
        """
        self.cmd = cmd
        self.__vector = []
        self.__cur_arg = None
        self.__quote_char = None
        self.__base_switcher = None

    class State(Enum):
        """Parse state enumeration
        """
        BASE = 1
        NORMAL = 2
        QUOTED = 3

    def get_vector(self):
        """Gets the call vector

        :return: A call vector
        """
        if not self.__vector:
            self.__make_vector()
        return self.__vector

    def __make_vector(self):
        """Parsed main function, runs a state machine to go over the command's characters
        """
        switcher = self.__make_state_machines()
        state = _CallVector.State.BASE
        for pos in range(0, len(self.cmd)):
            state = switcher[state](self.cmd[pos])
        if state != _CallVector.State.BASE:
            self.__collect_arg()

    def __make_state_machines(self):
        """Makes the state machines used in the parsing process

        :return: top-level state machine
        """
        self.__base_switcher = {
            ' ': (lambda x: _CallVector.State.BASE),
            '\t': (lambda x: _CallVector.State.BASE),
            '\'': self.__handle_base_quote,
            '"': self.__handle_base_quote
        }
        return {
            _CallVector.State.BASE: self.__handle_base,
            _CallVector.State.NORMAL: self.__handle_normal,
            _CallVector.State.QUOTED: self.__handle_quoted
        }

    def __handle_base(self, char):
        """Handles chars in-between arguments

        :param char: next char
        :return: next state
        """
        if char in self.__base_switcher.keys():
            return self.__base_switcher[char](char)
        self.__cur_arg = [char]
        return _CallVector.State.NORMAL

    def __handle_base_quote(self, char):
        """Handles quote chars
         (first encountered char in ' or " will make other char not count and a quote)

        :param char: next char
        :return: next state
        """
        if not self.__quote_char:
            self.__quote_char = char
            self.__base_switcher.pop('\'' if char == '"' else '"')
        self.__cur_arg = []
        return _CallVector.State.QUOTED

    def __handle_normal(self, char):
        """Handles chars in non-quoted arguments

        :param char: next char
        :return: next state
        """
        if char not in [' ', '\t']:
            self.__cur_arg.append(char)
            return _CallVector.State.NORMAL
        return self.__collect_arg()

    def __handle_quoted(self, char):
        """Handles chars in quoted arguments

        :param char: next char
        :return: next state
        """
        if char == self.__quote_char:
            return self.__collect_arg()
        self.__cur_arg.append(char)
        return _CallVector.State.QUOTED

    def __collect_arg(self):
        """Collects all of the current argument's chars into a string and appends it to the vector

        :return: next state
        """
        self.__vector.append(''.join(self.__cur_arg))
        return _CallVector.State.BASE

    def __str__(self):
        return str(self.__vector)


class CheckedCall:
    """Used to execute shell commands and hold the execution results

    Properties:
    stdout (string): command's standard output
    stderr (string): command's standard error
    success (bool): True if exit-code was 0, False otherwise
    """

    def __init__(self, cmd):
        """Initializes this instance with the specified command

        :param cmd: (string) shell command
        """
        print("Running command: \n> " + cmd)
        self.process = Popen(_CallVector(cmd).get_vector(),
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
        """Gets a string representation of this object

        :return: The call arguments
        """
        return str(self.process.args)

    def _run_and_get_streams(self):
        """Runs the process and gets the streams from the result

        :return (string, string): (stdout, stderr) strings
        """
        return tuple([stream.decode('ascii') for stream in self.process.communicate()])


class ProjectCommand(Command):
    """A custom command base for project commands"""

    more_options = []
    user_options = [('project=', None, 'Project name')] + more_options

    def __init__(self, dist):
        """Initialize this instance with default parameter values

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
        pass


class PylintCommand(ProjectCommand):
    """A custom command to run static-test on python files"""

    description = 'Run pylint static analysis on a package'

    def run(self):
        self.__pylint_call(*self._collect_target())

    @abstractmethod
    def _collect_target(self):
        pass

    def __pylint_call(self, *targets):
        failures = []
        for target in targets:
            self.announce(f'Static analysis of: {target}', level=INFO)
            cmd = CheckedCall(f'python -m pylint {target}')
            out = cmd.get_output()
            self.announce(out, DEBUG if cmd.success else ERROR)
            if not cmd.success:
                failures.append(target)
            else:
                self.announce('Rating: ' + '<--'.join(findall(r'\d+\.\d+/\d+', out)), INFO)
        if failures:
            raise DistutilsModuleError(f'Static analysis failed on {failures}')


class PylintProjectTestCommand(PylintCommand):
    """A custom command to run static-test on all python files in a package"""

    def _collect_target(self):
        return [path.join('src', self.project)]


class PylintSelfTestCommand(PylintCommand):
    """A custom command to run static-test on setup.py"""

    def _collect_target(self):
        return [argv[0], 'build.py']


class TwineCommand(ProjectCommand):
    """A custom command to upload the package to pypi"""

    description = 'Upload the project to pypi'
    more_options = [('index=', None, 'Index server (optional, default to pipy)'),
                    ('config=', None, 'pypirc location (optional, default to local file)')]

    def __init__(self, dist):
        """Initialize this instance with default parameter values

        :param dist: distribution
        """
        self.package = None
        self.project = None
        self.index = None
        self.config = None
        super(TwineCommand, self).__init__(dist)

    def initialize_options(self):
        """Set default values for options"""
        self.project = None
        self.index = 'pypi'
        self.config = 'pypirc'

    def finalize_options(self):
        """Post-process received options"""
        self.package = path.join('dist', f'{self.project}-{Package(self.project).version}.tar.gz')

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
        cmd = CheckedCall(f'python -m twine {command} --config-file {self.config}'
                          f' -r {self.index} {self.package}')
        if not cmd.success:
            self.announce(cmd.get_output(), ERROR)
            raise DistutilsModuleError(f'Twine {command} failed.')


class Package:
    """Python package

    :property project: The project's name
    :property version: The project's version
    """

    def __init__(self, project):
        """Initializes this instance to analyze the specified project

        :param project: The project's name
        """
        self._version_file = path.join('src', project, 'version.py')
        self.project = project
        self.version = self._get_version()

    @staticmethod
    def get_long_description():
        """Gets the contents of the README.md file

        :return: Long description
        """
        with open('README.md', 'r') as readme:
            return readme.read()

    def _get_version(self):
        """Gets the package version

        :return: The version
        :exception IndexError: Version not found
        """
        try:
            return self._get_version_from_file()
        except IOError:
            return pkg_resources.require(self.project)[0].version

    def _get_version_from_file(self):
        """Gets the version from the version file

        :return: The version
        :exception IOError: Version file doesn't exist
        :exception IndexError: Version not found in file
        """
        with open(self._version_file, 'r') as file:
            return findall("__version__ = '([^']*)'", file.read())[0]

    def __str__(self):
        """Gets a string representation of this object

        :return: a string
        """
        return f'{self.project} v{self.version}'


PACKAGE = Package('pykrete')
print(f'Handling pip package: {PACKAGE}')
setup(
    name='pykrete',
    version=PACKAGE.version,
    license='MIT',
    author='Shai A. Bennathan',
    author_email='shai.bennathan@intel.com',
    description='Build script foundation',
    long_description=PACKAGE.get_long_description(),
    long_description_content_type='text/markdown',
    url='http://ait-tool-center.iil.intel.com/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    test_suite='nose.collector',
    tests_require=['nose'],
    cmdclass={
        'pylint_self': PylintSelfTestCommand,
        'pylint': PylintProjectTestCommand,
        'twine': TwineCommand
    }
    # install_requires=[],
)
