from typing import Optional, Any

from .._typing import PropertyValueType
from .proxies import ArrayProxy
from ._Property import Property
from ._ProxyProperty import ProxyProperty
from ._RawProperty import RawProperty


class ArrayProperty(ProxyProperty):
    """
    Property which validates a regular array of elements.
    """
    def __init__(self,
                 name: Optional[str] = None,
                 element_property: Property = RawProperty(),
                 *,
                 min_elements: int = 0,
                 max_elements: Optional[int] = None,
                 unique_elements: bool = False,
                 optional: bool = False):
        # Create a closure class to proxy the array

        super().__init__(
            name,
            proxy=ArrayProxy.specify(element_property,
                                     min_elements,
                                     max_elements,
                                     unique_elements),
            optional=optional
        )

    def _validate_value(self, value: Any) -> PropertyValueType:
        # Convert other proxy-arrays and raw lists/tuples to our proxy-type
        if ((isinstance(value, ArrayProxy) and not isinstance(value, self.proxy_type))
                or isinstance(value, list)
                or isinstance(value, tuple)):
            return self.proxy_type(value)

        return super()._validate_value(value)
