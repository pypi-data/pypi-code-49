class PathNotResolvable(Exception):
    def __init__(self, name, value):
        msg = f"The provided path for {name}: '{value}' is not resolvable"
        super().__init__(msg)


class MissingVariable(Exception):
    def __init__(self, name):
        msg = f"Variable {name} is missing"
        super().__init__(msg)
