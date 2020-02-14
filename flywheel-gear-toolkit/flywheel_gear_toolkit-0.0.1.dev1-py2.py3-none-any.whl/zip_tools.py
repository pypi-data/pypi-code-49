"""
Module collection of zip utilities.
"""
from zipfile import ZipFile, ZIP_DEFLATED
import os
import os.path as op
import json
import logging
import re

log = logging.getLogger(__name__)


def unzip_all(input_zip_filename, output_dir, dry_run=False):
    """
    Deliver the contents of a zipped file to a specified location.

    unzip_all unzips the contents of input_zip_filename relative to output_dir,
    All of the files extracted can be tracked with zip_list.  Active if the
    'dry_run' parameter is False.

    Args:
        input_zip_filename (str): Zip file to extract relative to output_dir

        output_dir (str): Root directory to extract input_zip_filename relative
            to

        dry_run (boolean, optional): If True, this prevents initiation of the
            actual zipping of the file.  This is a flag used throughout a gear
            for debugging commands initiated, but not executed.  As some
            commands can take hours to complete, this is useful in finding
            points of failure.

    Examples:
        .. code-block:: python

            unzip_all('/flywheel/v0/inputs/ZIP/file.zip', '/flywheel/v0/work/')
            unzip_all('/flywheel/v0/inputs/ZIP/file.zip', '/flywheel/v0/work/', dry_run = True)
    """
    input_zip = ZipFile(input_zip_filename, 'r')
    log.info(
        'Unzipping file, %s',
        input_zip_filename
    )

    if not dry_run:
        input_zip.extractall(output_dir)


def unzip_config(input_zip_filename, search_str=r'_config\.json'):
    """
    Retrieve the json configuration from a gear zipped file.

    unzip_config reads a file with filename matching search_str from
    input_zip_filename. Returns the contents of that file as a python
    dictionary. Raises a generic exception otherwise. Great for extracting the
    configuration of previous gears in a sequence. Only works on json files.

    Args:
        input_zip_filename (str): Zip file to search for a file with search_str
            in its name

        search_str (regexp, optional): Regular Expression string for the name
            of the config file. Defaults to r'_config.json'.

    Returns:
        dictionary: config dictionary found in zip file

    Example:
        .. code-block:: python

            input_zipfile = '/flywheel/v0/inputs/ZIP/file.zip'
            config = unzip_config(input_zipfile)
    """

    config = {}
    zf = ZipFile(input_zip_filename)
    for fl in zf.filelist:
        if fl.filename[-1] != os.path.sep:  # not (fl.is_dir()):
            # if search_str in filename
            if re.search(search_str, fl.filename):
                json_str = zf.read(fl.filename).decode()
                config = json.loads(json_str)

                # This corrects for leaving the initial "config" key out
                # of previous gear versions without error
                if 'config' not in config.keys():
                    config = {'config': config}

    if not config:
        log.warning('Configuration file is empty or not found.')
        return None

    return config


def zip_output(root_dir, source_dir, output_zip_filename,
               dry_run=False, exclude_files=None):
    """
    Compress gear output into a zipped file.

    zip_output compresses the complete output of the gear relative to the
    root_dir (usually /flywheel/v0/work) and places it in the output
    directory (usually /flywheel/v0/output) to be catalogued by the
    application. The absolute path of the resultant file (output_zip_filename)
    needs to be specified in the upstream function.

    Args:
        output_zip_filename (str): complete path of the resultant output zip
            file

        root_dir (str): The root directory to zip relative to.

        source_dir (str): subdirectory (of <root_dir>) to zip

        dry_run (boolean, optional): Boolean value that determines whether or
            not to execute a full zip compression of source_dir

        exclude_files (list, optional): files in <root_dir>/<source_dir> to
            exclude from the zip file. Defaults to None.

    Raises:
        Exception: root_dir does not exist

    Examples:
        .. code-block:: python

            zip_output('output.zip','gear_output','/flywheel/v0/work')

            zip_output('output.zip','gear_output','/flywheel/v0/work',
                    exclude_files=['sub_dir1/file1.txt','sub_dir2/file2.txt'])

            zip_output('output.zip','gear_output','/flywheel/v0/work',
                    dry_run=True)
    """

    if exclude_files:
        exclude_from_output = exclude_files
    else:
        exclude_from_output = []

    # if root_dir is not defined, set it to the working directory
    if not op.exists(root_dir):
        raise FileNotFoundError(
            f'The directory, {root_dir}, does not exist.'
        )

    log.info('Zipping output file %s', output_zip_filename)
    if not dry_run:
        try:
            os.remove(output_zip_filename)
        except FileNotFoundError:
            pass

        os.chdir(root_dir)
        with ZipFile(output_zip_filename, 'w', ZIP_DEFLATED) as outzip:
            for root, subdirs, files in os.walk(source_dir):
                for fl in files + subdirs:
                    fl_path = op.join(root, fl)
                    # only if the file is not to be excluded from output
                    if fl_path not in exclude_from_output:
                        outzip.write(fl_path)


def zip_list(zip_filename):
    """
    List file contents of a zipfile

    zip_list opens the provided zip filename and returns a list of file paths
    without directories.

    Args:
        zip_filename (str): absolute path of zip file

    Returns:
        list: list of relative-path file members

    Example:
        .. code-block:: python

            zip_list = zip_list('/path/to/zipfile.zip')

    """

    return sorted(
        filter(lambda x: len(x) > 0, [
            x.filename
            if (x.filename[-1] != os.path.sep)
            else ''
            for x in ZipFile(zip_filename).filelist
        ])
    )
