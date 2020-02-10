from . import rule
from .field import Field, StringField
from .consts import id_string, name_string


class CompanyField(Field):
    def __init__(self):
        super().__init__()
        self.name = "company"
        self.value = {}

        self.id = StringField(id_string)
        self.company_name = StringField(name_string)
        self.fields = [self.id]
        self.rules = [rule.has_field(x.name) for x in self.fields]

    def set(self, value):
        self.value = value
        self.run_rules()
        if self.errors:  # checks for field names in value (type: dict)
            return self.errors
        self.set_fields(self.fields)
        return self.errors
