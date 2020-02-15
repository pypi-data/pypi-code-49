TOO_MANY_RPS_CODE = 6


class BasicError(Exception):
    pass


class api_error(BasicError):
    def __init__(self, vk, method, values, error):
        self.vk = vk
        self.method = method
        self.values = values
        self.raw = raw
        self.code = error["error_code"]
        self.error = error

    def try_method(self):
        """ Отправить запрос заново """

        return self.vk.method(self.method, self.values)

    def __str__(self):
        return "{} ({})".format(self.error["error_msg"], self.error["error_code"])

