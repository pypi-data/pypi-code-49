#!/usr/bin/env python3
""" basic-wrangler - A BASIC program listing line renumberer/cruncher. """

import logging
import os
import re
import sys
from pathlib import Path

import duallog
import pyperclip
from gooey import Gooey, GooeyParser

import basicwrangler.common.functions as functions
import basicwrangler.convert.helpers as helpers
import basicwrangler.convert.label as label
import basicwrangler.defs.basdefs as basdefs
import basicwrangler.renum.renumber as renumber

# constants
from basicwrangler.common.constants import NO_TOKENIZER, RE_QUOTES
from basicwrangler.lex.genlex import generate_lexer, generate_splitter

# This is needed to make the GUI version work on Windows.
if os.name == "nt":
    TARGET_EXE = "bw.exe"
else:
    TARGET_EXE = "bw"

# This is needed to make it not load the GUI when you only want to run the CLI.
if len(sys.argv) >= 2:
    if not "--ignore-gooey" in sys.argv:
        sys.argv.append("--ignore-gooey")

# This is needed to find files when running with pyinstaller.
if hasattr(sys, "_MEIPASS"):
    ICON_DIR = Path.joinpath(Path(sys._MEIPASS).resolve(), "icon")  # type: ignore # pylint: disable=no-member,protected-access
else:
    ICON_DIR = Path.joinpath(Path(__file__).resolve().parent, "icon")

VERSION = "0.6.0"
TOKENIZER_NAME_CONVERSION = {
    "pet": "cbm4",
    "vic20": "cbm2",
    "c64": "cbm2",
    "plus4": "cbm35",
    "c128": "cbm7",
    "trs80m4": "trs80l2",
}


def renum(args):
    """ Renumbers BASIC listings. """
    # set variables from CLI or GUI arguments
    basic_type = args.basic_type
    input_filename = args.input_filename
    paste_format = args.paste_mode
    basic_line_length = args.line_length
    numbering = args.numbering
    increment = args.increment
    user_filename = args.output_filename

    # open the input file
    with open(input_filename) as file:
        original_file = file.read()
    split_file = original_file.splitlines()

    # get BASIC definition namedtuple
    basic_defs, paste_format = basdefs.set_basic_defs(
        basic_type, paste_format, basic_line_length, numbering, increment
    )

    # strip and remove comments
    working_file = functions.strip_file(split_file)
    working_file = functions.remove_comments(working_file)

    # reformat DATA statements if needed
    for line in working_file:
        if line.startswith("#data"):
            working_file = functions.reformat_data_statements(working_file, basic_defs)

    # Generate a tokenizer
    if basic_type in TOKENIZER_NAME_CONVERSION:
        lexer_basic_type = TOKENIZER_NAME_CONVERSION[basic_type]
    elif basic_type in NO_TOKENIZER:
        lexer_basic_type = "generic"
    else:
        lexer_basic_type = basic_type
    Lexer = generate_lexer(lexer_basic_type, renum=True)

    # create a dictionary containing all the jump target labels
    label_dict, line_replacement = renumber.populate_label_data(Lexer, working_file)

    # renumber the BASIC file
    working_file = renumber.renumber_basic_file(
        Lexer, working_file, basic_defs, label_dict, line_replacement, basic_type
    )
    logging.debug("Labels and Computed Line Numbers: %s", label_dict)

    # abbreviate statements if needed
    if basic_defs.abbreviate:
        working_file = basdefs.abbreviate(working_file, basic_type)

    # add newlines back in to the file
    atascii_file = None
    if basic_type == "atari" and not paste_format:  # special ATASCII routine
        atascii_list = [a.encode() for a in working_file]
        atascii_file = b"\x9b".join(atascii_list)
        atascii_file = atascii_file + b"\x9b"
    else:
        final_file = "\n".join(working_file)
        final_file = final_file + "\n"

    # add a POKE statement to Atari pasted files to expand the display so more text can be pasted in
    if basic_type == "atari" and paste_format:
        final_file = "POKE 82,0\n" + final_file

    # adjust case if needed when pasting
    if paste_format and basic_defs.case == "lower":
        final_file = final_file.lower()
    elif paste_format and basic_defs.case == "invert":
        final_file = final_file.swapcase()
    elif basic_type == "zx81":
        # Set ZX81 output to uppercase and replace invalid characters.
        final_file = final_file.upper()
        final_file = final_file.replace("!", ".")
        final_file = final_file.replace("#", " ")
        final_file = final_file.replace("%", " ")
        final_file = final_file.replace("^", " ")
        final_file = final_file.replace("&", " ")
        final_file = final_file.replace("'", ",")

    # set the final filename
    if user_filename:
        temp_filename = user_filename
    else:
        temp_filename = input_filename
    if basic_type == "zx81":
        output_filename = temp_filename[0:-4] + "-out.b81"
    elif basic_type == "zxspectrum":
        output_filename = temp_filename[0:-4] + "-out.b82"
    elif basic_type == "amiga":
        output_filename = temp_filename[0:-4] + ".b"
    elif basic_type == "riscos":
        output_filename = temp_filename[0:-4] + ",ffb"
    elif not user_filename:
        output_filename = temp_filename[0:-4] + "-out.bas"
    else:
        output_filename = temp_filename

    # change the newline type if needed
    newline_type = "\r\n"
    if basic_type in ["amiga", "riscos"]:
        newline_type = "\n"

    # write or paste the renumbered file
    if paste_format:
        pyperclip.copy(final_file)
    if not paste_format or user_filename:
        if atascii_file:
            with open(output_filename, "wb") as file:
                file.write(atascii_file)
        else:
            with open(output_filename, "w", newline=newline_type) as file:
                file.write(final_file)

    # output to console that the file has been saved
    if not paste_format or user_filename:
        print(f"{input_filename} has been saved as {output_filename}")


