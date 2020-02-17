from collections.abc import Mapping, Hashable
from frozendict import frozendict
from .Caja import Caja

__CAJA_BASE__ = Caja
__CAJA_AGGREGATED_TRAIT__ = Mapping
__META__ = type('Meta', (type(__CAJA_BASE__), type(__CAJA_AGGREGATED_TRAIT__)), {})

class CajaMapping(__CAJA_BASE__, __CAJA_AGGREGATED_TRAIT__, metaclass=__META__):
    
    @classmethod
    def _default_content(self) -> Mapping:
        return frozendict()

    @__CAJA_BASE__.content.getter
    def content(self) -> Mapping:
        return type(self._content_)({
            key.content if isinstance(key, Caja) else key
            : value.content if isinstance(value, Caja) else value
            for key, value in self._content_.items() 
        })

    def _split_key(self, key: Hashable) -> tuple:
        if type(key) is str:
            return self.path_splitter(key)
        return key, None

    def values(self):
        return self._content_.values()