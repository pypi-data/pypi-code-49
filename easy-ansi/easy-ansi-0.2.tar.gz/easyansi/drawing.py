from typing import Optional
from easyansi._core.prnt import prnt as _prnt
from easyansi import cursor as _cursor
from easyansi._core.validations import validate_at_least_minimum as _validate_at_least_minimum
from easyansi._core.validations import validate_is_not_empty_string as _validate_is_not_empty_string
from easyansi._core.validations import validate_in_choices as _validate_in_choices
from easyansi._core.validations import validate_in_range as _validate_in_range
from easyansi._core.drawing import single_line_chars as single
from easyansi._core.drawing import double_line_chars as double
from easyansi._core.drawing import mixed_line_chars as mixed
from easyansi._core.drawing import keyboard_line_chars as keyboard
from easyansi._core.drawing import style_codes as styles

MIN_LINE_LENGTH = 1
MIN_BOX_WIDTH = 2
MIN_BOX_HEIGHT = 2
MAX_CORNER_LENGTH = 1


def hline_code(length: int, char: Optional[str] = None, style: Optional[str] = None) -> str:
    """Return a string to draw a horizontal line of a given length of a given style or specific character."""
    _validate_at_least_minimum(length, MIN_LINE_LENGTH, "Horizontal Line Length")
    char_temp = single.HORIZONTAL  # default character, style = single
    if char is not None:
        _validate_is_not_empty_string(text=char, field="Horizontal Line Character")
        char_temp = char
    elif style is not None:
        _check_style(style=style, field="Horizontal Line Style")
        if style == styles.DOUBLE:
            char_temp = double.HORIZONTAL
        elif style == styles.KEYBOARD:
            char_temp = keyboard.HORIZONTAL
    # Build the line
    line_sequence = ""
    len_idx = 0
    char_idx = 0
    char_temp_len = len(char_temp)
    while len_idx < length:
        line_sequence += char_temp[char_idx:char_idx + 1]
        if char_temp_len > 1:
            char_idx += 1
            if char_idx >= char_temp_len:
                char_idx = 0
        len_idx += 1
    return line_sequence


def hline(length: int, char: Optional[str] = None, style: Optional[str] = None) -> None:
    """Output a string to draw a horizontal line of a given length of a given style or specific character."""
    _prnt(hline_code(length=length, style=style, char=char))


def vline_code(length: int, char: Optional[str] = None, style: Optional[str] = None) -> str:
    """Return a string to draw a vertical line of a given length of a given style or specific character."""
    _validate_at_least_minimum(length, MIN_LINE_LENGTH, "Vertical Line Length")
    char_temp = single.VERTICAL  # default character, style = single
    if char is not None:
        _validate_is_not_empty_string(char, "Vertical Line Character")
        char_temp = char
    elif style is not None:
        _check_style(style=style, field="Vertical Line Style")
        if style == styles.DOUBLE:
            char_temp = double.VERTICAL
        elif style == styles.KEYBOARD:
            char_temp = keyboard.VERTICAL
    # Build the line
    line_sequence = ""
    len_idx = 0
    char_idx = 0
    char_temp_len = len(char_temp)
    while len_idx < length - 1:
        line_sequence += char_temp[char_idx:char_idx + 1]
        if char_temp_len > 1:
            char_idx += 1
            if char_idx >= char_temp_len:
                char_idx = 0
        line_sequence += _cursor.down_code(1)
        line_sequence += _cursor.left_code(1)
        len_idx += 1
    line_sequence += char_temp[char_idx:char_idx + 1]
    return line_sequence


def vline(length: int, char: Optional[str] = None, style: Optional[str] = None) -> None:
    """Output a string to draw a vertical line of a given length of a given style or specific character."""
    _prnt(vline_code(length=length, style=style, char=char))


