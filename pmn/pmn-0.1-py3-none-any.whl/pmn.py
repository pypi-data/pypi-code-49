import click as click

from pmn.application import Application


@click.command()
@click.version_option(message='%(prog)s %(version)s')
@click.option('-c', '--config')
def pmn(config):
    Application(config)
