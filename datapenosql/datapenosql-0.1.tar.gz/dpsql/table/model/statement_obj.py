from enum import Enum
from typing import List
from dpsql.table.model.criterion_obj import Criterion


class StatementClause(Enum):
    Where = 1
    GroupBy = 2
    OrderBy = 3
    Having = 4
    Distinct = 5


class Statement(object):

    def __init__(self, **kwargs):
        self._criteria: List[Criterion] = kwargs.get('criteria', None)
        self._clause: StatementClause = kwargs.get('clause', None)
        self._statement_str: str = ''

    def __str__(self):
        if self.statement_str_ != '':
            return self.statement_str_
        else:
            self._switch_statement()
            return self.statement_str_

    def __repr__(self):
        if self.statement_str_ != '':
            return self.statement_str_
        else:
            self._switch_statement()
            return self.statement_str_

    @property
    def criteria_(self):
        return self._criteria

    @criteria_.setter
    def criteria_(self, param):
        self._criteria = param

    @property
    def statement_str_(self):
        return self._statement_str

    @statement_str_.setter
    def statement_str_(self, param):
        self._statement_str = param

    @property
    def clause_(self):
        return self._clause

    @clause_.setter
    def clause_(self, param):
        self._clause = param

    def _distinct_(self):
        self.statement_str_ = f"Distinct {', '.join(str(var) for var in self.criteria_)}"

    def _where_(self):
        self.statement_str_ = f"Where {' and '.join(str(var) for var in self.criteria_)}"

    def _group_by_(self):
        self.statement_str_ = f"Group By {', '.join(str(var) for var in self.criteria_)}"

    def _order_by_(self):
        self.statement_str_ = f"Order By {', '.join(str(var) for var in self.criteria_)}"

    def _having_(self):
        self.statement_str_ = f"Having {', '.join(str(var) for var in self.criteria_)}"

    def _switch_statement(self):
        res_dict = {
            'Where': self._where_,
            'GroupBy': self._group_by_,
            'OrderBy': self._order_by_,
            'Having': self._having_,
            'Distinct': self._distinct_
        }
        return res_dict.get(self.clause_.name, '')()
