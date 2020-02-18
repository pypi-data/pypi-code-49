"""Output helper functions."""

import asyncio
import logging
import time
from sys import platform
from typing import Tuple

from colorama import Style

from pyconsoler.const import RIGHT_PAD, ERROR_COLOR, ATTENTION_COLOR

if platform == "win32":
    from colorama import init

    init()

_LOGGER = logging.getLogger(__name__)


def _out(text, color=None, end="\n"):
    if color:
        print(color + text, end=end)
    else:
        print(Style.RESET_ALL + text, end=end)


async def print_waiting_countdown(delay: int, clear=False):
    """Print a waiting message including a countdown timer

    Args:
        delay: The amount of seconds to countdown.
        clear: If True the countdown text is erased after finished.

    Returns:

    """
    prev = 0
    for i in range(delay, 0, -1):
        txt = f"waiting for {i} seconds\r"
        prev = len(txt)
        print(ATTENTION_COLOR + txt, end="", flush=True)
        await asyncio.sleep(1)

    if clear:
        print(f"{prev*' '}{Style.RESET_ALL}\r", end="")


def print_key_value(key, value, spacing=RIGHT_PAD, color=None):
    """Print a key-value with the value indented from the left border with a certain
        spacing

    Args:
        key: The key to print out
        value: The value to print out
        spacing: Print the value with an indentation relative to the left border
        color: A colorama color

    """
    _str = str(key).ljust(spacing) + str(value)
    _out(_str, color=color)


def key_value(key, value, spacing=RIGHT_PAD):
    """Return a key value pair with proper spacing."""

    return f"{key.ljust(spacing)}{value}"


def bordered_text(text: str, hor_spacing=2) -> Tuple[str]:
    """Put a border around a string

    Args:
        text: The text to border
        hor_spacing: Empty space left and right from the string

    Returns:

    """
    border_width = len(text) + 2 * hor_spacing
    top = f"┏{border_width * '━'}┓"
    middle = f"┃{text.center(border_width)}┃"
    bottom = f"┗{border_width * '━'}┛"

    return (top, middle, bottom)


def get_time_stamp(
    time_sec=None,
    add_date=True,
    add_time=True,
    date_sep="-",
    time_sep=":",
    date_time_sep=" ",
) -> str:
    if time_sec is None:
        _date = time.strftime(f"%Y{date_sep}%m{date_sep}%d")
        _time = time.strftime(f"%H{time_sep}%M{time_sep}%S")
    else:
        _date = time.strftime(f"%Y{date_sep}%m{date_sep}%d", time.localtime(time_sec))
        _time = time.strftime(f"%H{time_sep}%M{time_sep}%S", time.localtime(time_sec))

    if add_date and add_time:
        return f"{_date}{date_time_sep}{_time}"
    elif add_date:
        return _date
    else:
        return _time
