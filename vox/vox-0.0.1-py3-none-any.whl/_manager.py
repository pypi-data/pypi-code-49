import functools

import nox
import vox.linters

from ._flags import FlagsBuilder
from ._session import Session, session


class Manager:
    def __init__(self, files=None, flags=None):
        if flags is None:
            flags = FlagsBuilder().sugar()
        if files is not None:
            flags += FlagsBuilder().sugar(files=files)
        self._flags = flags
        self.messages = []
        self.display_fn = None

    def session(self, *args, program, **kwargs):
        def wrapper(fn):
            @session(*args, program=program, messages=self.messages, **kwargs)
            @functools.wraps(fn)
            def inner(session: Session):
                session._flags += self._flags
                session.notifier = self.display_fn
                return fn(session)

            return inner

        return wrapper

    def display(self, mutations=None, *, clear=True):
        def wrapper(fn):
            @nox.session
            @functools.wraps(fn)
            def inner(session):
                for mutation in mutations:
                    self.messages = mutation(self.messages)
                self.messages = list(self.messages)
                fn(self.messages)
                if self.messages:
                    session.error("There are errors to be fixed")
                if clear:
                    self.messages.clear()

            self.display_fn = inner
            return inner

        return wrapper

    def lint(self, linter: vox.linters.BaseLinter, command=None):
        def inner(session: vox.Session):
            session.lint(command=command)

        inner.__name__ = linter.NAME
        self.session(program=linter)(inner)
