import csv
import itertools as iter
import os

from VEnCode.utils import dir_and_file_handling

from VEnCode.utils import util


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
        path_working = dir_and_file_handling.path_handler(path)
        try:
            new_file = path_working + folder + file_name
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            raise
        dir_and_file_handling.check_if_and_makedir(path_working + folder)
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
    return


def write_one_value_dict_to_csv(file_name, dict_data, folder, path="parent"):
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
    with open(new_file, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=";", lineterminator='\n')
        for key, value in dict_data.items():
            writer.writerow([key, value])
    return


def write_dict_2_to_csv(file_name, dict_data, folder, path="normal"):
    path_working = dir_and_file_handling.path_handler(path)
    try:
        new_file = path_working + folder + file_name
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        raise
    dir_and_file_handling.check_if_and_makedir(path_working + folder)
    keys = sorted(dict_data.keys())
    rows = list(iter.zip_longest(*dict_data.values()))
    with open(new_file, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=";", lineterminator='\n')
        writer.writerow(keys)
        writer.writerows(rows)
    return


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