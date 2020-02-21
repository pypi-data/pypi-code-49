import json
import os


def read_text(path):
    with open(path, errors="replace") as file:
        text = file.read()
    return text


def write_text(path, data):
    with open(path, 'w+') as file:
        file.write(data)


def read_json(path):
    with open(path) as data_file:
        json_data = json.load(data_file)
    return json_data


def write_json(path, data):
    with open(path, 'w+') as outfile:
        json.dump(data, outfile, sort_keys=True, indent=4, separators=(',', ': '))


def get_files_in_dir(dir_path):
    return [dir_path + file_name for file_name in os.listdir(dir_path)]


def get_relative_path(path_name):
    script_directory = os.path.dirname(__file__)
    return os.path.join(script_directory, path_name)