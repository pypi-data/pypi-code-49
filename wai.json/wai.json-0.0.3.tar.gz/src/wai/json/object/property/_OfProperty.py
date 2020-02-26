from abc import abstractmethod, ABC
from typing import Tuple, List, Iterable, Callable, Optional, Any

from ...error import JSONPropertyError, OptionalDisallowed, OfPropertySelectionError
from ...schema import JSONSchema
from .._typing import Absent, PropertyValueType, OptionallyPresent
from ._Property import Property


class OfProperty(Property, ABC):
    """
    Base class for OneOfProperty and AnyOfProperty.
    """
    def __init__(self,
                 name: Optional[str] = None,
                 sub_properties: Iterable[Property] = tuple(),
                 *,
                 schema_function: Callable[[Iterable[JSONSchema]], JSONSchema] = None,  # one_of/any_of/all_of
                 optional: bool = False,
                 default: OptionallyPresent[PropertyValueType] = Absent):
        # Consume the sub-properties
        sub_properties = tuple(sub_properties)

        # Must provide at least 2 sub-properties
        if len(sub_properties) < 2:
            raise JSONPropertyError(f"Of properties require at least 2 sub-properties")

        # Sub-properties can't be optional
        for sub_property in sub_properties:
            if sub_property.is_optional:
                raise OptionalDisallowed(f"Can't use optional properties as sub-properties to any of the"
                                         f"'of' property variations")

        self._sub_properties: Tuple[Property] = sub_properties
        self._schema_function = schema_function

        super().__init__(
            name,
            optional=optional,
            default=default
        )

    def _get_json_validation_schema(self) -> JSONSchema:
        return self._schema_function(
            *(
                prop.get_json_validation_schema()
                for prop in self._sub_properties
            )
        )

    def _validate_value(self, value: Any) -> PropertyValueType:
        # Find the properties this value is valid for
        values = []
        for prop in self._sub_properties:
            # Record the validated value, or Absent if validation failed
            try:
                validated_value = prop.validate_value(value)
            except Exception:
                validated_value = Absent

            values.append(validated_value)

        # Select the canonical index
        subproperty_selection = self._choose_subproperty([value is not Absent for value in values])

        # Make sure the selection is in range
        if not isinstance(subproperty_selection, int) or not (0 <= subproperty_selection < len(self._sub_properties)):
            raise OfPropertySelectionError(f"Error in internal index for Of property. "
                                           f"Index should be integer in [0:{len(self._sub_properties)}), "
                                           f"got {subproperty_selection}")

        # Get the selection
        value = values[subproperty_selection]

        # Make sure the selected value is one of the successful ones
        if value is Absent:
            raise OfPropertySelectionError(f"Error selecting sub-property: selected sub-property "
                                           f"{subproperty_selection} which failed validation")

        return value

    @classmethod
    @abstractmethod
    def _choose_subproperty(cls, successes: List[bool]) -> int:
        """
        Allows the sub-classes to choose which sub-property should
        store a value based on the success or failure of all sub-
        properties validating the value. Should raise an exception if it
        can't decide.

        :param successes:   The list of property validation successes/failures.
        :return:            The index of the property to regard as storing the
                            value.
        """
        pass
