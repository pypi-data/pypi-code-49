from collections.abc import Set
from .Caja import Caja

__CAJA_BASE__ = Caja
__CAJA_AGGREGATED_TRAIT__ = Set
__META__ = type('Meta', (type(__CAJA_BASE__), type(__CAJA_AGGREGATED_TRAIT__)), {})

class CajaSet(__CAJA_BASE__, __CAJA_AGGREGATED_TRAIT__, metaclass=__META__):

    @classmethod
    def _default_content(self):
        return frozenset()