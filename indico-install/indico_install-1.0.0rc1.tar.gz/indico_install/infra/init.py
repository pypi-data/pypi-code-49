import click
import pkg_resources

from indico_install.cluster_manager import ClusterManager
from indico_install.config import yaml


def init(location):
    def wrapper():
        cluster_manager = ClusterManager()
        if cluster_manager.cm_exists:
            click.secho(
                f"Cluster config already exists. "
                "Please back this config up before running init.",
                fg="red",
            )
            return

        template = pkg_resources.resource_string(location, "cluster.yaml")
        cluster_manager.edit_cluster_config(changes=yaml.safe_load(template))
        cluster_manager.save()

        click.secho(f"Created Cluster Config", fg="green")

    return wrapper
