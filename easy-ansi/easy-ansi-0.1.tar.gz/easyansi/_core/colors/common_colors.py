from easyansi._core.prnt import prnt as _prnt
from easyansi._core.codes import CSI as _CSI
from easyansi._core.validations import validate_in_range as _validate_in_range
from easyansi._core.booleans import *

_DEFAULT_FG = _CSI + "39m"
_DEFAULT_BG = _CSI + "49m"
_DEFAULT_FG_AND_BG = _CSI + "39;49m"
_RESET = _CSI + "0m"


def reset_code() -> str:
    """Return the ANSI code to reset all colors, intensities, and attributes to defaults."""
    return _RESET


def reset() -> None:
    """Reset all colors, intensities, and attributes to defaults."""
    _prnt(reset_code())


def default_code(fg: int = 1, bg: int = 1) -> str:
    """Return the ANSI code to reset the foreground and/or background color to terminal defaults."""
    if fg is None and bg is None:
        raise ValueError("Neither foreground or background default was requested.")
    if fg is not None:
        _validate_in_range(fg, FALSE, TRUE, "Foreground Flag")
    if bg is not None:
        _validate_in_range(bg, FALSE, TRUE, "Background Flag")
    if fg is not None and fg == 1 and bg is not None and bg == 1:
        return _DEFAULT_FG_AND_BG
    if fg is not None and fg == 1:
        return _DEFAULT_FG
    return _DEFAULT_BG


def default(fg: int = 1, bg: int = 1) -> None:
    """Reset the foreground and/or background color to terminal defaults."""
    _prnt(default_code(fg=fg, bg=bg))
