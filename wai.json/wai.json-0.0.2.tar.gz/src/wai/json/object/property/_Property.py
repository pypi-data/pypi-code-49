from abc import ABC, abstractmethod
from typing import Any, Optional

from ...error import JSONPropertyError
from ...validator import StaticJSONValidator
from .._typing import PropertyValueType, Absent


class Property(StaticJSONValidator, ABC):
    """
    A property of a configuration describes a key to the object and the types
    of value it can take. The value of a property is a raw JSON element, or something
    that can be converted to/from raw JSON. The property name can be set to the
    empty string to inherit the attribute name it is set against in the
    configuration.
    """
    def __init__(self,
                 name: Optional[str] = None,  # Default tells the property to inherit its attribute name
                 *,
                 optional: bool = False):
        # Can't use the empty string as a name
        if name == "":
            raise JSONPropertyError("Can't name properties with the empty string")

        self._name: str = name if name is not None else ""
        self._attribute_name: str = ""
        self._optional: bool = optional

    @property
    def name(self) -> str:
        """
        Gets the name of this property.

        :return:    The property name.
        """
        return self._name

    @property
    def is_optional(self) -> bool:
        """
        Whether this property is an optional property.
        """
        return self._optional

    def __get__(self, instance, owner):
        # If accessed from the class, return the property itself
        if instance is None:
            return self

        # Check the instance is valid
        self._check_instance(instance, "get")

        return instance.get_property(self._name)

    def __set__(self, instance, value):
        # Check the instance is valid
        self._check_instance(instance, "set")

        # Don't need to validate the value as JSONObject will
        # call back to us as part of set_property.
        instance.set_property(self._name, value)

    def __delete__(self, instance):
        # Check the instance is valid
        self._check_instance(instance, "delete")

        instance.delete_property(self._name)

    def __set_name__(self, owner, name: str):
        # Can't reset the name
        if self._attribute_name != "" and self._attribute_name != name:
            raise JSONPropertyError(f"Attempted to reassign property '{self._name}' to attribute '{name}' "
                                    f"(already assigned to attribute '{self._attribute_name}')")

        # Can't have private properties (except for _additional_property)
        if name.startswith("_") and name != "_additional_property":
            raise JSONPropertyError(f"Property attribute names can't start with underscores ({name})")

        # Save the attribute name
        self._attribute_name = name

        # Inherit the attribute name as the property name if one wasn't
        # explicitly set
        if self._name == "":
            self._name = name

    @staticmethod
    def _check_instance(instance: Any, method: str):
        """
        Checks that the instance is available and a JSON object.

        :param instance:    The instance to check.
        :param method:      The method checking the instance, for error messages.
        """
        # JSONObject requires local import to avoid circular dependency
        from .._JSONObject import JSONObject

        # Instance must be a JSON object
        if not isinstance(instance, JSONObject):
            raise JSONPropertyError(f"Can only {method} value from a property "
                                    f"if called from a JSON object")

    def validate_value(self, value: Any) -> PropertyValueType:
        """
        Performs property value validation. Should raise an exception if
        validation fails, or return the actual value to store if validation
        passes.

        :param value:       The value to validate.
        :return:            The value to store.
        """
        # Default checking is for absent values on required properties
        if value is Absent:
            if not self.is_optional:
                raise JSONPropertyError(f"Required property '{self.name}' can't be set absent")

            return value

        return self._validate_value(value)

    @abstractmethod
    def _validate_value(self, value: Any) -> PropertyValueType:
        """
        Performs property value validation. Should raise an exception if
        validation fails, or return the actual value to store if validation
        passes.

        :param value:       The value to validate.
        :return:            The value to store.
        """
        pass
