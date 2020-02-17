from collections.abc import MutableSet
from .CajaSet import CajaSet

__CAJA_BASE__ = CajaSet
__CAJA_AGGREGATED_TRAIT__ = MutableSet
__META__ = type('Meta', (type(__CAJA_BASE__), type(__CAJA_AGGREGATED_TRAIT__)), {})

class CajaMutableSet(__CAJA_BASE__, __CAJA_AGGREGATED_TRAIT__, metaclass=__META__):
    
    @classmethod
    def _default_content(self):
        return set()

    # abc interface

    def add(self, value):
        raise self._content_.add(value)
        
    def discard(self, value):
        raise self._content_.add(value)