def convert(args):
    """ Converts between listing formats. """
    input_filename = args.input_filename
    user_filename = args.output_filename
    if args.basic_type:
        if args.basic_type in TOKENIZER_NAME_CONVERSION:
            basic_type = TOKENIZER_NAME_CONVERSION[args.basic_type]
        else:
            basic_type = args.basic_type
    else:
        basic_type = "generic"
    with open(input_filename) as file:
        original_file = file.read()
    if basic_type == "trs80l1":
        original_file = original_file.upper()
    split_file = original_file.splitlines()
    working_file = functions.strip_file(split_file)
    if basic_type == "trs80l1":
        working_file = basdefs.abbreviate(working_file, basic_type, True)
    if basic_type == "atari":
        working_file = basdefs.abbreviate(working_file, basic_type, True)
    if basic_type == "zxspectrum":
        for index, line in enumerate(working_file):
            working_file[index] = re.sub("GO TO" + RE_QUOTES, "GOTO", line)
        for index, line in enumerate(working_file):
            working_file[index] = re.sub("GO SUB" + RE_QUOTES, "GOSUB", line)
    if args.split:
        split_string = generate_splitter()
        new_file = []
        if basic_type.startswith("cbm"):
            splitter = re.compile("(" + split_string + r"|\".*?\")", re.IGNORECASE)
        else:
            splitter = re.compile("(" + split_string + r"|\".*?\")")
        for line in working_file:
            temp1 = re.split(splitter, line)
            temp2 = [x for x in temp1 if x.strip()]
            new_line = " ".join(temp2)
            new_file.append(new_line)
        working_file = new_file
    if not args.c64_list:
        working_file = label.label_listing(working_file, basic_type)
    if args.c64_list:
        working_file = helpers.c64_list(working_file)
    if args.data_formatter:
        working_file = helpers.data_format(working_file)
    final_file = "\n".join(working_file)
    final_file = final_file + "\n"
    if user_filename:
        temp_filename = user_filename
    else:
        temp_filename = input_filename
    if not user_filename:
        output_filename = temp_filename[0:-4] + "-out.bas"
    else:
        output_filename = temp_filename
    with open(output_filename, "w") as file:
        file.write(final_file)
    print(f"{input_filename} has been saved as {output_filename}")


@Gooey(
    program_name="BASIC Wrangler",
    default_size=(610, 695),
    navigation="TABBED",
    target=TARGET_EXE,
    image_dir=ICON_DIR,
    menu=[
        {
            "name": "File",
            "items": [
                {
                    "type": "AboutDialog",
                    "menuTitle": "About",
                    "name": "BASIC Wrangler",
                    "description": "A BASIC program listing line renumberer/cruncher",
                    "version": VERSION,
                    "copyright": "© 2020",
                    "website": "https://github.com/pahandav/basic-wrangler",
                    "license": "GPL v3",
                }
            ],
        }
    ],
)
def main():
    """ The main function. """
    duallog.setup("logs")

    # set up argument parser and get arguments
    parser = GooeyParser(
        description="A BASIC program listing line renumberer/cruncher."
    )
    subparsers = parser.add_subparsers(help="sub-command help")
    # renumber subparser
    parser_renum = subparsers.add_parser("renum", help="renum help")
    parser_renum.add_argument(
        "basic_type",
        choices=basdefs.get_basic_dialects(),
        metavar="BASIC_Type",
        help="Specify the BASIC dialect to use.",
    )
    parser_renum.add_argument(
        "input_filename",
        metavar="filename",
        help="Specify the file to process.",
        widget="FileChooser",
    )
    parser_renum.add_argument(
        "-o",
        "--output-filename",
        dest="output_filename",
        help="Set the output filename.",
        widget="FileSaver",
    )
    parser_renum.add_argument(
        "-p",
        "--paste-mode",
        dest="paste_mode",
        action="store_true",
        default=False,
        help="Sets paste to clipboard mode.",
    )
    parser_renum.add_argument(
        "-l",
        "--line-length",
        dest="line_length",
        type=int,
        help="Set a non-default maximum BASIC line length.",
    )
    parser_renum.add_argument(
        "-n",
        "--numbering_start",
        dest="numbering",
        type=int,
        help="Set the line number to begin numbering with.",
    )
    parser_renum.add_argument(
        "-i",
        "--increment",
        dest="increment",
        type=int,
        help="Set the increment between BASIC lines.",
    )
    parser_renum.set_defaults(func=renum)
    # convert subparser
    parser_convert = subparsers.add_parser("convert", help="convert help")
    parser_convert.add_argument(
        "input_filename",
        metavar="filename",
        help="Specify the file to process.",
        widget="FileChooser",
    )
    parser_convert.add_argument(
        "-b",
        "--basic-type",
        dest="basic_type",
        choices=basdefs.get_basic_dialects(True),
        metavar="BASIC_Type",
        help="Specify the BASIC dialect to use.",
    )
    parser_convert.add_argument(
        "-c",
        "--c64-list",
        action="store_true",
        default=False,
        help="Convert from C64List format.",
    )
    parser_convert.add_argument(
        "-d",
        "--data-formatter",
        action="store_true",
        default=False,
        help="Reformat DATA Statments.",
    )
    parser_convert.add_argument(
        "-s",
        "--split",
        action="store_true",
        default=False,
        help="Split a crunched listing.",
    )
    parser_convert.add_argument(
        "-o",
        "--output-filename",
        dest="output_filename",
        help="Set the output filename.",
        widget="FileSaver",
    )
    parser_convert.set_defaults(func=convert)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
