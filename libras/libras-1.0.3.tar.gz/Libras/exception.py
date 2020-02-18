class FlaskException(Exception):

    def __init__(self, message, code=None, status_code=404, payload=None):
        Exception.__init__(self)
        self.status_code = status_code
        self.message = message
        self.code = code
        self.payload = payload

    def __dict__(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        rv['code'] = self.code
        return rv
