#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Helpers for `npm_package_validator` package tests."""

import typing

from npm_package_validator import valid_new_package as _valid_new_package
from npm_package_validator import valid_old_package as _valid_old_package
from npm_package_validator import validate as _validate

validate_package = _validate.validate_package


def _validate_new_old(package_name: str) -> typing.Tuple[bool, bool]:
    return _valid_new_package(package_name), _valid_old_package(package_name)


def valid_new_package(package_name: str) -> bool:
    return _validate_new_old(package_name)[0] == True


def valid_old_package(package_name: str) -> bool:
    return _validate_new_old(package_name)[1] == True


def valid_new_and_old_package(package_name: str) -> bool:
    return _validate_new_old(package_name) == (True, True)


def invalid_package(package_name: str) -> bool:
    return _validate_new_old(package_name) == (False, False)


def assert_valid_new_package(package_name: str) -> _validate.ResultType:
    assert valid_new_package(package_name)
    return validate_package(package_name)


def assert_valid_old_package(package_name: str) -> _validate.ResultType:
    assert valid_old_package(package_name)
    return validate_package(package_name)


def assert_valid_new_and_old_package(package_name: str) -> _validate.ResultType:
    assert valid_new_and_old_package(package_name)
    return validate_package(package_name)


def assert_invalid_package(package_name: str) -> _validate.ResultType:
    assert invalid_package(package_name)
    return validate_package(package_name)


def contains(l: typing.List[str], conds: typing.Union[str, typing.List[str]]) -> bool:
    _conds: typing.List[str] = []
    if isinstance(conds, str):
        _conds = [conds]
    elif isinstance(conds, list):
        _conds = conds
    else:
        raise TypeError("Conditions must be string or list of strings")
    return all([any([cond in i for i in l]) for cond in _conds])
