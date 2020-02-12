""" This module contains former helper scripts. """

import logging
import re

from basicwrangler.common.constants import RE_QUOTES


def c64_list(input_file):
    """ This converts from C64List format. """
    logging.debug("Convert from C64List format.")
    for index, _ in enumerate(input_file):
        if input_file[index].startswith("{:") and input_file[index].endswith("}"):
            input_file[index] = input_file[index].replace("{:", "_")
            input_file[index] = input_file[index].replace("}", ":")
        else:
            input_file[index] = input_file[index].replace("{:", "_")
            input_file[index] = input_file[index].replace("}", "")
        # This replaces every REM not in quotes with an apostrophe
        input_file[index] = re.sub("REM" + RE_QUOTES, "'", input_file[index])
    return input_file


def data_format(input_file):
    """ This reformats DATA statements. """
    logging.debug("Reformatting DATA Statements into newline-delimitted format.")
    data_statement = "\n#data\n"
    remove_list = []
    for index, line in enumerate(input_file):
        if line.startswith("DATA"):
            stripped = line.lstrip("DATA")
            # This replaces every comma in between DATA statement values
            # not in quotes with a newline
            temp = stripped + "\n"
            temp = re.sub("," + RE_QUOTES, "\n", temp)
            temp = temp.lstrip()
            data_statement = data_statement + temp
            logging.debug("Current DATA block: %s", data_statement)
            remove_list.append(index)
    data_statement = data_statement + "#enddata"
    # This removes the original DATA statements from the file
    # Thanks to Igor Chubin on stackoverflow
    final = [i for j, i in enumerate(input_file) if j not in remove_list]
    final.append(data_statement)
    return final
