import base64
import os
import pty
import subprocess
from pathlib import Path
from functools import wraps
import click

from indico_install.config import CLUSTER_NAME


def options_wrapper(check_input=False, check_services=False):
    def opt_wrapper_outer(f):
        @wraps(f)
        @click.option(
            "-d",
            "--deployment-root",
            default=os.getcwd(),
            show_default=True,
            help="Root directory for installation files",
        )
        @click.option(
            "-c",
            "--cluster",
            default=CLUSTER_NAME,
            envvar="CLUSTER_NAME",
            show_default=True,
            help="Name of your cluster - can specify the input file to use",
        )
        @click.option(
            "-i",
            "--input-yaml",
            help="Input filepath - defaults to --deployment-root/values/--cluster.yaml",
        )
        @click.option(
            "-s",
            "--services-yaml",
            help="Services filepath - defaults to --deployment-root/values/services.yaml",
        )
        @click.option(
            "--yes/--no",
            "-y/-n",
            default=False,
            show_default=True,
            help="Accept changes",
        )
        def wrapped(
            *args,
            deployment_root=False,
            cluster=None,
            input_yaml=None,
            services_yaml=False,
            yes=False,
            **kwargs,
        ):
            # Backend
            input_yaml = (
                Path(input_yaml)
                if input_yaml
                else Path(deployment_root) / "values" / f"{cluster}.yaml"
            )
            services_yaml = (
                Path(services_yaml)
                if services_yaml
                else Path(deployment_root) / "values" / "services.yaml"
            )
            if check_input and not input_yaml.is_file():
                click.secho(f"Could not find {input_yaml}.", fg="red")
                return
            if check_services and not services_yaml.is_file():
                click.secho(f"Could not find {services_yaml}.", fg="red")
                return

            return f(
                *args,
                deployment_root=deployment_root,
                cluster=cluster,
                input_yaml=input_yaml,
                services_yaml=services_yaml,
                yes=yes,
                **kwargs,
            )

        return wrapped
    return opt_wrapper_outer


def _read(fd):
    return os.read(fd, 10240)


def with_pty(cmd: list):
    pty.spawn(cmd, master_read=_read, stdin_read=_read)


def run_cmd(mycmd, envvars: dict = None, silent=False, tty=False):
    if envvars is None:
        envvars = dict(os.environ)
    if tty and not isinstance(mycmd, list):
        raise AssertionError("Command must be passed in as a list for TTY")
    if not silent:
        click.secho(f"Running command: {mycmd}", fg="blue")

    popen_kwargs = dict(env=envvars, shell=True, stdout=subprocess.PIPE)
    if tty:
        return with_pty(mycmd)
    else:
        output = subprocess.Popen(mycmd, **popen_kwargs)
        stdout, _ = output.communicate()
        if stdout is not None:
            stdout = stdout.decode("utf-8").strip()
            if not silent:
                print(stdout, "\n")
        return stdout


def region_to_gmt(region):
    offset = "+0:00"
    if region.upper().startswith("us-east"):
        offset = "-5:00"
    return f"GMT{offset}"


def get_value(value_dict, keys):
    if not keys:
        return value_dict
    elif len(keys) == 1:
        return value_dict.get(keys[0], None)
    else:
        return get_value(value_dict[keys[0]], keys[1:])


def find_values(value_dict, target_value, base_key=None):
    if base_key is None:
        base_key = []
    for key, value in value_dict.items():
        if isinstance(value, dict):
            yield from find_values(value, target_value, base_key=base_key + [key])
        elif isinstance(value, str) and value.strip().lower() == target_value:
            yield value_dict, key, base_key


def base64file(filename):
    with open(filename, "r") as f:
        return convertb64(f.read())


def convertb64(mystring):
    return base64.b64encode(mystring.encode("utf-8")).decode("utf-8")

def decodeb64(mystring):
    return base64.b64decode(mystring.encode("utf-8")).decode("utf-8")


def determine_resource(deployment):
    for resource in ("deployment", "statefulset"):
        result = run_cmd(
            f"kubectl get {resource} | tail -n +2 | awk '{{print $1}}'", silent=True
        )
        if deployment in result.split():
            return resource


def current_user(clean=False):
    try:
        user = next(
            (
                s
                for s in run_cmd("gcloud auth list 2>/dev/null", silent=True).splitlines()
                if s.startswith("*")
            ),
            "- unknown",
        ).split()[1]
        if user == "unknown":
            return "service_acct" if os.getenv("GOOGLE_SERVICE_ACCOUNT") else None
        if clean:
            user = user.split('@', 1)[0].replace('gcr-', '')
        return user
    except Exception:
        return None


def find_gcs_key(deployment_root, quiet=False):
    # TODO: improve the gcr key finder
    key_file = run_cmd(f"ls {deployment_root}" + r" | grep -e '^gcr-.*\.json$'", silent=True)
    err = None
    if not key_file:
        err = "No GCR key file found in {deployment_root}! A GCR key file looks like 'gcr-<name>.json'"
    elif len(key_file.split("/n")) > 1:
        err = "Too many GCR key files found. Please only have 1"

    if err:
        if not quiet:
            click.secho(err, fg="red")
        return None
    return key_file


def string_to_tag(string):
    """Clean string to be used as folder path"""
    return "".join(
        [c if c.isalnum() or c in ("-", "_") else "_" for c in (string or "")]
    )
