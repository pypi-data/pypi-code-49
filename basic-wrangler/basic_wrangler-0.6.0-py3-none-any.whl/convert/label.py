""" This module contains the routines to convert a numbered listing to a labelled listing. """
# pylint: disable=bad-continuation

import logging
import sys

from basicwrangler.common.functions import tokenize_line
from basicwrangler.lex.genlex import generate_lexer


def sanity_check_listing(Lexer, numbered_file):
    """ First pass - This function returns a list of all the line numbers in the file. """
    logging.debug("Sanity Checking Numbered Listing.")
    original_line_numbers = []
    for line_no, line in enumerate(numbered_file):
        tokenized_line = tokenize_line(Lexer, line, line_no)
        if tokenized_line[0].type == "LINE":
            if len(original_line_numbers) == 0:
                original_line_numbers.append(tokenized_line[0].val)
            else:
                if tokenized_line[0].val in original_line_numbers:
                    # Duplicate Line sanity check
                    logging.critical(
                        "Fatal Error! Line number %s is a duplicate!",
                        tokenized_line[0].val,
                    )
                    sys.exit(1)
                if int(tokenized_line[0].val) < int(original_line_numbers[-1]):
                    # Out of order check.
                    logging.warning(
                        "Line number %s is out of order.", tokenized_line[0].val
                    )
                original_line_numbers.append(tokenized_line[0].val)
    logging.debug("Original Line Numbers: %s", original_line_numbers)
    return original_line_numbers


def extract_jump_targets(Lexer, numbered_file, original_line_numbers):
    """ Second pass - This function returns a set of jump targets. """
    logging.debug("Getting jump targets.")
    jump_targets = set()
    for line_no, line in enumerate(numbered_file):
        handled = []
        tokenized_line = tokenize_line(Lexer, line, line_no)
        tokenized_line_length = len(tokenized_line)
        indices = [i for i, x in enumerate(tokenized_line) if x.type == "FLOW"]
        logging.debug("Current Line: %s", line)
        logging.debug("Jump target indices: %s", indices)
        for index in indices:
            if index in handled:
                continue
            if tokenized_line[index].val == "ON":
                if (
                    tokenized_line[index + 1].type == "ID"
                    and tokenized_line[index + 2].type == "FLOW"
                ):
                    on_start_index = index + 2
                    handled.append(on_start_index)
                    for i in range(on_start_index + 1, tokenized_line_length):
                        if tokenized_line[i].type == "NUMBER":
                            target = tokenized_line[i].val
                            logging.debug("Jump target: %s", target)
                            if target not in original_line_numbers:
                                logging.critical(
                                    "Fatal Error! Attempt to jump to line number %s is invalid!",
                                    target,
                                )
                                sys.exit(1)
                            jump_targets.add(target)
                        elif tokenized_line[i].val == ",":
                            continue
            if index + 1 < tokenized_line_length:
                if tokenized_line[index + 1].type == "NUMBER":
                    target = tokenized_line[index + 1].val
                    logging.debug("Jump target: %s", target)
                    if target not in original_line_numbers:
                        logging.critical(
                            "Fatal Error! Attempt to jump to line number %s is invalid!",
                            target,
                        )
                        sys.exit(1)
                    jump_targets.add(target)
    logging.debug("Jump targets: %s", jump_targets)
    return jump_targets


