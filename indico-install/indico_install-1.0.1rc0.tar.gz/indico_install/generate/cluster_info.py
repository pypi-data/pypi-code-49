import shutil
import tarfile
import time
from pathlib import Path

import click
from click import secho

from indico_install.config import CLUSTER_NAME
from indico_install.infra.input_utils import auth_with_gsutil
from indico_install.utils import current_user, options_wrapper, run_cmd


@click.command("cluster-info")
@click.pass_context
@click.option(
    "--upload/--no-upload",
    default=True,
    show_default=True,
    help="Upload the cluster dump TAR to a private Google Storage bucket shared with Indico",
)
@click.option(
    "--sudo/--no-sudo",
    default=False,
    show_default=False,
    help="Use sudo to run cluster dump (useful if running into permission issues)",
)
@options_wrapper()
def cluster_info(ctx, *, upload, sudo, deployment_root, **kwargs):
    """
    Load and package all the information on the running cluster
    into a local TAR file.
    """
    dumpdir = Path(deployment_root) / f"cluster_info_{time.strftime('%Y%m%d-%H%M%S')}"
    secho(f"Pulling cluster info...", fg="blue")
    sudo = "sudo " if sudo else ""
    run_cmd(
        f"""
        {sudo}kubectl cluster-info dump -o yaml --output-directory={dumpdir};
        {sudo}kubectl get secrets --namespace=default -o yaml > {dumpdir}/secrets.yaml;
        {sudo}kubectl get configmaps --namespace=default -o yaml > {dumpdir}/configmaps.yaml;
        {sudo}kubectl get ingress --namespace=default -o yaml > {dumpdir}/ingress.yaml;
        {sudo}kubectl get pv --namespace=default -o yaml > {dumpdir}/pv.yaml;
        {sudo}kubectl get pvc --namespace=default -o yaml > {dumpdir}/pvc.yaml;
        """,
        silent=True,
    )
    dump_tar = str(dumpdir.resolve()) + ".tar.gz"
    with tarfile.open(dump_tar, "w:gz") as tar:
        tar.add(dumpdir, arcname="")

    secho(f"Cluster information saved to {dump_tar}", fg="green")
    shutil.rmtree(dumpdir, ignore_errors=True)
    if not upload:
        return

    cluster_user = (
        current_user(clean=True) if auth_with_gsutil(deployment_root) else CLUSTER_NAME
    )
    if not cluster_user:
        secho(
            "Cannot authenticate with Google - please upload cluster info manually",
            fg="yellow",
        )
        return

    result = run_cmd(
        f"gsutil cp {dump_tar} gs://client_{cluster_user}/{Path(dump_tar).name} 2>&1",
        silent=True,
    )
    msgs = (
        (
            "Operaction completed",
            "Cluster information successfully shared with Indico",
            "green",
        ),
        (
            "BucketNotFoundException",
            f"Bucket for user {cluster_user} does not exist. Please ask Indico to create this and try sharing again, or manually share your cluster info TAR",
            "yellow",
        ),
        (
            "",
            f"Unable to share cluster info with Indico. Please share the cluster info TAR manually",
            "red",
        ),
    )
    for res, msg, color in msgs:
        if res in result:
            secho(msg, fg=color)
            break
