class ValidationError(Exception):
    def __init__(self, validation_data: dict):
        super().__init__(
            f"Couldn't validate following data : {validation_data}"
        )