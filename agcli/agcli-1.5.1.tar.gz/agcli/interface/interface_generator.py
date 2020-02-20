from ..docparser import parameters_extractor
import os.path
from ..utils import yaml, file_handler


type_deduction = {
    "dir": "Directory",
    "file": "File",
    "int": "Integer",
    "percent": "Percentage"
}

types = ["Directory", "File",
        "Integer", "Percentage",
        "String"]

class InterfaceGenerator():

    def __init__(self, cmd):
        self.cmd = cmd
        self.interface_file = file_handler.file_handler.get_interface_file()

    def deduce_type(self, name):
        """
        Deduce the type of an element according to its name. This process is
        not case-sensitive. If no type can be deduce, the default type 'String'
        is chosen.
        """
        return type_deduction.get(name.casefold(), 'String')

    def add_type(self, elements, key_name):
        """
        Add a type field for each element in the elements list. The type is deduce
        from the value of the 'key_name' field. If an element has no 'key_name' field,
        no process is applied to it and this function keep processing the remainder
        of the elements list.
        """
        for element in elements:
            try:
                type_ = self.deduce_type(element[key_name])
                element['argument_type'] = type_
            except Exception as e:
                continue

    def format_command(self, parser):
        """
        Format all the informations gathered by the parser into a dict in order to
        export it in YAML format.
        """
        self.add_type(parser.options, 'argument_name')
        self.add_type(parser.arguments, 'name')
        yaml_command =  parser.options + parser.arguments + parser.commands
        return yaml_command

    def format_empty(self):
        """
        Generate empty interface
        """
        yaml_command = []
        return yaml_command

    def generate_interface(self, is_empty, parsers_name):
        """
        Generate a YAML file that represents the interface of the command 'cmd'.
        If the interface for this command already exists, this function does nothing
        """
        if os.path.isfile(self.interface_file):
            #The interface already exists
            return
        if is_empty:
            yaml_command = self.format_empty()
        else:
            parser = parameters_extractor.ParametersExtractor(self.cmd, parsers_name)
            yaml_command = self.format_command(parser)
            # /!\ handle command in 2 words, i.e: 'python3 naval_fate.py'
        yaml.write_yaml(self.interface_file, yaml_command)
