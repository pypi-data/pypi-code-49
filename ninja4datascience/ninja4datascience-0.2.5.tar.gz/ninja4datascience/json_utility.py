import json
import os
import stat


def reset_json_values(json_file):
    if os.path.isfile(json_file):
        is_valid = False
        with open(json_file, "r") as f:
            obj_json = json.load(f)
            if len(obj_json) > 0:
                is_valid = True
                i = 0
                while len(obj_json) > i:
                    for j in obj_json[i]:
                        obj_json[i][j] = ""
                    i = i + 1

        if is_valid:
            with open(json_file, "w") as f:
                json.dump(obj_json, f)


def json_replace(data, key):
    key = str(key).replace("_", "").upper()
    return data[0][key]


def set_file_permission(file_path):
    if os.path.isfile(file_path):
        os.chmod(file_path, stat.S_IRWXG)
