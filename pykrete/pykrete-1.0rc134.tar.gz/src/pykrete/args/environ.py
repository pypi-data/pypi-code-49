"""
Environment argument handling
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
import os


def environ(var_name, role):
    """Gets an environment variable's value

    :param var_name: The variable's name
    :param role: The variable's role
    :return: The variable's value
    :exception SystemError: The variable is not defined in the environment
    """
    try:
        return os.environ[var_name]
    except KeyError:
        raise SystemError(f'Build requires that the "{var_name}"'
                          f' environment variable is set to {role}')
