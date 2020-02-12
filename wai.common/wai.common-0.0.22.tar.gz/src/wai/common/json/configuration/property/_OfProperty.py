from abc import abstractmethod
from typing import Tuple, List, Any, Iterable, Callable
from weakref import WeakKeyDictionary

from ...schema import JSONSchema
from ..._typing import RawJSONElement
from .._OptionallyPresent import OptionallyPresent
from .._Absent import Absent
from ._Property import Property
from ._DummyInstance import DummyInstance


class OfProperty(Property):
    """
    Base class for OneOfProperty and AnyOfProperty.
    """
    def __init__(self,
                 name: str = "",
                 sub_properties: Iterable[Property] = tuple(),
                 schema_function: Callable[[Iterable[JSONSchema]], JSONSchema] = None,  # one_of/any_of/all_of
                 *,
                 optional: bool = False):
        # Consume the sub-properties
        sub_properties = tuple(sub_properties)

        # Must provide at least 2 sub-properties
        if len(sub_properties) < 2:
            raise ValueError(f"Of properties require at least 2 sub-properties")

        super().__init__(
            name,
            optional=optional
        )

        self.__sub_properties: Tuple[Property] = sub_properties
        self.__instance_keys = WeakKeyDictionary()
        self.__schema_function = schema_function

    def _get_current_subproperty(self, instance) -> Tuple[OptionallyPresent[Property],
                                                          OptionallyPresent[DummyInstance]]:
        """
        Gets the sub-property which contains the value for the
        given instance, and the key to that value.

        :return:    The property and the instance key to its value,
                    or a pair of Absents if the value is absent.
        """
        # Only valid for instances
        self._require_instance(instance)

        # Get the current value
        value = super().__get__(instance, None)

        # If it's an index, convert it to the sub-property at that index
        if isinstance(value, int):
            return self.__sub_properties[value], self.__instance_keys[instance]

        return Absent, Absent

    def get_json_validation_schema(self) -> JSONSchema:
        return self.__schema_function(
            *(
                property.get_json_validation_schema()
                for property in self.__sub_properties
            )
        )

    def _set_unchecked(self, instance, value):
        # If setting an instance's value to absent, discard its
        # current instance key if it has one
        if value is Absent and instance in self.__instance_keys:
            del self.__instance_keys[instance]

        # Set as usual
        super()._set_unchecked(instance, value)

    def select_from_valid_subproperties(self, instance, value) -> Tuple[Any, int]:
        """
        Tests the given value against all sub-properties, and returns
        the validated value along with the index of the sub-property
        it should be stored against.

        :param instance:    The instance the value is for.
        :param value:       The value.
        :return:            The value to store, and the sub-property index
                            to store it against.
        """
        # Find the properties this value is valid for
        values = []
        for property in self.__sub_properties:
            # Record the validated value, or Absent if validation failed
            try:
                validated_value = property.validate_value(instance, value)
            except Exception:
                validated_value = Absent

            values.append(validated_value)

        # Select the canonical index
        subproperty_selection = self.choose_subproperty([value is not Absent for value in values])

        # Make sure the selection is in range
        if not isinstance(subproperty_selection, int) or not (0 <= subproperty_selection < len(self.__sub_properties)):
            raise ValueError(f"Error in internal index for Of property. "
                             f"Index should be integer in [0:{len(self.__sub_properties)}), "
                             f"got {subproperty_selection}")

        # Get the selection
        value = values[subproperty_selection]

        # Make sure the selected value is one of the successful ones
        if value is Absent:
            raise ValueError(f"Error selecting sub-property: selected sub-property {subproperty_selection} "
                             f"which failed validation")

        return value, subproperty_selection

    @abstractmethod
    def choose_subproperty(self, successes: List[bool]) -> int:
        """
        Allows the sub-classes to choose which sub-property should
        store a value based on the success or failure of all sub-
        properties validating the value. Should raise an ValueError if it
        can't decide.

        :param successes:   The list of property validation successes/failures.
        :return:            The index of the property to regard as storing the
                            value.
        """
        pass

    def __get__(self, instance, owner):
        # No instance returns the property itself
        if instance is None:
            return self

        # Get the current sub-property
        subproperty, instance_key = self._get_current_subproperty(instance)

        # If the current sub-property is absent then so is the value
        if subproperty is Absent:
            return Absent

        return subproperty.__get__(instance_key, owner)

    def _value_as_raw_json(self, instance, value) -> RawJSONElement:
        # Get the sub-property the value is stored in
        subproperty, instance_key = self._get_current_subproperty(instance)

        # Use the sub-property to convert the value to raw JSON
        return subproperty._value_as_raw_json(instance_key, value)

    def validate_value(self, instance, value) -> Any:
        # Select the sub-property to use
        value, subproperty_index = self.select_from_valid_subproperties(instance, value)

        # Set the value against the selected sub-property
        key = DummyInstance()
        self.__sub_properties[subproperty_index].__set__(key, value)
        self.__instance_keys[instance] = key

        # Our stored value is the sub-property index
        return subproperty_index
