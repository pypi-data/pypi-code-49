from abc import ABC
from typing import Type, Optional, Any

from wai.common.abc import is_abstract_class

from ...error import JSONPropertyError
from ...schema import JSONSchema
from ...serialise import JSONValidatedBiserialisable
from .._typing import PropertyValueType, Absent, OptionallyPresent
from ._Property import Property


class ProxyProperty(Property, ABC):
    """
    Property which takes values of a type that is serialisable
    to/from JSON.
    """
    def __init__(self,
                 name: Optional[str] = None,
                 *,
                 proxy: Type[JSONValidatedBiserialisable] = JSONValidatedBiserialisable,
                 optional: bool = False,
                 default: OptionallyPresent[PropertyValueType] = Absent):
        # Type argument must be concrete
        if is_abstract_class(proxy):
            raise JSONPropertyError(f"Proxy type argument must be a concrete class, got {proxy.__name__}")

        # The type of values this property takes
        self._type: Type[JSONValidatedBiserialisable] = proxy

        super().__init__(
            name,
            optional=optional,
            default=default
        )

    @property
    def proxy_type(self) -> Type[JSONValidatedBiserialisable]:
        """
        Gets the type of values this proxy-property takes.
        """
        return self._type

    def _get_json_validation_schema(self) -> JSONSchema:
        # Use the value-type's schema
        return self._type.get_json_validation_schema()

    def _validate_value(self, value: Any) -> PropertyValueType:
        # Must be an instance of the correct type, or JSON deserialisable to the correct type
        if not isinstance(value, self._type):
            try:
                if isinstance(value, str):
                    return self._type.from_json_string(value)
                else:
                    return self._type.from_raw_json(value)
            except Exception as e:
                raise JSONPropertyError(f"Error validating proxy value: {e}") from e

        return value
