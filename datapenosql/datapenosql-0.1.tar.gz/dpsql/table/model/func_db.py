import logging
from enum import Enum
from typing import Tuple, List

from dpsql.table.model.case_obj import CaseObjectContent


class ExtractField(Enum):
    Year = 1
    Month = 2
    Day = 3
    Hour = 4
    Minute = 5
    Second = 6
    TimeZone_Hour = 7
    TimeZone_Minute = 8
    TimeZone_Region = 9
    TimeZone_ABBR = 10


class DBFunc(object):
    def __init__(self, **kwargs):
        self._alias = kwargs.get('alias', '')
        self._func_str: str = ''

    @property
    def alias_(self):
        return self._alias

    @property
    def func_str_(self):
        return self._func_str

    @alias_.setter
    def alias_(self, param):
        self._alias = param

    @func_str_.setter
    def func_str_(self, param):
        self._func_str = param

    def __str__(self):
        return self.func_str_

    def __repr__(self):
        return self.func_str_

    def extract_(self, column: str = '', field: ExtractField = None):
        res = ''
        if field != ''and column != '':
            res = f"Extract({field.name} From {column})"
        self.func_str_ = res
        return res

    def case_(self, cases: List[CaseObjectContent], else_: str = ''):

        res = 'CASE '
        for case in cases:
            res += f"WHEN {str(case.when_criteria_)} THEN {case.then_} "

        if else_ != '':
            res += f"ELSE {else_}"

        res = f"{res} END"
        self.func_str_ = res
        return res

    def exists_(self, query: str = ''):
        res = ''
        if query != '':
            res = f"Exists ({query})"
        self.func_str_ = res
        return res

    def not_exists_(self, query: str = ''):
        res = ''
        if query != '':
            res = f"Not Exists ({query})"
        self.func_str_ = res
        return res

    @staticmethod
    def custom_function_(func_method: str = '', alias: str = ''):
        res = f"{func_method}"
        if alias != '':
            res += f' {alias}'

        return res


class StrFunc(DBFunc):
    def __init__(self, **kwargs):
        super(StrFunc, self).__init__(**kwargs)
        self._input_source: List = kwargs.get('columns', '')

    @property
    def input_source_(self):
        return self._input_source

    @input_source_.setter
    def input_source_(self, param):
        self._input_source = param

    def lpad_(self, length=0, pad_by=''):
        src = self.input_source_[0]
        if pad_by == '':
            res = f"LPAD({src}, {length})"
        else:
            res = f"LPAD({src}, {length}, '{pad_by}')"

        self.func_str_ = res
        return res

    def rpad_(self, length=0, pad_by=''):
        src = self.input_source_[0]
        if pad_by == '':
            res = f"RPAD({src}, {length})"
        else:
            res = f"RPAD({src}, {length}, '{pad_by}')"

        self.func_str_ = res
        return res

    def rtrim_(self, rtrim_by=''):
        src = self.input_source_[0]
        if rtrim_by == '':
            res = f"RTRIM({src})"
        else:
            res = f"RTRIM({src}, '{rtrim_by}')"

        self.func_str_ = res
        return res

    def ltrim_(self, ltrim_by=''):
        src = self.input_source_[0]
        if ltrim_by == '':
            res = f"LTRIM({src})"
        else:
            res = f"LTRIM({src}, '{ltrim_by}')"

        self.func_str_ = res
        return res

    def trim_(self, trim_by='', leading=False, trailing=False, both=False):
        src = self.input_source_[0]
        if trim_by == '':
            res = f"TRIM({src})"
        else:
            if leading is False and trailing is False and both is False:
                res = f"TRIM('{trim_by}' FROM {src})"

            elif leading is True:
                res = f"TRIM(LEADING '{trim_by}' FROM {src})"

            elif trailing is True:
                res = f"TRIM(TRAILING '{trim_by}' FROM {src})"

            elif both is True:
                res = f"TRIM(BOTH '{trim_by}' FROM {src})"

        self.func_str_ = res
        return res

    def substr_(self, start=1, steps=0):
        src = self.input_source_[0]
        if steps == 0:
            res = f"SUBSTR({src}, {start})"
        else:
            res = f"SUBSTR({src}, {start}, {steps})"

        self.func_str_ = res
        return res

    def concat_(self):
        res = ' || '.join(var for var in self.input_source_)

        self.func_str_ = res
        return res

    def decode_(self, options: List[Tuple]):
        src = self.input_source_[0]
        res = ''
        if options:
            res = f"Decode({src}"
            for tup in options:
                if len(tup) > 1:
                    res += f', {tup[0]}, {tup[1]}'
                else:
                    res += f', {tup[0]}'
            res += ')'
        self.func_str_ = res
        return res
