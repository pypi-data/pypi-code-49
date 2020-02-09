"""directory_handlers.py: module for handling directory operations."""
import os, errno
from pathlib import Path
from VEnCode.utils.general_utils import str_replace_multi

def file_directory_handler(file_name, folder="", path_type="normal"):
    path = path_handler(path_type)
    try:
        new_file = os.path.join(path, folder, file_name)
        directory = os.path.join(path, folder)
    except TypeError:
        new_file = path + file_name
        directory = path
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        raise
    check_if_and_makedir(directory)
    return new_file


def check_if_and_makedir(folder):
    """
    Checks if directory exists. If not, makes new folder.
    :param folder: directory to check and make.
    :return: None
    """
    if not os.path.exists(folder):
        os.makedirs(folder)
        return


def check_if_and_makefile(filename, path=None, file_type=".csv", path_type="normal"):
    """
    Checks if file and folders exist in path (optional, otherwise specify path_type). If folder does not exist, makes
    new folder. If file exists, appends an unique number in front of the name before assigning the file type.
    :param filename: name of file to check
    :param path: Path to check/create. Optional, if None then path_type is used.
    :param file_type: Desired file extension.
    :param path_type: If path is None then path_type is used to get the path.
    :return: New file path
    """
    if path is None:
        file_path = file_directory_handler(filename, path_type=path_type)
    else:
        file_path = os.path.join(path, filename)
    file_path += file_type
    folder, name = os.path.split(file_path)
    if folder:
        check_if_and_makedir(folder)
    name = str_replace_multi(name, {":": "-", "*": "-", "?": "-", "<": "-", ">": "-"})
    file_path_updated = os.path.join(folder, name)
    if os.path.exists(file_path_updated):
        for i in range(1, 10000):
            file_path_updated = file_path_updated.replace(file_type, "") + "-" + str(i) + file_type
            if os.path.exists(file_path_updated):
                continue
            else:
                break
    return file_path_updated


def path_handler(path_type):
    """ Gets the desired path in your OS """
    if path_type == "parent":
        # path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
        path = str(Path(__file__).parents[1])
    elif path_type == "parent2":
        # path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.pardir))
        path = str(Path(__file__).parents[2])
    elif path_type == "parent3":
        path = str(Path(__file__).parents[3])
    elif path_type == "normal":
        path = os.getcwd()
    else:
        raise Exception("path name not recognized!")
    return path


def remove_file(file_path):
    """
    Removes the file if it exists.
    :param file_path: the path to the file to remove.
    """
    try:
        os.remove(file_path)
    except OSError as e:
        if e.errno != errno.ENOENT:  # errno.ENOENT = no such file or directory
            raise  # re-raise exception if a different error occurred
