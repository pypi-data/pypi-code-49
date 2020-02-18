from __future__ import annotations

import logging
from enum import Enum
from typing import List, Dict

from dpsql.table.model.func_aggregate import AggregateFunc
from dpsql.table.model.func_db import DBFunc
from dpsql.table.model.criterion_obj import AttrCriterion


class QueryTable(object):
    def __init__(self, **kwargs):
        self._columns: Dict[Column]  = kwargs.get('columns', None)
        self._name: str = kwargs.get('name', '')
        self._alias: str = kwargs.get('alias', '')
        self._from_name: str = kwargs.get('from_name', '')
        self._join_str = ''

    def __str__(self):
        return self.table_name_getter()

    def __repr__(self):
        return self.table_name_getter()

    @property
    def columns_(self):
        return self._columns

    @property
    def from_name_(self):
        self._from_name = self.table_name_set_alias()
        return self._from_name

    @property
    def name_(self):
        return self._name

    @property
    def alias_(self):
        return self._alias

    @property
    def join_str_(self):
        return self._join_str

    @columns_.setter
    def columns_(self, param: List[Column]):
        self._columns = param

    @from_name_.setter
    def from_name_(self, param: str):
        self._from_name = param

    @name_.setter
    def name_(self, param: str):
        self._name = param

    @alias_.setter
    def alias_(self, param):
        self._alias = param

    @join_str_.setter
    def join_str_(self, param):
        self._join_str = param

    def table_name_getter(self):
        res = self.name_
        if self.alias_ != "":
            res = self.alias_

        return res

    def inner_join_(self, right_table, on):
        logger = logging.getLogger(__name__)
        res = ''
        try:
            left_t = self.from_name_
            right_t = right_table
            if self.join_str_ == '':
                res = f"{left_t} inner join {right_t} on ("
                res += f"{' and '.join(str(crit) for crit in on)}) "
                self.join_str_ = res
                right_t.join_str_ = res
            else:
                res = f"inner join {right_t} on ("
                res += f"{' and '.join(str(crit) for crit in on)}) "
                self.join_str_ += res
                right_t.join_str_ = self.join_str_

            return right_t

        except TypeError as error:
            logger.exception('The Join does not contain On attributes', exc_info=True)

    def left_outer_join_(self, right_table, on):
        logger = logging.getLogger(__name__)
        res = ''
        try:
            left_t = self.from_name_
            right_t = right_table
            if self.join_str_ == '':
                res = f"{left_t} left outer join {right_t} on ("
                res += f"{' and '.join(str(crit) for crit in on)}) "
                self.join_str_ = res
                right_t.join_str_ = res
            else:
                res = f"left outer join {right_t} on ("
                res += f"{' and '.join(str(crit) for crit in on)}) "
                self.join_str_ += res
                right_t.join_str_ = self.join_str_

            return right_t

        except TypeError as error:
            logger.exception('The Join does not contain On attributes', exc_info=True)

    def right_outer_join_(self, right_table, on):
        logger = logging.getLogger(__name__)
        res = ''
        try:
            left_t = self.from_name_
            right_t = right_table
            if self.join_str_ == '':
                res = f"{left_t} right outer join {right_t} on ("
                res += f"{' and '.join(str(crit) for crit in on)}) "
                self.join_str_ = res
                right_t.join_str_ = res
            else:
                res = f"right outer join {right_t} on ("
                res += f"{' and '.join(str(crit) for crit in on)}) "
                self.join_str_ += res
                right_t.join_str_ = self.join_str_

            return right_t

        except TypeError as error:
            logger.exception('The Join does not contain On attributes', exc_info=True)

    def natural_join_(self, right_table, on):
        logger = logging.getLogger(__name__)
        res = ''
        try:
            left_t = self.from_name_
            right_t = right_table
            if self.join_str_ == '':
                res = f"{left_t} natural join {right_t} on ("
                res += f"{' and '.join(str(crit) for crit in on)}) "
                self.join_str_ = res
                right_t.join_str_ = res
            else:
                res = f"natural join {right_t} on ("
                res += f"{' and '.join(str(crit) for crit in on)}) "
                self.join_str_ += res
                right_t.join_str_ = self.join_str_

            return right_t

        except TypeError as error:
            logger.exception('The Join does not contain On attributes', exc_info=True)

    def natural_left_join_(self, right_table, on):
        logger = logging.getLogger(__name__)
        res = ''
        try:
            left_t = self.from_name_
            right_t = right_table
            if self.join_str_ == '':
                res = f"{left_t} natural left join {right_t} on ("
                res += f"{' and '.join(str(crit) for crit in on)}) "
                self.join_str_ = res
                right_t.join_str_ = res
            else:
                res = f"natural left join {right_t} on ("
                res += f"{' and '.join(str(crit) for crit in on)}) "
                self.join_str_ += res
                right_t.join_str_ = self.join_str_

            return right_t

        except TypeError as error:
            logger.exception('The Join does not contain On attributes', exc_info=True)

    def natural_right_join_(self, right_table, on):
        logger = logging.getLogger(__name__)
        res = ''
        try:
            left_t = self.from_name_
            right_t = right_table
            if self.join_str_ == '':
                res = f"{left_t} natural right join {right_t} on ("
                res += f"{' and '.join(str(crit) for crit in on)}) "
                self.join_str_ = res
                right_t.join_str_ = res
            else:
                res = f"natural right join {right_t} on ("
                res += f"{' and '.join(str(crit) for crit in on)}) "
                self.join_str_ += res
                right_t.join_str_ = self.join_str_

            return right_t

        except TypeError as error:
            logger.exception('The Join does not contain On attributes', exc_info=True)

    def column_name_getter(self):
        table_name = self.table_name_getter()
        res = f"{table_name}.*"
        if self.columns_:
            res = ''
            for column in self.columns_:
                if column.alias_ != '':
                    if res != '':
                        res += f', {table_name}.{column.name_} AS {column.alias_}'
                    else:
                        res += f'{table_name}.{column.name_} AS {column.alias_}'
                else:
                    if res != '':
                        res += f', {table_name}.{column.name_}'
                    else:
                        res += f'{table_name}.{column.name_}'
        return res

    def table_name_set_alias(self):
        if self.alias_ != '':
            return f"{self.name_} {self.alias_}"
        else:
            return self.name_


