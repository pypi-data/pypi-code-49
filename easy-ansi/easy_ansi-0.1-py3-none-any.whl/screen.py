from typing import Tuple
import shutil
from easyansi._core.codes import CSI as _CSI
from easyansi._core.prnt import prnt
from easyansi._core.validations import validate_at_least_minimum as _validate_at_least_minimum
from easyansi.cursor import locate_code as _locate_code

MINIMUM_ROW = 0


def clear_code() -> str:
    """Return the ANSI code to clear the screen and locate the cursor to 0, 0."""
    return _CSI + "2J" + _locate_code(0, 0)


def clear() -> None:
    """Output the ANSI code to clear the screen and locate the cursor to 0, 0."""
    prnt(clear_code())


def clear_line_code(row: int) -> str:
    """Return the ANSI code to clear the line at a given row. The cursor will end at the beginning of the row."""
    _validate_at_least_minimum(number=row, minimum=MINIMUM_ROW, field="Row Number")
    return _locate_code(0, row) + _CSI + "2K"


def clear_line(row: int) -> None:
    """Output the ANSI code to clear the line at a given row. The cursor will end at the beginning of the row."""
    prnt(clear_line_code(row=row))


def get_size() -> Tuple[int, int]:
    """Return the screen size in cols, rows."""
    screen_size = shutil.get_terminal_size()
    return screen_size.columns, screen_size.lines
