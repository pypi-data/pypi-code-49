import click
from indico_install.utils import options_wrapper
from indico_install.config import ConfigsHolder
from indico_install.helm import render, apply
from indico_install.setup import get_tls
from indico_install.kube.svc.restart import restart


@click.command("update")
@click.pass_context
@click.argument("service", required=True, type=click.Choice(["ssl"]))
@click.option(
    "-r",
    "--remote-configs",
    help="Remote GCS folder with configs to render from. Ex: 'latest' or 'master.24235243'",
)
@options_wrapper(check_input=True)
def update(ctx, service, *, input_yaml, remote_configs, **kwargs):
    """
    Function to update an existing service.

    Args:

      <SERVICE>: The service to update. Choices are:

        - ssl : update certificates
    """
    if service == "ssl":
        # Handle these here to avoid recursive imports
        config = ConfigsHolder(config=input_yaml)
        get_tls(config, redo=True)
        ctx.invoke(render, input_yaml=input_yaml, remote_configs=remote_configs, **kwargs)
        ctx.invoke(
            apply, service="app-edge-nginx-conf", input_yaml=input_yaml, **kwargs
        )
        ctx.invoke(restart, service="app-edge")
