import os
import pwd
import shlex
import signal
import subprocess
from typing import List, Mapping, Union, Optional, Type

from ._inspection_result import *
from ._errors import *


class CompletedProcess:
    """
    Class representing a completed process, and providing access to its arguments, its output, and its return code
    """

    def __init__(self, completed_subprocess: subprocess.CompletedProcess):
        self.args: Union[str, List[str]] = completed_subprocess.args
        self.raw_stdout: bytes = completed_subprocess.stdout
        self.raw_stderr: bytes = completed_subprocess.stderr
        self._stdout: Optional[str] = None
        self._stderr: Optional[str] = None
        self.return_code: int = completed_subprocess.returncode

    def __bool__(self):
        return self.return_code == 0

    def __repr__(self):
        return f"CompletedProcess(\n" + \
               ",\n".join(f"    {name}={value!r}" for name, value in self.__dict__.items()) + \
               "\n)"

    @staticmethod
    def _decode_output(raw_output: bytes, encoding: str = "utf-8"):
        if raw_output is not None:
            return raw_output.decode(encoding)
        return None

    def check_decode(self, message: str, *, error_kind: Type = KOError, encoding: str = "utf-8"):
        """
        Check whether the output of the process can be decoded according to a given encoding

        :param message:         message in case of failure to explain the reason of said failure
        :param error_kind:      exception to raise if the check failed
        :param encoding:        encoding to use to decode the data
        """
        try:
            self._stdout = self._decode_output(self.raw_stdout, encoding)
        except UnicodeDecodeError as e:
            raise error_kind(f"{message}: {str(e)} (while decoding stdout)")
        try:
            self._stderr = self._decode_output(self.raw_stderr, encoding)
        except UnicodeDecodeError as e:
            raise error_kind(f"{message}: {str(e)} (while decoding stderr)")
        return self

    @property
    def stdout(self) -> str:
        if self._stdout is None:
            self._stdout = self._decode_output(self.raw_stdout)
        return self._stdout

    @property
    def stderr(self) -> str:
        if self._stderr is None:
            self._stderr = self._decode_output(self.raw_stderr)
        return self._stderr

    def _return_code_message(self) -> str:
        if self.return_code >= 0:
            return str(self.return_code)
        try:
            name = signal.Signals(-self.return_code).name
            return f"{128 + -self.return_code} ({name})"
        except ValueError:
            return str(self.return_code)

    def _get_fail_message(self, stdout: bool, stderr: bool, exit_code: bool) -> str:
        message = ""
        if exit_code:
            message += f"\nexit code: {self._return_code_message()}"
        if stdout:
            if self.raw_stdout is not None:
                try:
                    message += "\nstdout:\n" + self.stdout
                except UnicodeDecodeError:
                    message += "\nstdout (raw bytes):\n" + repr(self.raw_stdout)
            else:
                message += "\nstdout is empty"
        if stderr:
            if self.raw_stderr is not None:
                try:
                    message += "\nstderr:\n" + self.stderr
                except UnicodeDecodeError:
                    message += "\nstderr (raw bytes):\n" + repr(self.raw_stderr)
            else:
                message += "\nstderr is empty"
        return message

    def check(
            self,
            message: str,
            error_kind: Type = KOError,
            allowed_status: Union[int, List[int]] = 0,
            stdout: bool = True,
            stderr: bool = True,
            exit_code: bool = True
    ):
        """
        Check whether the execution of the process failed

        :param message:         message in case of failure to explain the reason of said failure
        :param allowed_status:  status or list of statuses that are considered successful
        :param error_kind:      exception to raise if the check failed
        :param stdout:          if True add the output of the process as a detail for the exception
        :param stderr:          if True add the error output of the process to the exception message
        :param exit_code:       if True add the exit_code of the process to the exception message
        """
        if isinstance(allowed_status, int):
            allowed_status = [allowed_status]
        if self.return_code not in allowed_status:
            message += self._get_fail_message(stdout, stderr, exit_code)
            raise error_kind(message)
        return self

    def expect(
            self,
            message: str,
            allowed_status: Union[int, List[int]] = 0,
            nb_points: int = 1,
            stdout: bool = True,
            stderr: bool = True,
            exit_code: bool = True
    ):
        """
        Check whether the execution of the process failed

        :param message:         message in case of failure to explain the reason of said failure
        :param allowed_status:  status or list of statuses that are considered successful
        :param nb_points:       the number of points granted by the expectation if it passes
        :param stdout:          if True add the output of the process as a detail for the exception
        :param stderr:          if True add the error output of the process to the exception message
        :param exit_code:       if True add the exit_code of the process to the exception message
        """
        if isinstance(allowed_status, int):
            allowed_status = [allowed_status]
        if self.return_code not in allowed_status:
            message += self._get_fail_message(stdout, stderr, exit_code)
        get_inspection_result()["requirements"].append((self.return_code in allowed_status, message, nb_points))
        return self


def _switch_to_user(username: str):
    info = pwd.getpwnam(username)
    os.setgid(info.pw_gid)
    os.setuid(info.pw_uid)


