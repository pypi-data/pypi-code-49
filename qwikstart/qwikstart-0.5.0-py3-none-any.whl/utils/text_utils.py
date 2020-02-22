import os
from typing import Iterable, Optional

from .core import first


def strip_empty_lines(text: Optional[str]) -> str:
    """Return multi-line string with leading and trailing empty lines stripped."""
    if not text:
        return ""
    lines_of_text = text.splitlines()
    try:
        i_first = index_of_non_empty_line(lines_of_text)
        i_last = len(lines_of_text) - index_of_non_empty_line(reversed(lines_of_text))
    except StopIteration:
        return ""
    return os.linesep.join(lines_of_text[i_first:i_last])


def index_of_non_empty_line(lines_of_text: Iterable[str]) -> int:
    return first(i for i, line in enumerate(lines_of_text) if len(line.strip()) > 0)
