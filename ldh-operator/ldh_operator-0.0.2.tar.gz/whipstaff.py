import click
import ldh_operator.basic


@click.group()
@click.pass_context
def cli(ctx):
    """Whipstaff is a command-line tool for operating one or more
    Liberty Deckplan Hosts (LDHs) from your local session."""
    pass


@cli.command()
def debug():
    """Show debug information suitable for bug reports."""
    ldh_operator.basic.debug()


@cli.command()
def ping():
    """Ping all members of a Liberty Domain Host."""
    ldh_operator.basic.ping()
