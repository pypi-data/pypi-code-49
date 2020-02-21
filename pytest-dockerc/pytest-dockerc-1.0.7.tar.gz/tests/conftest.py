import pytest
import requests

from pytest_dockerc import Wait, Context


class DockercContext(Context):
    def wait_for_running_state(self):
        http = self.dockerc["http"]
        Wait(ignored_exns=(requests.ConnectionError,))(
            lambda: requests.get("http://{0}:{1}".format(http.addr, http.port))
        )


@pytest.fixture(scope="session")
def ctx(dockerc, dockerc_logs):
    """ Create a context fixture

    This fixture handles dockerc, dockerc_logs and it returns the
    DockercContext to have some helpers in the test part.
    """
    context = DockercContext(dockerc)
    context.wait_for_running_state()
    yield context
