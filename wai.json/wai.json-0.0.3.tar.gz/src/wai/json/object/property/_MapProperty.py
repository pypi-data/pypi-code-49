from typing import Optional, Any

from .._typing import PropertyValueType, Absent, OptionallyPresent
from .proxies import MapProxy
from ._Property import Property
from ._ProxyProperty import ProxyProperty
from ._RawProperty import RawProperty


class MapProperty(ProxyProperty):
    """
    Property which validates a map of strings to some other type.
    """
    def __init__(self,
                 name: Optional[str] = None,
                 value_property: Property = RawProperty(),
                 *,
                 optional: bool = False,
                 default: OptionallyPresent[PropertyValueType] = Absent):
        super().__init__(
            name,
            proxy=MapProxy.specify(value_property),
            optional=optional,
            default=default
        )

    def _validate_value(self, value: Any) -> PropertyValueType:
        # Convert other map-proxies and raw dictionaries to our proxy-type
        if ((isinstance(value, MapProxy) and not isinstance(value, self.proxy_type))
                or isinstance(value, dict)):
            return self.proxy_type(value)

        return super()._validate_value(value)
