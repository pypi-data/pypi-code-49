from typing import List, Mapping
from functools import reduce
import operator
from glob import glob
import re

from .exec import CompletedProcess, command

_glob_magic_check = re.compile('([*?[])')


def _has_glob_magic_chars(s: str) -> bool:
    return _glob_magic_check.search(s) is not None


def _glob_if_magic(path: str) -> List[str]:
    return glob(path) if _has_glob_magic_chars(path) else [path]


def gcc(
        *src: str,
        version=None,
        output_file: str = None,
        options: List[str] = None,
        env: Mapping[str, str] = None
) -> CompletedProcess:
    """
    Compile a C program

    :param src:                 path or list of paths of file(s) to be compiled
    :param version:             version of gcc to use (only major version)
    :param output_file:         path to the output file
    :param options:             list of shell options to be passed to gcc (see man page for gcc for more info)
    :param env:                 environment to run the gcc command with (by default use the current shell environment)
    """
    src = list(map(_glob_if_magic, src))
    if not src:
        raise ValueError("no sources files provided")
    src = reduce(operator.concat, src)
    cmd = "gcc"
    output_file_option = ["-o", output_file] if output_file else []
    options = options or []
    if version:
        cmd += "-" + str(version)
    return command([cmd, *output_file_option, *src, *options], env=env)


def gpp(
        *src: str,
        version=None,
        output_file: str = None,
        options: List[str] = None,
        env: Mapping[str, str] = None
) -> CompletedProcess:
    """
    Compile a C++ program

    :param src:                 path or list of paths of file(s) to be compiled
    :param version:             version of g++ to use (only major version)
    :param output_file:         path to the output file
    :param options:             list of shell options to be passed to g++ (see man page for g++ for more info)
    :param env:                 environment to run the g++ command with (by default use the current shell environment)
    """
    src = list(map(_glob_if_magic, src))
    if not src:
        raise ValueError("no sources files provided")
    src = reduce(operator.concat, src)
    cmd = "g++"
    output_file_option = ["-o", output_file] if output_file else []
    options = options or []
    if version:
        cmd += "-" + str(version)
    return command([cmd, *output_file_option, *options, *src], env=env)


def javac(*source_files: str, options: List[str] = None, env: Mapping[str, str] = None) -> CompletedProcess:
    """
    Compile java classes

    :param source_files:        path or list of paths of sourcesfile(s) to be compiled
    :param options:             list of shell option to be passed to javac (see javac man page for more info)
    :param env:                 environment to run the javac command with (by default use the current shell environment)
    """
    source_files = list(map(_glob_if_magic, source_files))
    if not source_files:
        raise ValueError("no sources files provided")
    source_files = reduce(operator.concat, source_files)
    options = options or []
    cmd = "javac"
    return command([cmd, *source_files, *options], env=env)


def javac_annotate(
        *class_files: str,
        options: List[str] = None,
        env: Mapping[str, str] = None
) -> CompletedProcess:
    """
    Compile java classes

    :param class_files:         path or list of paths of class_file(s) to be processed for annotations
    :param options:             list of shell option to be passed to javac (see javac man page for more info)
    :param env:                 environment to run the javac command with (by default use the current shell environment)
    """
    class_files = list(map(_glob_if_magic, class_files))
    if not class_files:
        raise ValueError("no sources files provided")
    class_files = reduce(operator.concat, class_files)
    options = options or []
    cmd = "javac"
    return command([cmd, *options, *class_files], env=env)


def make(
        *targets: str,
        directory: str = '.',
        makefile: str = None,
        dry_run: bool = False,
        jobs: int = None,
        keep_going: bool = False,
        ignore_errors: bool = False,
        question_mode: bool = False,
        touch_only: bool = False,
        environment_overrides: bool = False,
        with_builtin_rules: bool = True,
        with_builtin_variables: bool = True,
        env: Mapping[str, str] = None
) -> CompletedProcess:
    """
    Use the make(1) command to run build scripts

    :param targets:                 the names of the targets to build
    :param directory:               the directory to use as working directory before running make (see make -C)
    :param makefile:                the name of the file to use as Makefile (default is "Makefile", see make -f)
    :param dry_run:                 whether make should only print the commands instead of running them (default is False, see make -n)
    :param jobs:                    the number of jobs make can run simultaneously (default is 1, see make -j)
    :param keep_going:              whether make should keep going as much as possible after an error (default is False, see make -k)
    :param ignore_errors:           whether make should ignore failing commands (default is False, see make -i)
    :param question_mode:           whether make should only run in question mode (default is False, see make -q)
    :param touch_only:              whether make should only touch target files instead of running their commands (default is False, see make -t)
    :param environment_overrides:   whether environment variables should override those defined in the Makefiles (default is False, see make -e)
    :param with_builtin_rules:      whether make should enable built-in implicit rules (default is True, see make -r)
    :param with_builtin_variables:  whether make should enable built-in variables (default is True, see make -R)
    :param env:                     the environment to run the make command with (by default use the current shell environment)
    """
    targets = targets or []
    options = []
    if directory != '.':
        options += '-C', directory
    if makefile is not None:
        options += '-f', makefile
    if dry_run is True:
        options += '--dry-run',
    if jobs is not None:
        options += '-j', str(jobs)
    if keep_going is True:
        options += '-k',
    if ignore_errors is True:
        options += '-i',
    if question_mode is True:
        options += '-q',
    if touch_only is True:
        options += '-t',
    if environment_overrides is True:
        options += '--environment-overrides',
    if with_builtin_rules is False:
        options += '--no-builtin-rules',
    if with_builtin_variables is False:
        options += '--no-builtin-variables',
    return command(['make', *options, *targets], env=env)
