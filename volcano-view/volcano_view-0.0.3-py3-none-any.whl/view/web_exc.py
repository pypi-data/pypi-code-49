
class WebException(Exception):
    def __init__(self, message_or_exc, http_code = 400):
        msg = str(message_or_exc) if isinstance(message_or_exc, Exception) else message_or_exc
        super().__init__(msg)
        self.http_code = http_code
