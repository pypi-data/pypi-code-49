from .PathSplitter import PathSplitter
from .PathSplitter import RegexSplitter

__DEFAULT_PATH_SPLITTER__ = RegexSplitter

__cajas__ = [
    'Caja',
    'CajaMapping',
    'CajaMutableMapping',
    'CajaMutableSequence',
    'CajaMutableSet',
    'CajaSequence',
    'CajaSet'
]

from .Caja import Caja
from .CajaMapping import CajaMapping
from .CajaMutableMapping import CajaMutableMapping
from .CajaMutableSequence import CajaMutableSequence
from .CajaMutableSet import CajaMutableSet
from .CajaSequence import CajaSequence
from .CajaSet import CajaSet

__DEFAULT_NONE_CAJA__ = CajaMutableMapping

__all__ = __cajas__ + ['PathSplitter', 'RegexSplitter']