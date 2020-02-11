import json
import os

import jsonschema
import yaml


def set_f_type(path, f_type):
    if not f_type or f_type not in ('json', 'yaml', 'raw'):
        if path.endswith('.json'):
            f_type = 'json'
        elif path.endswith('.yaml') or path.endswith('.yml'):
            f_type = 'yaml'
        else:
            f_type = 'raw'

    return f_type


def load_file(path, f_type=None):
    f_type = set_f_type(path, f_type)

    try:
        with open(path) as f:
            if f_type == 'json':
                out = json.load(f)
            elif f_type == 'yaml':
                out = yaml.safe_load(f)
            elif f_type == 'raw':
                out = f.read()
            else:
                out = None

        return out
    except Exception as e:
        raise(e)


def write_file(path, data, f_type=None):
    f_type = set_f_type(path, f_type)

    try:
        with open(path, 'w') as f:
            if f_type == 'json':
                json.dump(data, f)
            elif f_type == 'yaml':
                yaml.safe_dump(data, f)
            elif f_type == 'raw':
                f.write(data)
    except Exception as e:
        raise(e)


CONFIG_SCHEMA = load_file(os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    'config_schema.yaml'
))


def validate_config(conf):
    jsonschema.validate(conf, CONFIG_SCHEMA)
