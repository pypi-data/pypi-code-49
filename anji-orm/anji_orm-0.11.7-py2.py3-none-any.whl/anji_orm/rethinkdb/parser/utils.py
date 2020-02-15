from functools import reduce

import rethinkdb
import rethinkdb.ast
import rethinkdb.query

from ...core import QueryRow, DictQueryRow, QueryRowOrderMark

__author__ = "Bogdan Gladyshev"
__copyright__ = "Copyright 2017, Bogdan Gladyshev"
__credits__ = ["Bogdan Gladyshev"]
__license__ = "MIT"
__version__ = "0.11.7"
__maintainer__ = "Bogdan Gladyshev"
__email__ = "siredvin.dark@gmail.com"
__status__ = "Production"


def _build_row(row: QueryRow, document=rethinkdb.query.row) -> rethinkdb.ast.RqlQuery:
    if isinstance(row, DictQueryRow):
        return reduce(lambda x, y: x[y], row.row_path, document)
    return document[row.row_name]


def ensure_order_str(row, order: str):
    if order == 'desc':
        return rethinkdb.query.desc(row)
    return row


def ensure_order(row_order_mark: QueryRowOrderMark):
    if len(row_order_mark.row_path) == 1:
        result = row_order_mark.row_name
    else:
        def result(doc):
            return _build_row(row_order_mark.row, document=doc)

    return ensure_order_str(result, row_order_mark.order)
