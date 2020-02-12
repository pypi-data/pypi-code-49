"""All the functionality to do with the filesystem

:copyright: Copyright 2019 Edward Armitage.
:license: MIT, see LICENSE for details.
"""
import os
import shutil
from datetime import date
from pathlib import Path
from typing import List, Generator

from photoimport.ui import ConsoleWriter


class FileMover:
    """Class for moving files into a date-organised hierarchy"""

    def __init__(self, writer: ConsoleWriter, base_path: str, dry_run_mode: bool, month_only: bool) -> None:
        """
        :param writer: The ConsoleWriter used to inform of progress
        :param base_path: The directory to build the date-organised hierarchy within
        :param dry_run_mode When true, no folders will be created on the filesystem and no files will
                be actually moved
        :param month_only: Whether to store all files for a given month in the same folder, rather
                than separating by day (default is False)
        """
        self._writer = writer
        self._base_path = Path(base_path)
        self._dry_run_mode = dry_run_mode
        self._month_only = month_only

        if self._dry_run_mode:
            self._writer.status("In dry-run mode. No folders will be created or files moved.")

    def create_directory(self, folder_date: date) -> None:
        """Creates a directory for the given date

        If the required folder does not already exist, it will be created (if not in dry-run
        mode) and log when not in silent mode. If a top-level folder already exists (e.g. the
        year or month folder), the lower level (e.g. month or date) folders will be created
        alongside any existing files.

        :param folder_date: The date of the folder to be created
        """
        directory = self._build_path(folder_date)

        if not os.path.isdir(directory):
            self._writer.action("📂 Creating {}".format(directory))
            if not self._dry_run_mode:
                os.makedirs(directory, exist_ok=True)

    def move_file(self, file: Path, folder_date: date) -> None:
        """Moves a file into an appropriate directory for the given date

        Will only move files if not in dry-run mode. Will log when not in silent
        mode.

        :param file: The file to be moved
        :param folder_date: The date of the folder to move the file into
        """
        directory = self._build_path(folder_date)
        self._writer.action("➡️  Moving {} to {}".format(file, directory))
        if not self._dry_run_mode:
            shutil.move(str(file), directory)

    def _build_path(self, folder_date: date) -> str:
        year = "{:04d}".format(folder_date.year)
        month = "{:02d}".format(folder_date.month)
        day = "{:02d}".format(folder_date.day)

        if self._month_only:
            path = os.path.join(str(self._base_path), year, month)
        else:
            path = os.path.join(str(self._base_path), year, month, day)

        return path


def find_all_photos(source: Path, writer: ConsoleWriter) -> Generator[Path, None, None]:
    """Finds all photos at the given path

    If the source path is the path of a photo, then this is the photo that will be
    imported; alternatively if the source path is of a directory containing photos,
    then the photos within this directory will be imported.

    Any non-photo files will be ignored, but this will be logged if current config
    allows this.

    :param source:  the Path where photos should be found
    :param writer:  the writer used to output any information
    :return:  a generator yielding paths to the photos within source
    """

    def is_photo(file_path: Path):
        """Determine if a file_path points at a photo or not

        This is determined by checking that the provided path is to a file, and that
        the file has a ".jpg" extension.

        Logs a warning if the photo is not deemed to be a photo.

        :param file_path:  the path to be checked
        :return:  True if the path points to a photo; otherwise False
        """
        result = os.path.isfile(str(file_path)) and file_path.suffix == ".jpg"
        if not result:
            writer.status("⚠️ Ignoring {}".format(file_path.name))

        return result

    if is_photo(source):
        yield source
        return

    if os.path.isdir(str(source)):
        for file in source.iterdir():
            if not is_photo(file):
                continue

            yield file


def find_companion_files(file: Path) -> List[Path]:
    """Finds the companion files alongside the provided the file in a given directory

    A companion file is a file within the same directory as the original file, with the same
    name (ignoring file extensions). For example photo-001.raw is a companion to photo-001.jpg,
    but photo-0011.jpg is not.

    :param file: The file to find companions for
    :return: a list of Paths containing the provided file and all companion files
    """
    return list(file.parent.glob("{}.*".format(file.stem)))
