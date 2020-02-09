# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import absolute_import

import abc
from collections import OrderedDict
from textwrap import dedent

import six

from pytablereader import DataError

from ._acceptor import LoaderAcceptor
from ._logger import logger


try:
    import simplejson as json
except ImportError:
    import json


@six.add_metaclass(abc.ABCMeta)
class TableFormatterInterface(object):
    """
    The abstract class of table data validator.
    """

    @abc.abstractmethod
    def to_table_data(self):  # pragma: no cover
        pass


class TableFormatter(LoaderAcceptor, TableFormatterInterface):
    """
    The abstract class of |TableData| formatter.
    """

    def _validate_source_data(self):
        if not self._source_data:
            raise DataError("source data is empty")

    def __init__(self, source_data):
        self._source_data = source_data

        self._validate_source_data()

    def _extract_type_hints(self, headers=None):
        if self._loader.type_hints:
            return self._loader.type_hints

        if not self._loader.type_hint_rules or not headers:
            return []

        type_hints = []
        for header in headers:
            for regexp, type_hint in self._loader.type_hint_rules.items():
                if regexp.search(header):
                    type_hints.append(type_hint)
                    break
            else:
                type_hints.append(None)

        logger.debug(
            dedent(
                """\
                extracted type hints:
                {}
                """
            ).format(
                json.dumps(
                    OrderedDict(
                        {
                            header: six.text_type(type_hint)
                            for header, type_hint in zip(headers, type_hints)
                        }
                    ),
                    indent=4,
                )
            )
        )

        return type_hints
