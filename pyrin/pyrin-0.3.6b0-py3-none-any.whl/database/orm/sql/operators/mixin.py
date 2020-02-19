# -*- coding: utf-8 -*-
"""
database orm sql operators mixin module.
"""

from datetime import datetime

from sqlalchemy.sql.operators import ColumnOperators

import pyrin.utils.datetime as datetime_utils

from pyrin.utils.sqlalchemy import like_prefix, like_exact_prefix, \
    like_suffix, like_exact_suffix


class ColumnOperatorsMixin(ColumnOperators):
    """
    column operators mixin.
    this class provides some practical benefits
    to its subclasses for sql operations.
    """

    def between(self, cleft, cright, symmetric=False, **options):
        """
        produces an `expression.between` clause against the parent
        object, given the lower and upper range. this method is overridden
        to be able to handle datetime values more practical.

        :param object cleft: lower bound of clause.
        :param object cright: upper bound of clause.

        :param bool symmetric: specifies to emmit `between symmetric` to database.
                               note that not all databases support symmetric.
                               but `between symmetric` is equivalent to
                               `between least(a, b) and greatest(a, b)`.

        :keyword bool consider_begin_of_day: specifies that consider begin
                                             of day for lower datetime.
                                             defaults to True if not provided.
                                             this only has effect on datetime value.

        :keyword bool consider_end_of_day: specifies that consider end
                                           of day for upper datetime.
                                           defaults to True if not provided.
                                           this only has effect on datetime value.

        :returns: operation result
        """

        consider_begin_of_day = options.get('consider_begin_of_day', True)
        consider_end_of_day = options.get('consider_end_of_day', True)
        is_lower_datetime = isinstance(cleft, datetime)
        is_upper_datetime = isinstance(cright, datetime)
        if consider_begin_of_day is True and is_lower_datetime is True:
            cleft = datetime_utils.begin_of_day(cleft)

        if consider_end_of_day is True and is_upper_datetime is True:
            cright = datetime_utils.end_of_day(cright)

        # swapping values in case of user mistake.
        if symmetric is True and is_lower_datetime is True \
                and is_upper_datetime is True and cleft > cright:
            cleft, cright = cright, cleft
            symmetric = False

        return super().between(cleft, cright, symmetric)

    def _process_like_prefix(self, value, **options):
        """
        processes the value that should be prefixed to
        value for `like` expression based on given options.

        :param str value: expression to be compared.

        :keyword bool exact: specifies that value should be emitted without any
                             modifications. defaults to False if not provided.

        :keyword int begin_count: count of `_` chars to be attached to beginning.
                                  if not provided, `%` will be used.

        :note begin_count: this value has a limit of `LIKE_CHAR_COUNT_LIMIT`,
                           if the provided value goes upper than this limit,
                           a `%` will be attached instead of it. this limit
                           is for security reason.

        :returns: operation result
        """

        exact = options.get('exact', False)
        if exact is False:
            begin_wrapper = like_prefix, [value]
            begin_count = options.get('begin_count', None)
            if begin_count is not None:
                begin_wrapper = like_exact_prefix, [value, begin_count]

            value = begin_wrapper[0](*begin_wrapper[1])

        return value

    def _process_like_suffix(self, value, **options):
        """
        processes the value that should be suffixed to
        value for `like` expression based on given options.

        :param str value: expression to be compared.

        :keyword bool exact: specifies that value should be emitted without any
                             modifications. defaults to False if not provided.

        :keyword int end_count: count of `_` chars to be attached to end.
                                if not provided, `%` will be used.

        :note end_count: this value has a limit of `LIKE_CHAR_COUNT_LIMIT`,
                         if the provided value goes upper than this limit,
                         a `%` will be attached instead of it. this limit
                         is for security reason.

        :returns: operation result
        """

        exact = options.get('exact', False)
        if exact is False:
            end_wrapper = like_suffix, [value]
            end_count = options.get('end_count', None)
            if end_count is not None:
                end_wrapper = like_exact_suffix, [value, end_count]

            value = end_wrapper[0](*end_wrapper[1])

        return value

    def like(self, other, escape=None, **options):
        """
        implements the `like` operator.
        this method is overridden to apply `%` or couple of `_`
        place holders on both sides of input string in default mode.
        if you want to apply place holder to just one side, use
        `startswith()` or `endswith()` methods.

        :param str other: expression to be compared.

        :param str escape: optional escape character,
                           renders the `escape` keyword.

        :keyword bool exact: specifies that value should be emitted without any
                             modifications. defaults to False if not provided.

        :keyword int begin_count: count of `_` chars to be attached to beginning.
                                  if not provided, `%` will be used.

        :keyword int end_count: count of `_` chars to be attached to end.
                                if not provided, `%` will be used.

        :note begin_count, end_count: this value has a limit of `LIKE_CHAR_COUNT_LIMIT`,
                                      if the provided value goes upper than this limit,
                                      a `%` will be attached instead of it. this limit
                                      is for security reason.

        :returns: operation result
        """

        other = self._process_like_prefix(other, **options)
        other = self._process_like_suffix(other, **options)
        return super().like(other, escape)

    def ilike(self, other, escape=None, **options):
        """
        implements the `ilike` operator.
        this method is overridden to apply `%` or couple of `_`
        place holders on both sides of input string in default mode.
        if you want to apply place holder to just one side, use
        `istartswith()` or `iendswith()` methods.

        :param str other: expression to be compared.

        :param str escape: optional escape character,
                           renders the `escape` keyword.

        :keyword bool exact: specifies that value should be emitted without any
                             modifications. defaults to False if not provided.

        :keyword int begin_count: count of `_` chars to be attached to beginning.
                                  if not provided, `%` will be used.

        :keyword int end_count: count of `_` chars to be attached to end.
                                if not provided, `%` will be used.

        :note begin_count, end_count: this value has a limit of `LIKE_CHAR_COUNT_LIMIT`,
                                      if the provided value goes upper than this limit,
                                      a `%` will be attached instead of it. this limit
                                      is for security reason.

        :returns: operation result
        """

        other = self._process_like_prefix(other, **options)
        other = self._process_like_suffix(other, **options)
        return super().like(other, escape)

    def istartswith(self, other, **kwargs):
        """
        implements the `startswith` operator.
        produces an `ilike` expression that tests against a match for the
        start of a string value. for example:
        column like <other> || '%' or column like <other> || '_'
        this method provides a case-insensitive variant of `startswith()`
        method.

        :param str other: expression to be compared.

        :keyword bool autoescape: establishes an escape character within the like
                                  expression, then applies it to all occurrences of
                                  `%`, `_` and the escape character itself within the
                                  comparison value.

        :keyword str escape: optional escape character,
                             renders the `escape` keyword.

        :keyword bool exact: specifies that value should be emitted without any
                             modifications. defaults to False if not provided.

        :keyword int end_count: count of `_` chars to be attached to end.
                                if not provided, `%` will be used.

        :note end_count: this value has a limit of `LIKE_CHAR_COUNT_LIMIT`,
                         if the provided value goes upper than this limit,
                         a `%` will be attached instead of it. this limit
                         is for security reason.

        :returns: operation result
        """
