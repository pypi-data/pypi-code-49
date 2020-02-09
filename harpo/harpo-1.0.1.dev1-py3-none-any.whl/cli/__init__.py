# coding=utf-8

import logging

import click

from harpo.cli.domain.commands import domain
from harpo.cli.group.commands import group
from harpo.cli.key.commands import key
from harpo.cli.secret.commands import secret
from harpo.cli.system.commands import system
from harpo.cli.user.commands import user
from harpo.logging import configure_logging
from pbr import version


@click.group()
@click.option('--debug', is_flag=True)
@click.option('--format', type=click.Choice(choices=['json', 'yaml', 'normal']),
              default='normal', show_default=True)
@click.option('--base-dir', type=click.Path())
@click.option('--gpg-home', type=click.Path(), default='$HOME/.gnupg', show_default=True)
@click.version_option(version=version.VersionInfo('harpo'))
def main(debug, format, base_dir, gpg_home):
    """Harpo CLI

    PROTIP: Enable autocompletion using the following command:

        eval "$(_HARPO_COMPLETE=source harpo)"
    """
    level = logging.DEBUG if debug else logging.INFO
    configure_logging(level)


main.add_command(domain)
main.add_command(group)
main.add_command(key)
main.add_command(secret)
main.add_command(user)
main.add_command(system)
