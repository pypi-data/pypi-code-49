from typing import Tuple
from typing import Optional
import shutil
from easyansi._core.codes import CSI as _CSI
from easyansi._core.prnt import prnt
from easyansi._core.validations import validate_at_least_minimum as _validate_at_least_minimum
from easyansi.cursor import locate_code as _locate_code
from easyansi.cursor import get_location as _get_location

MINIMUM_ROW = 0


def clear_code() -> str:
    """Return the ANSI code to clear the screen and locate the cursor to 0, 0."""
    return _CSI + "2J" + _locate_code(0, 0)


def clear() -> None:
    """Output the ANSI code to clear the screen and locate the cursor to 0, 0."""
    prnt(clear_code())


def clear_line_code(row: Optional[int] = None) -> str:
    """Return the ANSI code to clear the line at a given row. The cursor will end at the beginning of the row.
    If row is not provided, it will be queried from the cursor location."""
    the_row = row
    if the_row is None:
        cursor_x, cursor_y = _get_location()
        the_row = cursor_y
    else:
        _validate_at_least_minimum(number=the_row, minimum=MINIMUM_ROW, field="Row Number")
    return _locate_code(0, the_row) + _CSI + "2K"


def clear_line(row: Optional[int] = None) -> None:
    """Output the ANSI code to clear the line at a given row. The cursor will end at the beginning of the row.
    If row is not provided, it will be queried from the cursor location."""
    prnt(clear_line_code(row=row))


def get_size() -> Tuple[int, int]:
    """Return the screen size in cols, rows."""
    screen_size = shutil.get_terminal_size()
    return screen_size.columns, screen_size.lines
