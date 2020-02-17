from collections.abc import MutableSequence
from .CajaSequence import CajaSequence

__CAJA_BASE__ = CajaSequence
__CAJA_AGGREGATED_TRAIT__ = MutableSequence
__META__ = type('Meta', (type(__CAJA_BASE__), type(__CAJA_AGGREGATED_TRAIT__)), {})

class CajaMutableSequence(__CAJA_BASE__, __CAJA_AGGREGATED_TRAIT__, metaclass=__META__):
    
    @classmethod
    def _default_content(self):
        return list()

    # abc interface

    def __setitem__(self, key, value) -> None:
        self._assign_item(key, value)
    
    def __delitem__(self, key) -> None:
        self._del_item(key)
    
    def insert(self, index, value) -> None:
        self._content_.insert(index, value)
