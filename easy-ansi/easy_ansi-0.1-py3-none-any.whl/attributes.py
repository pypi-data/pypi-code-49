from easyansi._core.codes import CSI as _CSI
from easyansi._core.prnt import prnt as _prnt
from easyansi._core.colors.common_colors import reset_code, reset


def _build_attribute_code(color_cd: str) -> str:
    """Take an attribute code and return the ANSI sequence."""
    return _CSI + color_cd + "m"


_COLOR_DICT = {"bright": _build_attribute_code("1"),
               "dim": _build_attribute_code("2"),
               "normal": _build_attribute_code("22"),
               "italic": _build_attribute_code("3"),
               "italic_off": _build_attribute_code("23"),
               "underline": _build_attribute_code("4"),
               "underline_off": _build_attribute_code("24"),
               "blink": _build_attribute_code("5"),
               "blink_off": _build_attribute_code("25"),
               "reverse": _build_attribute_code("7"),
               "reverse_off": _build_attribute_code("27"),
               "conceal": _build_attribute_code("8"),
               "conceal_off": _build_attribute_code("28"),
               "strikethrough": _build_attribute_code("9"),
               "strikethrough_off": _build_attribute_code("29"),
               }


def bright_code() -> str:
    """Return the ANSI code to turn bright on."""
    # Testing has shown bright does not always work unless the normal code is sent first.
    return _COLOR_DICT["normal"] + _COLOR_DICT["bright"]


def bright() -> None:
    """Output the ANSI code to turn bright on."""
    _prnt(bright_code())


def dim_code() -> str:
    """Return the ANSI code to turn dim on."""
    # Testing has shown dim does not always work unless the normal code is sent first.
    return _COLOR_DICT["normal"] + _COLOR_DICT["dim"]


def dim() -> None:
    """Output the ANSI code to turn dim on."""
    _prnt(dim_code())


def normal_code() -> str:
    """Return the ANSI code to turn normal (not bright or dim) on."""
    return _COLOR_DICT["normal"]


def normal() -> None:
    """Output the ANSI code to turn normal (not bright or dim) on."""
    _prnt(normal_code())


def italic_code() -> str:
    """Return the ANSI code to turn italics on."""
    return _COLOR_DICT["italic"]


def italic() -> None:
    """Output the ANSI code to turn italics on."""
    _prnt(italic_code())


def italic_off_code() -> str:
    """Return the ANSI code to turn italics off."""
    return _COLOR_DICT["italic_off"]


def italic_off() -> None:
    """Output the ANSI code to turn italics off."""
    _prnt(italic_off_code())


def underline_code() -> str:
    """Return the ANSI code to turn underline on."""
    return _COLOR_DICT["underline"]


def underline() -> None:
    """Output the ANSI code to turn underline on."""
    _prnt(underline_code())


def underline_off_code() -> str:
    """Return the ANSI code to turn underline off."""
    return _COLOR_DICT["underline_off"]


def underline_off() -> None:
    """Output the ANSI code to turn underline off."""
    _prnt(underline_off_code())


def blink_code() -> str:
    """Return the ANSI code to turn blink on."""
    return _COLOR_DICT["blink"]


def blink() -> None:
    """Output the ANSI code to turn blink on."""
    _prnt(blink_code())


def blink_off_code() -> str:
    """Return the ANSI code to turn blink off."""
    return _COLOR_DICT["blink_off"]


def blink_off() -> None:
    """Output the ANSI code to turn blink off."""
    _prnt(blink_off_code())


def reverse_code() -> str:
    """Return the ANSI code to turn reverse on."""
    return _COLOR_DICT["reverse"]


def reverse() -> None:
    """Output the ANSI code to turn reverse on."""
    _prnt(reverse_code())


def reverse_off_code() -> str:
    """Return the ANSI code to turn reverse off."""
    return _COLOR_DICT["reverse_off"]


def reverse_off() -> None:
    """Output the ANSI code to turn reverse off."""
    _prnt(reverse_off_code())


def conceal_code() -> str:
    """Return the ANSI code to turn conceal on."""
    return _COLOR_DICT["conceal"]


def conceal() -> None:
    """Output the ANSI code to turn conceal on."""
    _prnt(conceal_code())


def conceal_off_code() -> str:
    """Return the ANSI code to turn conceal off."""
    return _COLOR_DICT["conceal_off"]


def conceal_off() -> None:
    """Output the ANSI code to turn conceal off."""
    _prnt(conceal_off_code())


def strikethrough_code() -> str:
    """Return the ANSI code to turn strikethrough on."""
    return _COLOR_DICT["strikethrough"]


def strikethrough() -> None:
    """Output the ANSI code to turn strikethrough on."""
    _prnt(strikethrough_code())


def strikethrough_off_code() -> str:
    """Return the ANSI code to turn strikethrough off."""
    return _COLOR_DICT["strikethrough_off"]


def strikethrough_off() -> None:
    """Output the ANSI code to turn strikethrough off."""
    _prnt(strikethrough_off_code())
