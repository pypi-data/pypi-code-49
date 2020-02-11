import copy
import os
import re
import tempfile
from collections import defaultdict
from contextlib import contextmanager
from pathlib import Path

import click

from indico_install.cluster_manager import ClusterManager
from indico_install.config import (
    REMOTE_TEMPLATES_PATH,
    ConfigsLoader,
    merge_dicts,
    yaml,
)
from indico_install.setup import setup
from indico_install.utils import options_wrapper, run_cmd, string_to_tag

var_regex = re.compile(r"<\!var:([^<>]*)>")
lookup_regex = re.compile(r"<\!lookup:([^<>]*)>")


@contextmanager
def _resolve_values(values):
    f = tempfile.NamedTemporaryFile(mode="w")
    yaml.dump(dict(values.items()), f, default_flow_style=False)
    yield f" -f {f.name}"
    f.close()


def _resolve_template(template_values, variables, conf):
    if isinstance(template_values, dict):
        new_values = {}
        for key, value in template_values.items():
            new_values[_resolve_template(key, variables, conf)] = _resolve_template(
                value, variables, conf
            )
        return new_values
    elif isinstance(template_values, list):
        return [_resolve_template(value, variables, conf) for value in template_values]
    elif isinstance(template_values, str):
        var_matches = var_regex.findall(template_values)
        lookup_matches = lookup_regex.findall(template_values)
        while var_matches or lookup_matches:
            for match in var_matches:
                parts = match.split("=", 1)
                if len(parts) > 1:
                    default = str(parts[1])
                else:
                    default = ""
                template_values = template_values.replace(
                    f"<!var:{match}>", str(variables.get(parts[0], default))
                )
            for match in lookup_matches:
                look_up_keys = match.split("|")
                target_value = dict(conf)
                parts = look_up_keys[-1].split("=", 1)
                if len(parts) > 1:
                    default = str(parts[1])
                    look_up_keys[-1] = parts[0]
                else:
                    default = ""
                for look_up_key in look_up_keys:
                    target_value = target_value.get(look_up_key, {})
                template_values = template_values.replace(
                    f"<!lookup:{match}>",
                    str(target_value) if target_value != {} else default,
                )
            var_matches = var_regex.findall(template_values)
            lookup_matches = lookup_regex.findall(template_values)

    return template_values


def helm_render(
    deployment_root,
    templates_dir,
    group,
    template,
    values,
    values_files="",
    enabled_resource_validation=True,
):
    generated_dir = deployment_root / "generated"
    click.echo(f"Generating {values['name']}.yaml")
    with _resolve_values(values) as resolved_str:
        results = run_cmd(
            f"helm template {values_files} {templates_dir / group} --execute templates/{template}.yaml{resolved_str}",
            silent=True,
        )
        if enabled_resource_validation:
            validate_resource_constraints(results)

    with open(generated_dir / f"{values['name']}.yaml", "w") as f:
        f.write(results)


def validate_resource_constraints(generated_results):
    """
    validate that a generated template has the required resource section
    """
    results = yaml.safe_load_all(generated_results)
    deploys = [
        result
        for result in results
        if isinstance(result, dict)
        and result.get("kind") in ("Deployment", "StatefulSet", "DaemonSet")
    ]
    for deploy in deploys:
        for container in deploy["spec"]["template"]["spec"]["containers"]:
            if "resources" not in container:
                raise Exception(
                    f"No resource specifications set for {deploy['kind']}: {deploy['metadata']['name']}"
                )


def resolve_templates(templates):
    unresolved_templates = lambda: {  # noqa
        template_name: template
        for template_name, template in templates.items()
        if "<!template>" in template
    }
    templates_to_resolve = unresolved_templates()
    while templates_to_resolve:
        for template_name, template in templates_to_resolve.items():
            template_to_merge = template.pop("<!template>")
            templates[template_name] = merge_dicts(
                copy.deepcopy(templates[template_to_merge]), templates[template_name]
            )
        templates_to_resolve = unresolved_templates()


def resolve_all(configs):
    resolve_templates(configs["_templates"])

    for resource, helm_info in configs["services"].items():
        if "<!template>" in helm_info:
            template_name = helm_info.pop("<!template>")
            configs["services"][resource] = merge_dicts(
                copy.deepcopy(configs["_templates"][template_name]), helm_info
            )
            # Attach additional values
        configs["services"][resource]["values"] = configs["services"][resource].get(
            "values", {}
        )
        configs["services"][resource] = _resolve_template(
            configs["services"][resource], configs["services"][resource], configs
        )

    configs.update(
        _resolve_template(
            {k: v for k, v in configs.items() if k not in ("_templates", "services")},
            {},
            configs,
        )
    )


def format_resources(helm_info):
    """
    If resource contraints are specified within a 'resources' key, set that
    value in 'limits' and 'requests'. Else, use the value set in the limits
    key; otherwise, rely on the values.yaml default for a value
    """
    if (
        "requests" in helm_info["values"]["resources"]
        or "limits" in helm_info["values"]["resources"]
    ):
        click.secho(
            "Usage of 'limits' and 'requests' in templates is deprecated; please specify resource constraints in a single 'resources' block",
            fg="yellow",
        )
    updated_resources = defaultdict(dict, helm_info["values"]["resources"])
    for resource in ("cpu", "memory", "nvidia.com/gpu"):
        if helm_info["values"]["resources"].get(resource):
            val = updated_resources.pop(resource)
            updated_resources["limits"].update({resource: val})
            updated_resources["requests"].update({resource: val})

        elif resource in updated_resources.get("limits"):
            updated_resources["requests"][resource] = updated_resources["limits"][
                resource
            ]
        elif resource in updated_resources.get("requests"):
            updated_resources["limits"][resource] = updated_resources["requests"][
                resource
            ]

    helm_info["values"]["resources"] = dict(updated_resources)
    return helm_info


