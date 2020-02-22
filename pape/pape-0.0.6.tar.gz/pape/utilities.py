# # # # # # # # # # # # # # # # # # # #
# Pape (a Python package)
# Copyright 2020 Carter Pape
# 
# See file LICENSE for licensing terms.
# # # # # # # # # # # # # # # # # # # #

import math
import typing
import os.path

_typical_prefix_map = {
    0: "th",
    1: "st",
    2: "nd",
    3: "rd",
    4: "th",
    5: "th",
    6: "th",
    7: "th",
    8: "th",
    9: "th",
}

_ap_number_replacements_map = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

def ordinal(number: int) -> str:
    if not isinstance(number, int):
        raise TypeError(f"Expected {int} but got {type(number)}")
    
    elif _is_teenthish(abs(number)):
        return f"{number}th"
    else:
        return f"{number}{_typical_prefix_map[abs(number) % 10]}"

def _is_teenthish(number: int) -> bool:
    return (math.floor(number / 10) % 10) == 1

def pluralize(*,
    singular_form: str,
    count,
    plural_form = None,
    use_AP_style = True,
    include_count = True,
) -> str:
    if plural_form == None:
        plural_form = f"{singular_form}s"
        
    correct_form = singular_form if count == 1 else plural_form
    
    if use_AP_style and count in _ap_number_replacements_map:
        count = _ap_number_replacements_map[count]
    
    return (
        f"{count} {correct_form}"
        if include_count
        else f"{correct_form}"
    )

def strip_file_extension(*,
    from_path: typing.AnyStr,
    basename_only: bool = False,
) -> typing.AnyStr:
    path = os.path.basename(from_path) if basename_only else from_path
    return os.path.splitext(path)[0]
