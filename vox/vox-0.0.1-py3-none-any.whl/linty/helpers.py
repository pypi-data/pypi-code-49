"""Conversion helpers."""
# nosa: pylint[:Unused argument 'task']
from __future__ import annotations

import dataclasses
import logging
import os
import re
import string
from typing import (
    Any,
    Callable,
    Dict,
    Generic,
    Iterator,
    List,
    Mapping,
    Optional,
    Sequence,
    Tuple,
    TypeVar,
    Union,
)

import parse  # nosa: (mypy)
from typing_extensions import Protocol  # nosa: pylint[E0401]

# nosa: pylint[:Module 'parse' has no]


"""Core objects."""
# nosa: E501,pylint[:Line too long]

__all__ = [
    "TTask",
    "Task",
    "Format",
    "Message",
    "MessageKeys",
    "create_internal",
    "regex_line_match",
    "chain",
    "extract_files",
    "extract_lines",
    "format_matches",
    "Converter",
]


TTask = Dict[str, Any]

# nosa(4): pylint[C0103]
logger = logging.getLogger(__name__)
T = TypeVar("T")
TIn = TypeVar("TIn", contravariant=True)
TOut = TypeVar("TOut", covariant=True)


class Task:
    """Task names."""

    NAME = "name"
    EXTENDS = "extends"
    DEPS = "deps"
    CONFIG_PATH = "config_path"
    CONVERTER = "converter"
    PYTHON = "python"
    COMMAND = "command"


class Less:
    """Object that is always less than anything."""

    def __str__(self):
        return "None"  # For when output doesn't convert from Less.

    # nosa: pylint[C0123]
    def __lt__(self, other: Any) -> bool:
        """Less than anything."""
        return True

    def __le__(self, other: Any) -> bool:
        """Less than or equal to anything."""
        return True

    def __eq__(self, other: Any) -> bool:
        """Equal to itself."""
        return type(other) is Less

    def __ne__(self, other: Any) -> bool:
        """Not equal to anything but Less."""
        return type(other) is not Less

    def __gt__(self, other: Any) -> bool:
        """Greater than nothing."""
        return False

    def __ge__(self, other: Any) -> bool:
        """Greater than nothing, equal to self."""
        return type(other) is Less

    def __hash__(self) -> int:
        """Hashable."""
        return 1355

    @classmethod
    def default(cls, obj: Union[Less, T], default: T) -> T:
        """Change Less item to default."""
        if isinstance(obj, Less):
            return default
        return obj


LESS = Less()


class MessageKeys:
    """Message names."""

    APP = "app"
    PATH = "path"
    LINE = "line"
    CHAR = "char"
    CODE = "code"
    CODE_READABLE = "code_readable"
    MESSAGE = "msg"
    EXTENDS = "extends"
    EXTRAS = "extras"


def _default(value, obj, default):
    return value if value is not obj else default


@dataclasses.dataclass
class Message:
    """Message object."""

    app: str
    path: Union[str, Less]
    line: Union[int, Less]
    char: Union[int, Less]
    code: Union[str, Less]
    code_readable: Union[str, Less]
    message: Union[str, Less]
    extends: List[str]
    extras: List[Dict[str, Any]]

    @classmethod
    def from_dict(cls, obj):
        """Build message from dictionary."""
        return cls(
            app=obj[MessageKeys.APP],
            path=_default(obj.get(MessageKeys.PATH), None, LESS),
            line=_default(obj.get(MessageKeys.LINE), None, LESS),
            char=_default(obj.get(MessageKeys.CHAR), None, LESS),
            code=_default(obj.get(MessageKeys.CODE), None, LESS),
            code_readable=_default(obj.get(MessageKeys.CODE_READABLE), None, LESS),
            message=_default(obj.get(MessageKeys.MESSAGE), None, LESS),
            extends=obj.get(MessageKeys.EXTENDS) or [],
            extras=obj.get(MessageKeys.EXTRAS) or [],
        )

    def to_dict(self):
        """Convert message to dictionary."""
        return {
            MessageKeys.APP: self.app,
            MessageKeys.PATH: _default(self.path, LESS, None),
            MessageKeys.LINE: _default(self.line, LESS, None),
            MessageKeys.CHAR: _default(self.char, LESS, None),
            MessageKeys.CODE: _default(self.code, LESS, None),
            MessageKeys.CODE_READABLE: _default(self.code_readable, LESS, None),
            MessageKeys.MESSAGE: _default(self.message, LESS, None),
            MessageKeys.EXTENDS: self.extends,
            MessageKeys.EXTRAS: self.extras,
        }