class Table(QueryTable):
    def __init__(self, **kwargs):
        super(Table, self).__init__(**kwargs)
        self._primary_columns: List[PrimaryColumn] = kwargs.get('primary_columns', None)
        self._foreign_columns: List[RefColumn] = kwargs.get('foreign_columns', None)

    @property
    def primary_columns_(self):
        return self._primary_columns

    @property
    def foreign_columns_(self):
        return self._foreign_columns

    @primary_columns_.setter
    def primary_columns_(self, param: List[PrimaryColumn]):
        self._primary_columns = param

    @foreign_columns_.setter
    def foreign_columns_(self, param: List[RefColumn]):
        self._foreign_columns = param


class Column(object):
    def __init__(self, **kwargs):
        self._name: str = kwargs.get('name', '')
        self._alias: str = kwargs.get('alias', '')
        self._type: str = kwargs.get('type', '')
        self._col_str: str = ''
        self._table_name: str = kwargs.get('table', '')

    @property
    def name_(self):
        return self._name

    @property
    def alias_(self):
        return self._alias

    @property
    def type_(self):
        return self._type

    @property
    def col_str_(self):
        return self._col_str

    @property
    def table_name_(self):
        return self._table_name

    @name_.setter
    def name_(self, param):
        self._name = param

    @alias_.setter
    def alias_(self, param):
        self._alias = param

    @type_.setter
    def type_(self, param):
        self._type = param

    @col_str_.setter
    def col_str_(self, param):
        self._col_str = param

    @table_name_.setter
    def table_name_(self, param):
        self._table_name = param

    def __str__(self):
        self.col_str_ = self.table_col_name()
        return self.col_str_

    def table_col_name(self) -> str:
        if self.table_name_ != '':
            return f'{self.table_name_}.{self.name_}'

    def set_col_alias(self):
        attrib_alias = self.alias_ if self.alias_ != "" else ""
        if attrib_alias != "":
            return f'{self.table_col_name()}  {attrib_alias}'
        else:
            return str(self)


