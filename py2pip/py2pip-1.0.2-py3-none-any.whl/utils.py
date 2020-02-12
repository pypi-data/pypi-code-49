


def validPySupportVersion(py_support_version):
    """
    Validate if the py_support version is a valid one
    :param py_support_version:  should be x.y (x>=2)
    :return: Boolean
    """
    try:
        py_version_split = py_support_version.split('.')

        # Must be 2 or more
        return int(py_version_split[0]) >= 2

    except (AttributeError, ValueError) as exp:
        return False