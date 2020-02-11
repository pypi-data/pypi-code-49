"""
Entrypoint for the brewblox-dev tool
"""

import click
from dotenv import find_dotenv, load_dotenv

from brewblox_dev import docker, localbuild, repository

cli = click.CommandCollection(
    sources=[
        localbuild.cli,
        repository.cli,
        docker.cli,
    ])


def main():  # pragma: no cover
    load_dotenv(find_dotenv(usecwd=True))
    cli()


if __name__ == '__main__':
    main()
