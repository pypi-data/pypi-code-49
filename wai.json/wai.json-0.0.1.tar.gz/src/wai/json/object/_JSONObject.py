from typing import Dict, TypeVar, List, Any, Union, Optional, Iterator, Tuple

from ..error import JSONValidationError, RequiredDisallowed, JSONPropertyError
from ..raw import RawJSONElement, RawJSONObject
from ..schema import JSONSchema, standard_object, IS_JSON_SCHEMA, IS_JSON_DEFINITION, TRIVIALLY_FAIL_SCHEMA, is_schema
from ..schema.constants import DEFINITIONS_KEYWORD
from ..serialise import JSONValidatedBiserialisable
from ..validator import StaticJSONValidator
from .property import RawProperty, Property
from ._typing import Absent, OptionallyPresent, PropertyValueType

# The type of this configuration
SelfType = TypeVar("SelfType", bound="Configuration")

# A schema which accepts any valid JSON value
DEFAULT_SCHEMA: JSONSchema = {DEFINITIONS_KEYWORD: IS_JSON_DEFINITION}
DEFAULT_SCHEMA.update(IS_JSON_SCHEMA)


def additional_properties_validation_as_property(validation: Union[JSONSchema, Property, None]) -> Optional[Property]:
    """
    Helper function which converts the prescribed additional properties validation
    into a property.

    :param validation:  The validation as returned from JSONObject._additional_properties_validation.
    :return:            The additional properties property.
    """
    # Return None for no validation or trivially-failing validation
    if validation is None or validation is TRIVIALLY_FAIL_SCHEMA:
        return None

    # If it's already a property, just make sure it's optional
    if isinstance(validation, Property):
        if not validation.is_optional:
            raise RequiredDisallowed(f"Validation for additional properties must be optional")

        return validation

    # Otherwise it's a schema, so make sure it's valid
    if not is_schema(validation):
        raise JSONValidationError(f"Validation for additional properties must be a property or a schema, "
                                  f"not a {type(validation).__name__}: {validation}")

    return RawProperty(schema=validation, optional=True)


