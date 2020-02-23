from pytest import raises

from {{cookiecutter.project}}.error import BaseError


def test_baseerror():
    with raises(BaseError):
        raise BaseError()
