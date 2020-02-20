#!/usr/bin/env python3
'''RAO data downloader'''
import logging
import sys
from dateutil import parser
from dateutil.parser import ParserError
from getraodata import exceptions
from raodata.Data import Data
import raodata


def parse_arguments():
    directory = ""

    try:
        if len(sys.argv) < 3:
            raise BaseException
        instrument = sys.argv[1]
        filetype = sys.argv[2]
        timefrom = parser.parse(sys.argv[3])
        if len(sys.argv) > 4:
            timeto = parser.parse(sys.argv[4])
            if len(sys.argv) > 5:
                directory = sys.argv[5].rstrip("/")
        else:
            timeto = None

        if timeto is None:
            timeto = timefrom
            timeto = timeto.replace(hour=23, minute=59, second=59)

    except (BaseException, ParserError):
        message = (
                   "Radioastronomy Observatory of Institute of " +
                   "Solar-Terrestrial Physics data downloader\n\n" +
                   "Usage:\n" +
                   "    getraodata <instrument> <filetype> <datetimefrom> " +
                   "[datetimeto [directory]]\n\n" +
                   "Available instruments and relevant file types:"
                  )
        instruments = Data().get_types_by_instruments()
        for instrument in instruments:
            string = ", ".join(instrument["types"]["type"])
            message += "\n    " + instrument["instrument"] + " with file type"
            if len(instrument["types"]["type"]) > 1:
                message += "s"
            message += " " + string
        raise exceptions.CannotParseArguments(message)

    return {
            "instrument": instrument,
            "filetype": filetype,
            "timefrom": timefrom,
            "timeto": timeto,
            "saveto": directory
           }


def download_files(files, directory):
    files = list(files)
    total = len(files)
    i = 0
    failed = 0
    downloaded = 0
    print(str(i) + " of " + str(total) + " " +
          plural(total) + " processed", end="")
    for file in files:
        i += 1
        if directory == "":
            date = file.date
            string = (
                      date.strftime("%Y") + "/" +
                      date.strftime("%m") + "/" +
                      date.strftime("%d")
                     )
        else:
            string = directory

        try:
            file.save_to(string + "/" + file.name)
            downloaded += 1
        except (
                raodata.exceptions.CannotDownloadFile,
                raodata.exceptions.InvalidFileHash,
                raodata.exceptions.CannotCreateDirectory
               ):
            failed += 1

        text = (
                "\r" + str(i) + " of " + str(total) +
                " " + plural(total) + " processed"
               )
        if failed > 0:
            text += (
                     ", " +
                     str(downloaded) + " " +
                     plural(downloaded) + " downloaded, " +
                     str(failed) + " " +
                     plural(failed) + " failed"
                    )
        print(text, end="")
    print("")


def plural(n):
    if n != 1:
        return "files"
    else:
        return "file"


def main():
    logging.basicConfig(format='%(message)s')
    logging.getLogger().setLevel(logging.INFO)
    logging.terminator = ""

    logging.getLogger("zeep").setLevel("ERROR")
    logging.getLogger("urllib3.connectionpool").setLevel("ERROR")
    try:
        args = parse_arguments()
        files = Data().get_files(args["instrument"], args["filetype"],
                                 args["timefrom"], args["timeto"])
        download_files(files, args["saveto"])
    except BaseException as error:
        logging.error(str(error))
