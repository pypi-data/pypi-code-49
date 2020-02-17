import pytest

from decaptcha.notarobot import NotARobot


@pytest.fixture(scope="session")
def janet():
    janet = NotARobot()
    janet.set_model("yolo.h5")
    return janet


def test_janet(janet):
    janet.run()
    assert isinstance(janet.state.victory, bool)
