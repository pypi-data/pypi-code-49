""" This module processes the BASIC definitions. """
import logging
import re
import sys
from collections import namedtuple
from pathlib import Path

import yaml

from basicwrangler.common.constants import NO_TOKENIZER, RE_QUOTES

# This is needed to find files when running with pyinstaller.
if hasattr(sys, "_MEIPASS"):
    SCRIPT_DIR = Path.joinpath(Path(sys._MEIPASS).resolve(), "defs")  # type: ignore # pylint: disable=no-member,protected-access
else:
    SCRIPT_DIR = Path(__file__).resolve().parent


def abbreviate(working_file, basic_type, reverse_this=False):
    """ Returns the file with keywords abbreviated or with the abbreviations removed. """
    logging.debug("Converting to/from abbreviated format.")
    yaml_path = Path.joinpath(SCRIPT_DIR, "abbrevs.yaml")
    with open(yaml_path) as yaml_file:
        yaml_dict = yaml.safe_load(yaml_file)
    abbrev_dict = yaml_dict[basic_type]
    reversed_dict = {}
    if reverse_this:
        reversed_dict = {v.replace(".", "[.]"): k for k, v in abbrev_dict.items()}
        for key in sorted(reversed_dict, key=len, reverse=True):
            for index, line in enumerate(working_file):
                working_file[index] = re.sub(key + RE_QUOTES, reversed_dict[key], line)
    else:
        for key in sorted(abbrev_dict, key=len, reverse=True):
            for index, line in enumerate(working_file):
                working_file[index] = re.sub(key + RE_QUOTES, abbrev_dict[key], line)
    return working_file


def get_basic_dialects(convert=False):
    """ Returns a list of BASIC dialects from the basdefs.yaml file. """
    yaml_path = Path.joinpath(SCRIPT_DIR, "basdefs.yaml")
    with open(yaml_path) as yaml_file:
        yaml_dict = yaml.safe_load(yaml_file)
    dialect_list = sorted(yaml_dict)
    if convert:
        for dialect in NO_TOKENIZER:
            dialect_list.remove(dialect)
    return dialect_list


def set_basic_defs(basic_type, paste_format, basic_line_length, numbering, increment):
    """ Return a namedtuple containing the BASIC definitions. """
    BasicDefs = namedtuple(
        "BasicDefs",
        [
            "basic_type",
            "basic_line_length",
            "combine",
            "crunch",
            "print_as_question",
            "statement_joining_character",
            "numbering",
            "case",
            "increment",
            "abbreviate",
            "tokenize",
            "data_length",
            "paste_format",
        ],
    )
    yaml_path = Path.joinpath(SCRIPT_DIR, "basdefs.yaml")
    with open(yaml_path) as yaml_file:
        yaml_dict = yaml.safe_load(yaml_file)
    def_dict = yaml_dict[basic_type]
    if "paste_line_length" not in def_dict:
        paste_format = False
    elif "file_line_length" not in def_dict:
        paste_format = True
    if basic_line_length is None:
        if paste_format:
            basic_line_length = def_dict["paste_line_length"]
        elif not paste_format:
            basic_line_length = def_dict["file_line_length"]
    combine = def_dict["combine"]
    crunch = def_dict["crunch"]
    print_as_question = def_dict["print_as_question"]
    if "statement_joining_character" in def_dict:
        statement_joining_character = def_dict["statement_joining_character"]
    else:
        statement_joining_character = ":"
    if numbering is None:
        numbering = def_dict["numbering"]
    if "case" in def_dict:
        case = def_dict["case"]
    else:
        case = ""
    if increment is None:
        if "increment" in def_dict:
            increment = def_dict["increment"]
        else:
            increment = 1
    abbreviate = def_dict["abbreviate"]
    tokenize = def_dict["tokenize"]
    if "data_length" in def_dict:
        data_length = def_dict["data_length"]
    else:
        data_length = None
    basic_defs = BasicDefs(
        basic_type,
        basic_line_length,
        combine,
        crunch,
        print_as_question,
        statement_joining_character,
        numbering,
        case,
        increment,
        abbreviate,
        tokenize,
        data_length,
        paste_format,
    )
    logging.debug("BASIC Definitions: %s", basic_defs)
    return basic_defs, paste_format
