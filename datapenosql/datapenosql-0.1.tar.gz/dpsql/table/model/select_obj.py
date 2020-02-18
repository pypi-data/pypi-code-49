from typing import List

from dpsql.table.model.db_objects import Column, QueryTable


class Select(object):
    def __init__(self, **kwargs):
        self._tables: List[QueryTable] = kwargs.get('tables', '')
        self._tables_str: str = ''
        self._columns: List[Column] = kwargs.get('columns', '')
        self._calculated_column: List = kwargs.get('calculated_columns', '')
        self._aggregated_column: List = kwargs.get('aggregated_columns', '')
        self._custom_column: List = kwargs.get('custom_columns', '')
        self._column_str: str = ''
        self._calculated_column_str: str = ''
        self._aggregated_column_str: str = ''
        self._custom_column_str: str = ''
        self._where: str = kwargs.get('where', '')
        self._where_str: str = ''
        self._group_by: str = kwargs.get('group_by', '')
        self._group_by_str: str = ''
        self._having: str = kwargs.get('having', '')
        self._having_str: str = ''
        self._order_by: str = kwargs.get('order_by', '')
        self._order_by_str: str = ''
        self._is_attrib: bool = kwargs.get('is_attrib', False)
        self._is_sub_query: bool = kwargs.get('is_sub_query', False)
        self._alias: str = kwargs.get('alias', '')
        self._select_str: str = kwargs.get('select_query', '')
        self._is_distinct: bool = kwargs.get('is_distinct', False)
        self._union: Select = kwargs.get('union', None)
        self._union_all: Select = kwargs.get('union_all', None)
        self._intersect: Select = kwargs.get('intersect', None)
        self._except: Select = kwargs.get('except', None)

    def __str__(self):
        self._select_builder()
        return self.select_str_

    def __repr__(self):
        self._select_builder()
        return self.select_str_

    @property
    def union_(self):
        return self._union

    @property
    def union_all_(self):
        return self._union_all

    @property
    def intersect_(self):
        return self._intersect

    @property
    def except_(self):
        return self._except

    @property
    def tables_(self):
        return self._tables

    @property
    def columns_(self):
        return self._columns

    @property
    def calculated_column_(self):
        return self._calculated_column

    @property
    def aggregated_column_(self):
        return self._aggregated_column

    @property
    def custom_column_(self):
        return self._custom_column

    @property
    def where_(self):
        return self._where

    @property
    def group_by_(self):
        return self._group_by

    @property
    def having_(self):
        return self._having

    @property
    def order_by_(self):
        return self._order_by

    @property
    def is_attrib_(self):
        return self._is_attrib

    @property
    def is_sub_query_(self):
        return self._is_sub_query

    @property
    def is_distinct_(self):
        return self._is_distinct

    @property
    def alias_(self):
        return self._alias

    @property
    def select_str_(self):
        return self._select_str

    @tables_.setter
    def tables_(self, param):
        self._tables = param

    @columns_.setter
    def columns_(self, param):
        self._columns = param

    @calculated_column_.setter
    def calculated_column_(self, param):
        self._calculated_column = param

    @aggregated_column_.setter
    def aggregated_column_(self, param):
        self._aggregated_column = param

    @custom_column_.setter
    def custom_column_(self, param):
        self._custom_column = param

    @where_.setter
    def where_(self, param):
        self._where = param

    @group_by_.setter
    def group_by_(self, param):
        self._group_by = param

    @having_.setter
    def having_(self, param):
        self._having = param

    @order_by_.setter
    def order_by_(self, param):
        self._order_by = param

    @is_attrib_.setter
    def is_attrib_(self, param):
        self._is_attrib = param

    @is_sub_query_.setter
    def is_sub_query_(self, param):
        self._is_sub_query = param

    @is_distinct_.setter
    def is_distinct_(self, param):
        self._is_distinct = param

    @alias_.setter
    def alias_(self, param):
        self._alias = param

    @select_str_.setter
    def select_str_(self, param):
        self._select_str = param

    @union_.setter
    def union_(self, param):
        self._union = param

    @union_all_.setter
    def union_all_(self, param):
        self._union_all = param

    @intersect_.setter
    def intersect_(self, param):
        self._intersect = param

    @except_.setter
    def except_(self, param):
        self._except = param

    def query_alias(self) -> str:
        if self.alias_ != "" and self.is_attrib_ is True:
            return f'({self.select_str_}) AS {self.alias_}'

        elif self.alias_ != "" and self.is_sub_query_ is True:
            return f'({self.select_str_}) {self.alias_}'

        else:
            return self.select_str_

    def _tables_builder(self):
        if self.tables_:
            self._tables_str = f"{', '.join(table.from_name_ for table in self.tables_)}"

    def _columns_builder(self):
        if self.columns_:
            self._column_str = f"{', '.join(str(col.set_col_alias()) for col in self.columns_)}"

    def _calculated_columns_builder(self):
        if self.calculated_column_:
            self._calculated_column_str = f"{', '.join(str(column) for column in self.calculated_column_)}"

    def _aggregated_columns_builder(self):
        if self.aggregated_column_:
            self._aggregated_column_str = f"{', '.join(str(column) for column in self.aggregated_column_)}"

    def _custom_columns_builder(self):
        if self.custom_column_:
            self._custom_column_str = f"{', '.join(str(column) for column in self.custom_column_)}"

    def _select_builder(self):
        if self.tables_:
            self._tables_builder()
        if self.columns_:
            self._columns_builder()
        if self.calculated_column_:
            self._calculated_columns_builder()
        if self.aggregated_column_:
            self._aggregated_columns_builder()
        if self.custom_column_:
            self._custom_columns_builder()
        operation_list = list()
        if self.union_:
            operation_str = f"Union {str(self.union_)}"
            operation_list.append(operation_str)
        elif self.union_all_:
            operation_str = f"Union All {str(self.union_all_)}"
            operation_list.append(operation_str)
        elif self.intersect_:
            operation_str = f"Intersect {str(self.intersect_)}"
            operation_list.append(operation_str)
        elif self.except_:
            operation_str = f"Except {str(self.except_)}"
            operation_list.append(operation_str)

        columns = self._column_str if self._column_str != '' else '*'
        calc_columns = self._calculated_column_str if self._calculated_column_str != '' else ''
        aggr_columns = self._aggregated_column_str if self._aggregated_column_str != '' else ''
        custom_columns = self._custom_column_str if self._custom_column_str != '' else ''
        columns_combiner = list()
        columns_combiner.append(columns)

        if columns != '*':
            if calc_columns != '':
                columns_combiner.append(calc_columns)
            if aggr_columns != '':
                columns_combiner.append(aggr_columns)
            if custom_columns != '':
                columns_combiner.append(custom_columns)

        if self.is_distinct_ is True:
            select_temp = f"Select Distinct {', '.join(elm for elm in columns_combiner)}"
        else:
            select_temp = f"Select {', '.join(elm for elm in columns_combiner)}"

        select_temp += f" From {self._tables_str}"

        if self.where_ != '':
            select_temp += f" {self.where_}"

        if self.group_by_ != '':
            select_temp += f" {self.group_by_}"

            if self.having_ != '':
                select_temp += f" {self.having_}"

            if self.order_by_ != '':
                select_temp += f" {self.order_by_}"

        elif self.having_ != '':
            select_temp += f" {self.having_}"

            if self.order_by_ != '':
                select_temp += f" {self.order_by_}"

        elif self.order_by_ != '':
            select_temp += f" {self.order_by_}"

        if operation_list:
            select_temp += f" {operation_list[0]}"

        if self.is_sub_query_:
            select_temp = f"({select_temp.rstrip()}) {self.alias_}"

        self.select_str_ = select_temp

        return self.select_str_
