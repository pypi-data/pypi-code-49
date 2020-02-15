# -*- coding: utf-8 -*-

"""Main module."""

import re
import typing
from urllib.parse import quote

from npm_package_validator.constants import blacklist, builtins, scoped_package_pattern

ResultType = typing.Tuple[typing.List[str], typing.List[str]]


def _encode_uri_component_equiv(s: str) -> str:
    """
        Python equivalent to the javascript encodeURIComponent function
        see https://stackoverflow.com/a/6618858
    """
    return quote(s.encode("utf-8"), safe="~()*!.'")


def validate_package(package_name: str) -> ResultType:
    """
        Validates a given package name
        Based on https://github.com/npm/validate-npm-package-name/blob/master/index.js
    """
    warnings: typing.List[str] = []
    errors: typing.List[str] = []

    if package_name is None:
        errors.append("name cannot be none")
        return errors, warnings

    if not isinstance(package_name, str):
        errors.append("name must be a string")
        return errors, warnings

    if len(package_name) < 1:
        errors.append("name length must be greater than zero")

    if re.match(r"^\..*$", package_name):
        errors.append("name cannot start with a period")

    if re.match(r"^_.*$", package_name):
        errors.append("name cannot start with an underscore")

    if package_name.strip() != package_name:
        errors.append("name cannot contain leading or trailing spaces")

    for name in blacklist:
        if name == package_name.lower():
            errors.append(f"{name} is a blacklisted name")

    # The following issues are warnings as they have been allowed back in the days
    # They still hold for validating old, existing packages but are errors when creating new packages

    for name in builtins:
        if name == package_name.lower():
            warnings.append(f"{name} is a core module name")

    if len(package_name) > 214:
        warnings.append("name can no longer contain more than 214 characters")

    if package_name.lower() != package_name:
        warnings.append("name can no longer contain capital letters")

    if re.search(r"[~\'!()*]", package_name.split("/")[-1]):
        warnings.append("name can no longer contain special characters like ~'!()*")

    if not _encode_uri_component_equiv(package_name) == package_name:
        # Maybe it is a scoped package names, like @user/package
        package = re.match(scoped_package_pattern, package_name)
        if package is not None:
            user = package.group(1)
            pkg = package.group(2)
            if not ("" in [user, pkg] or None in [user, pkg]):
                if (
                    _encode_uri_component_equiv(user) == user
                    and _encode_uri_component_equiv(pkg) == pkg
                ):
                    return errors, warnings

        errors.append("name can only contain URL-friendly characters")

    return errors, warnings
