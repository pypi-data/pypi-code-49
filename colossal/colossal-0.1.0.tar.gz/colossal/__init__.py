import codecs

from . import jinja_encoding
from . import macros_encoding


def register():
    codecs.register(jinja_encoding.search_function)
    codecs.register(macros_encoding.search_function)
