import warnings

from pycurl_requests import api


class Session:
    def __init__(self, **kwargs):
        warnings.warn('Session objects are only partially implemented')
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def get(self, *args, **kwargs):
        return self.request('GET', *args, **kwargs)

    def head(self, *args, **kwargs):
        return self.request('HEAD', *args, **kwargs)

    def options(self, *args, **kwargs):
        return self.request('OPTIONS', *args, **kwargs)

    def patch(self, *args, **kwargs):
        return self.request('PATCH', *args, **kwargs)

    def post(self, *args, **kwargs):
        return self.request('POST', *args, **kwargs)

    def put(self, *args, **kwargs):
        return self.request('PUT', *args, **kwargs)

    def request(self, *args, **kwargs):
        return api.request(*args, **kwargs)


def session():
    """
    Create a Session

    .. deprecated:: 1.0.0
        Use :class:`~pycurl_requests.sessions.Session` instead.
    """
    return Session()
