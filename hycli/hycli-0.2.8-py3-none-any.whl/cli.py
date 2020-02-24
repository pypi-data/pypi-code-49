import os

import click
import toml

from .commands import to_csv, to_xml, to_xlsx, config
from .commons.endpoints import default_endpoints


@click.group()
@click.option(
    "-c",
    "--config-file",
    type=click.Path(),
    default="~/.hycli/config.toml",
    show_default=True,
)
@click.option(
    "-e",
    "--endpoint-env",
    default="production",
    show_default=True,
    type=click.Choice(["localhost", "staging", "production"], case_sensitive=False),
    help="endpoint environment",
)
@click.option(
    "-u",
    "--username",
    envvar="HYCLI_USERNAME",
    default=None,
    help="your API username for accessing the environment",
)
@click.option(
    "-p",
    "--password",
    envvar="HYCLI_PASSWORD",
    default=None,
    help="your API password for accessing the environment",
)
@click.option(
    "--extractor", help="extractor endpoint",
)
@click.pass_context
def main(ctx, config_file, endpoint_env, username, password, extractor):
    """
    Can convert 1 invoice to xml or a directory of invoices to csv/xlsx.
    It is advised to configurate credentials and endpoints before use with: \n >> hycli config
    """
    filename = os.path.expanduser(config_file)
    ctx.obj = {"config_file": filename, "env": endpoint_env}

    try:
        with open(filename) as cfg:
            conf = toml.loads(cfg.read())

        ctx.obj["config"] = conf[endpoint_env]

    except (FileNotFoundError, KeyError):
        click.echo(
            f"No configuration found, using default endpoints for {endpoint_env} environment."
        )
        click.echo("Define custom endpoints for environment with: >> hycli config \n")
        ctx.obj["config"] = {
            "endpoints": {
                k: v
                for k, v in default_endpoints[endpoint_env].items()
                if v is not None
            }
        }

    if username:
        ctx.obj["config"]["username"] = username

    if password:
        ctx.obj["config"]["password"] = password

    if extractor:
        ctx.obj["config"]["endpoints"]["extractor"] = extractor


main.add_command(to_xml.to_xml)
main.add_command(to_csv.to_csv)
main.add_command(to_xlsx.to_xlsx)
main.add_command(config.config)

if __name__ == "__main__":
    main()
