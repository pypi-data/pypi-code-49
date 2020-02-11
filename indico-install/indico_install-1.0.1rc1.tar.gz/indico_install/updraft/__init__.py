import json
import os
import tempfile
from pathlib import Path
from subprocess import call

import click

from indico_install.cluster_manager import ClusterManager
from indico_install.config import merge_dicts, yaml
from indico_install.helm.apply import apply
from indico_install.helm.render import render
from indico_install.utils import options_wrapper, pretty_diff, string_to_tag

EDITOR = os.environ.get("EDITOR", "vim")


def refresh_cluster_manager(ctx, cluster_manager, deployment_root, yes, backup=False):
    """
    Given recent changes, apply them to the cluster
    """
    cluster_manager.lock()
    try:
        ctx.invoke(
            render,
            cluster_manager=cluster_manager,
            deployment_root=deployment_root,
            allow_image_overrides=backup,
        )
        ctx.invoke(
            apply,
            cluster_manager=cluster_manager,
            deployment_root=deployment_root,
            yes=yes,
        )
    finally:
        cluster_manager.save()
        cluster_manager.unlock()


@click.group("updraft")
def updraft():
    """Manage deployments and versioning"""
    pass


@updraft.command("version")
@click.pass_context
def show_version(ctx):
    """
    Display version details about <TAG>. Defaults to current cluster rendered_tag
    """
    click.secho(f"Known version: {ClusterManager().indico_version}")


@updraft.command("current")
@click.pass_context
def show_current(ctx):
    """
    Display current configmap state (alias for viewing the configmap)
    """
    click.secho(ClusterManager().to_str())


@updraft.command("edit")
@click.pass_context
@click.option(
    "-I", "--interactive", is_flag=True, help=f"Open configmap in your editor",
)
@click.option("-v", "--version", help=f"Update to new updraft version")
@click.option("--force", help=f"")
@click.option("--patch-file", type=click.File("r"), help="JSON-formatted patch file")
@click.argument("patch", required=False)
@options_wrapper()
def edit_configmap(
    ctx, *, interactive, patch, patch_file, version, yes, deployment_root, **kwargs
):
    """
    Edit configmap with some patch, or interactively.
    Only allows editing of the main cluster config portion

    PATCH - if not interactive, and no patch-file is provided,
    pass in a json string to patch the configmap with

    ex: indico updraft edit '{"apiDomain": "api-foo.indico.io"}'
    """
    cluster_manager = ClusterManager()
    if not cluster_manager.cm_exists:
        click.secho(
            "Cannot edit cluster config. Please initialize with indico updraft init",
            fg="red",
        )
        return
    changes = None
    service_state = cluster_manager.clean_services()
    if interactive:
        with tempfile.NamedTemporaryFile(suffix=".tmp") as tf:
            tf.write(
                yaml.dump(
                    cluster_manager.cluster_config, default_flow_style=False
                ).encode("utf-8")
            )
            tf.flush()
            call([EDITOR, tf.name])
            tf.seek(0)
            changes = yaml.safe_load(tf)
    elif patch_file:
        changes = json.load(patch_file)
    elif patch:
        changes = json.loads(patch)

    if not changes and (
        not version or string_to_tag(version) == cluster_manager.indico_version
    ):
        click.secho(f"No changes or new version provided", fg="yellow")
        return

    cluster_manager.edit_cluster_config(
        changes=merge_dicts(changes, service_state), version=string_to_tag(version)
    )

    if yes or click.confirm("Render and apply with changes?"):
        cluster_manager.save(backup=True)
        refresh_cluster_manager(ctx, cluster_manager, deployment_root, yes)


@updraft.command("restore")
@click.pass_context
@options_wrapper()
def restore_version(ctx, deployment_root, yes):
    """
    (Alpha) If an old version of the cluster_manager exists, pull it
    load the original state, and apply
    """
    cluster_manager = ClusterManager()
    if not cluster_manager.load_from_cluster(backup=True):
        click.secho("No backup available!", fg="red")
        return

    cluster_manager.lock()
    try:
        if yes or click.confirm("Apply backup?"):
            refresh_cluster_manager(
                ctx, cluster_manager, deployment_root, yes, backup=True
            )
    finally:
        cluster_manager.unlock()


@updraft.command("init")
@click.pass_context
@options_wrapper()
def init_tracking(ctx, input_yaml=None, yes=False, **kwargs):
    """
    Add or update version tracking to the cluster (idempotent)
    """
    if input_yaml and not Path(input_yaml).is_file():
        click.secho(
            f"Provided input yaml {input_yaml} does not exist. Ignoring", fg="yellow"
        )
        input_yaml = None
    cluster_manager = ClusterManager(reconcile=True, input_yaml=input_yaml)
    click.secho(cluster_manager.to_str())
    if yes or click.prompt("Save updated version cluster_manager [yN]"):
        cluster_manager.save()


@updraft.command("diff")
@click.pass_context
@click.argument("versions", required=False, nargs=-1)
@click.option(
    "--all/--no-all",
    "show_all",
    default=False,
    show_default=True,
    help="Include matches in diff",
)
def compare_versions(ctx, versions=None, show_all=False):
    """
    Compare versions
    If no versions are provided, diff rendered_release with current state
    If 1 version, diff current state with version
    If 2 versions, diff the versions
    """
    if len(versions) > 2:
        click.secho(
            "More that 2 versions provided for comparison. Ignoring extra versions"
        )
        versions = versions[:2]
    if versions:
        versions = [string_to_tag(v) for v in versions]

    cluster_manager = ClusterManager()
    if len(versions) == 2:
        diff = cluster_manager.diff(*versions)
    else:
        diff = cluster_manager.diff_version(tag=versions[0] if versions else None)

    pretty_diff(diff, show_all=show_all)
