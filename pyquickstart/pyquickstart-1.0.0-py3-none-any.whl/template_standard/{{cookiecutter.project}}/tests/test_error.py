from pytest import raises

from {{cookiecutter.project}}.error import BaseError, ConfigurationError


def test_baseerror():
    with raises(BaseError):
        raise BaseError()


def test_configurationerror_enforces_message():
    with raises(TypeError) as exc:
        ConfigurationError()

    assert 'positional argument' in str(exc.value)
    assert 'message' in str(exc.value)