class Format:
    """Lazy formatting object."""

    def __init__(self, format_: str, *args: Any, **kwargs: Any) -> None:
        """Initialize object."""
        self.format = format_
        self.args = args
        self.kwargs = kwargs

    def __str__(self) -> str:
        """Build string."""
        return self.format.format(*self.args, **self.kwargs)


class Converter(Protocol, Generic[TIn, TOut]):
    """Converter interface."""

    def __call__(self, task: TTask, output: TIn) -> TOut:
        """Convert task and output to TOut."""


def cast(value: Any, type_: Callable[[Any], T], default: Any = None,) -> Optional[T]:
    """Cast value defaulting to default on TypeError."""
    try:
        return type_(value)
    except TypeError:
        return default


@parse.with_pattern(r".:.+?|.*?")
def _parse_file(path: str) -> str:
    """Handle File types in formats."""
    return path


def create_internal(task: TTask, msg: Dict[str, Any]) -> Message:
    """Create message from task and values."""
    path = msg.pop(MessageKeys.PATH, None)
    if path is not None and not os.path.isabs(path):
        path = os.path.abspath(path)
    return Message.from_dict(
        {
            MessageKeys.APP: msg.pop(MessageKeys.APP, None) or task[Task.NAME],
            MessageKeys.PATH: path,
            MessageKeys.LINE: cast(msg.pop(MessageKeys.LINE, None), int),
            MessageKeys.CHAR: cast(msg.pop(MessageKeys.CHAR, None), int),
            MessageKeys.CODE: msg.pop(MessageKeys.CODE, None),
            MessageKeys.CODE_READABLE: msg.pop(MessageKeys.CODE_READABLE, None),
            MessageKeys.MESSAGE: msg.pop(MessageKeys.MESSAGE, None),
            MessageKeys.EXTENDS: task.get(Task.EXTENDS, []),
            MessageKeys.EXTRAS: [msg],
        }
    )


def regex_line_match(regex: str) -> Converter[str, Iterator[Message]]:
    """Parse file using provided regex to extract message."""
    pattern = re.compile(regex)

    def inner(task: TTask, output: str) -> Iterator[Message]:
        for line in output.split("\n"):
            match = pattern.match(line)
            if not match:
                if line:
                    logger.warning(
                        Format(
                            "No match for {regex} in {line}.", regex=regex, line=line,
                        )
                    )
                continue
            group = match.groupdict()
            yield create_internal(task, group)

    return inner


def chain(*calls: Converter[Any, Any],) -> Converter[str, Iterator[Message]]:
    """Chain multiple Converters."""

    def inner(task, output):
        for call in calls:
            output = call(task, output)
        yield from output

    return inner


def format_matches(format_string: str,) -> Converter[List[str], Iterator[Message]]:
    """Convert messages from string to dict."""
    compiled_format = None

    def inner(task: TTask, matches: List[str]) -> Iterator[Message]:
        nonlocal compiled_format
        if compiled_format is None:
            compiled_format = parse.compile(format_string, {"File": _parse_file},)

        for line in matches:
            match = compiled_format.parse(line.lstrip())
            if not match:
                if line:
                    logger.warning(
                        Format(
                            "No match for {format_string} in {line}.",
                            format_string=format_string,
                            line=line,
                        )
                    )
                continue
            yield create_internal(task, match.named)

    # TODO: figure out why mypy complains
    return inner


def extract_lines(task: TTask, output: str) -> List[str]:
    """Split output into lines."""
    return output.splitlines()


def extract_files(task: TTask, output: str) -> Iterator[str]:
    """Extract data that are grouped by file."""
    path = None
    for line in output.splitlines():
        if not line.startswith("    "):
            path = line
            continue

        yield (path or "") + ": " + line[4:]


def from_format(
    format_string: str, extract: Callable = extract_lines,
) -> Converter[str, Iterator[Message]]:
    """Handle output which follow set format."""
    return chain(extract, format_matches(format_string))
