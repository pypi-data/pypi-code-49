"""directory_handlers.py: module for handling directory operations."""
import csv
import itertools as iter
import os, errno
from pathlib import Path
import glob
import pandas as pd

from VEnCode.utils import util
from VEnCode.utils.general_utils import str_replace_multi


def file_directory_handler(file_name, folder="", path_type="normal"):
    path = path_handler(path_type)
    file_name = str_replace_multi(file_name, {":": "-", "*": "-", "?": "-", "<": "-", ">": "-", "/": "-"})
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
    name = str_replace_multi(name, {":": "-", "*": "-", "?": "-", "<": "-", ">": "-", "/": "-"})
    file_path_updated = os.path.join(folder, name)
    if os.path.exists(file_path_updated):
        for i in range(1, 10000):
            file_path_temp = file_path_updated.replace(file_type, "") + "-" + str(i) + file_type
            if os.path.exists(file_path_temp):
                continue
            else:
                file_path_updated = file_path_temp
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


""" Writing to File """


def write_list_to_csv(file_name, list_data, folder, path="parent"):
    if path == "parent":
        current_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    elif path == "normal":
        current_path = os.getcwd()
    else:
        raise Exception("path name not recognized!")
    try:
        new_file = current_path + folder + file_name
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        raise
    if not os.path.exists(current_path + folder):
        os.makedirs(current_path + folder)
    with open(new_file, mode='wt', encoding='utf-8') as myfile:
        for line in list_data:
            myfile.write(line)
            myfile.write('\n')


def write_dict_to_csv(file_name, dict_data, folder=None, path="normal", deprecated=True, method="w"):
    """ Starting with a dictionary having key, value pairs where value is a list or similar, writes the dictionary
    to a file named 'file_name'. Remember to include file extension in 'file_name'."""
    if deprecated:
        path_working = path_handler(path)
        try:
            new_file = path_working + folder + file_name
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            raise
        check_if_and_makedir(path_working + folder)
    else:
        new_file = file_name
    keys = sorted(dict_data.keys())
    with open(new_file, method) as csv_file:
        writer = csv.writer(csv_file, delimiter=";", lineterminator='\n')
        writer.writerow(keys)
        try:
            writer.writerows(zip(*[dict_data[key] for key in keys]))
        except TypeError:
            new = [dict_data[key] for key in keys]
            writer.writerow(new)


def write_one_value_dict_to_csv(file_path, dict_data, method="w"):
    """
    Writes a dictionary into a .csv file. This dictionary should have values that are not lists. If so, refer to the
    function "write_dict_to_csv".
    :param str file_path: The complete path to write the data, including file name and .csv extension
    :param dict dict_data: The data
    :param method: method used to write/append to file. "w" writes, "a" appends.
    """
    with open(file_path, method) as csv_file:
        writer = csv.writer(csv_file, delimiter=";", lineterminator='\n')
        for key, value in dict_data.items():
            writer.writerow([key, value])


def write_dict_2_to_csv(file_name, dict_data, folder, path="normal"):
    path_working = path_handler(path)
    try:
        new_file = path_working + folder + file_name
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        raise
    check_if_and_makedir(path_working + folder)
    keys = sorted(dict_data.keys())
    rows = list(iter.zip_longest(*dict_data.values()))
    with open(new_file, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=";", lineterminator='\n')
        writer.writerow(keys)
        writer.writerows(rows)


def files_in_folder_to_csv(folder, file_name):
    files = util.file_names_to_list(folder)
    to_write = {}
    for file in files:
        with open(file) as f:
            values = list()
            for line in f:
                (key, val) = line.rstrip("\n").split(";")
                values.append(val)
            key = file.split("\\")[-1].rstrip(".csv")
            to_write[key] = values
    write_dict_2_to_csv(file_name, to_write, folder, path="parent")


""" Reading from File """


def read_append_multiple_files(dir_, pattern, mode="df", sep=";"):
    files = [f for f in glob.iglob(dir_ + "**/{}.csv".format(pattern), recursive=True)]
    df_from_each_file = (pd.read_csv(f, sep=sep, engine="python") for f in files)
    df_concatenated = pd.concat(df_from_each_file, ignore_index=True)
    if mode == "df":
        return df_concatenated
    elif mode == "csv":
        file_name = "Appended {}".format(pattern)
        path = os.path.join(dir_, file_name)
        df_concatenated.to_csv(path)
        return
    else:
        raise AttributeError("Argument 'mode' is invalid. Check valid values for 'mode'.")
