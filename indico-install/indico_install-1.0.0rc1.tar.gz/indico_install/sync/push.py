import re

import click
from click import confirm, secho
import tempfile
from pathlib import Path
from indico_install.config import ConfigsHolder
from indico_install.helm.apply import apply
from indico_install.helm.render import render, resolve_all
from indico_install.kube.svc.restart import restart
from indico_install.utils import run_cmd, options_wrapper, APP_MAP, get_non_matching_images
from indico_install.cluster_manager import ClusterManager, get_deployed_frontend


REVERSE_APP_MAP = {value: key for key, value in APP_MAP.items()}


@click.group("push")
@click.pass_context
def push(ctx):
    """Push hash(es) and image(s) to the cluster"""
    ctx.ensure_object(dict)
    ctx.obj["TRACKER"] = ClusterManager()


@push.command("all")
@click.pass_context
@options_wrapper(check_services=True)
def push_all(
    ctx, *, services_yaml, cluster, yes, deployment_root, forwarded=True
):
    """
    All service and frontend hashes in the services yaml
    will be pushed to the current cluster.
    """
    if forwarded is True:
        ctx.invoke(push_all, forwarded=False)

    configs = ConfigsHolder(config=services_yaml)
    for (
        _,
        resource,
        deployment,
        saved_image,
        cluster_image,
    ) in get_non_matching_images(configs):
        secho(f"{deployment}:\nOn Cluster: {cluster_image}\nOn Disk: {saved_image}")

        if yes or confirm("Push new image?"):
            secho(
                run_cmd(
                    f"kubectl set image --record=true {resource}/{deployment} "
                    f"{deployment}=gcr.io/new-indico/{saved_image}"
                ),
                fg="green",
            )
            ctx.obj["TRACKER"].update({deployment: saved_image})
        else:
            secho(f"Skipping {deployment}", fg="yellow")

    # Frontend
    ctx.invoke(
        render,
        service="app-edge-nginx-conf",
        deployment_root=deployment_root,
        cluster=cluster,
        cluster_manager=ctx.obj["TRACKER"],
        services_yaml=services_yaml,
    )
    ctx.invoke(
        apply, service="app-edge-nginx-conf", deployment_root=deployment_root, yes=yes
    )
    ctx.obj["TRACKER"].update(frontend=get_deployed_frontend())
    ctx.invoke(restart, service="app-edge")
    secho("Done pushing changes", fg="green")


@push.command("svc")
@click.pass_context
@click.argument("svc")
@click.option("--exclude", default=None)
@options_wrapper(check_services=True)
def push_svc(ctx, svc, *, services_yaml, yes, image=None, exclude=None, **kwargs):
    resources = []
    for resource_type in ("deployment", "statefulset"):
        options = run_cmd(
            f"kubectl get {resource_type} -o wide "
            f"| grep indico "
            f"| awk '{{print $1}}'| grep {svc}",
            silent=True,
        )

        resources.extend(
            [(resource_type, resource) for resource in options.split("\n") if resource]
        )

    if exclude is not None:
        resources = [
            (resource_type, resource)
            for resource_type, resource in resources
            if not re.match(rf".*{exclude}.*", resource)
        ]

    click.secho(f"Matched {[x[1] for x in resources]}", fg="green")
    configs = ConfigsHolder(config=services_yaml)
    resolve_all(configs)
    resources = [
        (r_type, resource, configs["services"][resource]["values"]["image"])
        for r_type, resource in resources
    ]

    for resource_type, resource, image in resources:
        secho(f"{resource_type}/{resource}:\n Update with: {image}")

        if yes or confirm("Push new image?"):
            secho(
                run_cmd(
                    "kubectl set image --record=true "
                    f"{resource_type}/{resource} {resource}=gcr.io/new-indico/{image}",
                    silent=True,
                )
            )
            ctx.obj["TRACKER"].update({resource: image})
        else:
            secho(f"Skipping {resource}", fg="yellow")


@push.command("image")
@click.pass_context
@click.argument("image_name")
@click.argument("image", required=False, default=None)
@options_wrapper()
def push_image(ctx, image_name, *, services_yaml, yes, image=None, **kwargs):
    """
    Update <IMAGE_NAME> matching deployment/statefulset
    with image saved in current cluster config.
    Ex. indico push image noct
    """
    resources = []
    for resource_type, column in [("deployment", 7), ("statefulset", 5)]:
        options = run_cmd(
            f"kubectl get {resource_type} -o wide "
            f"| grep indico "
            f"| awk '${column} ~ /{image_name}/ {{print $1}}'",
            silent=False,
        )

        resources.extend(
            [(resource_type, resource) for resource in options.split("\n") if resource]
        )

    if image is None:
        if not Path(services_yaml).is_file():
            secho(f"Could not find {services_yaml}", fg="red")
            return
        configs = ConfigsHolder(config=services_yaml)
        image = configs["images"][image_name.replace("-", "").replace("_", "")]

    for resource_type, resource in resources:
        secho(f"{resource_type}/{resource}:\n Update with: {image}")

        if yes or confirm("Push new image?"):
            secho(
                run_cmd(
                    "kubectl set image --record=true "
                    f"{resource_type}/{resource} {resource}=gcr.io/new-indico/{image}",
                    silent=True,
                )
            )
            ctx.obj["TRACKER"].update({resource: image})
        else:
            secho(f"Skipping {resource}", fg="yellow")


@push.command("client")
@click.pass_context
@click.argument("fehash")
def push_client(ctx, fehash):
    """Update frontend <FEHASH>. Will also update app_edge"""
    output = run_cmd(
        """kubectl get configmap app-edge-nginx-conf -o json | jq '.data["nginx.conf"]'""",
        silent=True,
    )

    nginx_conf = re.sub(
        r"set \$clientversion [^;]*;",
        f"set $clientversion {fehash};",
        output,
        flags=re.MULTILINE,
    )

    with tempfile.NamedTemporaryFile() as temp:
        temp.write(str.encode('{"data": {"nginx.conf":' + f"{nginx_conf}" + "}}')"))
        command = (
            f'kubectl patch configmap app-edge-nginx-conf --patch "$(cat {temp.name})"'
        )
        secho(run_cmd(command, silent=True))
        ctx.obj["TRACKER"].update(frontend=fehash)
        ctx.invoke(restart, service="app-edge")
        secho("Done pushing changes", fg="green")