def _subprocess_run_wrapper(*args, **kwargs) -> CompletedProcess:
    """
    Run a subprocess

    This is a wrapper for subprocess.run() and all the arguments are forwarded to it
    See the documentation of subprocess.run() for the list of all the possible arguments
    :raise quixote.inspection.TimeoutError: if the timeout argument is not None and expires before the child process terminates
    """
    try:
        return CompletedProcess(subprocess.run(*args, **kwargs))
    except subprocess.TimeoutExpired as e:
        raise TimeoutError(e)


def _run(*args, as_user: str = None, **kwargs):
    if as_user is not None:
        kwargs["preexec_fn"] = lambda: _switch_to_user(as_user)
    return _subprocess_run_wrapper(*args, **kwargs)


def _run_with_new_session(
        cmd: str, timeout: int = None,
        force_kill_on_timout: bool = False,
        env: Mapping[str, str] = None,
        as_user: str = None,
):
    extra_args = {}
    if as_user is not None:
        extra_args["preexec_fn"] = lambda: _switch_to_user(as_user)
    proc = subprocess.Popen(
        ["bash", "-c", cmd],
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
        start_new_session=True,
        env=env,
        **extra_args,
    )
    try:
        out, err = proc.communicate(timeout=timeout)
        return CompletedProcess(subprocess.CompletedProcess(proc.args, proc.returncode, out, err))
    except subprocess.TimeoutExpired as e:
        os.killpg(proc.pid, signal.SIGTERM)
        if force_kill_on_timout:
            os.killpg(proc.pid, signal.SIGKILL)  # Kill again, harder (in case some processes don't exit gracefully)
        proc.communicate()
        raise TimeoutError(e)


def command(
        cmd: Union[str, List[str]],
        timeout: int = None,
        env: Mapping[str, str] = None,
        as_user: str = None,
) -> CompletedProcess:
    """
    Run a single executable. It is not run in a shell.

    :param cmd:         command to be executed
    :param timeout:     the timeout in seconds. If it expires, the child process will be killed and waited for. Then TimeoutExpired exception will be raised after the child process has terminated.
    :param env:         the environment to use when running the command
    :param as_user:     the user as which the command should be executed
    :raise quixote.inspection.TimeoutError: if timeout is not None and expires before the child process terminates
    """
    if isinstance(cmd, str):
        cmd = shlex.split(cmd)
    return _run(cmd, capture_output=True, shell=False, timeout=timeout, env=env, as_user=as_user)


def bash(
        cmd: str,
        timeout: int = None,
        force_kill_on_timeout: bool = False,
        env: Mapping[str, str] = None,
        as_user: str = None,
) -> CompletedProcess:
    """
    Run one or a sequence of commands using the Bash shell.

    :param cmd:                     commands to be executed
    :param timeout:                 the timeout in seconds. If it expires, the child process will be killed and waited for. Then TimeoutExpired exception will be raised after the child process has terminated.
    :param force_kill_on_timeout:   whether processes should be terminated or killed
    :param env:                     the environment to use when running the command
    :param as_user:                 the user as which the commands should be executed
    :raise quixote.inspection.TimeoutError: if timeout is not None and expires before the child process terminates
    """
    if timeout is not None:
        return _run_with_new_session(cmd, timeout, force_kill_on_timout=force_kill_on_timeout, env=env, as_user=as_user)
    else:
        return _run(["bash", "-c", cmd], capture_output=True, shell=False, env=env, as_user=as_user)


def java(
        class_name: str,
        args: List[str] = [],
        timeout: int = None,
        options: List[str] = None,
        env: Mapping[str, str] = None,
) -> CompletedProcess:
    """
    Launch a java class

    :param class_name:                  path of the Java class file to launch
    :param args:                        list of arguments to pass to the launched class
    :param timeout:                     time to wait before terminating the process
    :param options:                     list of shell options to be passed to java (see java man page for more info)
    :param env:                         environment to run the java command (by default use the current shell environment)
  
    :raise quixote.inspection.TimeoutError: if timeout is not None and expires before the child process terminates
    """
    options = options or []
    cmd = "java"
    return _run([cmd, *options, class_name, *args], capture_output=True, timeout=timeout, env=env)


def javajar(
        jar_path: str,
        args: List[str] = [],
        timeout: int = None,
        options: List[str] = None,
        env: Mapping[str, str] = None
) -> CompletedProcess:
    """
    Launch a java archive

    :param jar_path:            path of the Java archive to launch
    :param args:                list of arguments to pass to the launched archive
    :param timeout:             time to wait before terminating the process
    :param options:             list of shell options to be passed to java (see java man page for more info)
    :param env:                 environment to run the java command (by default use the current shell environnment)

    :raise quixote.inspection.TimeoutError: if timeout is not None and expires before the child process terminates
    """
    options = options or []
    cmd = "java"
    return _run([cmd, *options, "-jar", jar_path, *args], capture_output=True, timeout=timeout, env=env)
