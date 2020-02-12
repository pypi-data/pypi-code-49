from ._Property import Property
from ._ProxyProperty import ProxyProperty
from ._MapProxy import MapProxy
from ._RawProperty import RawProperty


class MapProperty(ProxyProperty):
    """
    Property which validates a map of strings to some other type.
    """
    def __init__(self,
                 name: str = "",
                 value_property: Property = RawProperty(),  # Default property always fails, so will need replacing
                 *,
                 optional: bool = False):
        # Create a closure class to proxy the map
        class ClosureMapProxy(MapProxy):
            @classmethod
            def value_property(cls) -> Property:
                return value_property

        super().__init__(
            name,
            ClosureMapProxy,
            optional=optional
        )

    def validate_value(self, instance, value):
        # Convert other map-proxies and raw dictionaries to our proxy-type
        if (isinstance(value, MapProxy) and not isinstance(value, self.type())) or \
           isinstance(value, dict):
            value = self.type()(value)

        return super().validate_value(instance, value)
