import enum

from dos.prop import Prop, NO_VALUE, ValidationError


class OpenAPIPropWrapperType(enum.Enum):
    ONE_OF = "one_of"


class PropWrapper:
    def __init__(self, prop_list):
        self.prop_list = prop_list
        self.required = False

        for prop in prop_list:
            if prop.required is True:
                self.required = True

    @property
    def prop_list(self):
        return self._prop_list

    @prop_list.setter
    def prop_list(self, props):
        if not isinstance(props, list):
            raise Exception("prop_list must be a list!!")

        for prop in props:
            if not isinstance(prop, Prop):
                raise Exception("prop_list must be a list of Open API Props!!")

        self._prop_list = props  # pylint: disable=attribute-defined-outside-init


class OneOf(PropWrapper):
    prop_wrapper_type = OpenAPIPropWrapperType.ONE_OF

    def parse_input_and_validate(self, input_structure_field_name, body, prop_value=NO_VALUE):

        if prop_value is NO_VALUE:
            prop_value = body.get(input_structure_field_name)

        error_message_list = []

        for prop in self.prop_list:
            try:
                return prop.parse_input_and_validate(input_structure_field_name, body, prop_value)
            except ValidationError as validation_error:
                error_message_list.append(validation_error.message)

        raise ValidationError(get_one_of_error_message(error_message_list, prop_value, input_structure_field_name))

    def format_output_and_validate(self, output_structure_field_name, body, prop_value=NO_VALUE):

        if prop_value is NO_VALUE:
            prop_value = body.get(output_structure_field_name)

        error_message_list = []

        for prop in self.prop_list:
            try:
                return prop.format_output_and_validate(output_structure_field_name, body, prop_value)
            except ValidationError as validation_error:
                error_message_list.append(validation_error.message)

        raise ValidationError(get_one_of_error_message(error_message_list, prop_value, output_structure_field_name))


def get_one_of_error_message(error_message_list, prop_value, field_name):

    reasons = ", "
    reasons = reasons.join(error_message_list)

    error_message = (f"The value {prop_value!r} from field '{field_name}' is not "
                     f"valid for one of the defined props for the following reasons: {reasons}")

    return error_message
