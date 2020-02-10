from ruamel.yaml import YAML
from ruamel import yaml


def open_yaml(yaml_file):
    """
    Open a file in YAML format and represents it as a dictionary
    """
    with open(yaml_file, 'r') as file_:
        yaml_content = yaml.safe_load(file_)
    return yaml_content

def write_yaml(filename, data):
    """
    Write a data represented as a dictionary to the specified file. If it doesn't
    exists, the file is created.
    """
    with open(filename, 'w+') as file_:
        yaml = YAML()
        yaml.indent(sequence=6, offset=4)
        yaml.dump(data, file_)
