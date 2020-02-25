def camelize(s):
    """
    Convert string with _ to camelcase
    :param s:
    :return:
    """
    import re
    return ''.join(x.capitalize() or '_' for x in s.split('_'))
