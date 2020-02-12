from typing import Optional

from ._Property import Property
from ._ProxyProperty import ProxyProperty
from ._ArrayProxy import ArrayProxy
from ._RawProperty import RawProperty


class ArrayProperty(ProxyProperty):
    """
    Property which validates a regular array of elements.
    """
    def __init__(self,
                 name: str = "",
                 element_property: Property = RawProperty(),  # Default property always fails, so will need replacing
                 min_elements: int = 0,
                 max_elements: Optional[int] = None,
                 unique_elements: bool = False,
                 *,
                 optional: bool = False):
        # Create a closure class to proxy the array
        class ClosureArrayProxy(ArrayProxy):
            @classmethod
            def element_property(cls) -> Property:
                return element_property

            @classmethod
            def min_elements(cls) -> int:
                return min_elements

            @classmethod
            def max_elements(cls) -> Optional[int]:
                return max_elements

            @classmethod
            def unique_elements(cls) -> bool:
                return unique_elements

        super().__init__(
            name,
            ClosureArrayProxy,
            optional=optional
        )

    def validate_value(self, instance, value):
        # Convert other proxy-arrays and raw lists/tuples to our proxy-type
        if (isinstance(value, ArrayProxy) and not isinstance(value, self.type())) or \
           isinstance(value, list) or isinstance(value, tuple):
            value = self.type()(value)

        return super().validate_value(instance, value)
