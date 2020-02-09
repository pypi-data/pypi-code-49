# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import absolute_import, unicode_literals

import abc

import six

from ..error import TypeConversionError


@six.add_metaclass(abc.ABCMeta)
class ValueConverterInterface(object):
    @abc.abstractmethod
    def force_convert(self):  # pragma: no cover
        pass


class AbstractValueConverter(ValueConverterInterface):
    __slots__ = "_value"

    def __init__(self, value, params):
        self._value = value
        self._params = params

    def __repr__(self):
        try:
            string = six.text_type(self.force_convert())
        except TypeConversionError:
            string = "[ValueConverter ERROR] failed to force_convert"

        return string
