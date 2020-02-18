from __future__ import annotations
from enum import Enum
from typing import List


class CriterionClause(Enum):
    Equal = 1
    Less = 2
    Greater = 3
    LessOrEqual = 4
    GreaterOrEqual = 5
    Between = 6
    IsIn = 7
    NotIn = 8
    Like = 9
    Max = 10
    Min = 11
    SUM = 12
    AVG = 13
    OrderDesc = 14
    OrderAsc = 15
    IsNull = 16
    IsNotNull = 17


class Criterion(object):
    def __init__(self, **kwargs):
        self._left_attr: str = kwargs.get('left_attr', None)
        self._clause: CriterionClause = kwargs.get('criteria', None)
        self._clause_str: str = ''
        self._alias: str = ''
        self._and: List[Criterion] = kwargs.get('and_', None)
        self._or: List[Criterion] = kwargs.get('or_', None)
        self._and_group: List[Criterion] = kwargs.get('and_group', None)
        self._or_group: List[Criterion] = kwargs.get('or_group', None)

    def __str__(self):
        self.clause_str_ = Criterion.criteria_str(self)
        return self.clause_str_

    def __repr__(self):
        self.clause_str_ = Criterion.criteria_str(self)
        return self.clause_str_

    @property
    def left_attr_(self):
        return self._left_attr

    @property
    def clause_(self):
        return self._clause

    @property
    def clause_str_(self):
        return self._clause_str

    @property
    def alias_(self):
        return self._alias

    @property
    def and_(self):
        return self._and

    @property
    def or_(self):
        return self._or

    @property
    def and_group_(self):
        return self._and_group

    @property
    def or_group_(self):
        return self._or_group

    @left_attr_.setter
    def left_attr_(self, param):
        self._left_attr = param

    @clause_.setter
    def clause_(self, param):
        self._clause = param

    @clause_str_.setter
    def clause_str_(self, param):
        self._clause_str = param

    @alias_.setter
    def alias_(self, param):
        self._alias = param

    @and_.setter
    def and_(self, param):
        self._and = param

    @or_.setter
    def or_(self, param):
        self._or = param

    @and_group_.setter
    def and_group_(self, param):
        self._and_group = param

    @or_group_.setter
    def or_group_(self, param):
        self._or_group = param

    def criteria_to_string(self):
        res = self._switch_criteria()
        return res

    def _switch_criteria(self):
        res_dict = {
            'Equal': self._is_,
            'Less': self._less_than_,
            'Greater': self._greater_than_,
            'LessOrEqual': self._less_than_or_equal_,
            'GreaterOrEqual': self._greater_than_or_equal_,
            'Between': self._between_,
            'IsIn': self._is_in_,
            'NotIn': self._is_not_in_,
            'Like': self._like_,
            'OrderDesc': self._order_desc_,
            'OrderAsc': self._order_asc_,
            'IsNull': self._is_null_,
            'IsNotNull': self._is_not_null_
        }
        if self.clause_:
            return res_dict.get(self.clause_.name, '')()
        else:
            return self._is_()

    def _between_(self):
        crit_type = type(self)
        res = ''

        if crit_type == ValCriterion:
            val1 = self.val_[0]
            val2 = self.val_[1]

            left_attr = self.left_attr_
            left_attr_name = left_attr

            res = f'{left_attr_name} BETWEEN {val1} AND {val2}'

        if self.alias_ != '':
            res = f'({res}) AS {self.alias_}'

        return res

    def _is_(self):
        crit_type = type(self)
        res = ''

        left_attr = self.left_attr_
        left_attr_name = left_attr

        if crit_type == ValCriterion:
            val = self.val_[0]
            res = f'{left_attr_name} = {val}'

        elif crit_type == AttrCriterion:
            right_attr = self.right_attr_
            right_attr_name = right_attr

            if self.join_expression_ == '':
                res = f'{right_attr_name} = {left_attr_name}'
            else:
                join_expression = self.join_expression_
                res = f'{right_attr_name} = {left_attr_name} {join_expression}'

        if self.alias_ != '':
            res = f'({res}) AS {self.alias_}'
        return res

    def _is_in_(self):
        crit_type = type(self)
        res = ''

        if crit_type == ValCriterion:
            left_attr = self.left_attr_
            left_attr_name = left_attr

            res = f'{left_attr_name} IN {tuple(self.val_)}'

        if self.alias_ != '':
            res = f'({res}) AS {self.alias_}'

        return res

    def _is_not_in_(self):
        crit_type = type(self)
        res = ''

        if crit_type == ValCriterion:
            left_attr = self.left_attr_
            left_attr_name = left_attr

            res = f'{left_attr_name} NOT IN {tuple(self.val_)}'

        return res

    def _is_not_null_(self):
        crit_type = type(self)
        res = ''

        if crit_type == ValCriterion:
            left_attr = self.left_attr_
            left_attr_name = left_attr

            res = f'{left_attr_name} IS NOT NULL'

        return res

    def _is_null_(self):
        crit_type = type(self)
        res = ''

        if crit_type == ValCriterion:
            left_attr = self.left_attr_
            left_attr_name = left_attr

            res = f'{left_attr_name} IS NULL'

        return res

    def _like_(self):
        crit_type = type(self)
        res = ''

        if crit_type == ValCriterion:
            val = self.val_[0]
            left_attr = self.left_attr_
            left_attr_name = left_attr

            res = f'{left_attr_name} LIKE {val}'

        if self.alias_ != '':
            res = f'({res}) AS {self.alias_}'

        return res

    def _less_than_(self):
        crit_type = type(self)
        res = ''

        if crit_type == ValCriterion:
            val = self.val_[0]
            left_attr = self.left_attr_
            left_attr_name = left_attr

            res = f'{left_attr_name} < {val}'

        if self.alias_ != '':
            res = f'({res}) AS {self.alias_}'

        return res

    def _greater_than_(self):
        crit_type = type(self)
        res = ''

        if crit_type == ValCriterion:
            val = self.val_[0]
            left_attr = self.left_attr_
            left_attr_name = left_attr

            res = f'{left_attr_name} > {val}'

        if self.alias_ != '':
            res = f'({res}) AS {self.alias_}'

        return res

    def _less_than_or_equal_(self):
        crit_type = type(self)
        res = ''

        if crit_type == ValCriterion:
            val = self.val_[0]
            left_attr = self.left_attr_
            left_attr_name = left_attr

            res = f'{left_attr_name} <= {val}'

        if self.alias_ != '':
            res = f'({res}) AS {self.alias_}'

        return res

    def _greater_than_or_equal_(self):
        crit_type = type(self)
        res = ''

        if crit_type == ValCriterion:
            val = self.val_[0]
            left_attr = self.left_attr_
            left_attr_name = left_attr

            res = f'{left_attr_name} >= {val}'

        if self.alias_ != '':
            res = f'({res}) AS {self.alias_}'

        return res

    def _order_desc_(self):
        left_attr = self.left_attr_
        left_attr_name = left_attr

        res = f'{left_attr_name} DESC'

        if self.alias_ != '':
            res = f'({res}) AS {self.alias_}'

        return res

    def _order_asc_(self):

        left_attr = self.left_attr_
        left_attr_name = left_attr

        res = f'{left_attr_name} ASC'

        if self.alias_ != '':
            res = f'({res}) AS {self.alias_}'

        return res

    @staticmethod
    def criteria_str(criteria):
        res = criteria.criteria_to_string()
        if criteria.and_:
            for crit in criteria.and_:
                res1 = Criterion.criteria_str(crit)
                res += Criterion.criteria_and(res1)

        if criteria.and_group_:
            for crit in criteria.and_group_:
                res1 = Criterion.criteria_str(crit)
                res += Criterion.criteria_and_group(res1)

        if criteria.or_:
            for crit in criteria.or_:
                res1 = Criterion.criteria_str(crit)
                res += Criterion.criteria_or(res1)

        if criteria.or_group_:
            for crit in criteria.or_group_:
                res1 = Criterion.criteria_str(crit)
                res += f"{Criterion.criteria_or_group(res1)}"

        return res

    @staticmethod
    def criteria_and(criteria):
        res = f" AND {str(criteria)}"
        return res

    @staticmethod
    def criteria_or(criteria):
        res = f" OR {str(criteria)}"
        return res

    @staticmethod
    def criteria_and_group(criteria):
        res = f" AND ({str(criteria)})"
        return res

    @staticmethod
    def criteria_or_group(criteria):
        res = f" OR ({str(criteria)})"
        return res


class AttrCriterion(Criterion):
    def __init__(self, **kwargs):
        super(AttrCriterion, self).__init__(**kwargs)
        self._right_attr: str = kwargs.get('right_attr', '')
        self._join_expression: str = kwargs.get('join_expression', '')

    @property
    def right_attr_(self):
        return self._right_attr

    @property
    def join_expression_(self):
        return self._join_expression

    @right_attr_.setter
    def right_attr_(self, param):
        self._right_attr = param

    @join_expression_.setter
    def join_expression_(self, param):
        self._join_expression = param


class ValCriterion(Criterion):
    def __init__(self, **kwargs):
        super(ValCriterion, self).__init__(**kwargs)
        self._val: List = kwargs.get('values', None)

    @property
    def val_(self):
        return self._val

    @val_.setter
    def val_(self, param):
        self._val = param

