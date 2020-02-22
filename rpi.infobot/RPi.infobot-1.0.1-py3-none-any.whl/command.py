import click
import rpi_infobot.config as config
import rpi_infobot.convo as convo

@click.command()
@click.option('--config-file', '-c', help='Alternative config YAML')
def bot(config_file=None):
    cfg = config.load(config_file)
    convo.start(cfg)
