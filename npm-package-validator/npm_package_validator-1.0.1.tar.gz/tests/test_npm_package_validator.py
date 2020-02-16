#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `npm_package_validator` package."""

import typing

import pytest
from click.testing import CliRunner

from npm_package_validator import cli
from tests.helpers import (
    assert_invalid_package,
    assert_valid_new_and_old_package,
    assert_valid_new_package,
    assert_valid_old_package,
    contains,
    invalid_package,
    valid_new_and_old_package,
    valid_new_package,
    valid_old_package,
    validate_package,
)


def test_validate_npm_package_name() -> None:
    """Test valid npm package names."""
    assert valid_new_and_old_package("some-package")
    assert valid_new_and_old_package("example.com")
    assert valid_new_and_old_package("under_score")
    assert valid_new_and_old_package("period.js")
    assert valid_new_and_old_package("123numeric")

    assert valid_old_package("my*-package")
    assert valid_old_package("(my)-package")
    assert valid_old_package("(my)~package")
    assert valid_old_package("my-'package'")

    errors, warnings = assert_valid_old_package("crazy!")
    assert contains(warnings, "can no longer contain special characters")


def test_validate_bad_char_npm_package_name() -> None:
    assert invalid_package(None)
    assert invalid_package(12)
    assert invalid_package("")
    assert invalid_package("my&package")
    assert invalid_package("my^package")
    assert invalid_package("my-package:)")
    assert invalid_package("my:package")
    assert invalid_package("my/package")


def test_validate_scoped_npm_package_name() -> None:
    """Test scoped npm package names introduced with npm 2+."""

    assert valid_new_and_old_package("@npm/thingy")
    errors, warnings = assert_valid_old_package("@npm-zors/money!time.js")
    assert contains(warnings, "can no longer contain special characters")


def test_validate_invalid_npm_package_name() -> None:
    """Test invalid npm package names."""

    errors, warnings = assert_invalid_package("")
    assert contains(errors, "length must be greater than zero")

    errors, warnings = assert_invalid_package(".start-with-period")
    assert contains(errors, "cannot start with a period")

    errors, warnings = assert_invalid_package("_start-with-underscore")
    assert contains(errors, "cannot start with an underscore")

    errors, warnings = assert_invalid_package("contain:colons")
    assert contains(errors, "only contain URL-friendly characters")

    errors, warnings = assert_invalid_package(" leading-space")
    assert contains(
        errors,
        [
            "cannot contain leading or trailing spaces",
            "only contain URL-friendly characters",
        ],
    )

    errors, warnings = assert_invalid_package("trailing-space ")
    assert contains(
        errors,
        [
            "cannot contain leading or trailing spaces",
            "only contain URL-friendly characters",
        ],
    )

    errors, warnings = assert_invalid_package("s/l/a/s/h/e/s")
    assert contains(errors, "only contain URL-friendly characters")

    errors, warnings = assert_invalid_package("my:pückage")
    assert contains(errors, "only contain URL-friendly characters")

    errors, warnings = assert_invalid_package("my@package")
    assert contains(errors, "only contain URL-friendly characters")

    errors, warnings = assert_valid_old_package(
        "ifyouwanttogetthesumoftwonumberswherethosetwonumbersarechosenbyfindingthelargestoftwooutofthreenumbersandsquaringthemwhichismultiplyingthembyitselfthenyoushouldinputthreenumbersintothisfunctionanditwilldothatforyou-"
    )
    assert contains(warnings, "no longer contain more than 214 characters")

    assert valid_new_and_old_package(
        "ifyouwanttogetthesumoftwonumberswherethosetwonumbersarechosenbyfindingthelargestoftwooutofthreenumbersandsquaringthemwhichismultiplyingthembyitselfthenyoushouldinputthreenumbersintothisfunctionanditwilldothatforyou"
    )

    errors, warnings = assert_valid_old_package("CAPITAL-LETTERS")
    assert contains(warnings, "can no longer contain capital letters")


def test_validate_blacklisted_npm_package_name() -> None:
    """Test blacklisted npm package names."""
    errors, warnings = assert_invalid_package("node_modules")
    assert contains(errors, "node_modules is a blacklisted name")

    errors, warnings = assert_invalid_package("favicon.ico")
    assert contains(errors, "favicon.ico is a blacklisted name")

    errors, warnings = assert_valid_old_package("http")
    assert contains(warnings, "http is a core module name")


def test_command_line_interface() -> None:
    """Test the CLI."""
    runner = CliRunner()

    # Invoking with no arguments fails
    result = runner.invoke(cli.main)
    assert result.exit_code != 0

    # Invoking with a bad package name fails
    result = runner.invoke(cli.main, args=["my@package"])
    assert result.exit_code != 0
    assert "Invalid" in result.output

    # Invoking with a good package name succeeds
    result = runner.invoke(cli.main, args=["my-package"])
    assert result.exit_code == 0
    assert "Valid" in result.output

    # Invoking an old package name fails except when using --old
    result = runner.invoke(cli.main, args=["MY-package"])
    assert result.exit_code != 0
    assert "Invalid" in result.output
    result = runner.invoke(cli.main, args=["MY-package", "--old"])
    assert result.exit_code == 0
    assert "Valid" in result.output

    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
