from datetime import datetime, timedelta
from math import modf
import re
from typing import Generator

ISO8601_SUFFIX = re.compile(r'^(.+?)([.,]\d+)?([-+]\d{2}:?\d{0,2}|Z)?$')


def gen_iso8601_formats() -> Generator[str, None, None]:
    # See https://en.wikipedia.org/wiki/ISO_8601 for details on spec
    date_separators = ('', '-',)
    time_separators = ('', ':',)
    date_formats = (
        ('%G', 'W%V', '%u',),
        ('%Y', '%j',),
        ('%Y', '%m', '%d',),
    )
    time_formats = (
        ('%H',),
        ('%H', '%M',),
        ('%H', '%M', '%S',),
    )
    for date_separator in date_separators:
        for time_separator in time_separators:
            for date_format in date_formats:
                for time_format in time_formats:
                    yield f'{date_separator.join(date_format)}T{time_separator.join(time_format)}'


def process_fraction(fraction, lowest_order_time_element):
    """
    TODO: Improve this function. It is not a very elegant brute-force algorithm

    >>> process_fraction(0.5555555555555555, 'H')
    (33, 20, 0)
    >>> process_fraction(0.5555555555555555, 'M')
    (0, 33, 333333)
    >>> process_fraction(0.5555555555555555, 'S')
    (0, 0, 555556)
    >>> process_fraction(0.5083676267901234, 'H')
    (30, 30, 123456)
    >>> process_fraction(0.5083676267901234, 'M')
    (0, 30, 502058)
    >>> process_fraction(0.5083676267901234, 'S')
    (0, 0, 508368)
    """
    if lowest_order_time_element == 'H':
        dec_0, whole_0 = modf(60 * fraction)
        dec_1, whole_1 = modf(60 * dec_0)
        dec_2, whole_2 = modf(round(whole_1 + dec_1, 6))
        return int(whole_0), int(whole_2), int(round(dec_2, 6) * 1e6)
    elif lowest_order_time_element == 'M':
        dec_1, whole_1 = modf(60 * fraction)
        dec_2, whole_2 = modf(round(whole_1 + dec_1, 6))
        return 0, int(whole_2), int(round(dec_2, 6) * 1e6)
    elif lowest_order_time_element == 'S':
        return 0, 0, int(round(fraction, 6) * 1e6)


def get_datetime_dict(dt: datetime) -> dict:
    # TODO: Fix ugly long lines with lots of repitition
    return {
        'iso-date': {
            'year': dt.year,
            'month': dt.month,
            'day': dt.day,
        },
        'iso-week-date': {
            'year': dt.strftime('%G'),
            'week': dt.strftime('%V'),
            'day': dt.strftime('%u'),
        },
        'iso-ordinal-date': {
            'year': dt.strftime('%Y'),
            'day': dt.strftime('%j'),
        },
        'iso-time': {
            'hour': dt.hour,
            'minute': dt.minute,
            'second': dt.second,
            'microsecond': dt.microsecond,
            'tzname': dt.tzname()
        },
        'iso-format': {
            'datetime': {
                'default': dt.isoformat(),
                'week': f'{dt.strftime("%G")}-W{dt.strftime("%V")}-{dt.strftime("%u")}T{dt.strftime("%H")}:{dt.strftime("%M")}:{dt.strftime("%S")}{"." + dt.strftime("%f") if dt.strftime("%f") != "000000" else ""}{dt.tzname().replace("UTC", "") or "+00:00" if dt.tzname() else ""}',
                'ordinal': f'{dt.strftime("%Y")}-{dt.strftime("%j")}T{dt.strftime("%H")}:{dt.strftime("%M")}:{dt.strftime("%S")}{"." + dt.strftime("%f") if dt.strftime("%f") != "000000" else ""}{dt.tzname().replace("UTC", "") or "+00:00" if dt.tzname() else ""}'
            },
            'date': {
                'default': f'{dt.strftime("%Y")}-{dt.strftime("%m")}-{dt.strftime("%d")}',
                'week': f'{dt.strftime("%G")}-W{dt.strftime("%V")}-{dt.strftime("%u")}',
                'ordinal': f'{dt.strftime("%Y")}-{dt.strftime("%j")}'
            },
            'time': {
                'default': f'{dt.strftime("%H")}:{dt.strftime("%M")}:{dt.strftime("%S")}{"." + dt.strftime("%f")  if dt.strftime("%f") != "000000" else ""}{dt.tzname().replace("UTC", "") or "+00:00" if dt.tzname() else ""}',
            },
            'name': {
                'month': {
                    'short': dt.strftime('%b'),
                    'long': dt.strftime('%B')
                },
                'day': {
                    'short': dt.strftime('%a'),
                    'long': dt.strftime('%A')
                }
            }
        }
    }


def get_datetime(time_string: str) -> datetime:
    """
    This function attempts to support all ISO 8601 formats.
    """
    # Necessary to recognise time strings ending with Z as UTC
    iso8601_suffix = ISO8601_SUFFIX.search(time_string)
    fraction = iso8601_suffix.group(2)
    utc_offset = iso8601_suffix.group(3)
    remainder_time_string = iso8601_suffix.group(1)
    if utc_offset:
        reformatted_utc_offset = utc_offset.replace('Z', '+0000').replace(':', '').ljust(5, '0')
        remainder_time_string += reformatted_utc_offset
    for fmt in gen_iso8601_formats():
        fmt_with_offset = fmt
        if utc_offset:
            fmt_with_offset = fmt + '%z'
        try:
            base_datetime = datetime.strptime(remainder_time_string, fmt_with_offset)
        except ValueError:
            pass
        else:
            mins, secs, microseconds = process_fraction(float(fraction or '.0'), lowest_order_time_element=fmt[-1])
            return base_datetime + timedelta(minutes=mins, seconds=secs, microseconds=microseconds)
    raise ValueError(f'{time_string} does not conform to an ISO 8601 compatible format.')
