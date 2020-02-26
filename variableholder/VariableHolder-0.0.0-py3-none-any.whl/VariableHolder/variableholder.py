class VariableHolder:
    def __init__(self, **kwargs):
        self._add_variables(**kwargs)

    def _add_variables(self, **kwargs):
        for name, value in kwargs.items():
            exec(f"self.{name} = {value}")

    def _set_value(self, variable_name: str, value) -> bool:
        if variable_name in dir(self)[28:]:
            exec(f"self.{variable_name} = value")
            success = True
        else:
            success = False
        return success

