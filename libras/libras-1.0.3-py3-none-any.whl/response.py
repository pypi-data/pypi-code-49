class ResponseBody:
    data = None
    code = 200
    message = "success"

    def __init__(self, data=None, code=200, message='success', **kwargs):
        self.data = data
        self.code = code
        self.message = message
        self.size = (len(data) if isinstance(data, (list, set)) else 1)
        for key in kwargs.keys():
            setattr(self, key, kwargs[key])
