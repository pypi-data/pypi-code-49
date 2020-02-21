import socket
import requests
import compose
import pytest

from pytest_dockerc import Wait


def test_basic_workflow(dockerc, dockerc_logs):
    """ Basic test to check that the container is started and that
    the http server is ready to listen on the documented port.
    """
    assert dockerc is not None
    assert len(dockerc.containers()) == 1

    container = dockerc.containers()[0]
    assert container.is_running is True
    assert container.labels["com.docker.compose.service"] == "http"

    inspect = container.inspect()
    networks = inspect["NetworkSettings"]["Networks"]
    assert len(networks) == 1
    network = next(iter(inspect["NetworkSettings"]["Networks"]))
    ipv4 = networks[network]["IPAddress"]
    assert len(inspect["NetworkSettings"]["Ports"]) == 1
    port = next(iter(inspect["NetworkSettings"]["Ports"])).split("/")[0]

    res = Wait(ignored_exns=(requests.ConnectionError,))(
        lambda: requests.get("http://{0}:{1}".format(ipv4, port))
    )
    assert res.status_code == requests.codes.ok


def test_context_and_hooks(ctx):
    """ Test the provided Context and Compose hooks
    """
    with pytest.raises(KeyError):
        ctx.dockerc["httttttttttp"]

    http = ctx.dockerc["http"]
    assert isinstance(http, compose.container.Container)

    with pytest.raises(AttributeError):
        http.pooort

    assert socket.inet_aton(http.addr)
    assert http.port == 80

    assert "PATH" in http.environment
    assert "NGINX_VERSION" in http.environment
