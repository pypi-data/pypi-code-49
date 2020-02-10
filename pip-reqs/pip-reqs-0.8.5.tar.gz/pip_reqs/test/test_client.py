from pip_reqs import client  # NOQA
from pip._vendor.requests.models import Response
import mock
import pytest

import six

POST_DEF = "pip._vendor.requests.Session.post"


def patch_post(status_code, content):
    response = Response()
    response._content = content
    response.status_code = status_code
    return mock.patch(POST_DEF, return_value=response)


def test_compile_response_fail():
    wheelsproxy_client = client.WheelsproxyClient("")

    with patch_post(status_code=400, content=b"bytes") as post:
        with pytest.raises(client.CompilationError) as exc_info:
            wheelsproxy_client.compile("")

        assert isinstance(exc_info.value.args[0], six.text_type)
        assert post.call_count == 1


def test_compile_response_success():
    wheelsproxy_client = client.WheelsproxyClient("")

    with patch_post(status_code=200, content=b"bytes") as post:
        response = wheelsproxy_client.compile("")
        assert isinstance(response, six.text_type)
        assert post.call_count == 1


def test_resolve_response():
    wheelsproxy_client = client.WheelsproxyClient("")

    with patch_post(status_code=200, content=b"bytes") as post:
        response = wheelsproxy_client.resolve("")
        assert isinstance(response, six.text_type)
        assert post.call_count == 1
