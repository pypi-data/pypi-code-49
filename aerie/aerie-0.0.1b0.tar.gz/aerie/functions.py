import sqlalchemy as sa

from aerie.fields import Field


class BaseFunction:
    func = None

    def __init__(self, field: Field):
        self._field = field

    def as_(self, alias: str):
        return sa.column(self()).label(alias)

    def __call__(self, *args, **kwargs):
        return self.func(self._field)

    def __str__(self):
        return str(self())


class Avg(BaseFunction):
    func = sa.func.avg


class Min(BaseFunction):
    func = sa.func.min


class Max(BaseFunction):
    func = sa.func.max


class Sum(BaseFunction):
    func = sa.func.sum


class Count(BaseFunction):
    func = sa.func.count
