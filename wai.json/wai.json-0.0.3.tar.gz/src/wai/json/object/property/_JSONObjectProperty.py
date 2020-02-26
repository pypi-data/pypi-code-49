from typing import Type, Optional

from .._typing import PropertyValueType, Absent, OptionallyPresent
from ._ProxyProperty import ProxyProperty


class JSONObjectProperty(ProxyProperty):
    """
    Property which validates a sub-configuration (essentially an object).
    """
    def __init__(self,
                 name: Optional[str] = None,
                 object_type: Optional[Type['JSONObject']] = None,
                 *,
                 optional: bool = False,
                 default: OptionallyPresent[PropertyValueType] = Absent):
        # Have to local-import JSONObject to avoid circular reference
        from .._JSONObject import JSONObject

        # If no object type specified, allow any object
        if object_type is None:
            object_type = JSONObject

        super().__init__(
            name,
            proxy=object_type,
            optional=optional,
            default=default
        )

    @property
    def object_type(self) -> Type['JSONObject']:
        """
        Gets the type of JSON object this property takes.
        """
        return self.proxy_type
