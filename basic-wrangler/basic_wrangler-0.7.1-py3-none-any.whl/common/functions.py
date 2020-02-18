""" This module contains functions that are accessed from multiple other modules. """

import re

from loguru import logger

from basicwrangler.common.constants import RE_QUOTES
from basicwrangler.lex.lexer import LexerError


def tokenize_line(Lexer, untokenized_line, line_no):
    """ This function returns an untokenized line as a list of tokens. """
    logger.debug("Tokenizing line number: {}", line_no + 1)
    Lexer.input(untokenized_line)
    token_list = []
    try:
        for tok in Lexer.tokens():
            logger.debug("Token: {}", tok)
            token_list.append(tok)
    except LexerError as err:
        print(f"LexerError at position {err.pos} in line number {line_no + 1}")
    return token_list


def strip_file(unstripped):
    """ Strip newlines and whitespace. """
    # strip whitespace
    stripped = [line.strip() for line in unstripped]
    stripped = list(filter(None, stripped))
    return stripped


def remove_comments(commented):
    """ This will remove comments from the file. """
    # strip comments
    uncommented = [
        b.rstrip() for b in [re.sub(RE_QUOTES + r"'.*?$", "", c) for c in commented]
    ]
    uncommented = list(filter(None, uncommented))
    return uncommented


def reformat_data_statements(input_file, basic_defs):
    """ Formats a newline-delimited list of values into DATA statements. """
    if basic_defs.data_length is None:
        data_statement_length = basic_defs.basic_line_length - 9
    elif basic_defs.data_length is not None:
        data_statement_length = basic_defs.data_length - 9
    if basic_defs.crunch != 1:
        data_statement_length += 1
    logger.debug("DATA Statement Reformatter Start.")
    output_file = []
    for index, line in enumerate(input_file):
        if line.startswith("#data"):
            start_data_block = index + 1
            break
        output_file.append(line)
    for index, line in enumerate(input_file):
        if line.startswith("#enddata"):
            end_data_block = index
    data_block = []
    for index in range(start_data_block, end_data_block):
        data_block.append(input_file[index])
    logger.debug("DATA Block: {}", data_block)
    if basic_defs.crunch == 1:
        data_statement_start = "DATA"
    else:
        data_statement_start = "DATA "
    data_statement = data_statement_start
    for index, line in enumerate(data_block):
        combined_line_length = len(data_statement) + len(line)
        if combined_line_length <= data_statement_length:
            data_statement = data_statement + line + ","
        elif combined_line_length > data_statement_length:
            data_statement = data_statement.rstrip(",")
            output_file.append(data_statement)
            data_statement = data_statement_start + line + ","
            logger.debug("DATA Statement: {}", data_statement)
        logger.debug("DATA Statement: {}", data_statement)
    data_statement = data_statement.rstrip(",")
    logger.debug("DATA Statement: {}", data_statement)
    output_file.append(data_statement)
    output_file = list(filter(None, output_file))
    return output_file


def create_external_file_dict(external_file):
    """ Returns a dict of labels or variables to replace. """
    external_dict = {}
    for line in external_file:
        current_list = line.split(" ")
        if len(current_list) > 1:
            external_dict[current_list[0]] = current_list[1]
    return external_dict
