import decimal
import logging
import enum

import arrow

from dos.parsers import extract_arrow, extract_number

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.CRITICAL)


NO_VALUE = object()


class OpenAPIPropType(enum.Enum):
    INTEGER = "integer"
    NUMBER = "number"
    STRING = "string"
    BOOLEAN = "boolean"
    ARRAY = "array"
    OBJECT = "object"


class ValidationError(ValueError):
    def __init__(self, message):
        super().__init__()
        self.message = message


class Prop:

    def __init__(self, description=None, required=True, nullable=False, validators=None):
        self.description = description
        self.required = required
        self.nullable = nullable
        self.validators = validators

    def __deepcopy__(self, memo):  # pylint: disable=unused-argument
        return type(self)(
            description=self.description,
            required=self.required,
            nullable=self.nullable,
            validators=self.validators
        )

    def parse_input(self, prop_value):  # pylint: disable=no-self-use
        return prop_value

    def format_output(self, prop_value):  # pylint: disable=no-self-use
        return prop_value

    def parse_input_and_validate(self, input_structure_field_name, body, prop_value=NO_VALUE):

        if prop_value is NO_VALUE:
            prop_value = body.get(input_structure_field_name)

        try:
            prop_value = self.parse_input(prop_value)
        except (ValueError, TypeError, decimal.InvalidOperation) as ambiguous_error:
            error = (f"The value {prop_value!r} from field '{input_structure_field_name}' "
                     f"is the wrong type, expected: {self.__class__.__name__}")
            LOGGER.critical(error + " /// Error: " + str(ambiguous_error))  # pylint: disable=logging-not-lazy
            raise ValidationError(error)

        return self.validate(input_structure_field_name, body, prop_value)

    def format_output_and_validate(self, output_structure_field_name, body, prop_value=NO_VALUE):

        if prop_value is NO_VALUE:
            if body is None:
                prop_value = None
            else:
                prop_value = body.get(output_structure_field_name)

        prop_value = self.validate(output_structure_field_name, body, prop_value)

        return self.format_output(prop_value)

    def validate(self, output_structure_field_name, body, prop_value):

        if self.required:
            if output_structure_field_name is not None and body is not None:
                if output_structure_field_name not in body:
                    raise ValidationError(
                        f"The field '{output_structure_field_name}' is required "
                        f"but not found in the body!"
                    )

        if not self.nullable:
            if body is not None:
                if output_structure_field_name in body:
                    if prop_value is None:
                        raise ValidationError(
                            f"Non nullable field '{output_structure_field_name}' "
                            f"is null!"
                        )

        if prop_value is not None:
            if not isinstance(prop_value, self.types):  # pylint: disable=no-member
                raise ValidationError(
                    f"The value {prop_value!r} from field '{output_structure_field_name}' "
                    f"is the wrong type, expected: {self.__class__.__name__}"
                )

        if self.validators is not None:
            for validator in self.validators:
                error_message = validator.validate_prop(prop_class=type(self), prop_value=prop_value)
                if error_message is not None:
                    raise ValidationError(error_message)

        return prop_value


class Integer(Prop):

    prop_type = OpenAPIPropType.INTEGER
    types = int

    def parse_input(self, prop_value):
        if prop_value is None:
            return None

        return int(prop_value)


class Number(Prop):

    prop_type = OpenAPIPropType.NUMBER
    types = (int, float, decimal.Decimal)

    def parse_input(self, prop_value):
        if prop_value is None:
            return None

        return extract_number(prop_value)


class Numeric(Number):

    types = (int, float, decimal.Decimal, str)


class String(Prop):

    prop_type = OpenAPIPropType.STRING
    types = str
    format = None


class DateTime(String):

    types = (str, arrow.Arrow)
    format = "date-time"

    def parse_input(self, prop_value):
        if prop_value is None:
            return None

        return extract_arrow(prop_value)

    def format_output(self, prop_value):
        return str(prop_value)


class Enum(String):

    types = enum.Enum

    def format_output(self, prop_value):
        return str(prop_value.value)


class Boolean(Prop):

    prop_type = OpenAPIPropType.BOOLEAN
    types = bool


class Object(Prop):

    prop_type = OpenAPIPropType.OBJECT
    types = dict

    def __init__(self, structure, description=None, required=True, nullable=False, validators=None):
        super().__init__(description=description, required=required, nullable=nullable, validators=validators)
        self.structure = structure

    def __deepcopy__(self, memo):  # pylint: disable=unused-argument
        return Object(
            self.structure,
            description=self.description,
            required=self.required,
            nullable=self.nullable,
        )

    def format_output_and_validate(self, output_structure_field_name, body, prop_value=NO_VALUE):
        prop_value = super().format_output_and_validate(
            output_structure_field_name,
            body,
            prop_value,
        )

        validated_dict = {}

        for field_name, field_prop in self.structure.items():
            validated_dict[field_name] = field_prop.format_output_and_validate(field_name, prop_value)

        return validated_dict


class Array(Prop):

    prop_type = OpenAPIPropType.ARRAY
    types = list

    def __init__(self, repeated_structure, description=None, required=True, nullable=False, validators=None):
        super().__init__(description=description, required=required, nullable=nullable, validators=validators)
        self.repeated_structure = repeated_structure

    def __deepcopy__(self, memo):  # pylint: disable=unused-argument
        return Array(
            self.repeated_structure,
            description=self.description,
            required=self.required,
            nullable=self.nullable,
        )

    def format_output_and_validate(self, output_structure_field_name, body, prop_value=NO_VALUE):
        prop_value = super().format_output_and_validate(
            output_structure_field_name,
            body,
            prop_value,
        )

        validated_list = []

        if prop_value:
            for value in prop_value:
                validated_list.append(self.repeated_structure.format_output_and_validate(None, None, value))

        return validated_list
