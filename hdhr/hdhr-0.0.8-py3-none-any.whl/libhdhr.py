import logging

from ctypes import cdll
from ctypes.util import find_library

_LOGGER = logging.getLogger(__name__)

_FILEPATH = find_library('hdhomerun')
if _FILEPATH is None:
    _FILEPATH = 'libhdhomerun.so'

_LOGGER.debug("Found libhdhomerun library: %s" % _FILEPATH)

library = cdll.LoadLibrary(_FILEPATH)

