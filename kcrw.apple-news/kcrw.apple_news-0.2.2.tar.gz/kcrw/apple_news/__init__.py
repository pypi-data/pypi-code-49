# -*- coding: utf-8 -*-

"""Package for kcrw.apple_news."""

__title__ = "kcrw.apple_news"
__summary__ = "Library for using the Apple News API"
__url__ = "https://github.com/KCRW-org/kcrw.apple_news"

__version__ = "0.2.2"

__author__ = "Alec Mitchell"
__email__ = "alecpm@gmail.com"

__license__ = "MIT license",

from .api import API, AppleNewsError

__all__ = [
    "__title__", "__summary__", "__url__", "__version__", "__author__",
    "__email__", "__license__", "API", "AppleNewsError"
]
