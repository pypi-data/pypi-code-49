import json
import re
from datetime import datetime, timedelta


'''
DATES relatives parsers
_______________________
'''


def absolute_date(str_date):
    ''' finds a date in a iso-type format 
    input : str() : "2020-01-20" or "2020-01-20T12" or "2020-01-20T17:44:34.581634Z"
    output : {"found":True|False, "datetime":datetime()}

    '''
    if type(str_date) != str:
        return{"found": False}
    match = re.search(
        '([1-2][0-9]{3})-([0-1][0-9])-([0-3][0-9])T?([0-2][0-9])?:?([0-5][0-9])?:?([0-5][0-9])?.?([0-9]{6})?', str_date)
    if match:
        year = int(match.group(1))
        month = int(match.group(2))
        day = int(match.group(3))
        hours = int(match.group(4) if match.group(4) is not None else 0)
        minutes = int(match.group(5) if match.group(5) is not None else 0)
        seconds = int(match.group(6) if match.group(6) is not None else 0)
        milli = int(match.group(7) if match.group(7) is not None else 0)
        return {"found": True, "datetime": datetime(year, month, day, hours, minutes, seconds, milli)}
    else:
        return {"found": False}


def relative_date(str_date):
    ''' finds a date in a relative format (relative to datetime.now)
    input : str() : "days:1", "days:4", "hours:10", "minutes:10"
    output : {"found":True|False, "datetime":datetime()}

    '''
    try:
        str_splitted = str_date.split(':')
        if str_splitted[0] == "minutes":
            return {"found": True, "datetime": datetime.utcnow() + timedelta(minutes=int(str_splitted[1]))}
        elif str_splitted[0] == "hours":
            return {"found": True, "datetime": datetime.utcnow() + timedelta(hours=int(str_splitted[1]))}
        elif str_splitted[0] == "days":
            return {"found": True, "datetime": datetime.utcnow() + timedelta(days=int(str_splitted[1]))}
        return {"found": False}
    except:
        return {"found": False}


def get_abs_rel_date(str_date):
    ''' Combines absolute_date and relative_date
    input: str() (see above)
    output:datetime()|None
    '''
    absolute = absolute_date(str_date)
    if absolute["found"]:
        return absolute["datetime"]
    relative = relative_date(str_date)
    if relative["found"]:
        return relative["datetime"]
    else:
        return str_date


def str_to_timedelta(str_date):
    try:
        str_splitted = str_date.split(":")
        if str_splitted[0] == "minutes":
            return timedelta(minutes=int(str_splitted[1]))
        elif str_splitted[0] == "hours":
            return timedelta(hours=int(str_splitted[1]))
        elif str_splitted[0] == "days":
            return timedelta(days=int(str_splitted[1]))
        return None
    except:
        return None
