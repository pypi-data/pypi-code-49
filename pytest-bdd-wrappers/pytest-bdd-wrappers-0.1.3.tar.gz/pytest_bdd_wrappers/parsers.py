"""Additional parsers for BDD
"""
import re
from abc import ABC

from pytest_bdd.parsers import StepParser, string


class MultiLineStepParser(StepParser, ABC):
    """Base class for multi line parsers
    """
    def __init__(self, name, converters=None):
        """
        :type name: StepParser|str
        :param converters:
            Dict with converters for data table values.
            Converter is called with original string value from scenario.
        :type converters: dict
        """
        self._name_parser = (
            name if isinstance(name, StepParser) else string(name)
        )
        self._converters = converters or dict()
        super(MultiLineStepParser, self).__init__(self._name_parser.name)

    def _convert_values(self, arguments):
        """
        :type arguments: dict
        :rtype: dict
        """
        return {
            key: self._converters.get(key, str)(value)
            for key, value in arguments.items()
        }

    @staticmethod
    def _split_name_and_body(name):
        """
        :type name: str
        :rtype: tuple[str, list[str]]
        """
        lines = name.strip().split('\n')
        return lines[0], lines[1:]


class dtparser(MultiLineStepParser):
    """Parser for steps with DataTable
    Example:
        Given accounts:
          | login | email       |
          | test1 | test1@email |
          | test2 | test1@email |
    """
    def parse_arguments(self, name):
        """
        :type name: str
        :rtype: dict
        """
        name, body = self._split_name_and_body(name)
        arguments = self._name_parser.parse_arguments(name)

        header_line, dt_lines = body[0], body[1:]
        headers = self._split_dt_line(header_line)

        arguments['datatable'] = [
            self._convert_values(
                dict(zip(headers, self._split_dt_line(line)))
            )
            for line in dt_lines
        ]
        return arguments

    @staticmethod
    def _split_dt_line(line):
        """
        :type line: str
        :rtype: list[str]
        """
        return [col.strip() for col in line.strip().split('|') if col.strip()]

    def is_matching(self, name):
        """
        :type name: str
        :rtype: bool
        """
        name, body = self._split_name_and_body(name)
        if len(body) < len(['header', 'data line']):
            return False

        header, dt = body[0], body[1:]
        if not self._name_parser.is_matching(name):
            return False

        col_splitters = header.count('|')
        if col_splitters < len(['opening', 'closing']):
            return False

        if any([l.count('|') != col_splitters for l in dt]):
            return False

        return True


class mvparser(MultiLineStepParser):
    def parse_arguments(self, name):
        """
        :type name: str
        :rtype: dict
        """
        name, body = self._split_name_and_body(name)
        arguments = self._name_parser.parse_arguments(name)
        values = dict(self._split_value_line(line) for line in body)
        arguments['values'] = self._convert_values(values)
        return arguments

    @staticmethod
    def _split_value_line(line):
        """
        :type line: str
        :rtype: tuple[str, str]
        """
        name, value = line.strip().split(':')
        return name.strip(), value.strip()

    def is_matching(self, name):
        """
        :type name: str
        :rtype: bool
        """
        name, body = self._split_name_and_body(name)
        if not body:
            return False

        value_line_pattern = re.compile(r'\s*[A-Za-z0-9_]+\s*:.*')
        if not all(map(value_line_pattern.match, body)):
            return False

        return True
