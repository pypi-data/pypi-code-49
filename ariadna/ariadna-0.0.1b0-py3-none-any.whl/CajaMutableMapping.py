from .CajaMapping import CajaMapping
from collections.abc import MutableMapping, Hashable

__CAJA_BASE__ = CajaMapping
__CAJA_AGGREGATED_TRAIT__ = MutableMapping
__META__ = type('Meta', (type(__CAJA_BASE__), type(__CAJA_AGGREGATED_TRAIT__)), {})

class CajaMutableMapping(__CAJA_BASE__, __CAJA_AGGREGATED_TRAIT__, metaclass=__META__):

    @classmethod
    def _default_content(self) -> MutableMapping:
        return dict()

    # abc interface

    def __setitem__(self, key : Hashable, value) -> None:
        self._assign_item(key, value)
        
    def __delitem__(self, key : Hashable) -> None:
        self._del_item(key)
