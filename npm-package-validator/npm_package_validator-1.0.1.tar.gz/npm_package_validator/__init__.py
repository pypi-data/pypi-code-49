# -*- coding: utf-8 -*-

"""Top-level package for npm-package-validator."""

__author__ = """romnnn"""
__email__ = "contact@romnn.com"
__version__ = "1.0.1"

from npm_package_validator.validate import validate_package


def valid_new_package(package_name: str) -> bool:
    errors, warnings = validate_package(package_name)
    return len(errors) == len(warnings) == 0


def valid_old_package(package_name: str) -> bool:
    errors, warnings = validate_package(package_name)
    return len(errors) == 0


# validate = _validate.validate
# _validate.valid_new_package
# _validate.valid_new_package
