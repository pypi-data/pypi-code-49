from __future__ import annotations

import collections.abc
import copy
import itertools
import shlex
from typing import List, Mapping, Optional, Set

from vox import chain_node


def deep_copy(obj):
    return {key: value.copy() for key, value in obj.items()}


def deep_update(dest, src):
    for key, value in src.items():
        if key not in dest:
            dest[key] = value.copy()
        else:
            dest[key].update(value)


class Null:
    def __repr__(self):
        return "Null"


class Options(chain_node.ChainObject):
    arg_sep: str
    flag_sep: str
    flag_join: str
    commands: Flags
    mapping: dict
    name: Optional[str]
    flag: bool
    order: int

    def format_flag(self, key, arguments):
        if not isinstance(self.name, Null):
            key = self.name
        if key is None or not self.flag:
            return self.arg_sep.join(arguments)
        if not arguments:
            return key
        return key + self.flag_sep + self.flag_join.join(arguments)


class Flags:
    _commands: Mapping[Optional[str], List[str]]
    _options: Options
    _flags: Mapping[str, Options]

    def __init__(
        self,
        commands: Mapping[Optional[str], List[str]],
        options: Options,
        flags: Mapping[str, Options],
    ) -> None:
        self._commands = commands
        self._options = options
        self._flags = flags

    def __add__(self, other):
        ret = self.copy()
        if other is not None:
            for flag, command in other._commands.items():
                if command:
                    ret._commands[flag] = command
            ret._options.update(other._options)
            deep_update(ret._flags, other._flags)
        return ret

    def __repr__(self):
        return f"Flags({self}, {self._options}, {self._flags})"

    def __str__(self):
        return " ".join(
            self._flags.get(flag, self._options).format_flag(flag, arguments)
            for flag, arguments in self._normalized_commands.items()
        ).lstrip()

    def __iter__(self):
        return iter(shlex.split(str(self)))

    def __getitem__(self, key):
        return self._flags[key]

    def get(self, key, default=None):
        return self._flags.get(key, default)

    @property
    def _normalized_commands(self):
        return self._normalize_args(self._commands)

    def _sort_flags(self, item):
        key, _ = item
        options = self._flags.get(key, self._options)
        return options.flag, options.order, (key or "")

    def _normalize_args(self, commands):
        return dict(sorted(commands.items(), key=self._sort_flags))

    def copy(self):
        return Flags(
            self._commands.copy(), self._options.copy(), deep_copy(self._flags)
        )


class _Input:
    def __init__(self, flag=True, hyphen="_"):
        self._flag = self._select_flag(flag)
        self._hyphen = self._select_hyphen(hyphen)

    def __call__(self, flags):
        commands = {}
        for command, values in flags.items():
            if command is not None:
                if not command.startswith("-") and self._flag:
                    command = self._flag(command) + command
                command = command.translate(self._hyphen)
            commands[command] = values
        return commands

    def _select_hyphen(self, hyphen):
        return str.maketrans(hyphen, "-" * len(hyphen))

    def _select_flag(self, flag):
        if flag is False:
            return None
        if flag is True:
            return self._flag_normal
        if flag == "-":
            return self._flag_single
        if flag == "--":
            return self._flag_double
        raise ValueError(f"Invalid flag option {flag}")

    @staticmethod
    def _flag_normal(command):
        return "-" if len(command) == 1 else "--"

    @staticmethod
    def _flag_single(command):
        return "-"

    @staticmethod
    def _flag_double(command):
        return "--"


class Builder:
    __slots__ = ("_options", "_flags")

    _options: Options

    def __init__(self, options, flags=None):
        if not isinstance(options, Options):
            options = Options(None, **options)
        self._options = options
        _flags = {}
        for flag, options in (flags or {}).items():
            if not isinstance(options, Options):
                options = Options(self._options, **options)
            else:
                options = options.copy()
                options.parent = self._options
            _flags[flag] = options
        self._flags = _flags

    def custom(self, flag=True, hyphen="_"):
        changer = _Input(flag, hyphen)

        def inner(*arguments, **flags) -> Flags:
            return self._build(changer(self._normalize_input(arguments, flags)))

        return inner

    def build(self, *arguments, **flags) -> Flags:
        return self.custom()(*arguments, **flags)

    def raw(self, *arguments, **flags) -> Flags:
        return self.custom(flag=False, hyphen="")(*arguments, **flags)

    def sugar(self, *arguments, **flags) -> Flags:
        return self.build(*arguments, **flags)

    # TODO: add a from string option

    def _build(self, commands):
        return self._options.commands(
            commands, self._options.copy(), copy.deepcopy(self._flags),
        )

    @classmethod
    def _normalize_input(cls, arguments, flags):
        flags = {
            None: list(arguments),
            **flags,
        }
        commands = {}
        for command, values in flags.items():
            if command is not None and not isinstance(command, str):
                raise ValueError("All commands must be strings or None")
            if values is None:
                commands[command] = values
                continue

            if isinstance(values, str):
                values = [values]
            elif isinstance(
                values, (collections.abc.Iterable, collections.abc.Iterator)
            ):
                values = list(values)

            has_non_string = any(not isinstance(value, str) for value in values)
            if has_non_string:
                raise ValueError("All values must be strings or iterables of strings.")
            commands[command] = values
        return commands