class JSONObject(JSONValidatedBiserialisable[SelfType], StaticJSONValidator):
    """
    Base class for Python representations of JSON-format configuration files.
    All configurations are validated against a schema for format correctness.
    The attributes of a configuration should be either JSON types or nested
    configurations.
    """
    # Forward-declarations of class attributes
    # If JSONObject is instantiated directly, it has only additional properties
    # and they can be anything
    _required_properties: Dict[str, Property] = {}
    _optional_properties: Dict[str, Property] = {}
    _additional_property: Optional[Property] = additional_properties_validation_as_property(DEFAULT_SCHEMA)

    def __init__(self, **initial_values):
        # Create the property values container
        self._property_values: Dict[str, PropertyValueType] = {}

        # Make sure all required properties have values
        for required_property in self._required_properties:
            if required_property not in initial_values:
                raise JSONPropertyError(f"Value for required property '{required_property}' not set")

        # Set all properties named in initial values
        for name, value in initial_values.items():
            self.set_property(name, value)

    def has_property(self, name: str) -> bool:
        """
        Whether this object has a property with the given name. If the object
        allows additional properties, this will include additional properties
        which currently have values, and required/optional properties regardless
        of value.

        :param name:    The property name.
        :return:        True if the object has the property.
        """
        return name in self._property_values or name in self._optional_properties

    def get_property(self, name: str) -> PropertyValueType:
        """
        Gets the value of a property by name.

        :param name:    The name of the property.
        :return:        The property's value.
        """
        # Get the property's value if we have one
        if name in self._property_values:
            return self._property_values[name]

        return Absent

    def get_property_as_raw_json(self, name: str) -> OptionallyPresent[RawJSONElement]:
        """
        Gets the value of a property as raw JSON.

        :param name:    The property name.
        :return:        The raw JSON.
        """
        # Get the value
        value = self.get_property(name)

        # If it's a serialisable type, serialise it
        if isinstance(value, JSONValidatedBiserialisable):
            value = value.to_raw_json()

        return value

    def set_property(self, name: str, value: PropertyValueType):
        """
        Sets the value of a property by name.

        :param name:    The property to set.
        :param value:   The value to set.
        """
        # Get the property for setting the value
        prop = self._get_property(name)

        # Use the property to validate the value
        value = prop.validate_value(value)

        if value is Absent:
            if name in self._property_values:
                del self._property_values[name]
        else:
            self._property_values[name] = value

    def delete_property(self, name: str):
        """
        Removes the given property's value from this object.

        :param name:    The property's name.
        """
        self.set_property(name, Absent)

    def iterate_properties(self) -> Iterator[Tuple[bool, str, PropertyValueType]]:
        """
        Iterates through all properties of the object.

        :return:    A triple consisting of:
                     - Whether the property is optional.
                     - The property's name.
                     - The property's value.
        """
        # Required properties first
        for name in self._required_properties:
            yield False, name, self.get_property(name)

        # Optional properties
        for name in self._required_properties:
            yield True, name, self.get_property(name)

        # Additional properties
        for name, value in self._property_values.items():
            if name not in self._required_properties and name not in self._optional_properties:
                yield True, name, value

    @classmethod
    def allows_additional_properties(cls) -> bool:
        """
        Whether this object can contain additional properties.

        :return:    True if the object can contain additional properties.
        """
        return cls._additional_property is not None

    @classmethod
    def _get_property(cls, name: str) -> Property:
        """
        Gets the property descriptor to handle the named property.

        :param name:    The property name.
        :return:        The property descriptor.
        """
        if name in cls._required_properties:
            return cls._required_properties[name]
        elif name in cls._optional_properties:
            return cls._optional_properties[name]
        elif cls.allows_additional_properties():
            return cls._additional_property

        raise JSONPropertyError(f"JSONObject '{cls.__name__}' has no property '{name}', "
                                f"and doesn't allow additional properties")

    def __getitem__(self, item: str) -> PropertyValueType:
        return self.get_property(item)

    def __setitem__(self, key: str, value: PropertyValueType):
        self.set_property(key, value)

    def _serialise_to_raw_json(self) -> RawJSONObject:
        return {name: self.get_property_as_raw_json(name)
                for name in self._property_values}

    @classmethod
    def _deserialise_from_raw_json(cls, raw_json: RawJSONObject) -> SelfType:
        return cls(**raw_json)

    @classmethod
    def _get_json_validation_schema(cls) -> JSONSchema:
        # Extract the required property schemas
        required_properties_schema: Dict[str, JSONSchema] = {
            name: prop.get_json_validation_schema()
            for name, prop in cls._required_properties.items()
        }

        # Extract the optional property schemas
        optional_properties_schema: Dict[str, JSONSchema] = {
            name: prop.get_json_validation_schema()
            for name, prop in cls._optional_properties.items()
        }

        # If no additional properties allowed, return a schema indicating this
        if not cls.allows_additional_properties():
            return standard_object(required_properties_schema, optional_properties_schema)

        # Extract the additional properties schema
        additional_properties_schema: JSONSchema = cls._additional_property.get_json_validation_schema()

        # Create the schema
        return standard_object(required_properties_schema,
                               optional_properties_schema,
                               additional_properties=additional_properties_schema)

    @classmethod
    def _get_all_defined_properties(cls) -> Dict[str, Property]:
        """
        Gets all defined properties of this configuration.

        :return:    A dictionary of the properties of this configuration.
        """
        # Get all attribute names
        attribute_names: List[str] = dir(cls)

        # Get all public attributes
        attributes: List[Any] = [getattr(cls, name)
                                 for name in attribute_names
                                 if not name.startswith("_")]

        # Create the empty properties dict
        defined_properties = {}

        # Add each property in turn, checking for duplicate names
        for attribute in attributes:
            # Skip anything that's not a property
            if not isinstance(attribute, Property):
                continue

            # Check if another property is already using the name
            if attribute.name in defined_properties:
                raise JSONPropertyError(f"Multiple properties named '{attribute.name}' "
                                        f"for JSON object '{cls.__qualname__}'")

            # Add the property
            defined_properties[attribute.name] = attribute

        return defined_properties

    @classmethod
    def _additional_properties_validation(cls) -> Union[JSONSchema, Property, None]:
        """
        Gets the schema/property to validate any additional properties set
        on this configuration. By default all additional properties are allowed.
        Override to modify this behaviour.
        """
        return DEFAULT_SCHEMA

    def __init_subclass__(cls, **kwargs):
        # Perform any super initialisation
        super().__init_subclass__(**kwargs)

        # Get all of the defined properties
        defined_properties = cls._get_all_defined_properties()

        # Filter the required properties
        cls._required_properties: Dict[str, Property] = {
            name: value
            for name, value in defined_properties.items()
            if not value.is_optional
        }

        # Filter the optional properties
        cls._optional_properties: Dict[str, Property] = {
            name: value
            for name, value in defined_properties.items()
            if value.is_optional
        }

        # Create the additional property if allowed
        cls._additional_property: Optional[Property] = additional_properties_validation_as_property(
            cls._additional_properties_validation()
        )
