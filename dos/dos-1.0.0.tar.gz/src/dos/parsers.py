import datetime
import re
from decimal import Decimal, InvalidOperation
from typing import Union

import arrow
import arrow.parser


def extract_number(val: Union[int, float, Decimal, str]) -> Decimal:

    if isinstance(val, (int, float, Decimal)):
        return Decimal(val)

    val = str(val)
    val = re.sub(r'([$,%]|\s)', "", val)

    if val == "-":
        val = "0"

    if re.search(r'^\(\d+(\.\d+)?\)$', val):
        val = "-" + re.sub(r'[()]', "", val)

    try:
        return Decimal(val)
    except InvalidOperation:
        raise InvalidOperation(val)


def extract_arrow(val: Union[str, int, datetime.datetime, arrow.Arrow]) -> arrow.Arrow:

    if isinstance(val, datetime.datetime):
        return arrow.get(val)

    if isinstance(val, arrow.Arrow):
        return val

    if isinstance(val, int):
        val = str(val)
        if not val.startswith("20"):
            raise ValueError(
                "Year must begin with 20 (value was {!r})"
                .format(val)
            )

        if len(val) != 8:
            raise ValueError(
                "When parsing an integer as a date, it must have length 8, not "
                "{} (value was {!r})"
                .format(len(val), val)
            )

        return arrow.get("{}-{}-{}".format(val[0:4], val[4:6], val[6:8]))

    val = val.strip()

    if len(val) == 8 and val.isdigit():
        return arrow.get("{}-{}-{}".format(val[0:4], val[4:6], val[6:8]))

    if "/" in val:
        parts = val.split("/")
        parts = [p.zfill(2) for p in parts]
        val = "/".join(parts)

    try:
        formats = [
            "MM/DD/YYYY",
            "MM/DD/YY",
        ]

        return arrow.get(val, formats)
    except arrow.parser.ParserError:
        return arrow.get(val)
