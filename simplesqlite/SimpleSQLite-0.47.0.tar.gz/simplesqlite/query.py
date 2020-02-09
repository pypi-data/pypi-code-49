# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import abc
import re

import six
import typepy
from pathvalidate import (
    InvalidCharError,
    InvalidReservedNameError,
    NullNameError,
    ValidReservedNameError,
    ascii_symbols,
    unprintable_ascii_chars,
)

from ._func import validate_table_name
from ._validator import validate_sqlite_attr_name
from .error import SqlSyntaxError


@six.add_metaclass(abc.ABCMeta)
class QueryItemInterface(object):
    @abc.abstractmethod
    def to_query(self):  # pragma: no cover
        pass


class QueryItem(QueryItemInterface):
    def __init__(self, value):
        try:
            self._value = value.strip()
        except AttributeError:
            raise TypeError("name must be a string")

    def __repr__(self):
        return self.to_query()

    def __format__(self, format_spec):
        return self.to_query()


class Table(QueryItem):
    """
    :param str name: Table name.
    :return: String that suitable for table name of a SQLite query.

    :Examples:
        >>> from simplesqlite.query import Table
        >>> Table("length")
        'length'
        >>> Table("length(cm)")
        '[length(cm)]'
        >>> Table("string length")
        "'string length'"
    """

    __RE_NEED_BRACKET = re.compile("[{:s}]".format(re.escape("%()-+/.,")))
    __RE_NEED_QUOTE = re.compile(r"[\s]+")

    def to_query(self):
        name = self._value

        if self.__RE_NEED_BRACKET.search(name):
            return "[{:s}]".format(name)

        if self.__RE_NEED_QUOTE.search(name):
            return "'{:s}'".format(name)

        return name


class Attr(QueryItem):
    """
    :param str name: Attribute name.
    :param str operation:
        Used as a SQLite function if the value is not empty.
    :return: String that suitable for attribute name of a SQLite query.
    :rtype: str

    :Examples:
        >>> from simplesqlite.query import Attr
        >>> Attr("key")
        'key'
        >>> Attr("a+b")
        '[a+b]'
        >>> Attr("key", operation="SUM")
        'SUM(key)'
    """

    __RE_NEED_QUOTE = re.compile("[{:s}]".format(re.escape("[]_")))
    __RE_NEED_BRACKET = re.compile(
        r"[{:s}0-9\s]".format(re.escape("%(){}-+/.;:`'\"\0\\*?<>|!#&=~^@"))
    )
    __RE_SANITIZE = re.compile("[{:s}\n\r]".format(re.escape("'\",")))

    @classmethod
    def sanitize(cls, name):
        try:
            return cls.__RE_SANITIZE.sub("_", name)
        except TypeError:
            return six.text_type(name)

    def __init__(self, name, operation=""):
        super(Attr, self).__init__(name)

        self.__operation = operation

    def to_query(self):
        name = self.sanitize(self._value)
        need_quote = self.__RE_NEED_QUOTE.search(name) is not None

        try:
            validate_sqlite_attr_name(name)
        except InvalidReservedNameError:
            need_quote = True
        except (ValidReservedNameError, NullNameError, InvalidCharError):
            pass

        if need_quote:
            sql_name = '"{:s}"'.format(name)
        elif self.__RE_NEED_BRACKET.search(name):
            sql_name = "[{:s}]".format(name)
        elif name == "join":
            sql_name = "[{:s}]".format(name)
        else:
            sql_name = name

        if typepy.is_not_null_string(self.__operation):
            sql_name = "{:s}({:s})".format(self.__operation, sql_name)

        return sql_name


