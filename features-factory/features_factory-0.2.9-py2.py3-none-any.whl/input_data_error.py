import copy
from typing import Tuple, Dict, Hashable

import pandas as pd


class InputDataError:
    """
    Class that collects errors in the input data.

    There are 3 types of errors:
    1. missing columns
    2. columns with nan
    3. columns with wrong format
    """

    def __init__(self):
        self._missing_columns = set()
        self._columns_with_nan = set()
        self._columns_with_wrong_format = set()
        self._wrong_format_values_per_column = dict()

    def __add__(self, other):
        ies_sum = copy.deepcopy(self)

        ies_sum._missing_columns = ies_sum._missing_columns.union(other._missing_columns)
        ies_sum._columns_with_nan = ies_sum._columns_with_nan.union(other._columns_with_nan)
        ies_sum._columns_with_wrong_format = ies_sum._columns_with_wrong_format.union(other._columns_with_wrong_format)

        for k, vs in other._wrong_format_values_per_column.items():
            if k in ies_sum._wrong_format_values_per_column.keys():
                ies_sum._wrong_format_values_per_column[k] += vs
            else:
                ies_sum._wrong_format_values_per_column[k] = vs

        return ies_sum

    def is_empty(self) -> bool:
        return False if any((self.has_missing_columns(),
                             self.has_columns_with_nan(),
                             self.has_columns_with_wrong_format())) else True

    def has_missing_columns(self) -> bool:
        return True if len(self._missing_columns) > 0 else False

    def has_columns_with_nan(self) -> bool:
        return True if len(self._columns_with_nan) > 0 else False

    def has_columns_with_wrong_format(self) -> bool:
        return True if len(self._columns_with_wrong_format) > 0 else False

    def get_missing_columns(self) -> Tuple:
        return tuple(self._missing_columns)

    def get_columns_with_nan(self) -> Tuple:
        return tuple(self._columns_with_nan)

    def get_columns_with_wrong_format(self) -> Tuple:
        return tuple(self._columns_with_wrong_format)

    def get_wrong_format_values_per_column(self) -> Dict:
        return self._wrong_format_values_per_column.copy()

    def add_missing_column(self, column_name: str):
        self._missing_columns.add(column_name)

    def add_column_with_nan(self, column_name: str):
        self._columns_with_nan.add(column_name)

    def add_column_with_wrong_format(self, column_name: str, value: Hashable = None):
        self._columns_with_wrong_format.add(column_name)

        if value is not None:
            if column_name not in self._wrong_format_values_per_column.keys():
                self._wrong_format_values_per_column[column_name] = [value]
            else:
                self._wrong_format_values_per_column[column_name].append(value)

    def to_string(self) -> str:
        lines = list()
        lines.append('InputDataError {}'.format('is empty.' if self.is_empty() else 'contains errors:'))

        if self.has_missing_columns():
            lines.append(' * missing columns = ' + ', '.join(self.get_missing_columns()))

        if self.has_columns_with_nan():
            lines.append(' * columns with nan = ' + ', '.join(self.get_columns_with_nan()))

        if self.has_columns_with_wrong_format():
            lines.append(' * columns with wrong format = ' + ', '.join(self.get_columns_with_wrong_format()))

            if len(self._wrong_format_values_per_column) > 0 :
                lines.append('    * examples of wrong format values:')
                for k, vs in self._wrong_format_values_per_column.items():
                    lines.append('      [{}] : {}'.format(k, pd.Series(vs).unique()))

        return '\n'.join(lines)
