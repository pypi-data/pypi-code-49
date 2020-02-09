"""
Small utils shared between components
"""
import sys
import pkg_resources


def filter_nones(**kwargs):
    """Removes `None` parameters from kwargs

    Args:
        **kwargs:

    Returns:
        dict: `dict` of the non-null arguments
    """
    return {k: v for k, v in kwargs.items() if v is not None}


def pkg_version(package):
    """Gets the version of an installed (pip) package

    Args:
        package: the package name

    Returns:
        str: The version of the installed package.
    """
    try:
        dist = pkg_resources.get_distribution(package)
    except pkg_resources.DistributionNotFound:
        return None

    return str(dist.version)


def disco_version():
    """Gets disco's version"""
    return pkg_version('disco') or 'dev'


def str_without_prefix(data: str, prefix='/'):
    """Removes prefix (if present) from string.

    Args:
        data (str):
        prefix: prefix to be remove, defaults to '/'

    Returns:
        the string without the prefix if it was present
    """
    if data is None:
        return None
    return data if not data.startswith(prefix) else data[len(prefix):]


def str_without_suffix(data: str, suffix='/'):
    """Removes suffix (if present) from string.

    Args:
        data (str):
        suffix: suffix to be remove, defaults to '/'

    Returns:
        str: the string without the suffix if it was present
    """
    if data is None:
        return None
    return data if not data.endswith(suffix) else data[:-len(suffix)]


def is_venv():
    """Checks if the current code is executed in venv.
    Does NOT cover pyenv, conda and other setups

     Returns:
        bool: `True` if running venv, `False` otherwise
    """
    # https://stackoverflow.com/a/42580137/133568
    _has_real_prefix = hasattr(sys, 'real_prefix')
    _has_base_prefix = hasattr(sys, 'base_prefix')
    return _has_real_prefix or \
           (_has_base_prefix and sys.base_prefix != sys.prefix)


def shorten_string(data: str, max_len=15, short_tag: str = None):
    """Shortens thisverylongstring to thi..

    Args:
        data (str): input string
        max_len (int): max len of output
        short_tag (str): string to be used instead of shortened text

    Returns:
        str: the shortened text

    """
    short_tag = short_tag or '...'
    if not data or not isinstance(data, str) or len(data) <= max_len:
        return data

    return data[max_len - len(short_tag)] + short_tag


def merge_dictionaries(*args) -> dict:
    """Shallow merge dictionaries provided as arg

    Args:
        *args:

    Returns:
        dict: new instances of merged dictionaries
    """
    res = {}
    for arg in args:
        if arg is None or not isinstance(arg, dict):
            continue
        res.update(arg)
    return res
