from math import floor

import pmn.string_format as sf


class Method:
    FIT = 1
    LIMIT = 2
    AVAILABLE = 3


class Unit:
    PX = 1
    FR = 2
    SELF = 3


class Align:
    LEFT = 1
    RIGHT = 2


class Size:
    def __init__(self, value: float, method: Method = Method.FIT, unit: Unit = Unit.SELF, align: Align = Align.LEFT):
        self.method = method
        self.value = value
        self.unit = unit
        self.align = align

    def format(self, string: str):
        if self.unit == Unit.SELF:
            return string
        if self.method == Method.LIMIT:
            return self._limit(string)
        elif self.method == Method.FIT:
            return self._fit(string)

    def _limit(self, string):
        if self.align == Align.LEFT:
            return string[:self.value]
        elif self.align == Align.RIGHT:
            return string[self.value:]

    def _fit(self, string):
        if self.method == Unit.PX:
            return sf.left_fit(string, floor(self.value))

    @classmethod
    def self(cls):
        return Size(0, Method.FIT, Unit.SELF)
