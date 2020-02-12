"""Photo Import.

A tool for importing photos from one directory into a hierarchical folder
structure in another directory based on the EXIF data of the photos.

Usage:
    photo-import [options] SOURCE DESTINATION

Arguments:
    SOURCE      directory or photo to be imported
    DESTINATION directory to move photos into

Options:
    -h --help           Show this help.
    -s --silent         Silent mode. No logs will be output to stdout. Not
                        compatible with --dry-run.
    -d --dry-run        Dry-run-only mode. No directories will be created and
                        no files will be moved.
    -m --month-only     Only create folders for months, not individual days.
    -v --version        Show version.

"""
from pathlib import Path

from docopt import docopt

from photoimport import __version__
from photoimport.folders import FileMover, find_companion_files, find_all_photos
from photoimport.photos import read_date
from photoimport.ui import ConsoleWriter


def main():
    """Main entry-point for the photo-import command.

    Processes all provided arguments, and performs the desired actions before
    exiting.
    """
    arguments = docopt(__doc__, version=__version__)

    if arguments["--silent"] and arguments["--dry-run"]:
        ConsoleWriter.fatal(-1, "--silent flag can't be used with --dry-run mode")

    writer = ConsoleWriter(arguments["--silent"])
    mover = FileMover(writer, arguments["DESTINATION"], arguments["--dry-run"], arguments["--month-only"])

    for photo in find_all_photos(Path(arguments["SOURCE"]), writer):
        import_photo(photo, mover)


def import_photo(photo: Path, mover: FileMover) -> None:
    """Import an individual photo using the provided FileMover"""
    date = read_date(photo)
    files = find_companion_files(photo)

    mover.create_directory(date)
    for file in files:
        mover.move_file(file, date)
