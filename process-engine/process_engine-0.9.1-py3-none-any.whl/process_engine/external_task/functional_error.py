
class FunctionalError(Exception):
    
    def __init__(self, code, message):
        super(FunctionalError, self).__init__()
        self._code = code
        self._message = message

    def get_code(self):
        return self._code

    def get_message(self):
        return self._message