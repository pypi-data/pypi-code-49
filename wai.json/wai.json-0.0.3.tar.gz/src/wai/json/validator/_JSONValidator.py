import json
from abc import ABC, abstractmethod
from functools import wraps
from typing import Callable, Any

import jsonschema
from wai.common.decorator import ensure_error_type
from wai.common.meta import does_not_raise, instanceoptionalmethod

from ..error import JSONValidationError
from ..raw import RawJSONElement, deep_copy
from ..schema import JSONSchema


class JSONValidator(ABC):
    """
    Interface for classes which can validate raw JSON.
    """
    @instanceoptionalmethod
    def with_validation(self, function: Callable[[Any], RawJSONElement]) -> Callable[[Any], RawJSONElement]:
        """
        Decorator which adds validation to a function returning raw JSON.

        :param function:    The function to decorate.
        :return:            The decorated function.
        """
        @wraps(function)
        def validated(*args, **kwargs) -> RawJSONElement:
            # Call the function
            raw_json: RawJSONElement = function(*args, **kwargs)

            # Perform validation
            self.validate_raw_json(raw_json)

            return raw_json

        return validated

    @instanceoptionalmethod
    @ensure_error_type(JSONValidationError, "Error validating raw JSON element {raw_json}: {0}")
    def validate_raw_json(self, raw_json: RawJSONElement):
        """
        Validates the raw JSON using this object's validation methods
        (schema, special).

        :param self:        The validator instance/class.
        :param raw_json:    The raw JSON to validate.
        """
        # Get the jsonschema validator
        validator = self.get_validator()

        # Perform schema validation
        validator.validate(raw_json)

        # Perform special validation
        self.perform_special_json_validation(raw_json)

    @instanceoptionalmethod
    def is_valid_raw_json(self, raw_json: RawJSONElement) -> bool:
        """
        Checks if the raw JSON is valid.

        :param self:        The validator instance/class.
        :param raw_json:    The raw JSON to check.
        :return:            True if the JSON is valid,
                            False if not.
        """
        return does_not_raise(self.validate_raw_json, raw_json)

    @instanceoptionalmethod
    @ensure_error_type(JSONValidationError, "Error validating JSON-format string {json_string}: {0}")
    def validate_json_string(self, json_string: str):
        """
        Validates the JSON-format string using this object's validation methods
        (schema, special).

        :param self:            The validator instance/class.
        :param json_string:     The JSON-format string to validate.
        """
        # Convert the string to raw JSON
        raw_json = json.loads(json_string)

        # Validate the raw JSON
        self.validate_raw_json(raw_json)

    @instanceoptionalmethod
    def is_valid_json_string(self, json_string: str) -> bool:
        """
        Checks if the JSON-format string is valid.

        :param self:            The validator instance/class.
        :param json_string:     The JSON-format string to check.
        :return:                True if the JSON is valid,
                                False if not.
        """
        return does_not_raise(self.validate_json_string, json_string)

    @instanceoptionalmethod
    @ensure_error_type(JSONValidationError, "Error getting JSON validation schema: {0}")
    def get_json_validation_schema(self) -> JSONSchema:
        """
        Gets the schema to validate JSON for objects of this type.
        This may be a cached object, so if it is necessary to modify
        the schema, use clone_json_validation_schema instead.

        :param self:    The validator instance/class.
        :return:        The schema.
        """
        if instanceoptionalmethod.will_fail_on_missing_instance(self._get_json_validation_schema):
            raise JSONValidationError(f"Method '{JSONValidator._get_json_validation_schema.__name__}' was "
                                      f"overridden by an instance-method, but was called from the "
                                      f"'{self.__name__}' class")

        return self._get_json_validation_schema()

    @abstractmethod
    @instanceoptionalmethod
    def _get_json_validation_schema(self) -> JSONSchema:
        """
        Gets the schema to validate JSON for objects of this type.
        This may be a cached object, so if it is necessary to modify
        the schema, use clone_json_validation_schema instead.

        :param self:    The validator instance/class.
        :return:        The schema.
        """
        pass

    @instanceoptionalmethod
    @ensure_error_type(JSONValidationError, "Error getting JSON validator: {0}")
    def get_validator(self):
        """
        Gets the jsonschema validator to use to perform JSON validation.

        :param self:    The validator instance/class.
        :return:        The jsonschema validator.
        """
        # Get our schema
        schema: JSONSchema = self.get_json_validation_schema()

        # Get the validator class
        validator_type = jsonschema.validators.validator_for(schema)

        # Check the schema is valid
        validator_type.check_schema(schema)

        # Create the instance
        return validator_type(schema)

    @instanceoptionalmethod
    @ensure_error_type(JSONValidationError, "Error cloning JSON validator: {0}")
    def clone_json_validation_schema(self) -> JSONSchema:
        """
        Gets a copy of the validation schema for this validator.
        Use this if you need to modify the schema.

        :param self:    The validator instance/class.
        :return:        The copy of the schema.
        """
        return deep_copy(self.get_json_validation_schema())

    @instanceoptionalmethod
    @ensure_error_type(JSONValidationError, "Error performing special JSON validation: {0}")
    def perform_special_json_validation(self, raw_json: RawJSONElement):
        """
        Optional method to perform custom validation of raw JSON elements
        for objects of this type. Should throw an exception if the raw JSON
        element doesn't meet the special validation criteria. By default
        does nothing.

        :param self:        The validator instance/class.
        :param raw_json:    The raw JSON to validate.
        """
        self._perform_special_json_validation(raw_json)

    @instanceoptionalmethod
    def _perform_special_json_validation(self, raw_json: RawJSONElement):
        """
        Optional method to perform custom validation of raw JSON elements
        for objects of this type. Should throw an exception if the raw JSON
        element doesn't meet the special validation criteria. By default
        does nothing.

        :param self:        The validator instance/class.
        :param raw_json:    The raw JSON to validate.
        """
        pass
