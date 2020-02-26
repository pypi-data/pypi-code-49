import tempfile
import time
import uuid
from pathlib import Path

import click
import yaml

from indico_install.config import ConfigsHolder, merge_dicts
from indico_install.helm.render import _resolve_remote, render
from indico_install.kube.svc.restart import restart
from indico_install.setup import configure_gcr_key
from indico_install.utils import current_user, options_wrapper, run_cmd


def diff_files(f1, f2):
    diff_out = run_cmd(f"diff {f1} {f2}", silent=True)
    for line in diff_out.splitlines():
        if line.startswith("+"):
            click.secho(line, fg="green")
        elif line.startswith("-"):
            click.secho(line, fg="red")
        else:
            click.echo(line)


class Deployment:
    def __init__(self):
        self.key = str(uuid.uuid4())
        self.start = time.time()
        self.user = current_user()

    def get_deployment_version_data(self):
        curr_vers = run_cmd(
            "kubectl get configmap deployed-version -o yaml 2>&1", silent=True
        )
        assert (
            "NotFound" not in curr_vers
        ), "Configmap for current version not found! Please indico apply to initialize the cluster"
        return yaml.safe_load(curr_vers)["data"]

    def set_deployment_version(self, services_yaml_version, templates_version=None):
        run_cmd(
            """kubectl patch configmap deployed-version -p '{"data":{"services.yaml": "%s","templates": "%s","updated_by":"%s", "last_updated":"%s"}}'"""
            % (
                services_yaml_version,
                templates_version or services_yaml_version,
                self.user,
                time.strftime("%m/%d/%y %H:%M:%S %z", time.localtime(self.start)),
            )
        )

    def is_version_locked(self):
        # lock exists, wasn't set by us, and is less than 10 min old
        curr_lock = self.get_deployment_version_data().get("lock", {})
        return (
            curr_lock
            and curr_lock["applied_by"] != self.key
            and int(self.start - int(curr_lock["time"])) < 10 * 60
        )

    def set_deployment_lock(self, remove=False, wait=0):
        while wait:
            if self.is_version_locked():
                time.sleep(1)
                wait -= 1
            else:
                break
        assert not self.is_version_locked(), "deploymet is already locked"
        lock_val = (
            "null"
            if remove
            else '{"applied_by":"%s","time":"%d"}' % (self.key, self.start)
        )
        run_cmd(
            """kubectl patch configmap deployed-version -p '{"data":{"lock":%s}}'"""
            % lock_val,
            silent=True,
        )


@click.command("info")
@click.pass_context
def info(ctx):
    """
    Grab the deployed-version configmap
    for information on the state of the cluster
    """
    click.echo(Deployment().get_deployment_version_data())


@click.command("apply-patch")
@click.pass_context
@click.option("-f", "--patch-file", required=True, help="Patch file to apply")
@click.option(
    "-w",
    "--wait",
    type=int,
    default=0,
    show_default=True,
    help="Seconds to wait for deploymewnt to unlock",
)
@options_wrapper(check_input=True)
def apply_patch(ctx, patch_file=None, wait=0, *, deployment_root, yes, **kwargs):
    """
    Apply a patch to the current services - this will NOT override params in cluster.yaml
    Example patch yaml to update the moonbow image for all moonbow services

      images: {moonbow: moonbow:development.32532464564574637}
    """
    try:
        from indico_install.helm.upload import upload
    except ImportError:
        click.secho("Unable to apply patch without indico pip dependencies", fg="red")
        return

    if not Path(patch_file).is_file():
        click.secho(f"Could not find patch file {patch_file}", fg="red")
        return
    dep = Deployment()
    curr_vers = dep.get_deployment_version_data()
    # curr_vers = {"services.yaml": "development", "templates": "development"}
    dep.set_deployment_lock(wait=wait)

    try:
        with open(patch_file, "r") as f:
            patches = yaml.safe_load(f)

        services_yaml, templates_dir = _resolve_remote(
            Path(deployment_root), curr_vers["services.yaml"]
        )
        new_services_file = Path(tempfile.gettempdir()) / "services.yaml"
        run_cmd(f"cp {services_yaml} {new_services_file}")
        new_services = ConfigsHolder(new_services_file)
        new_services.update(merge_dicts(new_services, patches))
        new_services.save()
        diff_files(services_yaml, new_services_file)

        if yes or click.confirm("Apply changes?"):
            run_cmd(f"mv {new_services_file} {services_yaml}", silent=True)

            new_version = f"{dep.start}_{dep.user}"

            versions = ctx.invoke(
                upload,
                tag=[new_version],
                deployment_root=templates_dir.parent,
                services_yaml=services_yaml,
            )
            new_version = versions[0]
            ctx.invoke(
                render, deployment_root=deployment_root, remote_configs=new_version
            )
            ctx.invoke(apply, deployment_root=deployment_root, yes=True, **kwargs)
            dep.set_deployment_version(new_version)
    finally:
        dep.set_deployment_lock(remove=True)