class AttrList(list, QueryItemInterface):
    """
    :param list/tuple names: Attribute names.
    :param str operation:
        Used as a SQLite function if the value is not empty.

    :Examples:
        >>> from simplesqlite.query import AttrList
        >>> AttrList(["key", "a+b"]))
        ['key', '[a+b]']
        >>> AttrList(["key", "a+b"], operation="AVG")
        ['AVG(key)', 'AVG([a+b])']

    .. seealso::
        :py:class:`Attr`
    """

    @classmethod
    def sanitize(self, names):
        return [Attr.sanitize(name) for name in names]

    def __init__(self, names, operation=""):
        self.__operation = operation

        try:
            super(AttrList, self).__init__([Attr(name, operation) for name in names])
        except AttributeError:
            raise TypeError("name must be a string")

    def __repr__(self):
        return self.to_query()

    def __format__(self, format_spec):
        return self.to_query()

    def to_query(self):
        return ",".join([six.text_type(attr) for attr in self])

    def append(self, item):
        if not isinstance(item, (six.text_type, Attr)):
            raise TypeError("item should be a str/Attr instance: actual={}".format(type(item)))

        if isinstance(item, six.text_type):
            item = Attr(item, operation=self.__operation)

        super(AttrList, self).append(item)


class Distinct(QueryItem):
    @property
    def key(self):
        return self.__key

    def __init__(self, key):
        if not isinstance(key, (six.text_type, Attr, AttrList)):
            raise TypeError(
                "key should be a string/Attr/AttrList instance: actual={}".format(type(key))
            )

        self.__key = key
        if isinstance(key, six.text_type):
            self.__key = Attr(key)

    def to_query(self):
        return "DISTINCT {}".format(self.key)


class Value(QueryItem):
    """
    :param str value: Value associated with a key.
    :return:
        String that suitable for a value of a key.
        Return ``"NULL"`` if the value is |None|.
    :rtype: str

    :Examples:
        >>> from simplesqlite.query import Value
        >>> Value(1.2)
        '1.2'
        >>> Value("value")
        "'value'"
        >>> Value(None)
        'NULL'
    """

    def __init__(self, value):
        self._value = value

    def to_query(self):
        value = self._value

        if value is None:
            return "NULL"

        if typepy.Integer(value).is_type() or typepy.RealNumber(value).is_type():
            return six.text_type(value)

        try:
            if value.find("'") != -1:
                return '"{}"'.format(value)
        except (TypeError, AttributeError):
            pass

        return "'{}'".format(value)


class Where(QueryItem):
    """
    ``WHERE`` query clause.

    :param str key: Attribute name of the key.
    :param str value: Value of the right hand side associated with the key.
    :param str cmp_operator: Comparison  operator of WHERE query.
    :raises simplesqlite.SqlSyntaxError:
        If **a)** ``cmp_operator`` is invalid operator. Valid operators are as follows:
        ``"="``, ``"=="``, ``"!="``, ``"<>"``, ``">"``, ``">="``, ``"<"``, ``"<="``.
        **b)** the ``value`` is |None| and the ``cmp_operator`` is not ``"="``/``"!="``.

    :Examples:
        >>> from simplesqlite.query import Where
        >>> Where("key", "hoge")
        "key = 'hoge'"
        >>> Where("value", 1, cmp_operator=">")
        'value > 1'
    """

    __VALID_CMP_OPERATOR_LIST = ("=", "==", "!=", "<>", ">", ">=", "<", "<=")

    @property
    def key(self):
        return self._value

    @property
    def value(self):
        return self.__rhs

    def __init__(self, key, value, cmp_operator="="):
        super(Where, self).__init__(key)

        self.__rhs = value
        self.__cmp_operator = cmp_operator

        if not self.__cmp_operator:
            raise SqlSyntaxError("cmp_operator required")

        if self.__cmp_operator not in self.__VALID_CMP_OPERATOR_LIST:
            raise SqlSyntaxError("operator not supported: {}".format(self.__cmp_operator))

    def to_query(self):
        if self.value is None:
            if self.__cmp_operator == "=":
                return "{} IS NULL".format(Attr(self.key))
            elif self.__cmp_operator == "!=":
                return "{} IS NOT NULL".format(Attr(self.key))

            raise SqlSyntaxError(
                "Invalid operator ({:s}) with None right-hand side".format(self.__cmp_operator)
            )

        return "{} {:s} {}".format(Attr(self.key), self.__cmp_operator, Value(self.value))


