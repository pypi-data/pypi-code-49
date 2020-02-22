from typing import Optional

from easyansi._core.codes import CSI as _CSI
from easyansi._core.validations import validate_in_range as _validate_in_range
from easyansi._core.prnt import prnt as _prnt
from easyansi._core.colors.common_colors import reset_code, reset
from easyansi._core.colors.standard_colors import *
from easyansi._core.colors.gray_colors import *

MIN_COLOR = 0
MAX_COLOR = 255
MIN_ENHANCED_COLOR = 16
MAX_ENHANCED_COLOR = 231


def _build_color_code(color_idx: int, fg: bool) -> str:
    """Take a 256 color index value and return the ANSI sequence."""
    color_cd = _CSI
    color_cd += "38" if fg else "48"
    color_cd += ";5;" + str(color_idx) + "m"
    return color_cd


def color_code(fg: Optional[int] = None, bg: Optional[int] = None) -> str:
    """Return the ANSI code sequence for the selected 256 color combination."""
    if (fg is None) and (bg is None):
        raise ValueError("Must provide either a foreground or background color index")
    color_sequence = ""
    if fg is not None:
        _validate_in_range(fg, MIN_COLOR, MAX_COLOR, "Foreground 256 Color Index")
        color_sequence += _build_color_code(fg, True)
    if bg is not None:
        _validate_in_range(bg, MIN_COLOR, MAX_COLOR, "Background 256 Color Index")
        color_sequence += _build_color_code(bg, False)
    return color_sequence


def color(fg: Optional[int] = None, bg: Optional[int] = None) -> None:
    """Output the selected 256 color combination."""
    _prnt(color_code(fg=fg, bg=bg))
