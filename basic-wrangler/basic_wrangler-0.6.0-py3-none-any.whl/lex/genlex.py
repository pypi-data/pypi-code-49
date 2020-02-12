""" This module contains functions to generate lexers. """

import logging
import sys
from pathlib import Path

import yaml

import basicwrangler.lex.lexer as lexer

LABEL_RULES = [
    "LINE",
    "KEYWORDS",
    "FLOW",
    "NUMBER",
    "COMMENT",
    "DATA",
    "LET",
    "ID",
    "STATEMENT",
    "STRING",
    "PRINT",
    "PUNCTUATION",
]
RENUM_RULES = [
    "LABEL",
    "LINE",
    "PRINT",
    "KEYWORDS",
    "FLOW",
    "THEN",
    "NUMBER",
    "COMMENT",
    "DATA",
    "LET",
    "ID",
    "STATEMENT",
    "STRING",
    "PUNCTUATION",
]

# This is needed to find files when running with pyinstaller.
if hasattr(sys, "_MEIPASS"):
    SCRIPT_DIR = Path.joinpath(Path(sys._MEIPASS).resolve(), "lex")  # type: ignore # pylint: disable=no-member,protected-access
else:
    SCRIPT_DIR = Path(__file__).resolve().parent


def generate_splitter():
    """ Loads the splitting regex from the file. """
    yaml_path = Path.joinpath(SCRIPT_DIR, "rules.yaml")
    with open(yaml_path) as yaml_file:
        yaml_dict = yaml.safe_load(yaml_file)
    specific_dict = yaml_dict["label"]
    split_string = specific_dict["split"]
    return split_string


def generate_lexer(basic_type, *, label=False, renum=False):
    """ Generates a lexer for converting to labelled format. """
    if label:
        regex_dict_order = LABEL_RULES
    if renum:
        regex_dict_order = RENUM_RULES
    yaml_path = Path.joinpath(SCRIPT_DIR, "rules.yaml")
    with open(yaml_path) as yaml_file:
        yaml_dict = yaml.safe_load(yaml_file)
    if label:
        specific_dict = yaml_dict["label"]
    if renum:
        specific_dict = yaml_dict["renum"]
    regex_dict = specific_dict[basic_type]
    rules = []
    for key in regex_dict_order:
        temp_tuple = (regex_dict[key], key)
        rules.append(temp_tuple)
    logging.debug("Lexer Rules: %s", rules)
    if basic_type.startswith("cbm") and label:
        lx = lexer.Lexer(rules, skip_whitespace=True, ignore_case=True)
    else:
        lx = lexer.Lexer(rules, skip_whitespace=True)
    return lx
