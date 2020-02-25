import functools


class FattureInCloudError(Exception):
    def __init__(self, error_message="", response_code=None, response_body=None):

        Exception.__init__(self, error_message)
        # Http status code
        self.response_code = response_code
        # Full http response
        self.response_body = response_body
        # Parsed error message from fattureincloud
        try:
            # if we receive str/bytes we try to convert to unicode/str to have
            # consistent message types (see #616)
            self.error_message = error_message.decode()
        except Exception:
            self.error_message = error_message

    def __str__(self):
        if self.response_code is not None:
            return "{0}: {1}".format(self.response_code, self.error_message)
        else:
            return "{0}".format(self.error_message)


class FattureInCloudOperationError(FattureInCloudError):
    pass


class FattureInCloudHttpError(FattureInCloudError):
    pass


class FattureInCloudListaError(FattureInCloudOperationError):
    pass


class FattureInCloudDettagliError(FattureInCloudOperationError):
    pass


class FattureInCloudNuovoError(FattureInCloudOperationError):
    pass


class FattureInCloudModificaError(FattureInCloudOperationError):
    pass


class FattureInCloudEliminaError(FattureInCloudOperationError):
    pass


class FattureInCloudInfoError(FattureInCloudOperationError):
    pass


class FattureInCloudInfoMailError(FattureInCloudOperationError):
    pass



def on_http_error(error):
    """Manage FattureInCloudHttpError exceptions.

    This decorator function can be used to catch FattureInCloudHttpError exceptions
    raise specialized exceptions instead.

    Args:
        error(Exception): The exception type to raise -- must inherit from
            FattureInCloudError
    """

    def wrap(f):
        @functools.wraps(f)
        def wrapped_f(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except FattureInCloudHttpError as e:
                raise error(e.error_message, e.response_code, e.response_body)

        return wrapped_f

    return wrap