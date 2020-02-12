""" This module contains the line number renumbering routines. """
# pylint: disable=bad-continuation
import logging
import re
import sys

from basicwrangler.common.constants import CBM_BASIC, RE_QUOTES
from basicwrangler.common.functions import tokenize_line

SINCLAIR_BASIC = ["zx81", "zxspectrum"]


def populate_label_data(Lexer, working_file):
    """ This function populates a dictionary with labels and determines
        how many bytes to assume when replacing a line label. """
    logging.debug("Populating Label Dictionary.")
    file_length = len(working_file)
    line_count = 0
    label_dict = {}
    # add labels to dictionary
    for line_no, line in enumerate(working_file):
        tokenized_line = tokenize_line(Lexer, line, line_no)
        if tokenized_line[0].type == "LABEL":
            label = tokenized_line[0].val.rstrip(":")
            label_dict[label] = 0
            line_count += 1
            logging.debug("Label: %s", label)
    lines_total = file_length - line_count
    logging.debug("Total number of lines: %s", lines_total)
    # determine how many bytes are needed when replacing labels
    if lines_total < 10:
        line_replacement = 1
    elif lines_total < 100:
        line_replacement = 2
    elif lines_total < 1000:
        line_replacement = 3
    elif lines_total < 10000:
        line_replacement = 4
    else:
        line_replacement = 5
    logging.debug("Line replacement value: %s", line_replacement)
    logging.debug("Labels: %s", label_dict)
    return label_dict, line_replacement


def check_new_line(line):
    """ Checks to see if a new line is mandatory. """
    need_new_line = False
    if (
        any(token.type == "FLOW" for token in line)
        or any(token.type == "DATA" for token in line)
        or any(token.type == "COMMENT" for token in line)
    ):
        need_new_line = True
    """ if any(token.type == 'DATA' for token in line):
        need_new_line = True
    if any(token.type == 'COMMENT' for token in line):
        need_new_line = True """
    return need_new_line


def crunch_line(tokenized_line, label_dict, line_replacement, line_no, basic_defs):
    """ This function crunches lines.

        If crunch is 0, it will join with spaces,
        and if crunch is 1 it will join with no spaces. """
    tokenized_line_length = len(tokenized_line)
    logging.debug("Tokenizing line %s.", line_no)
    current_line_length = 0
    current_buffer = ""
    for index, token in enumerate(tokenized_line):
        current_value = ""
        if token.type == "LINE":
            logging.critical(
                "This listing appears to be numbered BASIC. Check your filename."
            )
            sys.exit(1)
        elif token.type == "ID" and token.val in label_dict:
            # Correct line length for labels.
            current_value = token.val
            current_line_length += line_replacement
        elif basic_defs.basic_type in SINCLAIR_BASIC:
            # Sinclair BASIC laziness features.
            # Insert LET before assignment at beginning of statement.
            if (
                index == 0
                and index + 1 < tokenized_line_length
                and token.type == "ID"
                and token.val not in label_dict
                and any(token.val == "=" for token in tokenized_line)
            ):
                current_value = "LET " + token.val
            # Insert LET if assignment is after THEN.
            elif (
                token.type == "THEN"
                and tokenized_line[index + 1].type == "ID"
                and tokenized_line[index + 1].val not in label_dict
                and any(token.val == "=" for token in tokenized_line[index:])
            ):
                current_value = "THEN LET"
            # Insert GOTO after THEN.
            elif (
                token.type == "THEN"
                and tokenized_line[index + 1].type == "ID"
                and tokenized_line[index + 1].val in label_dict
            ):
                if basic_defs.basic_type == "zxspectrum":
                    current_value = "THEN GO TO"
                else:
                    current_value = "THEN GOTO"
            # Fix spacing for ZX Spectrum.
            elif token.val == "GOTO":
                if basic_defs.basic_type == "zxspectrum":
                    current_value = "GO TO"
                else:
                    current_value = "GOTO"
            elif token.val == "GOSUB":
                if basic_defs.basic_type == "zxspectrum":
                    current_value = "GO SUB"
                else:
                    current_value = "GOSUB"
            else:
                current_value = token.val
                current_line_length += len(token.val)
        elif token.type == "LET":
            continue
        elif (
            token.val == "GOTO"
            and index > 0
            and tokenized_line[index - 1].val == "THEN"
        ):
            continue
        elif basic_defs.basic_type in CBM_BASIC:
            # Format into upper-case correctly for CBM BASIC
            if token.type == "COMMENT" and token.val.isupper():
                current_value = token.val.lower()
                current_line_length += len(token.val)
            elif token.type == "COMMENT":
                current_value = "rem" + token.val[3:]
                current_line_length += len(token.val)
            elif token.type == "DATA" and token.val.isupper():
                current_value = token.val.lower()
                current_line_length += len(token.val)
            elif token.type == "DATA":
                current_value = "data" + token.val[4:]
                current_line_length += len(token.val)
            elif token.type == "STRING" and token.val.isupper():
                current_value = token.val.lower()
                current_line_length += len(token.val)
            elif token.type == "STRING":
                current_value = token.val
                current_line_length += len(token.val)
            elif token.type == "PRINT" and basic_defs.print_as_question:
                # Output question mark for PRINT when needed.
                if basic_defs.paste_format:
                    current_value = "?"
                    current_line_length += 1
                elif not basic_defs.tokenize:
                    current_value = "?"
                    current_line_length += 1
                else:
                    current_value = token.val.lower()
                    current_line_length += len(token.val)
            else:
                current_value = token.val.lower()
                current_line_length += len(token.val)
        else:
            # Normal output routine.
            if token.type == "PRINT" and basic_defs.print_as_question:
                # Output question mark for PRINT when needed.
                if basic_defs.paste_format:
                    current_value = "?"
                    current_line_length += 1
                elif not basic_defs.tokenize:
                    current_value = "?"
                    current_line_length += 1
                else:
                    current_value = token.val
                    current_line_length += len(token.val)
            else:
                current_value = token.val
                current_line_length += len(token.val)
        current_buffer = current_buffer + current_value
        if basic_defs.crunch != 1:
            # Insert spaces.
            if index + 1 < tokenized_line_length:
                if token.type == "ID" and token.val.endswith("("):
                    continue
                if (
                    not token.type == "PUNCTUATION"
                    and not tokenized_line[index + 1].type == "PUNCTUATION"
                    and not token.type == "STATEMENT"
                ):
                    current_buffer = current_buffer + " "
                    current_line_length += 1
                # The following elif is not redundant. It fixes formatting errors.
                elif (
                    tokenized_line[index + 1].type == "FLOW"
                    and not token.type == "STATEMENT"
                ):
                    current_buffer = current_buffer + " "
                    current_line_length += 1
    return current_line_length, current_buffer


