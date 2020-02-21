import os
import shlex
import shutil
import sys
from subprocess import (
    PIPE,
    Popen,
)
from threading import Thread
from typing import (
    ClassVar,
    Generator,
    List,
    Optional,
    TextIO,
    Tuple,
    Type,
    Union,
    cast,
)

from setuptools import Command

from .cfg import SetupCfgCommandConfig


def _reader(
        stream: TextIO,
        output: TextIO,
) -> None:
    while True:
        line = stream.readline()
        if not line:
            break
        output.write(line)


def _execute(
        command: Tuple[str, ...],
        out: Optional[TextIO] = None,
        err: Optional[TextIO] = None
) -> int:
    if out is None:
        out = sys.stdout
    if err is None:
        err = sys.stderr
    out = cast(TextIO, out)
    err = cast(TextIO, err)
    process = Popen(
        command,
        bufsize=-1,
        stdout=PIPE,
        stderr=PIPE,
        universal_newlines=True
    )
    thd1 = Thread(
        target=_reader,
        args=(process.stdout, out)
    )
    thd1.start()
    thd2 = Thread(
        target=_reader,
        args=(process.stderr, err)
    )
    thd2.start()
    process.wait()
    thd1.join()
    thd2.join()
    return process.returncode


def _get_path(cmd: str) -> str:
    if cmd.startswith(os.path.sep):
        if os.path.isfile(cmd) is True:
            out = cmd
        else:
            raise FileNotFoundError('Unable to find the file: %r' % cmd)
    else:
        out = ''
        path = shutil.which(cmd)
        if path is not None:
            out = str(path)

    if out:
        if os.access(out, os.X_OK) is False:
            raise PermissionError(
                'You do not have execute permission to run the file: %r'
                % out
            )
        return out
    raise FileNotFoundError(
        'Unable to find the file path for the command: %r'
        % cmd
    )


def _each_command(
        commands: Union[List[str], Tuple[str, ...]]
) -> Generator[Tuple[str, ...], None, None]:
    for command in commands:
        command = command.strip()
        hold = []
        for x, part in enumerate(shlex.split(command)):
            if x == 0:
                hold.append(_get_path(part))
            else:
                hold.append(part)
        if hold:
            yield tuple(hold)


_DIVIDER = '\n\n{:-<79}\n'.format('')


def _show_command(
        command: Tuple[str, ...],
        out: TextIO
) -> None:
    out.write(_DIVIDER)
    for x, part in enumerate(command):
        if x == 0:
            out.write('{}\n'.format(part))
        else:
            out.write('  {}\n'.format(part))
    out.write('\n\n')


# pylint: disable=W0613
# noinspection PyUnusedLocal
def _initialize_options(self) -> None:
    pass


# noinspection PyUnusedLocal
def _finalize_options(self) -> None:
    pass


def _run(self) -> None:
    out: TextIO = sys.stdout
    err: TextIO = sys.stderr
    for command in _each_command(self.commands):
        _show_command(command, out)
        val = _execute(command, out=out, err=err)
        if val != 0:
            sys.exit(val)
            return
    sys.exit(0)


_type = type  # Allows for easy mocking of type.


def build_setup_cfg_command_class(
        setup_command_cfg: SetupCfgCommandConfig
) -> Type[Command]:
    setup_klass = _type(
        'SetupCfgCommand',
        (object,),
        {
            '__annotations__': {
                'name': ClassVar[str],
                'root_path': ClassVar[str],
                'description': ClassVar[str],
                'user_options': ClassVar[List[str]],
                'commands': ClassVar[Tuple[str, ...]],
            },
            '__module__': __name__,
            '__doc__': None,
            'name': setup_command_cfg.name,
            'root_path': '',
            'description': setup_command_cfg.description,
            'user_options': [],
            'commands': setup_command_cfg.commands,
            'initialize_options': _initialize_options,
            'finalize_options': _finalize_options,
            'run': _run,
        }
    )
    klass_name = '%sCommand' % setup_command_cfg.camel
    klass = _type(klass_name, (setup_klass, Command), {})
    return klass
