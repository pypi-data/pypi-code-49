#!/usr/bin/env python3
import click


from indico_install.infra.init import init
from indico_install.utils import options_wrapper
from indico_install.cluster_manager import ClusterManager
from .setup import aks_setup, ask_for_infra_input
from . import storage, cluster


@click.group("aks")
@click.pass_context
def aks(ctx):
    """
    Indico infrastructure setup and validation for Azure Kubernetes Service
    """
    ctx.ensure_object(dict)
    ctx.obj["TRACKER"] = ClusterManager()


aks.command("init")(init(__name__))


@aks.command("check")
@click.pass_context
@options_wrapper()
def check(ctx, *, deployment_root, **kwargs):
    """
    Check the state of an existing cluster to validate
    that it meets certain requirements
    """
    aks_setup(deployment_root)
    conf = ctx.obj["TRACKER"].cluster_config
    ask_for_infra_input(conf)
    cluster.check(conf)
    storage.check(conf)
    ctx.obj["TRACKER"].save()



@aks.command("create")
@click.pass_context
@click.option(
    "--upload/--no-upload",
    default=False,
    help="Upload Indico API data to the Indico file share",
    show_default=True,
)
@options_wrapper()
def create(ctx, upload=False, *, deployment_root, **kwargs):
    """
    Configure your AKS installation
    """
    aks_setup(deployment_root)
    conf = ctx.obj["TRACKER"].cluster_config
    ask_for_infra_input(conf)
    cluster.create(conf)
    storage.create(deployment_root, conf, upload=upload)
    ctx.obj["TRACKER"].save()
