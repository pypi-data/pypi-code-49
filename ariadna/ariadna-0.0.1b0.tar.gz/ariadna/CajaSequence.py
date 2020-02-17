from collections.abc import Sequence, Iterator
from .Caja import Caja

__CAJA_BASE__ = Caja
__CAJA_AGGREGATED_TRAIT__ = Sequence
__META__ = type('Meta', (type(__CAJA_BASE__), type(__CAJA_AGGREGATED_TRAIT__)), {})

class CajaSequence(__CAJA_BASE__, __CAJA_AGGREGATED_TRAIT__, metaclass=__META__):
    
    @classmethod
    def _default_content(self) -> Sequence:
        return tuple()

    @__CAJA_BASE__.content.getter
    def content(self) -> Sequence:
        return type(self._content_)([
            item.content() if isinstance(item, Caja) else item
            for item in self._content_
        ])
    
    def _split_key(self, key) -> tuple:
        right = None
        if type(key) is slice or type(key) is int:
            left = key
        else:
            left, right = self.path_splitter(key)
            try: 
                left = int(left)
            except ValueError:
                left = self._parse_splice(left)
        return left, right

    def _parse_splice(self, splice_str: str) -> slice:
        parts = splice_str.split(':')
        start = int(parts[0]) if parts[0] else None
        stop  = int(parts[1]) if parts[1] else None
        step  = int(parts[2]) if len(parts) == 3 and parts[2] else None
        return slice(start, stop, step)

    # mixin methods

    def __reversed__(self) -> Iterator:
        return reversed(self._content_)
