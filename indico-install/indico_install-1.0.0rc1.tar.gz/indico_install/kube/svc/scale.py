import click
from indico_install.utils import run_cmd, options_wrapper

@click.command("delete")
@click.pass_context
@click.argument("service", required=True, type=str)
def delete(ctx, service):
    """
    Delete a K8S deployment/statefulset/service

    ARGS:
        <SERVICE> grep string of deployments, statefulsets, services to delete
    """
    updated_svcs = []
    for svc_type in ["deployment", "statefulset", "service"]:
        out = run_cmd(
            """kubectl get %s --no-headers | grep "%s" | awk '{print $1}'"""
            % (svc_type, service),
            silent=True,
        )
        if not out:
            continue
        for _svc in out.splitlines():
            if click.confirm(f"Ok to delete {svc_type} {_svc}"):
                click.secho(
                    run_cmd(f"kubectl delete {svc_type} {_svc}"),
                    fg="green",
                )
                updated_svcs.append(_svc)

    if updated_svcs:
        ctx.obj["TRACKER"].edit_cluster_config(changes={"services": {
            _svc: {"<!disabled>": True} for _svc in updated_svcs
        }})
        ctx.obj["TRACKER"].save()


@click.command("scale")
@click.pass_context
@click.argument("service", required=True, type=str)
@click.argument("amount", required=True, type=int)
@options_wrapper()
def scale(ctx, service, amount):
    """
    Scale a K8S cluster deployment or statefulset

    ARGS:
        <SERVICE> grep string of deployments and statefulsets to scale

        <AMOUNT> number of pods to create
    """
    updated_svcs = []
    for svc_type in ["deployment", "statefulset"]:
        out = run_cmd(
            """kubectl get %s --no-headers | grep "%s" | awk '{print $1}'"""
            % (svc_type, service),
            silent=True,
        )
        if not out:
            continue
        for _svc in out.splitlines():
            click.secho(
                run_cmd(f"kubectl scale --replicas={amount} {svc_type} {_svc}"),
                fg="green",
            )
            updated_svcs.append(_svc)

    if updated_svcs:
        ctx.obj["TRACKER"].edit_cluster_config(changes={"services": {
            _svc: {"values": {"replicas": amount}} for _svc in updated_svcs
        }})
        ctx.obj["TRACKER"].save()
