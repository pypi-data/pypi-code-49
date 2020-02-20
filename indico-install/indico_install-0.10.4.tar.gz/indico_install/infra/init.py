from pathlib import Path
import click
import pkg_resources

from indico_install.config import CLUSTER_NAME


def init(location):
    def wrapper():
        values_dir = Path("values")
        if not values_dir.exists():
            values_dir.mkdir(exist_ok=True, parents=True)

        dest_file = values_dir / f"{CLUSTER_NAME}.yaml"
        if dest_file.exists():
            click.secho(
                f"{dest_file.resolve()} already exists. "
                "Please back this file up before running init.",
                fg="red",
            )
            return

        template = pkg_resources.resource_string(location, "cluster.yaml")
        with open(dest_file, "wb") as f:
            f.write(template)

        click.secho(f"Created {dest_file}", fg="green")

    return wrapper
