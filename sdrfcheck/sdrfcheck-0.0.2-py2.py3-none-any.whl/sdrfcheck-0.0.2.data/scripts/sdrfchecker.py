import logging

import click
from sdrfcheck.sdrf.exceptions import AppConfigException
from sdrfcheck.sdrf.sdrf import SdrfDataFrame

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    """This is the main tool that give access to all commands and options provided by the sdrfchecker"""


@click.command('validate-sdrf', short_help='Command to validate the sdrf file')
@click.option('--sdrf_file', '-s', help='SDRF file to be validated')
@click.pass_context
def validate_sdrf(ctx, sdrf_file):
    if sdrf_file is None:
        msg = "The config file for the pipeline is missing, please provide one "
        logging.error(msg)
        raise AppConfigException(msg)

    df = SdrfDataFrame.parse(sdrf_file)
    df.validate()


cli.add_command(validate_sdrf)

if __name__ == "__main__":
    cli()
