from .version import Version

def compare(v1, v2):
    """Compares version v1 with version v2
    
    :param v1: Version 1 as a string.
    :param v2: Version 2 as a string.
    :return: 1 if v1 > v2, -1 if v1 < v2, 0 otherwise.
    """    
    v1 = Version(v1)
    v2 = Version(v2)

    if v1 > v2:
        return 1
    if v1 < v2:
        return -1
    return 0