class RefColumn(Column):
    def __init__(self, **kwargs):
        super(RefColumn, self).__init__(**kwargs)
        self._foreign_table: QueryTable = kwargs.get('foreign_table', None)

    @property
    def foreign_table_(self):
        return self._foreign_table

    @foreign_table_.setter
    def foreign_table_(self, param):
        self._foreign_table = param


class PrimaryColumn(Column):
    def __init__(self, **kwargs):
        super(PrimaryColumn, self).__init__(**kwargs)
        self._is_identity: bool = kwargs.get('is_identity', False)
        self._increment_factor: int = kwargs.get('increment_factor', 0)

    @property
    def is_identity(self):
        return self._is_identity

    @property
    def increment_factor(self):
        return self._increment_factor

    @is_identity.setter
    def is_identity(self, param):
        self._is_identity = param

    @increment_factor.setter
    def increment_factor(self, param):
        self._increment_factor = param


class FuncColumn(Column):
    def __init__(self, **kwargs):
        super(FuncColumn, self).__init__(**kwargs)
        self._db_func: DBFunc = kwargs.get('db_function', None)

    def __str__(self):
        if self.alias_ != '':
            self.col_str_ = f'({str(self._db_func)}) {self.alias_}'
        return self.col_str_

    @property
    def db_func_(self):
        return self._db_func

    @db_func_.setter
    def db_func_(self, param):
        self._db_func = param


class CalculatedColumn(Column):
    def __init__(self, **kwargs):
        super(CalculatedColumn, self).__init__(**kwargs)
        self._db_calc: AggregateFunc = kwargs.get('db_calc', None)

    def __str__(self):
        if self.alias_ != '':
            self.col_str_ = f'{str(self._db_calc)} {self.alias_}'
        return self.col_str_

    @property
    def db_calc_(self):
        return self._db_calc

    @db_calc_.setter
    def db_calc_(self, param):
        self._db_calc = param


class CustomColumn(object):
    def __init__(self, **kwargs):
        self._column: str = kwargs.get('column', '')
        self._alias: str =  kwargs.get('alias', '')

    def __str__(self):
        if self.alias_ != '':
            self.col_str_ = f'{str(self._column).rstrip()} {self.alias_}'
        return self.col_str_

    @property
    def column_(self):
        return self._column

    @property
    def alias_(self):
        return self._alias

    @column_.setter
    def column_(self, param):
        self._column = param

    @alias_.setter
    def alias_(self, param):
        self._alias = param


class JoinClause(Enum):
    Inner = 1
    LeftOuter = 2
    RightOuter = 3
    Cross = 4
    Natural = 5
    NaturalRight = 6
    NaturalLeft = 7


