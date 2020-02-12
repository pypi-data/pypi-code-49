from abc import ABC
from typing import Type

from ....abc import is_abstract_class
from ..._typing import RawJSONElement
from ...schema import JSONSchema
from ...serialise import JSONValidatedBiserialisable
from ._Property import Property


class ProxyProperty(Property, ABC):
    """
    Property which takes values of a type that is serialisable
    to/from JSON.
    """
    def __init__(self,
                 name: str = "",
                 type: Type[JSONValidatedBiserialisable] = JSONValidatedBiserialisable,
                 *,
                 optional: bool = False):
        super().__init__(
            name,
            optional=optional
        )

        # Type argument must be concrete
        if is_abstract_class(type):
            raise ValueError(f"type argument must be a concrete class, got {type.__name__}")

        # The type of values this property takes
        self.__type: Type[JSONValidatedBiserialisable] = type

    def type(self) -> Type[JSONValidatedBiserialisable]:
        """
        Gets the type of values this proxy-property takes.
        """
        return self.__type

    def get_json_validation_schema(self) -> JSONSchema:
        # Use the value-type's schema
        return self.__type.get_json_validation_schema()

    def _value_as_raw_json(self, instance, value: JSONValidatedBiserialisable) -> RawJSONElement:
        # Values are serialisable, so just serialise it
        return value.to_raw_json()

    def validate_value(self, instance, value):
        # Must be an instance of the correct type, or JSON deserialisable to the correct type
        if not isinstance(value, self.__type):
            try:
                if isinstance(value, str):
                    return self.__type.from_json_string(value)
                else:
                    return self.__type.from_raw_json(value)
            except Exception as e:
                raise ValueError(f"Error validating proxy value: {e}") from e

        return value
