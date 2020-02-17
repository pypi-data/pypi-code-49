"""
This module contains classes which extend Exception.
"""


class ConverterError(Exception):
    """
    An exception class for exceptional behavior that occurs while converting different molecule representations.
    """
    pass


class VectorsError(Exception):
    """
    An exception class for exceptional behavior that occurs while working with vectors.
    """
    pass


class ZMatError(Exception):
    """
    An exception class for exceptional behavior that occurs while working with z matrices.
    """
    pass
