import datetime


def DateToStr(date, mask='%d.%m.%Y', hours=0):
    return datetime.datetime.strftime(date + datetime.timedelta(hours=hours), mask)


def StrToDate(value_str, mask='%Y-%m-%dT%H:%M:%S'):
    value_str = str(value_str).split('.')[0]
    res = datetime.datetime.strptime(value_str, mask)
    return res
    # return res + datetime.timedelta(hours=3)
