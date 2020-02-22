from easyansi._core.codes import CSI as _CSI
from easyansi._core.validations import validate_at_least_minimum as _validate_at_least_minimum
from easyansi._core.prnt import prnt as _prnt

MIN_COLUMN = 0
MIN_ROW = 0
MIN_MOVEMENT = 1


def up_code(rows: int = 1) -> str:
    """Return the ANSI code to move the cursor up n rows on the screen."""
    _validate_at_least_minimum(rows, MIN_MOVEMENT, "Rows up")
    return _CSI + str(rows) + "A"


def up(rows: int = 1) -> None:
    """Output the ANSI code to move the cursor up n rows on the screen."""
    _prnt(up_code(rows=rows))


def down_code(rows: int = 1) -> str:
    """Return the ANSI code to move the cursor down n rows on the screen."""
    _validate_at_least_minimum(rows, MIN_MOVEMENT, "Rows down")
    return _CSI + str(rows) + "B"


def down(rows: int = 1) -> None:
    """Output the ANSI code to move the cursor down n rows on the screen."""
    _prnt(down_code(rows=rows))


def right_code(cols: int = 1) -> str:
    """Return the ANSI code to move the cursor right n columns on the screen."""
    _validate_at_least_minimum(cols, MIN_MOVEMENT, "Columns right")
    return _CSI + str(cols) + "C"


def right(cols: int = 1) -> None:
    """Output the ANSI code to move the cursor right n columns on the screen."""
    _prnt(right_code(cols=cols))


def left_code(cols: int = 1) -> str:
    """Return the ANSI code to move the cursor left n columns on the screen."""
    _validate_at_least_minimum(cols, MIN_MOVEMENT, "Columns left")
    return _CSI + str(cols) + "D"


def left(cols: int = 1) -> None:
    """Output the ANSI code to move the cursor left n columns on the screen."""
    _prnt(left_code(cols=cols))


def locate_code(x: int, y: int) -> str:
    """Return the ANSI code to move the cursor to the x, y coordinates on the screen.
       The coordinate system is 0, 0 based."""
    _validate_at_least_minimum(x, MIN_COLUMN, "X-Coordinate")
    _validate_at_least_minimum(y, MIN_ROW, "Y-Coordinate")
    return _CSI + str(y+1) + ";" + str(x+1) + "H"


def locate(x: int, y: int) -> None:
    """Output the ANSI code to move the cursor to the x, y coordinates on the screen.
       The coordinate system is 0, 0 based."""
    _prnt(locate_code(x=x, y=y))


def hide_code() -> str:
    """Return the ANSI code to hide the cursor."""
    return _CSI + "?25l"


def hide() -> None:
    """Output the ANSI code to hide the cursor."""
    _prnt(hide_code())


def show_code() -> str:
    """Return the ANSI code to show the cursor."""
    return _CSI + "?25h"


def show() -> None:
    """Output the ANSI code to show the cursor."""
    _prnt(show_code())
