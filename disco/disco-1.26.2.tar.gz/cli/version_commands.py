import click
import cli.utilities.utils as utils


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command('version', context_settings=CONTEXT_SETTINGS)
def cli_version():
    """
    Show the installed Dis.co CLI version.

    $ disco version
    """
    click.echo(f'Dis.co Command Line version {utils.disco_cli_version()} is installed')
