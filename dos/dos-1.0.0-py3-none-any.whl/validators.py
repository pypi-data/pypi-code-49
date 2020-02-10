from dos import prop, validation_helpers


class Validator:
    supported_prop_classes = []

    def validate_prop(self, prop_class, _):
        if prop_class not in self.supported_prop_classes:
            raise prop.ValidationError(f"{self.__class__.__name__} is not supported for class {prop_class.__name__}!!")


class ExactLength(Validator):
    supported_prop_classes = [prop.String, prop.Number, prop.Numeric, prop.Integer]

    def __init__(self, exact_length=None):
        self.exact_length = exact_length

    def validate_prop(self, prop_class, prop_value):
        super().validate_prop(prop_class, prop_value)

        if len(prop_value) != self.exact_length:
            return (f"{prop_class.__name__} is not the correct length! The string \'{prop_value}\' is "
                    f"{len(prop_value)} characters long, not {self.exact_length}!")

        return None


class SocialSecurityNumber(Validator):
    supported_prop_classes = [prop.String]

    def validate_prop(self, prop_class, prop_value):
        super().validate_prop(prop_class, prop_value)

        if validation_helpers.validate_social_security_number(prop_value) is False:
            return f"{str(prop_value)} is not a valid social security number!"

        return None
