"""
Contains the class that parses helm values.yaml files into a convenient structure
to use and display in main program.
"""

import yaml
import json
from pprint import pprint
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter

class ValueParser:
    """
    Class that parses values.yaml files to produce a dictionary
    of depth 1 of the form:
    {'key/subkey/.../subsubkey':value}
    """
    def __init__(self):
        self.values = {}

    def parse(self, file):
        """
        Main method that creates the dictionary
        :param file: Path to file to parse
        :type file: String
        :rtype: List
        """
        values = []
        values = yaml.safe_load(open(file))
        for key, value in values.items():
            self.get_value(key, value)

        return self.values

    def get_value(self, k, v):
        """
        Recursive function that creates the tree structure of the dictionary
        :param k: Key of dict
        :type k: String
        :param v: Value of dict
        :type v: String, List or Dict
        :rtype: None
        """
        if isinstance(v, dict):
            if len(v) != 0:
                for key, value in v.items():
                    self.get_value(str(k) + '.' + str(key), value)
            else:
                self.add_entry(k, v)

        elif isinstance(v, list):
            self.add_entry(k, [])
            if len(v) != 0:
                for value in v:
                    if isinstance(value, dict):
                        if value.keys() == dict.keys({'name':'', 'value':''}):
                            self.add_entry(str(k) + '.' + str(list(value.values())[0]),
                                           list(value.values())[1])

                        else:
                            self.get_value(str(k), value)

                    else:
                        self.add_entry(k, value, is_list=True)
            else:
                self.add_entry(k, v)
        else:
            self.add_entry(k, v)

    def add_entry(self, key, value, is_list=False):
        """
        Function that adds the tips of the branches from
        the tree structure to the ValueParser's data.
        :param key: Key of dict
        :type key: String
        :param value: Value of dict
        :type value: String or List
        """
        if is_list:
            self.values[key].append(value)
        else:
            self.values[key] = value

    def parse_with_JSON(self, file):
        """
        Same as parse method but enables JSON syntax coloring down the line
        """

        parsed_dict = self.parse(file)
        for key, value in parsed_dict.items():
            try:
                res = json.loads(value)
                res = json.dumps(res, indent=4)
                res = highlight(res, JsonLexer(), TerminalFormatter()).replace('\n','\n\t'+(len(key)-1)*' ').strip().strip('\n\t')
                parsed_dict[key] = res
            except (ValueError, TypeError):
                pass

        return parsed_dict