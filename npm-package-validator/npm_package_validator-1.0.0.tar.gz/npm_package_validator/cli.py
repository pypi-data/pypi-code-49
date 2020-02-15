# -*- coding: utf-8 -*-

"""Console script for npm_package_validator."""
import sys

import click

from npm_package_validator import valid_new_package, valid_old_package
from npm_package_validator.validate import validate_package


@click.command()
@click.argument("package_name", type=str)
@click.option("--old", is_flag=True, default=False)
def main(package_name: str, old: bool) -> int:
    """Console script for npm_package_validator."""
    valid_old = valid_old_package(package_name)
    valid_new = valid_new_package(package_name)
    errors, warnings = validate_package(package_name)
    if old and not valid_old:
        click.echo("Invalid :(")
        for msg in errors:
            click.echo(msg)
        sys.exit(1)
    elif not old and not valid_new:
        click.echo("Invalid :(")
        for msg in errors + warnings:
            click.echo(msg)
        sys.exit(1)
    click.echo("Valid!")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
