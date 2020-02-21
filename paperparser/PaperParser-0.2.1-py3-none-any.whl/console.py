"""Command-line interface."""
import click

from . import __version__, page


@click.command()
@click.argument("url")
@click.argument("strategy")
@click.version_option(version=__version__)
def main(url: str, strategy: str) -> None:
    """Parse the bibtex from a URL using the STRATEGY."""
    p = page.BibTeXPage(url=url, strategy=strategy)
    click.echo(p.as_dict())
