
"""
webtest wrapper
"""

# pylint: disable=C0103

from webtest import TestApp


def fmt(func, *args, **kwargs):
    """
    Response formatting decorator.
    """
    retval = type('response', (object,), {})()

    def __format_response(resp):
        # keep original response here
        retval.resp = resp
        try:
            json = resp.json
            retval.code = resp.status_int
            retval.errno = json['errno']
            retval.data = json['data']
        except (ValueError, AttributeError):
            # in case there's non-JSON data
            retval.code = 500
            retval.errno = -1
            retval.data = None
        return retval

    def __apply(*args, **kwargs):
        return __format_response(func(*args, **kwargs))

    return __apply


class WebDriver(object):
    """
    WebDriver class.
    """

    app = None

    def make_app(self, app):
        """
        Store app to property.
        """
        self.app = TestApp(app)

    @fmt
    def HEAD(self, *args, **kwargs):
        """
        HEAD request.
        """
        return self.app.head(expect_errors=True, *args, **kwargs)

    @fmt
    def OPTIONS(self, *args, **kwargs):
        """
        OPTIONS request.
        """
        return self.app.options(expect_errors=True, *args, **kwargs)

    @fmt
    def GET(self, *args, **kwargs):
        """
        GET request.
        """
        return self.app.get(expect_errors=True, *args, **kwargs)

    @fmt
    def POST(self, *args, **kwargs):
        """
        POST request.
        """
        return self.app.post(expect_errors=True, *args, **kwargs)

    @fmt
    def PUT(self, *args, **kwargs):
        """
        PUT request.
        """
        return self.app.put(expect_errors=True, *args, **kwargs)

    @fmt
    def PATCH(self, *args, **kwargs):
        """
        PATCH request.
        """
        return self.app.patch(expect_errors=True, *args, **kwargs)

    @fmt
    def DELETE(self, *args, **kwargs):
        """
        DELETE request.
        """
        return self.app.delete(expect_errors=True, *args, **kwargs)


if __name__ == '__main__':
    pass
