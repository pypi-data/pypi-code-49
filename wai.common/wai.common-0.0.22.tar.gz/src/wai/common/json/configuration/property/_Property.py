import functools
from abc import abstractmethod, ABC
from typing import Any
from weakref import WeakKeyDictionary

from .._OptionallyPresent import OptionallyPresent
from .._Absent import Absent
from ..._typing import RawJSONElement
from ...validator import JSONValidatorInstance


class Property(JSONValidatorInstance, ABC):
    """
    A property of a configuration describes a key to the object and the types
    of value it can take. The value of a property is a raw JSON element, or something
    that can be converted to/from raw JSON. The property name can be set to the
    empty string to inherit the attribute name it is set against in the
    configuration.
    """
    def __init__(self,
                 name: str = "",  # Default tells the property to inherit its attribute name
                 *,
                 optional: bool = False):
        self.__name: str = name
        self.__optional: bool = optional

        # The instance values of this property
        self.__values = WeakKeyDictionary()

    def name(self) -> str:
        """
        Gets the name of this property.

        :return:    The property name.
        """
        return self.__name

    def is_optional(self) -> bool:
        """
        Whether this property is an optional property.
        """
        return self.__optional

    def __get__(self, instance, owner):
        # If accessed from the class, return the property itself
        if instance is None:
            return self

        # Make sure a value has been set for this property
        if instance not in self.__values:
            raise AttributeError(f"{instance.__class__.__name__} has no value for property '{self.name()}'")

        # Get the value for this property
        return self.__values[instance]

    def get_as_raw_json(self, instance) -> OptionallyPresent[RawJSONElement]:
        """
        Gets the value of this property as raw JSON.

        :param instance:    The instance to get the value for.
        :return:            The raw JSON, or Absent.
        """
        # Make sure we have an instance
        self._require_instance(instance)

        # Get the value for the instance
        value = self.__get__(instance, None)

        # If the value is present, convert it to raw JSON
        if value is not Absent:
            value = self._value_as_raw_json(instance, value)

        return value

    def __set__(self, instance, value):
        # Must be accessed via an instance
        self._require_instance(instance)

        # Validate the value
        if value is not Absent:
            value = self.validate_value(instance, value)
        elif not self.is_optional():
            raise ValueError(f"Cannot set non-optional property '{self.name()}' as absent")

        # Set the value in the instance dictionary
        self._set_unchecked(instance, value)

    def _set_unchecked(self, instance, value):
        """
        Sets the value of this property without performing
        any validation.

        :param instance:    The instance to set the value against.
        :param value:       The value to set.
        """
        self.__values[instance] = value

    def __delete__(self, instance):
        # Can't delete the property itself
        if instance is None:
            raise AttributeError(f"Can't delete configuration properties")

        # Deleting the property value for an instance sets it as absent
        self.__set__(instance, Absent)

    def __set_name__(self, owner, name: str):
        # Can't have private properties
        if name.startswith("_"):
            raise AttributeError(f"Property names can't start with underscores ({name})")

        # Default the property name to the attribute name if one wasn't set
        if self.__name == "":
            self.__name = name

    @staticmethod
    def _require_instance(instance):
        """
        Helper method which raises an exception if instance is None.

        :param instance:    The instance.
        """
        # Make sure we are accessed via an instance
        if instance is None:
            raise AttributeError("Cannot access property through class (requires instance)")

    @functools.lru_cache(maxsize=None)
    def get_validator(self):
        return super().get_validator()

    @abstractmethod
    def _value_as_raw_json(self, instance, value) -> RawJSONElement:
        """
        Converts a value of this property to raw JSON.

        :param instance:    The instance the value belongs to.
        :param value:       The value to convert.
        :return:            The raw JSON.
        """
        pass

    @abstractmethod
    def validate_value(self, instance, value) -> Any:
        """
        Performs property value validation. Should raise a ValueError if
        validation fails, or return the actual value to store if validation
        passes.

        :param instance:    The instance the value is for.
        :param value:       The value to validate.
        :return:            The value to store.
        """
        pass
