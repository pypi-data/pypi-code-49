class BaseK50Exception(Exception):
    pass


class K50APIException(BaseK50Exception):
    def __init__(self, error: dict, *args):
        super().__init__(args)
        self.error = error

    def __str__(self):
        return f'code {self.error["code"]}, detail: {self.error["message"]}'
