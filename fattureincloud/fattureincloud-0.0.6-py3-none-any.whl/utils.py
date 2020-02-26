def format_date(d):
    """
    Format a python date object into a value suitable for the API
    :param d: date timestamp
    :return:
    """
    return d.strftime('%d/%m/%Y')


def format_time(dt):
    """
    Format a python datetime object into a value suitable for the API
    :param dt: datetime timestamp
    :return:
    """
    return dt.strftime('%d/%m/%Y %H:%M:%S')