def render_from_local(
    deployment_root, templates_dir, cluster, services_yaml, input_yaml, service=None
):
    generated = deployment_root / "generated"
    click.secho(f"clearing {generated}", fg="yellow")
    os.makedirs(generated, exist_ok=True)
    run_cmd(f"rm -rf {generated/ '*.yaml'}", silent=True)

    setup(input_yaml)
    # images will be "updated" by Indico and contains cluster defaults
    # input is customer overrides
    configs = ConfigsLoader(services_yaml, input_yaml)
    resolve_all(configs)

    with _resolve_values(configs) as resolved_str:
        for resource, helm_info in configs["services"].items():
            if service and service not in resource:
                continue

            helm_info["values"] = helm_info.get("values", {})
            helm_info["values"]["name"] = resource
            configs["services"][resource] = helm_info
            if helm_info.pop("<!disabled>", None):
                continue
            extra_keys = {
                k: v
                for k, v in helm_info.items()
                if k not in ("group", "template", "values")
            }
            helm_info["values"] = merge_dicts(extra_keys, helm_info["values"])
            [helm_info.pop(k) for k in extra_keys.keys()]

            if "resources" in helm_info["values"]:
                helm_info = format_resources(helm_info)

            try:
                helm_render(
                    deployment_root,
                    templates_dir,
                    values_files=f" {resolved_str}",
                    enabled_resource_validation=(
                        not configs.get("disableResourceLimits", False)
                    ),
                    **helm_info,
                )
            except Exception as e:
                click.secho(f"Unable to render template for {resource}: {e}")

    configs.save(deployment_root / "configuration" / f"{cluster}.yaml")


def _resolve_remote(deployment_root, remote_path):
    """
    Download remote templates and services yaml and unpack
    Unpack if necessary, and validate contents (error if validation fails)
    Return the location of the local, unpacked templates dir
    """
    remote_templates_path = REMOTE_TEMPLATES_PATH + remote_path + "/templates.tar.gz"
    remote_services_yaml = REMOTE_TEMPLATES_PATH + remote_path + "/services.yaml"
    local_directory = (
        deployment_root
        / "remote_configs"
        / "".join(c for c in str(remote_path) if c.isalnum)
    )
    if not local_directory.parent.exists():
        local_directory.parent.mkdir(exist_ok=True, parents=True)

    click.secho(f"Downloading remote configs to {local_directory}", fg="yellow")
    if local_directory.is_dir():
        run_cmd(f"rm -rf {local_directory}", silent=True)
    os.makedirs(local_directory / "templates", exist_ok=True)

    run_cmd(
        f"wget {remote_templates_path} -O - | tar -xz -C {local_directory / 'templates'}"
    )
    run_cmd(f"wget {remote_services_yaml} -O {local_directory / 'services.yaml'}")
    return (local_directory / "services.yaml", local_directory / "templates")


@click.command("render")
@click.pass_context
@click.argument("service", required=False)
@click.option(
    "-r",
    "--remote-configs",
    help="Remote GCS folder with configs to render from. Ex: 'latest' or 'master.24235243'",
)
@options_wrapper(check_input=True)
def render(
    ctx,
    service=None,
    *,
    deployment_root,
    cluster,
    input_yaml,
    services_yaml,
    remote_configs,
    cluster_manager=None,
    allow_image_overrides=False,
    **kwargs,
):
    """
    Render Helm templates from the "templates" directories.

    Only render the template for services with names containing <SERVICE> if provided
    """
    deployment_root = Path(deployment_root)
    templates_dir = deployment_root / "templates"

    cluster_manager = cluster_manager or ClusterManager(input_yaml=input_yaml)
    if not cluster_manager.indico_version and remote_configs:
        cluster_manager.indico_version = string_to_tag(remote_configs)

    if cluster_manager.indico_version:
        services_yaml, templates_dir = _resolve_remote(
            deployment_root, cluster_manager.indico_version
        )

    if not services_yaml.is_file():
        click.secho(f"Could not find {services_yaml}.", fg="red")
        return

    with tempfile.NamedTemporaryFile(suffix=".tmp", delete=False) as input_yaml:

        # We keep track of which custom images were applied. We only use these to override
        # generated images in the templates if specified
        # Generally not used unless we're recovering to a previous state
        old_conf = cluster_manager.clean_services() if allow_image_overrides else {}
        input_yaml.write(
            yaml.dump(cluster_manager.cluster_config, default_flow_style=False).encode(
                "utf-8"
            )
        )
        input_yaml.flush()
        try:
            render_from_local(
                deployment_root,
                templates_dir,
                cluster,
                services_yaml,
                input_yaml.name,
                service=service,
            )
            input_yaml.seek(0)
            cluster_manager.edit_cluster_config(
                changes=merge_dicts(yaml.safe_load(input_yaml), old_conf)
            )
            cluster_manager.save()
        finally:
            os.remove(input_yaml.name)

    click.secho("Templates generated!", fg="green", bold=True)
