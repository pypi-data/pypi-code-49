""" This module contains the routines to convert a numbered listing to a labelled listing. """
# pylint: disable=bad-continuation

import sys

from loguru import logger

from basicwrangler.common.functions import strip_file, tokenize_line
from basicwrangler.lex.genlex import generate_lexer
from basicwrangler.renum.renumber import populate_label_data


def sanity_check_listing(Lexer, numbered_file):
    """ First pass - This function returns a list of all the line numbers in the file. """
    logger.debug("Sanity Checking Numbered Listing.")
    original_line_numbers = []
    for line_no, line in enumerate(numbered_file):
        tokenized_line = tokenize_line(Lexer, line, line_no)
        if tokenized_line[0].type == "LINE":
            if len(original_line_numbers) == 0:
                original_line_numbers.append(tokenized_line[0].val)
            else:
                if tokenized_line[0].val in original_line_numbers:
                    # Duplicate Line sanity check
                    logger.critical(
                        "Fatal Error! Line number {} is a duplicate!",
                        tokenized_line[0].val,
                    )
                    sys.exit(1)
                if int(tokenized_line[0].val) < int(original_line_numbers[-1]):
                    # Out of order check.
                    logger.warning(
                        "Line number {} is out of order.", tokenized_line[0].val
                    )
                original_line_numbers.append(tokenized_line[0].val)
    logger.debug("Original Line Numbers: {}", original_line_numbers)
    return original_line_numbers


def extract_jump_targets(Lexer, numbered_file, original_line_numbers):
    """ Second pass - This function returns a set of jump targets. """
    logger.debug("Getting jump targets.")
    jump_targets = set()
    for line_no, line in enumerate(numbered_file):
        handled = []
        tokenized_line = tokenize_line(Lexer, line, line_no)
        tokenized_line_length = len(tokenized_line)
        indices = [i for i, x in enumerate(tokenized_line) if x.type == "FLOW"]
        logger.debug("Current Line: {}", line)
        logger.debug("Jump target indices: {}", indices)
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
                            logger.debug("Jump target: {}", target)
                            if target not in original_line_numbers:
                                logger.critical(
                                    "Fatal Error! Attempt to jump to line number {} is invalid!",
                                    target,
                                )
                                sys.exit(1)
                            jump_targets.add(target)
                        elif tokenized_line[i].val == ",":
                            continue
            if index + 1 < tokenized_line_length:
                if tokenized_line[index + 1].type == "NUMBER":
                    target = tokenized_line[index + 1].val
                    logger.debug("Jump target: {}", target)
                    if target not in original_line_numbers:
                        logger.critical(
                            "Fatal Error! Attempt to jump to line number {} is invalid!",
                            target,
                        )
                        sys.exit(1)
                    jump_targets.add(target)
    logger.debug("Jump targets: {}", jump_targets)
    return jump_targets


def output_basic_listing(
    Lexer, numbered_file, jump_targets, basic_type, external_dict={}
):
    """ Final pass - This function returns the labelled BASIC file. """
    logger.debug("Converting to labeled format.")
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
                    logger.debug("Jump target at line number: {}", token.val)
                    check_value = "_" + token.val
                    if check_value in external_dict:
                        labeled_file = (
                            labeled_file
                            + "\n"
                            + external_dict[check_value]
                            + ":"
                            + "\n"
                        )
                    else:
                        labeled_file = (
                            labeled_file + "\n" + "_" + token.val + ":" + "\n"
                        )
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
                    if current_value in external_dict:
                        current_value = external_dict[current_value]
                elif set_flow and not set_on:
                    current_value = "_" + token.val
                    if current_value in external_dict:
                        current_value = external_dict[current_value]
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
                    if current_value in external_dict:
                        current_value = external_dict[current_value]
                elif set_flow and not set_on:
                    current_value = "_" + token.val
                    if current_value in external_dict:
                        current_value = external_dict[current_value]
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


def replace_in_labeled_file(Lexer, labeled_file, *, external_dict={}):
    """ Returns a labeled file with stuff replaced. """
    logger.debug("Replacing label names.")
    final_file = ""
    for line_no, line in enumerate(labeled_file):
        tokenized_line = tokenize_line(Lexer, line, line_no)
        tokenized_line_length = len(tokenized_line)
        for index, token in enumerate(tokenized_line):
            if token.type == "LABEL":
                label_val = token.val.rstrip(":")
                if label_val in external_dict:
                    current_value = "\n" + external_dict[label_val] + ":" + "\n"
                else:
                    current_value = "\n" + token.val + "\n"
            elif token.val in external_dict:
                current_value = external_dict[token.val]
            else:
                current_value = token.val
            final_file = final_file + current_value
            if index + 1 < tokenized_line_length:
                # Insert spaces.
                if token.type == "ID" and token.val.endswith("("):
                    continue
                if (
                    not token.type == "PUNCTUATION"
                    and not tokenized_line[index + 1].type == "PUNCTUATION"
                    and not token.type == "STATEMENT"
                ):
                    final_file = final_file + " "
                # The following elif is not redundant. It fixes formatting errors.
                elif (
                    tokenized_line[index + 1].type == "FLOW"
                    and not token.type == "STATEMENT"
                ):
                    final_file = final_file + " "
        final_file = final_file + "\n"
    return final_file


def label_listing(
    numbered_file, basic_type, *, extract=False, external_dict=None, labeled=False
):
    """ This function returns a labeled BASIC listing. """
    jump_list = None
    if labeled:
        Lexer = generate_lexer(basic_type, renum=True)
        numbered_file = strip_file(numbered_file)
        if extract:
            label_dict, line_replacement = populate_label_data(Lexer, numbered_file)  # type: ignore # pylint: disable=unused-variable
            jump_list = [k for k in label_dict]
        if external_dict:
            labeled_list = replace_in_labeled_file(
                Lexer, numbered_file, external_dict=external_dict
            )
        else:
            labeled_list = replace_in_labeled_file(Lexer, numbered_file)
        pass
    else:
        Lexer = generate_lexer(basic_type, label=True)
        original_line_numbers = sanity_check_listing(Lexer, numbered_file)
        jump_targets = extract_jump_targets(Lexer, numbered_file, original_line_numbers)
        if extract:
            jump_list_int = [int(a) for a in jump_targets]
            sorted_jump_list_int = sorted(jump_list_int)
            jump_list = ["_" + str(a) for a in sorted_jump_list_int]
        if external_dict:
            labeled_list = output_basic_listing(
                Lexer, numbered_file, jump_targets, basic_type, external_dict
            )
        else:
            labeled_list = output_basic_listing(
                Lexer, numbered_file, jump_targets, basic_type
            )
    labeled_file = labeled_list.splitlines()
    return labeled_file, jump_list
