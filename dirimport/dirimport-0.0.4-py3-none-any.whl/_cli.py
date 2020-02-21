import os
import click
from . import gen
from ._version import VERSION


@click.group(invoke_without_command=True)
@click.version_option(VERSION)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        print(ctx.get_help())


@cli.command("diff")
@click.argument("path", type=click.Path(exists=True, dir_okay=True, file_okay=False))
@click.option("--filename", default="__init__.py")
def diffcmd(path, filename):
    data = gen.dig(path)
    click.echo(
        "\n".join(map(lambda f: f.rstrip(), gen.diff(data, path, filename))))


@cli.command("generate")
@click.argument("path", type=click.Path(exists=True, dir_okay=True, file_okay=False))
@click.option("--filename", default="__init__.py")
def generatecmd(path, filename):
    data = gen.dig(path)
    gen.generate(data, path, filename)


@cli.command("eval")
@click.argument("path", type=click.Path(exists=True, dir_okay=True, file_okay=False))
@click.argument("expr")
def evalcmd(path, expr):
    bn = os.path.basename(path)
    globals()[bn] = gen.importall(path)
    click.echo(eval(expr))


if __name__ == "__main__":
    cli()