class Join(object):
    def __init__(self, **kwargs):
        self._left_table: QueryTable = kwargs.get('left_table', None)
        self._right_table: QueryTable = kwargs.get('right_table', None)
        self._type: JoinClause = kwargs.get('join_clause', None)
        self._cross_join_tables: List[QueryTable] = kwargs.get('cross_tables', None)
        self._on_attribs_criteria: List[AttrCriterion] = kwargs.get('on', None)
        self._where_attribs_criteria: List[AttrCriterion] = kwargs.get('where', None)
        self._join_str: str = ''

    def __str__(self):
        if self.join_str_:
            return self.join_str_

    def __repr__(self):
        if self.join_str_:
            return self.join_str_

    @property
    def left_table_(self):
        return self._left_table

    @property
    def right_table_(self):
        return self._right_table

    @property
    def type_(self):
        return self._type

    @property
    def join_str_(self):
        return self._join_str

    @property
    def cross_join_tables_(self):
        return self._cross_join_tables

    @property
    def on_attribs_criteria_(self):
        return self._on_attribs_criteria

    @property
    def where_attribs_criteria_(self):
        return self._where_attribs_criteria

    @property
    def join_(self):
        return self._join

    @join_.setter
    def join_(self, param):
        self._join = param

    @left_table_.setter
    def left_table_(self, param):
        self._left_table = param

    @right_table_.setter
    def right_table_(self, param):
        self._right_table = param

    @type_.setter
    def type_(self, param):
        self._type = param

    @join_str_.setter
    def join_str_(self, param):
        self._join_str = param

    @cross_join_tables_.setter
    def cross_join_tables_(self, param):
        self._cross_join_tables = param

    @on_attribs_criteria_.setter
    def on_attribs_criteria_(self, param):
        self._on_attribs_criteria = param

    @where_attribs_criteria_.setter
    def where_attribs_criteria_(self, param):
        self._where_attribs_criteria = param

    def join_to_string(self):
        return self.join_str_

    def inner_(self):
        logger = logging.getLogger(__name__)
        res = ''
        try:
            left_t = self.left_table_.from_name_
            right_t = self.right_table_.from_name_
            res = f"{left_t} inner join {right_t} on ("
            res += f"{' and '.join(str(crit) for crit in self.on_attribs_criteria_)}) "
            self.join_str_ = res

        except TypeError as error:
            logger.exception('The Join does not contain On attributes', exc_info=True)

    def left_outer_(self):
        logger = logging.getLogger(__name__)
        res = ''
        try:
            left_t = self.left_table_.from_name_
            right_t = self.right_table_.from_name_
            res = f"{left_t} left outer join {right_t} on ("
            res += f"{' and '.join(str(crit) for crit in self.on_attribs_criteria_)})"
            self.join_str_ = res

        except TypeError as error:
            logger.exception('The Join does not contain On attributes', exc_info=True)

    def right_outer_(self):
        logger = logging.getLogger(__name__)
        res = ''
        try:
            left_t = self.left_table_.from_name_
            right_t = self.right_table_.from_name_
            res = f"{left_t} right outer join {right_t} on ("
            res += f"{' and '.join(str(crit) for crit in self.on_attribs_criteria_)})"
            self.join_str_ = res

        except TypeError as error:
            logger.exception('The Join does not contain On attributes', exc_info=True)

    def cross_(self):
        logger = logging.getLogger(__name__)
        res = ''
        try:
            res = f"{', '.join(table_in.from_name_ for table_in in self.cross_join_tables_)}"
            if len(self.cross_join_tables_) == 2:
                if self.on_attribs_criteria_:
                    res += f" on ({' and '.join(str(crit) for crit in self.on_attribs_criteria_)})"
                # elif self.where_attribs_criteria_:
                #     res += f" Where {' and '.join(str(crit) for crit in self.where_attribs_criteria_)}"
            self.join_str_ = res

        except TypeError as error:
            logger.exception('The Join does not contain On or Where attributes', exc_info=True)

    def natural_(self):
        logger = logging.getLogger(__name__)
        res = ''
        try:
            left_t = self.left_table_.from_name_
            right_t = self.right_table_.from_name_
            res = f"{left_t} natural join {right_t} on ("
            res += f"{' and '.join(str(crit) for crit in self.on_attribs_criteria_)})"
            self.join_str_ = res
        except TypeError as error:
            logger.exception('The Join does not contain On attributes', exc_info=True)

    def natural_left_(self):
        logger = logging.getLogger(__name__)
        res = ''
        try:
            left_t = self.left_table_.from_name_
            right_t = self.right_table_.from_name_
            res = f"{left_t} natural left join {right_t} on ("
            res += f"{' and '.join(str(crit) for crit in self.on_attribs_criteria_)})"
            self.join_str_ = res

        except TypeError as error:
            logger.exception('The Join does not contain On attributes', exc_info=True)

    def natural_right_(self):
        logger = logging.getLogger(__name__)
        res = ''
        try:
            left_t = self.left_table_.from_name_
            right_t = self.right_table_.from_name_
            res = f"{left_t} natural right join {right_t} on ("
            res += f"{' and '.join(str(crit) for crit in self.on_attribs_criteria_)})"
            self.join_str_ = res

        except TypeError as error:
            logger.exception('The Join does not contain On attributes', exc_info=True)