def box_code(width: int, height: int, style: Optional[str] = None,
             top: Optional[str] = None, bottom: Optional[str] = None,
             left: Optional[str] = None, right: Optional[str] = None,
             top_left: Optional[str] = None, top_right: Optional[str] = None,
             bottom_left: Optional[str] = None, bottom_right: Optional[str] = None,
             top_bottom: Optional[str] = None, left_right: Optional[str] = None,
             all_corners: Optional[str] = None, all_sides: Optional[str] = None,
             all_chars: Optional[str] = None) -> str:
    """Return the ANSI codes to draw a box."""
    _validate_at_least_minimum(number=width, minimum=MIN_BOX_WIDTH, field="Box Width")
    _validate_at_least_minimum(number=height, minimum=MIN_BOX_HEIGHT, field="Box Height")

    # Set Defaults, style = single
    top_left_temp = single.TOP_LEFT
    top_right_temp = single.TOP_RIGHT
    bottom_left_temp = single.BOTTOM_LEFT
    bottom_right_temp = single.BOTTOM_RIGHT
    top_temp = single.HORIZONTAL
    bottom_temp = single.HORIZONTAL
    left_temp = single.VERTICAL
    right_temp = single.VERTICAL

    # Apply styles
    if style is not None:
        _check_style(style=style, field="Box Line Style")
        if style == styles.DOUBLE:
            top_left_temp = double.TOP_LEFT
            top_right_temp = double.TOP_RIGHT
            bottom_left_temp = double.BOTTOM_LEFT
            bottom_right_temp = double.BOTTOM_RIGHT
            top_temp = double.HORIZONTAL
            bottom_temp = double.HORIZONTAL
            left_temp = double.VERTICAL
            right_temp = double.VERTICAL
        elif style == styles.KEYBOARD:
            top_left_temp = keyboard.TOP_LEFT
            top_right_temp = keyboard.TOP_RIGHT
            bottom_left_temp = keyboard.BOTTOM_LEFT
            bottom_right_temp = keyboard.BOTTOM_RIGHT
            top_temp = keyboard.HORIZONTAL
            bottom_temp = keyboard.HORIZONTAL
            left_temp = keyboard.VERTICAL
            right_temp = keyboard.VERTICAL

    # Apply character overrides: corners
    if all_chars is not None:
        top_left_temp = _set_box_corner(corner_char=all_chars, field="All Characters")
        top_right_temp = top_left_temp
        bottom_left_temp = top_left_temp
        bottom_right_temp = top_left_temp
    if all_corners is not None:
        top_left_temp = _set_box_corner(corner_char=all_corners, field="All Corners")
        top_right_temp = top_left_temp
        bottom_left_temp = top_left_temp
        bottom_right_temp = top_left_temp
    if top_left is not None:
        top_left_temp = _set_box_corner(corner_char=top_left, field="Top Left")
    if top_right is not None:
        top_right_temp = _set_box_corner(corner_char=top_right, field="Top Right")
    if bottom_left is not None:
        bottom_left_temp = _set_box_corner(corner_char=bottom_left, field="Bottom Left")
    if bottom_right is not None:
        bottom_right_temp = _set_box_corner(corner_char=bottom_right, field="Bottom Right")

    # Apply character overrides: sides
    # Because the box is drawn with hline and vline, which have their own validations, we
    # do not need to perform validations here.
    if all_chars is not None:
        top_temp = all_chars
        bottom_temp = all_chars
        left_temp = all_chars
        right_temp = all_chars
    if all_sides is not None:
        top_temp = all_sides
        bottom_temp = all_sides
        left_temp = all_sides
        right_temp = all_sides
    if top_bottom is not None:
        top_temp = top_bottom
        bottom_temp = top_bottom
    if left_right is not None:
        left_temp = left_right
        right_temp = left_right
    if top is not None:
        top_temp = top
    if bottom is not None:
        bottom_temp = bottom
    if left is not None:
        left_temp = left
    if right is not None:
        right_temp = right

    # Draw the box
    hline_length = width - 2
    vline_length = height - 2
    # Top
    box_sequence = top_left_temp
    if hline_length > 0:
        box_sequence += hline_code(hline_length, char=top_temp)
    box_sequence += top_right_temp
    box_sequence += _cursor.down_code(1) + _cursor.left_code(1)
    # Right
    if vline_length > 0:
        box_sequence += vline_code(vline_length, char=right_temp)
        if vline_length > 1:
            box_sequence += _cursor.up_code(vline_length - 1)
        box_sequence += _cursor.left_code(1)
    box_sequence += _cursor.left_code(width - 1)
    # Left
    if vline_length > 0:
        box_sequence += vline_code(vline_length, char=left_temp)
        box_sequence += _cursor.down_code(1) + _cursor.left_code(1)
    # Bottom
    box_sequence += bottom_left_temp
    if hline_length > 0:
        box_sequence += hline_code(hline_length, char=bottom_temp)
    box_sequence += bottom_right_temp
    return box_sequence


def box(width: int, height: int, style: Optional[str] = None,
        top: Optional[str] = None, bottom: Optional[str] = None,
        left: Optional[str] = None, right: Optional[str] = None,
        top_left: Optional[str] = None, top_right: Optional[str] = None,
        bottom_left: Optional[str] = None, bottom_right: Optional[str] = None,
        top_bottom: Optional[str] = None, left_right: Optional[str] = None,
        all_corners: Optional[str] = None, all_sides: Optional[str] = None,
        all_chars: Optional[str] = None) -> None:
    """Output the ANSI codes to draw a box."""
    _prnt(box_code(width=width, height=height, style=style, top=top, bottom=bottom,
                   left=left, right=right, top_left=top_left, top_right=top_right,
                   bottom_left=bottom_left, bottom_right=bottom_right, top_bottom=top_bottom,
                   left_right=left_right, all_corners=all_corners, all_sides=all_sides,
                   all_chars=all_chars))


# helper methods


def _check_style(style: str, field: str) -> None:
    """Convenience method to check if the provided style code is valid."""
    _validate_in_choices(style, field, styles.SINGLE, styles.DOUBLE, styles.KEYBOARD)


def _set_box_corner(corner_char: str, field: str) -> str:
    """Convenience method to check corner overrides on a box."""
    _validate_is_not_empty_string(text=corner_char, field=field + " Character")
    _validate_in_range(number=len(corner_char), minimum=MAX_CORNER_LENGTH,
                       maximum=MAX_CORNER_LENGTH, field=field + " Character Length")
    return corner_char
