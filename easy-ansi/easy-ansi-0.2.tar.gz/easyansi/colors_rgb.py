from typing import Optional

from easyansi._core.codes import CSI as _CSI
from easyansi._core.validations import validate_in_range as _validate_in_range
from easyansi._core.prnt import prnt as _prnt
from easyansi._core.colors.common_colors import reset_code, reset

MIN_COLOR = 0
MAX_COLOR = 255


def __build_color_code(r: int, g: int, b: int, fg: bool) -> str:
    """Take an rgb value and return the ANSI sequence."""
    color_cd = _CSI
    color_cd += "38" if fg else "48"
    color_cd += ";2;" + str(r) + ";" + str(g) + ";" + str(b) + "m"
    return color_cd


def color_code(r: Optional[int] = None, g: Optional[int] = None, b: Optional[int] = None,
               bg_r: Optional[int] = None, bg_g: Optional[int] = None, bg_b: Optional[int] = None) -> str:
    """Return the ANSI code sequence for the provided rgb combination."""
    color_sequence = ""
    if r is None and g is None and b is None and bg_r is None and bg_g is None and bg_b is None:
        raise ValueError("No RGB color values provided")
    if r is not None or g is not None or b is not None:
        _validate_in_range(r, MIN_COLOR, MAX_COLOR, "RGB Red Foreground Value")    # type: ignore
        _validate_in_range(g, MIN_COLOR, MAX_COLOR, "RGB Green Foreground Value")  # type: ignore
        _validate_in_range(b, MIN_COLOR, MAX_COLOR, "RGB Blue Foreground Value")   # type: ignore
        color_sequence += __build_color_code(r, g, b, True)                        # type: ignore
    if bg_r is not None or bg_g is not None or bg_b is not None:
        _validate_in_range(bg_r, MIN_COLOR, MAX_COLOR, "RGB Red Background Value")    # type: ignore
        _validate_in_range(bg_g, MIN_COLOR, MAX_COLOR, "RGB Green Background Value")  # type: ignore
        _validate_in_range(bg_b, MIN_COLOR, MAX_COLOR, "RGB Blue Background Value")   # type: ignore
        color_sequence += __build_color_code(bg_r, bg_g, bg_b, False)                 # type: ignore
    return color_sequence


def color(r: Optional[int] = None, g: Optional[int] = None, b: Optional[int] = None,
          bg_r: Optional[int] = None, bg_g: Optional[int] = None, bg_b: Optional[int] = None) -> None:
    """Output the provided rgb combination."""
    _prnt(color_code(r=r, g=g, b=b, bg_r=bg_r, bg_g=bg_g, bg_b=bg_b))
