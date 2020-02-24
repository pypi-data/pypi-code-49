from typing import Optional

from easyansi._core.codes import CSI as _CSI
from easyansi._core.validations import validate_in_range as _validate_in_range
from easyansi._core.prnt import prnt as _prnt
from easyansi._core.colors.common_colors import *
from easyansi._core.colors.standard_colors import *


def _build_single_color_code(color_cd: str) -> str:
    """Take a color code and return the ANSI sequence."""
    return _CSI + color_cd + "m"


def _build_double_color_code(fg: str, bg: str) -> str:
    """Take a foreground and background color code and return the ANSI sequence."""
    return _CSI + fg + ";" + bg + "m"


# color index = row index, tuple = (foreground code, background code)
_COLOR_LIST = [("30", "40"),   # black
               ("31", "41"),   # red
               ("32", "42"),   # green
               ("33", "43"),   # yellow
               ("34", "44"),   # blue
               ("35", "45"),   # magenta
               ("36", "46"),   # cyan
               ("37", "47"),   # white
               ("90", "100"),  # bright black
               ("91", "101"),  # bright_red
               ("92", "102"),  # bright_green
               ("93", "103"),  # bright_yellow
               ("94", "104"),  # bright_blue
               ("95", "105"),  # bright_magenta
               ("96", "106"),  # bright_cyan
               ("97", "107")]  # bright_white

MIN_COLOR = MIN_STANDARD_COLOR
MAX_COLOR = MAX_STANDARD_COLOR


def color_code(fg: Optional[int] = None, bg: Optional[int] = None) -> str:
    """Return the ANSI code sequence for the selected color combination."""
    if (fg is None) and (bg is None):
        raise ValueError("Must provide either a foreground or background color index")
    if fg is not None:
        _validate_in_range(fg, MIN_COLOR, MAX_COLOR, "Foreground Color Index")
    if bg is not None:
        _validate_in_range(bg, MIN_COLOR, MAX_COLOR, "Background Color Index")
    if fg is not None and bg is not None:
        return _build_double_color_code(_COLOR_LIST[fg][0], _COLOR_LIST[bg][1])
    if fg is not None:
        return _build_single_color_code(_COLOR_LIST[fg][0])
    # bg has already been checked to be a valid integer by this point
    return _build_single_color_code(_COLOR_LIST[bg][1])  # type: ignore


def color(fg: Optional[int] = None, bg: Optional[int] = None) -> None:
    """Output the ANSI code sequence for the selected color combination."""
    _prnt(color_code(fg=fg, bg=bg))
