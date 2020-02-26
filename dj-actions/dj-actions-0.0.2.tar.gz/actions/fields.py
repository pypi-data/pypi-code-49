from django import forms
from django.core import validators
import json


class CommaSeparatedCharField(forms.Field):
    def __init__(self, dedup=True, max_length=None, min_length=None, *args, **kwargs):
        self.dedup, self.max_length, self.min_length = dedup, max_length, min_length
        super(CommaSeparatedCharField, self).__init__(*args, **kwargs)
        if min_length is not None:
            self.validators.append(MinLengthValidator(min_length))
        if max_length is not None:
            self.validators.append(MaxLengthValidator(max_length))

    def to_python(self, value):
        if value in validators.EMPTY_VALUES:
            return []

        value = [item.strip() for item in value.split(',') if item.strip()]
        if self.dedup:
            value = list(set(value))

        return value

    def clean(self, value):
        value = self.to_python(value)
        self.validate(value)
        self.run_validators(value)
        return value


class JSONTextField(forms.CharField):
    schema = None

    def __init__(self, schema=None, *args, **kwargs):
        if schema is not None:
            self.schema = schema
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        if value:
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                raise ValidationError('Please provide valid json input')
        return value

    def clean(self, value):
        value = self.to_python(value)
        super(JSONTextField, self).clean(value)
        if self.schema:
            validate(value, self.schema)
        return value