class Select(QueryItem):
    """
    ``SELECT`` query clause.

    :param str select: Attribute for SELECT query.
    :param str table: Table name of executing the query.
    :param str where:
        Add a WHERE clause to execute query, if the value is not |None|.
    :param extra extra:
        Add additional clause to execute query, if the value is not |None|.
    :raises ValueError: ``select`` is empty string.
    :raises simplesqlite.NameValidationError:
        |raises_validate_table_name|

    :Examples:
        >>> from simplesqlite.query import Select, Where
        >>> Select(select="value", table="example")
        'SELECT value FROM example'
        >>> Select(select="value", table="example", where=Where("key", 1))
        'SELECT value FROM example WHERE key = 1'
        >>> Select(select="value", table="example", where=Where("key", 1), extra="ORDER BY value")
        'SELECT value FROM example WHERE key = 1 ORDER BY value'
    """

    def __init__(self, select, table, where=None, extra=None):
        self.__select = select
        self.__table = table
        self.__where = where
        self.__extra = extra

        validate_table_name(self.__table)

        if self.__where and not isinstance(where, (six.text_type, Where, And, Or)):
            raise TypeError(
                "where should be a str/Where/And/Or instance: actual={}".format(type(self.__where))
            )

        if not self.__select:
            raise ValueError("SELECT query required")

    def to_query(self):
        query_list = ["SELECT {}".format(self.__select), "FROM {}".format(Table(self.__table))]

        if self.__where:
            query_list.append("WHERE {}".format(self.__where))
        if self.__extra:
            query_list.append(self.__extra)

        return " ".join(query_list)


class Or(list, QueryItemInterface):
    """
    ``OR`` query clause.

    Args:
        where_list (list of |arg_where_type|):
            Query items that concatenating with ``OR``.
    """

    def __init__(self, where_list):
        for where in where_list:
            if not isinstance(where, (six.text_type, Where, And, Or)):
                raise TypeError(
                    "where_list item must either string or Where/And/Or class instance: actual={}".format(
                        type(where)
                    )
                )

        super(Or, self).__init__(where_list)

    def __repr__(self):
        return self.to_query()

    def __format__(self, format_spec):
        return self.to_query()

    def to_query(self):
        item_list = []

        for where in self:
            if isinstance(where, And):
                item_list.append("({})".format(where))
            else:
                item_list.append("{}".format(where))

        return " OR ".join(item_list)


class And(list, QueryItemInterface):
    """
    ``AND`` query clause.

    Args:
        where_list (list of |arg_where_type|):
            Query items that concatenating with ``AND``.
    """

    def __init__(self, where_list):
        for where in where_list:
            if not isinstance(where, (six.text_type, Where, And, Or)):
                raise TypeError(
                    "where_list item must either string or Where/And/Or class instance: actual={}".format(
                        type(where)
                    )
                )

        super(And, self).__init__(where_list)

    def __repr__(self):
        return self.to_query()

    def __format__(self, format_spec):
        return self.to_query()

    def to_query(self):
        item_list = []

        for where in self:
            if isinstance(where, Or):
                item_list.append("({})".format(where))
            else:
                item_list.append("{}".format(where))

        return " AND ".join(item_list)


class Insert(QueryItem):
    """
    INSERT query.

    :param str table: Table name of executing the query.
    :param AttrList attrs: Attributes that inserting to..
    :raises simplesqlite.NameValidationError:
        |raises_validate_table_name|
    """

    def __init__(self, table, attrs):
        validate_table_name(table)

        if not isinstance(attrs, AttrList):
            raise TypeError("attr must be a AttrList class instance: actual={}".format(type(attrs)))

        if typepy.is_empty_sequence(attrs):
            raise ValueError("empty attributes")

        self.__table = table
        self.__attrs = attrs

    def to_query(self):
        return "INSERT INTO {:s}({:s}) VALUES ({:s})".format(
            Table(self.__table),
            ",".join([attr.to_query() for attr in self.__attrs]),
            ",".join(["?" for _ in self.__attrs]),
        )


def make_index_name(table_name, attr_name):
    import hashlib

    re_invalid_chars = re.compile(
        "[{:s}]".format(re.escape("".join(ascii_symbols + unprintable_ascii_chars))), re.UNICODE
    )

    index_hash = hashlib.md5((table_name + attr_name).encode("utf8")).hexdigest()[:4]

    return "{:s}_{:s}_index_{}".format(
        re_invalid_chars.sub("", table_name), re_invalid_chars.sub("", attr_name), index_hash
    )
