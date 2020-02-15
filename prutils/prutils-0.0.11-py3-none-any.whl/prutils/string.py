import re


def get_re_first(pattern, string, flags=0):
    """
    print(get_re_first("\\d", "abc1") == "1")
    :param pattern:
    :param string:
    :param flags:
    :return:
    """
    r = re.search(pattern, string, flags)
    return r.group()


def get_re_all(pattern, string, flags=0):
    r = re.findall(pattern, string, flags)
    return r


def get_re_last(pattern, string, flags=0):
    return get_re_all(pattern, string, flags)[-1]



