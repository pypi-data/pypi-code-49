import functools
from typing import Optional

import nox
import vox.linters
from vox import flaggy, linty


class Statuses:
    """Allow all status types."""

    last: Optional[int] = None

    def __init__(self, values=None):
        self._values = values

    def __contains__(self, item: int) -> bool:
        """Allow all status types, store last."""
        self.last = item
        return self._values is None or item in self._values


class Session:
    _linter: vox.linters.BaseLinter

    def __init__(
        self, linter: vox.linters.BaseLinter, session, messages, notify
    ) -> None:
        self._linter = linter
        self._flags = linter.COMMAND
        self._session = session
        self.messages = messages
        self.notifier = notify

    def install(self):
        dependencies = " ".join(self._linter.DEPENDENCIES)
        if dependencies:
            self._session.install(dependencies)

    def nox_run(self, *args, silent=True, success_codes=None, **kwargs):
        _success_codes = Statuses(success_codes)
        ret = self._session.run(
            *args, **kwargs, silent=silent, success_codes=_success_codes
        )
        return _success_codes.last, ret

    def run(self, command: Optional[flaggy.Flags] = None):
        joint = self._flags + command
        code, output = self.nox_run(*joint)
        if not isinstance(output, str):
            return code, iter([])
        return (
            code,
            self._linter.extract_errors(
                {linty.helpers.Task.NAME: self._linter.NAME}, output,
            ),
        )

    def notify(self, command):
        if not isinstance(command, str):
            command = command.__name__
        return self._session.notify(command)

    def lint(self, command=None):
        self.install()
        code, msgs = self.run(command)
        if self.messages is not None:
            self.messages.extend(msgs)
        if self.notifier is not None:
            self.notify(self.notifier)
        return code


def session(
    *args,
    program: vox.linters.BaseLinter,
    messages=None,
    notify=None,
    reuse_venv=True,
    **kwargs,
):
    if program.PYTHON is not None:
        kwargs.setdefault("python", program.PYTHON)

    def wrapper(fn):
        @nox.session(*args, reuse_venv=reuse_venv, **kwargs)
        @functools.wraps(fn)
        def inner(session):
            return fn(Session(program, session, messages, notify))

        return inner

    return wrapper
