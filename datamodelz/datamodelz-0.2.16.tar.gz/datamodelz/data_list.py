from .field import Field
from .data_object import DataObject


class DataList(Field):
    def __init__(self):
        super().__init__()
        self.name = "data"
        self.value = []  # list of TimeseriesObjectField
        self.rules = []

    def append_obj(self, lst):
        observation = DataObject()
        err = observation.set(lst) # checks length = 2 then sets
        if err:
            self.error_many(err)
            return
        self.value.append(observation)
        return self.errors

    def set(self, value):
        for lst in value:
            self.append_obj(lst)
        return self.errors

    def validate(self) -> list:
        for field in self.value:
            self.validate_field(field)
        if self.errors:
            return self.errors
        self.run_rules()
        if not self.errors:
            self.valid = True
        return self.errors
