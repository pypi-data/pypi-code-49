from indico_install.generate.update import update
from indico_install.generate.cluster_info import cluster_info
import click


@click.group("generate")
def generate():
    """Scale and configure cluster from dump"""
    pass


generate.add_command(update)
generate.add_command(cluster_info)
