import re

import httpretty
import pytest
import testypie
from httpapi import HttpApi


@pytest.fixture(autouse=True)
def mock_responses(request):
    def callback(http_request, uri, headers, method="get"):
        httpretty.disable()

        response = testypie.get_response(
            uri, http_request.headers, method=method
        )

        headers.update(
            {key.lower(): value for key, value in response["headers"].items()}
        )

        httpretty.enable()
        return response["code"], headers, response["body"].encode("utf-8")

    httpretty.register_uri(httpretty.GET, re.compile(".*"), body=callback)
    httpretty.enable()

    request.addfinalizer(httpretty.disable)
    request.addfinalizer(httpretty.reset)


@pytest.fixture
def http_bin():
    return HttpApi("http://httpbin.org/")


@pytest.fixture
def github():
    return HttpApi("https://api.github.com/")


def test_html(http_bin):
    html = http_bin.html
    assert html.base_url == "http://httpbin.org/html"
    assert "<!DOCTYPE html>" in html.get().text


def test_404(http_bin):
    assert 404 == http_bin.status(404).get().status_code


def test_github(github):
    repo = github.repos("avengerpenguin", "httpapi")
    assert (
        repo.base_url == "https://api.github.com/repos/avengerpenguin/httpapi"
    )
    assert repo.get().status_code == 200
    assert repo.get().json()["full_name"] == "avengerpenguin/httpapi"
