from enum import Enum


class AggregateClause(Enum):
    MAX = 10
    MIN = 11
    SUM = 12
    AVG = 13
    COUNT = 14
    Generic = 15


class AggregateFunc(object):

    def __init__(self, **kwargs):
        self._attr: str = kwargs.get('target', '')
        self._is_func: bool = kwargs.get('is_func', False)
        self._alias: str = kwargs.get('alias', '')
        self._aggregate_func: AggregateClause = kwargs.get('aggregate_func', AggregateClause.Generic)
        self._aggregate_str: str = ''
        self._calc_method: str = kwargs.get('calc_method', '')
        self._distinct: bool = kwargs.get('distinct', False)
        self._star: bool = kwargs.get('star_attr', False)

    def __str__(self):
        self._switch_aggregate()
        return self.aggregate_str_

    def __repr__(self):
        self._switch_aggregate()
        return self.aggregate_str_

    @property
    def attr_(self):
        return self._attr

    @property
    def is_func_(self):
        return self._is_func

    @property
    def alias_(self):
        return self._alias

    @property
    def aggregate_func_(self):
        return self._aggregate_func

    @property
    def aggregate_str_(self):
        return self._aggregate_str

    @property
    def distinct_(self):
        return self._distinct

    @property
    def star_(self):
        return self._star

    @property
    def calc_method_(self):
        return self._calc_method

    @attr_.setter
    def attr_(self, param):
        self._attr = param

    @is_func_.setter
    def is_func_(self, param):
        self._is_func = param

    @alias_.setter
    def alias_(self, param):
        self._alias = param

    @aggregate_func_.setter
    def aggregate_func_(self, param):
        self._aggregate_func = param

    @aggregate_str_.setter
    def aggregate_str_(self, param):
        self._aggregate_str = param

    @distinct_.setter
    def distinct_(self, param):
        self._distinct = param

    @star_.setter
    def star_(self, param):
        self._star = param

    @calc_method_.setter
    def calc_method_(self, param):
        self._calc_method = param

    def _max_(self):
        res = ''
        if self._alias != '':
            res = f'MAX({self.attr_}) {self.alias_}'
        else:
            res = f'MAX({self.attr_})'

        self.aggregate_str_ = res

    def _min_(self):
        res = ''
        if self._alias != '':
            res = f'MIN({self.attr_}) {self.alias_}'
        else:
            res = f'MIN({self.attr_})'

        self.aggregate_str_ = res

    def _sum_(self):
        res = ''
        if self._alias != '':
            res = f'SUM({self.attr_}) {self.alias_}'
        else:
            res = f'SUM({self.attr_})'

        self.aggregate_str_ = res

    def _avg_(self):
        res = ''
        if self._alias != '':
            res = f'AVG({self.attr_}) {self.alias_}'
        else:
            res = f'AVG({self.attr_})'

        self.aggregate_str_ = res

    def _count_(self):
        res = ''
        if self.distinct_ is True:
            res = f'COUNT(DISTINCT {self.attr_})'
        elif self.star_ is True:
            res = f'COUNT(*)'
        else:
            res = f'COUNT({self.attr_})'

        if self._alias != '':
            res += f' {self.alias_}'

        self.aggregate_str_ = res

    def _generic_calc_(self):
        res = ''
        res = f"{self.calc_method_}"
        if self._alias != '':
            res += f' {self.alias_}'

        self.aggregate_str_ = res

    def _switch_aggregate(self):
        res_dict = {
            'MAX': self._max_,
            'MIN': self._min_,
            'SUM': self._sum_,
            'AVG': self._avg_,
            'COUNT': self._count_,
            'Generic': self._generic_calc_
        }
        return res_dict.get(self.aggregate_func_.name, '')()