def output_basic_listing(Lexer, numbered_file, jump_targets, basic_type):
    """ Final pass - This function returns the labelled BASIC file. """
    logging.debug("Converting to labeled format.")
    labeled_file = ""
    for line_no, line in enumerate(numbered_file):
        set_flow = False
        set_on = False
        tokenized_line = tokenize_line(Lexer, line, line_no)
        tokenized_line_length = len(tokenized_line)
        for index, token in enumerate(tokenized_line):
            current_value = ""
            if token.type == "LINE":
                # Insert a jump target.
                if token.val in jump_targets:
                    logging.debug("Jump target at line number: %s", token.val)
                    labeled_file = labeled_file + "\n" + "_" + token.val + ":" + "\n"
                    continue
                continue
            if (
                token.type == "STATEMENT"
                and tokenized_line[index + 1].type == "COMMENT"
            ):
                # Deal with comments after statements.
                labeled_file = labeled_file + " "
                set_flow = False
                set_on = False
                continue
            if token.type == "STATEMENT":
                # Insert a newline when there's a statement end.
                labeled_file = labeled_file.rstrip() + "\n"
                set_flow = False
                set_on = False
                continue
            if basic_type.startswith("cbm"):
                # Format into upper-case correctly for CBM BASIC.
                # Output valid labels.
                if set_on and token.type == "NUMBER":
                    current_value = "_" + token.val
                elif set_flow and not set_on:
                    current_value = "_" + token.val
                    set_flow = False
                # ON handling.
                elif (
                    token.type == "FLOW"
                    and token.val == "ON"
                    and index + 1 < tokenized_line_length
                    and tokenized_line[index + 1].type == "ID"
                ):
                    set_on = True
                    current_value = token.val.upper()
                elif (
                    token.type == "FLOW"
                    and index + 1 < tokenized_line_length
                    and tokenized_line[index + 1].type == "NUMBER"
                ):
                    set_flow = True
                    current_value = token.val.upper()
                # Replace REM with '
                elif token.type == "COMMENT" and token.val.islower():
                    current_value = "'" + token.val[3:].upper()
                elif token.type == "COMMENT":
                    current_value = "'" + token.val[3:]
                elif token.type == "DATA" and token.val.islower():
                    current_value = token.val.upper()
                elif token.type == "DATA":
                    current_value = "DATA" + token.val[4:]
                elif token.type == "STRING" and token.val.islower():
                    current_value = token.val.upper()
                elif token.type == "STRING":
                    current_value = token.val
                # Handle question marks as PRINT.
                elif token.type == "PRINT":
                    current_value = "PRINT"
                else:
                    current_value = token.val.upper()
            else:
                # Output valid labels.
                if set_on and token.type == "NUMBER":
                    current_value = "_" + token.val
                elif set_flow and not set_on:
                    current_value = "_" + token.val
                    set_flow = False
                # ON handling.
                elif (
                    token.type == "FLOW"
                    and token.val == "ON"
                    and index + 1 < tokenized_line_length
                    and tokenized_line[index + 1].type == "ID"
                ):
                    set_on = True
                    current_value = token.val
                elif (
                    token.type == "FLOW"
                    and index + 1 < tokenized_line_length
                    and tokenized_line[index + 1].type == "NUMBER"
                ):
                    set_flow = True
                    current_value = token.val
                # Replace REM with '
                elif token.type == "COMMENT":
                    current_value = "'" + token.val[3:]
                # Handle question marks as PRINT.
                elif token.type == "PRINT":
                    current_value = "PRINT"
                else:
                    current_value = token.val
            labeled_file = labeled_file + current_value
            if index + 1 < tokenized_line_length:
                # Insert spaces.
                if token.type == "ID" and token.val.endswith("("):
                    continue
                if (
                    not token.type == "PUNCTUATION"
                    and not tokenized_line[index + 1].type == "PUNCTUATION"
                    and not token.type == "STATEMENT"
                ):
                    labeled_file = labeled_file + " "
                # The following elif is not redundant. It fixes formatting errors.
                elif (
                    tokenized_line[index + 1].type == "FLOW"
                    and not token.type == "STATEMENT"
                ):
                    labeled_file = labeled_file + " "
        labeled_file = labeled_file + "\n"
    return labeled_file


def label_listing(numbered_file, basic_type):
    """ This function returns a labeled BASIC listing. """
    Lexer = generate_lexer(basic_type, label=True)
    original_line_numbers = sanity_check_listing(Lexer, numbered_file)
    jump_targets = extract_jump_targets(Lexer, numbered_file, original_line_numbers)
    labeled_list = output_basic_listing(Lexer, numbered_file, jump_targets, basic_type)
    labeled_file = labeled_list.splitlines()
    return labeled_file
