import logging

import click
from sdrfcheck.sdrf.exceptions import AppConfigException
from sdrfcheck.sdrf.sdrf import SdrfDataFrame
from sdrfcheck.sdrf.sdrf_schema import ALL_TEMPLATES, DEFAULT_TEMPLATE

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    """This is the main tool that give access to all commands and options provided by the sdrfchecker"""


@click.command('validate-sdrf', short_help='Command to validate the sdrf file')
@click.option('--sdrf_file', '-s', help='SDRF file to be validated')
@click.option('--template', '-t', help='select the template that will be use to validate the file (default: default)',
              default='default', type=click.Choice(ALL_TEMPLATES,
                                                   case_sensitive=False), required=False)
@click.pass_context
def validate_sdrf(ctx, sdrf_file: str, template: str):
    if sdrf_file is None:
        msg = "The config file for the pipeline is missing, please provide one "
        logging.error(msg)
        raise AppConfigException(msg)
    if template is None:
        template = DEFAULT_TEMPLATE

    df = SdrfDataFrame.parse(sdrf_file)
    df.validate(template)


cli.add_command(validate_sdrf)

if __name__ == "__main__":
    cli()
