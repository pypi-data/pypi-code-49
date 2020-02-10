import copy


class Fields:

    def __init__(self, base_schema):
        self.base_schema = base_schema

    def all(self):
        return self.specialize()

    def specialize(self, overrides=None, only=None, exclude=None):

        cloned = copy.deepcopy(self.base_schema)

        if overrides:
            for override_name, override_values in overrides.items():

                prop = cloned[override_name]

                for override_attr, override_value in override_values.items():
                    setattr(prop, override_attr, override_value)

        if only:

            trimmed = {}

            for field_name in only:
                trimmed[field_name] = cloned[field_name]

            cloned = trimmed

        if exclude:
            for name in exclude:
                if name in cloned:
                    del cloned[name]

        return cloned
