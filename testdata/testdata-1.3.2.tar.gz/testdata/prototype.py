# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division, print_function, absolute_import
import inspect
import random
import sys

from .compat import *
from .utils import String


class Prototype(object):
    def __init__(self, count=0, min_size=None, max_size=None, empty=False):
        """
        :param count: int, the length, by default there is no length
        :param min_size: int, the minimum size the value can have
        :param max_size: int, the maximum size the value can have
        :param between: tuple, the min value and the max value (eg, (1, 100) for values
            between 1 and 100)
        :param empty: bool, if True then sometimes this will return None instead of
            a generated value
        """
        self.min_size = min_size
        self.max_size = max_size
        self.count = count
        self.empty = empty

    def __call__(self):
        """returns a value using the values passed to __init__, this makes prototype
        a psuedo callback and can be used interchangebly with things like lambda
        or testdata.get_name"""
        if self.empty and ChoicePrototype(self.empty)():
            ret = None

        else:
            ret = self.random()
        return ret

    def random(self):
        raise NotImplementedError()


class ChoicePrototype(Prototype):
    """
    Decide if we should perform this action, this is just a simple way to do something
    I do in tests every now and again

    :Example:
        # EXAMPLE -- simple yes or no question
        if ChoicePrototype()():
            # do this
        else:
            # don't do it

        # EXAMPLE -- multiple choice
        choice = ChoicePrototype(3)()
        if choice == 1:
            # do the first thing
        elif choice == 2:
            # do the second thing
        else:
            # do the third thing

        # EXAMPLE -- do something 75% of the time
        if ChoicePrototype(3)(0.75):
            # do it the majority of the time
        else:
            # but every once in a while don't do it

    https://github.com/Jaymon/testdata/issues/8

    :param specifier: int|float, if int, return a value between 1 and specifier.
        if float, return 1 approximately specifier percent of the time, return 0
        100% - specifier percent of the time
    :returns: integer, usually 1 (True) or 0 (False)
    """
    def __init__(self, specifier):
        self.specifier = specifier

    def random(self):
        specifier = self.specifier
        if specifier:
            if isinstance(specifier, int):
                choice = random.randint(1, specifier)

            else:
                if specifier < 1.0:
                    specifier *= 100.0

                specifier = int(specifier)
                x = random.randint(0, 100)
                choice = 1 if x <= specifier else 0

        else:
            choice = random.choice([0, 1])

        return choice


# class TypePrototype(object):
#     vtypes = []
#     _vtypes_cache = {}
#     def __new__(cls, vtype, *args, **kwargs):
#         if not cls._vtypes_cache:
#             class_filter = lambda x: inspect.isclass(x) and issubclass(x, cls)
#             for name, proto_class in inspect.getmembers(sys.modules[__name__], class_filter):
#                 for vt in proto_class.vtypes:
#                     cls._vtypes_cache[vt] = proto_class
# 
#         return super(Prototype, cls).__new__(cls._vtypes_cache[vtype])
# 
#     def __init__(self, vtype, count=0, min_size=0, max_size=0, empty=False):
#         """
#         :param vtype: type, the python type (eg, int, str, bool, float)
#         :param count: int, the length, by default there is no length
#         :param min_size: int, the minimum size the value can have
#         :param max_size: int, the maximum size the value can have
#         :param between: tuple, the min value and the max value (eg, (1, 100) for values
#             between 1 and 100)
#         :param empty: bool, if True then sometimes this will return None instead of
#             a generated value
#         """
#         self.vtype = vtype
#         self.min_size = min_size
#         self.max_size = max_size
#         self.count = count
#         self.empty = empty
# 
#     def __call__(self):
#         """returns a value using the values passed to __init__, this makes prototype
#         a psuedo callback and can be used interchangebly with things like lambda
#         or testdata.get_name"""
#         if self.empty and Yes(self.empty):
#             ret = None
# 
#         else:
#             ret = self.random()
#         return ret
# 
#     def random(self):
#         raise NotImplementedError()
# 

# TODO -- have prototype be common, but have a TypePrototype that takes the
# value, this will allow you to import IntegerPrototype and the like and allow
# us to create more interesting prototypes, while having TypePrototype be
# magical (and separate) for when you don't need the hassle of importing
# separate types


class FloatPrototype(Prototype):
    vtypes = [float]

    MINNEG = -sys.float_info.max
    MIN = 0.0
    MAX = 9999999999.999999
    MAXSYS = sys.float_info.max
    PRECISION = sys.float_info.dig

    def get_min(self):
        ret = self.min_size
        if ret is None:
            ret = self.MIN
        return ret

    def get_max(self):
        ret = self.max_size
        if ret is None:
            ret = self.MAX
        return ret

    def get_value(self, min_size, max_size):
        return random.uniform(min_size, max_size)

    def random(self):
        min_size = self.get_min()
        max_size = self.get_max()
        if self.count:
            bits = String(self.count).split(".")
            left = int(bits[0])
            right = self.PRECISION
            if len(bits) > 1:
                right = int(bits[1])

            max_size = min(float("{}.{}".format("9" * left, "9" * right)), max_size)
            min_size = max(-max_size, min_size)
            ret = self.get_value(min_size, max_size)
            ret = "{{:0>{}.{}f}}".format(left, right).format(ret)

        else:
            ret = self.get_value(min_size, max_size)

        return ret


class IntPrototype(FloatPrototype):
    vtypes = [int, long]

    MINNEG = -sys.maxsize
    MIN = 0
    MAX32 = 2**31-1
    MAX64 = 2**63-1
    MAXSYS = sys.maxsize
    MAX = MAX32

    def random(self): 
        min_size = self.get_min()
        max_size = self.get_max()
        if self.count:
            max_size = min(int("9" * self.count), max_size)
            ret = self.get_value(min_size, max_size)
            ret = "{{:0>{}}}".format(self.count).format(ret)

        else:
            ret = self.get_value(min_size, max_size)

        return ret

    def get_value(self, min_size, max_size):
        return random.randint(min_size, max_size)



# these tests were in testdata_test but I'm not sure I'm going to use these so
# I'm not committing them right now
from testdata.prototype import (
    FloatPrototype,
    IntPrototype,
)


class PrototypeTest(testdata.TestCase):
    def test_int(self):
        p = IntPrototype(count=2)
        for x in range(10):
            self.assertEqual(2, len(p()))

        p = IntPrototype(empty=100)
        self.assertIsNone(p())

        p = IntPrototype()
        for x in range(10):
            n = p()
            self.assertLessEqual(FloatPrototype.MIN, n)
            self.assertGreaterEqual(FloatPrototype.MAX, n)

    def test_float(self):
        p = FloatPrototype(1.2, min_size=0.0)
        for x in range(10):
            self.assertRegex(p(), r"\d\.\d{2}")

        p = FloatPrototype()
        for x in range(10):
            n = p()
            self.assertLessEqual(FloatPrototype.MIN, n)
            self.assertGreaterEqual(FloatPrototype.MAX, n)

    def test_str(self):
        p = StrPrototype()