def find_dependent_services(updated_services: list) -> set:
    """
    From a list of services, determine if any configs or secrets have been updated
    and return a list of deployment and statefulset names that need to be restarted
    to pick up changes. Determined if the services use any of the <updated_confs>
    in their envFrom or volumes.
    """
    svc_types_to_check = ("statefulset", "deployment", "configmap", "secret")
    updated_confs = [
        ups.split("/", 1)[1]
        for ups in updated_services
        if ups.startswith("secret/") or ups.startswith("configmap/")
    ]
    updated_services = {
        ups.split("/", 1)[1]: idx
        for idx, ups in enumerate(updated_services)
        if any(ups.startswith(svc_type) for svc_type in svc_types_to_check)
    }
    # We bank on the fact that names of deployments, statefulsets, configs, secrets are all unique

    dependency_info = []
    dependent_services = set([])
    # 1. Get all the conf dependencies for our resources
    for svc_type in ("deployment", "statefulset"):
        dependency_info.extend(
            run_cmd(
                f"kubectl get {svc_type} "
                "--no-headers -o custom-columns=NAME:.metadata.name,"
                "ENVFROM:{.spec.template.spec.containers[0].envFrom[*]},"
                "CONFIGMAPVOL:{.spec.template.spec.volumes[*]}",
                silent=True,
            ).splitlines()
        )

    # 2. For each conf, find the list of dependent resources
    for conf in updated_confs:
        conf_order = updated_services[conf]
        conf_deps = set([ds.split("  ", 1)[0] for ds in dependency_info if conf in ds])
        # remove any dependencies that were updated after the conf was updated
        conf_deps -= set(
            [cd for cd in conf_deps if updated_services.get(cd, 0) > conf_order]
        )
        dependent_services.update(conf_deps)

    return dependent_services


@click.command("apply")
@click.pass_context
@click.argument("service", required=False)
@click.option(
    "--restart-deps/--no-restart-deps",
    default=True,
    show_default=True,
    help="Restart services affected by updated configmap or secrets",
)
@options_wrapper()
def apply(ctx, restart_deps=True, service=None, deployment_root=None, yes=False, **kwargs):
    """
    Apply templates in the "generated/" directory.
    Apply only the template files matching <SERVICE> if provided.
    Creates the image pull secret if missing.
    Performs a dry-run for confirmation before applying. Skip dry-run with --yes
    """
    generated_dir = Path(deployment_root) / "generated"
    if not generated_dir.is_dir():
        click.secho(f"'generated/' directory not found in {deployment_root}")
        return

    configure_gcr_key(deployment_root)

    # These are services that were actually modified
    updated_services = []

    if service is not None:
        templates = run_cmd(
            f"ls {generated_dir} | grep '{service}'", silent=True
        ).splitlines()
        for t in templates:
            results = run_cmd(
                f"kubectl apply -f {generated_dir / t} --dry-run 2>&1 | grep -v 'support dry-run'"
            )

        if yes or click.confirm("Ready to apply these changes?"):
            outs = [run_cmd(f"kubectl apply -f {generated_dir / t}") for t in templates]
            updated_services.extend(
                [
                    out.split(" ", 1)[0]
                    for out in outs
                    if any(status in out for status in ("created", "configured"))
                ]
            )
    else:
        results = run_cmd(
            f"kubectl apply -R -f {generated_dir} --dry-run 2>&1 | grep -v 'support dry-run'",
            silent=True,
        )
        click.echo("\n".join(results.split(",")) + "\n")

        if yes or click.confirm("Ready to apply these changes?"):
            out = run_cmd(f"kubectl apply -R -f {generated_dir}", silent=True)
            for line in out.splitlines():
                color = "red"
                if "unchanged" in line:
                    color = "yellow"
                elif "configured" in line or "created" in line:
                    color = "green"
                    updated_services.append(line.split(" ", 1)[0])
                click.secho(line, fg=color)

    # Now we reroll any dependent services as necessary
    if updated_services:
        updated_confs = [
            ups
            for ups in updated_services
            if ups.startswith("secret/") or ups.startswith("configmap/")
        ]
        if not updated_confs:
            return
        if restart_deps:
            dependent_services = find_dependent_services(updated_services)
            if not dependent_services:
                click.secho(
                    f"No dependent services found that need to be restarted",
                    fg="yellow",
                )
                return
            for dep_service in dependent_services:
                ctx.invoke(restart, service=dep_service, contains=False, wait="2m")
        else:
            click.secho(f"{', '.join(updated_confs)} were updated. Make sure to restart dependent services")
