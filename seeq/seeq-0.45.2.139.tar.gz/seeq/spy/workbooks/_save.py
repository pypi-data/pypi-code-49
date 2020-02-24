import os
import tempfile
import zipfile

from seeq.base import system

from ._workbook import Workbook

from .. import _common
from .._common import Status


def save(workbooks, folder_or_zipfile=None, *, datasource_map_folder=None, clean=False):
    """
    Saves a list of workbooks to a folder on disk from Workbook objects in
    memory.

    Parameters
    ----------
    workbooks : {Workbook, list[Workbook]}
        A Workbook object or list of Workbook objects to save.

    folder_or_zipfile : str, default os.getcwd()
        A folder or zip file on disk to which to save the workbooks. It will be saved as a
        "flat" set of subfolders, no other hierarchy will be created. The string must end in
        ".zip" to cause a zip file to be created instead of a folder.

    datasource_map_folder : str, default None
        Specifies a curated set of datasource maps that should accompany the
        workbooks (as opposed to the default maps that were created during the
        spy.workbooks.pull call).

    clean : bool, default False
        True if the target folder should be removed prior to saving the
        workbooks.
    """
    _common.validate_argument_types([
        (workbooks, 'workbooks', (Workbook, list)),
        (folder_or_zipfile, 'folder_or_zipfile', str),
        (datasource_map_folder, 'datasource_map_folder', str),
        (clean, 'clean', bool)
    ])

    status = Status()

    try:
        if not isinstance(workbooks, list):
            workbooks = [workbooks]

        if folder_or_zipfile is None:
            folder_or_zipfile = os.getcwd()

        zip_it = folder_or_zipfile.lower().endswith('.zip')

        if clean and os.path.exists(folder_or_zipfile):
            status.update('Removing "%s"' % folder_or_zipfile, Status.RUNNING)
            if os.path.isdir(folder_or_zipfile):
                system.removetree(folder_or_zipfile, keep_top_folder=True)
            else:
                os.remove(folder_or_zipfile)

        datasource_maps = None if datasource_map_folder is None else Workbook.load_datasource_maps(
            datasource_map_folder)

        save_folder = None
        try:
            save_folder = tempfile.mkdtemp() if zip_it else folder_or_zipfile

            for workbook in workbooks:  # type: Workbook
                if not isinstance(workbook, Workbook):
                    raise RuntimeError('workbooks argument must be a list of Workbook objects')

                workbook_folder_name = '%s (%s)' % (workbook.name, workbook.id)
                workbook_folder = os.path.join(save_folder, system.cleanse_filename(workbook_folder_name))

                if datasource_maps is not None:
                    workbook.datasource_maps = datasource_maps

                status.update('Saving to "%s"' % workbook_folder, Status.RUNNING)
                workbook.save(workbook_folder)

            if zip_it:
                status.update('Zipping "%s"' % folder_or_zipfile, Status.RUNNING)
                with zipfile.ZipFile(folder_or_zipfile, "w", zipfile.ZIP_DEFLATED) as z:
                    for root, dirs, files in os.walk(save_folder):
                        for file in files:
                            filename = os.path.join(root, file)
                            if os.path.isfile(filename):  # regular files only
                                archive_name = os.path.join(os.path.relpath(root, save_folder), file)
                                print('Archiving %s' % archive_name)
                                z.write(filename, archive_name)

        finally:
            if save_folder and zip_it:
                system.removetree(save_folder)

        status.update('Success', Status.SUCCESS)

    except KeyboardInterrupt:
        status.update('Save canceled', Status.CANCELED)
