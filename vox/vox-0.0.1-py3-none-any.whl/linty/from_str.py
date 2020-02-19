"""Builtin conversions from std:out."""
# nosa: pylint[:Unused argument 'task']
# nosa: pylint[C0103]

import itertools
import json
import logging
import re
from typing import Iterator, List, Sequence, Tuple, TypeVar

from . import helpers as _helpers
from . import to_str

__all__ = [
    "echo",
    "pycodestyle",
    "pycodestyle_pylint",
    "mypy",
    "pyflakes",
    "mccabe",
    "pylint",
    "pylint_old",
    "pylint_visual_studio",
    "pylint_parsable",
    "vulture",
    "bandit_mam_custom",
    "pylama",
    "jedi",
    "pydiatra",
    "radon",
    "radon_mi",
    "pydocstyle",
    "prospector_json",
    "detect_secrets",
    "pyroma",
]

logger = logging.getLogger(__name__)


def echo(task: _helpers.TTask, data: str) -> List[_helpers.Message]:
    """Echo std:out to output. Good for adding new converters."""
    print(data)  # nosa: (flake8-print)
    return []


pycodestyle = _helpers.from_format(to_str.PYCODESTYLE)
pycodestyle_pylint = _helpers.from_format(to_str.PYCODESTYLE_PYLINT)
mypy = _helpers.from_format(to_str.MYPY)
pyflakes = _helpers.from_format(to_str.PYFLAKES)
mccabe = _helpers.from_format(to_str.MCCABE)
pylint = _helpers.from_format(to_str.PYLINT)
pylint_old = _helpers.from_format(to_str.PYLINT_OLD)
pylint_visual_studio = _helpers.from_format(to_str.PYLINT_VISUAL_STUDIO)
pylint_parsable = _helpers.from_format(to_str.PYLINT_PARSABLE)
vulture = _helpers.from_format(to_str.VULTURE)
bandit_mam_custom = _helpers.from_format(to_str.BANDIT_MAM_CUSTOM)
pylama = _helpers.from_format(to_str.PYLAMA)
jedi = _helpers.from_format(to_str.JEDI)
pydiatra = _helpers.from_format(to_str.PYDIATRA)
radon = _helpers.from_format(to_str.RADON, _helpers.extract_files)
radon_mi = _helpers.from_format(to_str.RADON_MI)

T = TypeVar("T")


def _pairwise(iterable: Sequence[T]) -> Iterator[Tuple[T, T]]:
    """Itertools recipe for pairwise iteration."""
    previous, current = itertools.tee(iterable)
    next(current, None)
    return zip(previous, current)


# file.py:1 at module level:
_pydocstyle_line = re.compile(
    r"^(?P<path>[^:]*)" r":(?P<line>[^ ]*)" r" (?P<extra>[^:]*)" r":.*$",
)

#         E001: example message
_pydocstyle_message = re.compile(r"^\s*(?P<code>[^:]*)" r":(?P<msg>.*)" r"$",)


def pydocstyle(task: _helpers.TTask, output: str) -> Iterator[_helpers.Message]:
    """Convert from pydocstyle output."""
    lines = _pairwise(output.split("\n"))
    for prev, curr in lines:
        if not prev:
            continue
        prev_match = _pydocstyle_line.match(prev)
        curr_match = _pydocstyle_message.match(curr)
        if prev_match is None and curr_match is None:
            if prev:
                logger.warning(
                    _helpers.Format("No match for pydocstyle in {line}.", line=prev,)
                )
            continue
        next(lines, None)
        group = prev_match.groupdict() if prev_match is not None else {}
        group.update(curr_match.groupdict() if curr_match is not None else {})
        yield _helpers.create_internal(task, group)


def prospector_json(task: _helpers.TTask, output: str) -> Iterator[_helpers.Message]:
    """Convert from prospector output."""
    for obj in json.loads(output)["messages"]:
        location = obj["location"]
        group = {
            _helpers.MessageKeys.APP: obj["source"],
            _helpers.MessageKeys.PATH: location["path"],
            _helpers.MessageKeys.LINE: location["line"],
            _helpers.MessageKeys.CHAR: location["character"],
            _helpers.MessageKeys.MESSAGE: obj["message"],
            "module": location["module"],
            "function": location["function"],
        }
        if obj["code"][0].islower():
            group[_helpers.MessageKeys.CODE_READABLE] = obj["code"]
        else:
            group[_helpers.MessageKeys.CODE] = obj["code"]
        yield _helpers.create_internal(task, group)


def detect_secrets(task: _helpers.TTask, output: str) -> Iterator[_helpers.Message]:
    """Convert from detect-secrets output."""
    for path, secrets in json.loads(output)["results"].items():
        for secret in secrets:
            yield _helpers.create_internal(
                task,
                {
                    _helpers.MessageKeys.PATH: path,
                    _helpers.MessageKeys.LINE: secret["line_number"],
                    _helpers.MessageKeys.CODE_READABLE: secret["type"],
                    _helpers.MessageKeys.MESSAGE: (
                        "Hashed secret {}".format(secret["hashed_secret"])
                    ),
                },
            )


def pyroma(task: _helpers.TTask, output: str) -> Iterator[_helpers.Message]:
    """Convert from Pyroma output."""
    seperator = 0
    for line in output.splitlines():
        if line.startswith("---"):
            seperator += 1
            continue
        if seperator == 2:
            yield _helpers.create_internal(task, {_helpers.MessageKeys.MESSAGE: line,})
