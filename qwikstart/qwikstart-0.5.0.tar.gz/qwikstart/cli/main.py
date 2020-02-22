#!/usr/bin/env python3
import click

from ..exceptions import UserFacingError
from ..parser import get_operations_mapping
from ..utils import logging
from . import utils
from .resolver import resolve_task


@click.group()
def cli() -> None:
    pass  # pragma: no cover


@cli.command()
@click.argument("task_path")
@click.option(
    "-v", "--verbose", is_flag=True, help="Print debug information", default=False
)
@click.option("--repo", help="Url for repo containing qwikstart task", default=None)
def run(task_path: str, verbose: bool, repo: str) -> None:
    """Run task in the current directory."""
    logging.configure_logger("DEBUG" if verbose else "INFO")
    task = resolve_task(task_path, repo_url=repo)
    task.execute()


@cli.command()
@click.argument("op_name")
def help(op_name: str) -> None:
    """Show help for the given operation."""
    env = utils.get_template_environment()
    template = env.get_template("operation_help.term")

    op_help = utils.get_operation_help(op_name)
    click.echo(template.render(op_help=op_help))


@cli.command()
def list_operations() -> None:
    """Show help for the given operation."""
    op_mapping = get_operations_mapping()
    for op_name, operation in op_mapping.items():
        click.echo(click.style(op_name, fg="green") + f": {operation.__doc__}")


def main() -> None:
    try:
        cli()
    except UserFacingError as error:
        click.secho("Command failed with the following error:\n", fg="red")
        click.echo(str(error))


if __name__ == "__main__":
    cli()  # pragma: no cover