def start_new_line(current_line_number):
    """ Starts a new BASIC line. """
    logging.debug("Starting new BASIC line.")
    current_line = str(current_line_number)
    current_line_length = len(current_line)
    return current_line, current_line_length


def renumber_basic_file(
    Lexer, input_file, basic_defs, label_dict, line_replacement, basic_type
):
    """ The main renumbering routine. """
    logging.debug("Numbering BASIC listing.")
    output_file = []
    current_line_number = basic_defs.numbering
    persistent_buffer, persistent_line_length = start_new_line(current_line_number)
    for line_no, line in enumerate(input_file):
        tokenized_line = tokenize_line(Lexer, line, line_no)
        logging.debug("Persistent Buffer: %s", persistent_buffer)
        # routine for jump targets
        if tokenized_line[0].type == "LABEL":
            label = tokenized_line[0].val.rstrip(":")
            if persistent_buffer != str(current_line_number):
                label_dict[label] = current_line_number + basic_defs.increment
                persistent_buffer = persistent_buffer.rstrip(
                    basic_defs.statement_joining_character
                )
                output_file.append(persistent_buffer)
                current_line_number = current_line_number + basic_defs.increment
            else:
                label_dict[label] = current_line_number
            logging.debug("Persistent Buffer: %s", persistent_buffer)
            persistent_buffer, persistent_line_length = start_new_line(
                current_line_number
            )
            continue
        # tokenizes lines, determines line length, and sets the current buffer to the tokenized line
        logging.debug("Current tokenized line: %s", tokenized_line)
        current_buffer_length, current_buffer = crunch_line(
            tokenized_line, label_dict, line_replacement, line_no, basic_defs
        )
        logging.debug("Current buffer length: %s", current_buffer_length)
        logging.debug("Current Buffer: %s", current_buffer)
        # when lines don't need to be combined
        if not basic_defs.combine:
            persistent_buffer = persistent_buffer + current_buffer
            output_file.append(persistent_buffer)
            current_line_number = current_line_number + basic_defs.increment
            logging.debug("Persistent Buffer: %s", persistent_buffer)
            persistent_buffer, persistent_line_length = start_new_line(
                current_line_number
            )
        # when lines do need to be combined
        else:
            combined_line_length = (
                persistent_line_length
                + len(basic_defs.statement_joining_character)
                + current_buffer_length
            )
            logging.debug("Combined line length: %s", combined_line_length)
            need_new_line = check_new_line(tokenized_line)
            # when a new line is mandatory
            if need_new_line:
                if basic_type in ["bbc", "riscos"] and current_buffer.startswith(
                    "DATA"
                ):
                    # This is to avoid Out of DATA errors in BBC BASIC
                    # it's the same code as the code below, I know,
                    # but using seperate functions for this stuff is trickier than it looks,
                    # and there's other features for this that are worth working on first.
                    persistent_buffer = persistent_buffer.rstrip(
                        basic_defs.statement_joining_character
                    )
                    output_file.append(persistent_buffer)
                    current_line_number = current_line_number + basic_defs.increment
                    logging.debug("Persistent Buffer: %s", persistent_buffer)
                    persistent_buffer, persistent_line_length = start_new_line(
                        current_line_number
                    )
                    persistent_buffer = persistent_buffer + current_buffer
                    output_file.append(persistent_buffer)
                    current_line_number = current_line_number + basic_defs.increment
                    logging.debug("Persistent Buffer: %s", persistent_buffer)
                    persistent_buffer, persistent_line_length = start_new_line(
                        current_line_number
                    )
                elif combined_line_length <= basic_defs.basic_line_length:
                    persistent_buffer = persistent_buffer + current_buffer
                    output_file.append(persistent_buffer)
                    current_line_number = current_line_number + basic_defs.increment
                    logging.debug("Persistent Buffer: %s", persistent_buffer)
                    persistent_buffer, persistent_line_length = start_new_line(
                        current_line_number
                    )
                elif combined_line_length > basic_defs.basic_line_length:
                    persistent_buffer = persistent_buffer.rstrip(
                        basic_defs.statement_joining_character
                    )
                    output_file.append(persistent_buffer)
                    current_line_number = current_line_number + basic_defs.increment
                    logging.debug("Persistent Buffer: %s", persistent_buffer)
                    persistent_buffer, persistent_line_length = start_new_line(
                        current_line_number
                    )
                    persistent_buffer = persistent_buffer + current_buffer
                    output_file.append(persistent_buffer)
                    current_line_number = current_line_number + basic_defs.increment
                    logging.debug("Persistent Buffer: %s", persistent_buffer)
                    persistent_buffer, persistent_line_length = start_new_line(
                        current_line_number
                    )
                continue
            # when a new line is not mandatory
            if combined_line_length <= basic_defs.basic_line_length:
                current_buffer = current_buffer + basic_defs.statement_joining_character
                persistent_buffer = persistent_buffer + current_buffer
                persistent_line_length = len(persistent_buffer)
            elif combined_line_length > basic_defs.basic_line_length:
                persistent_buffer = persistent_buffer.rstrip(
                    basic_defs.statement_joining_character
                )
                output_file.append(persistent_buffer)
                current_line_number = current_line_number + basic_defs.increment
                logging.debug("Persistent Buffer: %s", persistent_buffer)
                persistent_buffer, persistent_line_length = start_new_line(
                    current_line_number
                )
                persistent_buffer = (
                    persistent_buffer
                    + current_buffer
                    + basic_defs.statement_joining_character
                )
                persistent_line_length = len(persistent_buffer)
    # replace labels with line numbers
    for key in sorted(label_dict, key=len, reverse=True):
        for index, line in enumerate(output_file):
            output_file[index] = re.sub(key + RE_QUOTES, str(label_dict[key]), line)
    # warn if line is too long
    for index, line in enumerate(output_file):
        if len(line) > basic_defs.basic_line_length:
            line_number_match = re.search(r"^\d*", line)
            line_number = line[
                line_number_match.span()[0] : line_number_match.span()[1]
            ]
            logging.warning("Line number %s may be too long.", line_number)
    # add space in between line number and rest of line for certain basic versions
    if basic_type in ["bascom", "amiga"] or basic_type.startswith("zx"):
        for index, line in enumerate(output_file):
            space_index = re.search(r"^\d*", line)
            output_file[index] = (
                line[0 : space_index.span()[1]] + " " + line[space_index.span()[1] :]
            )
    return output_file
