import sentry_sdk  # type: ignore
import os

if os.getenv("TREEBEARD_ENVIRONMENT") == "development":
    env = "development"
else:
    env = "production"

sentry_sdk.init(
    "https://58543632a309471a88bb99f4f6bbdca0@sentry.io/2846147", environment=env
)

from treebeard.helper import (
    get_treebeard_env,
    set_credentials,
    get_config_path,
)
from treebeard.version import get_version
from treebeard.cli_helper import (
    check_for_updates,
    get_time,
    get_version,
    validate_notebook_directory,
    get_service_status_message,
)
from halo import Halo  # type: ignore
import warnings
import click
import time
import tarfile
import json
import os.path
import requests
from timeago import format as timeago_format  # type: ignore
from datetime import datetime
import sys
from humanfriendly import parse_size, format_size  # type: ignore
from dateutil import parser
import glob
import tempfile
from typing import IO, List, Any

config_path = get_config_path()

treebeard_env = get_treebeard_env()

if env == "development":
    click.echo("WARNING: RUNNING IN LOCAL MODE")
    url = "http://localhost:8080"
else:
    url = "https://scheduler-cvee2224cq-ew.a.run.app"

service_status_endpoint = f"{url}/service_status"
msg = get_service_status_message(service_status_endpoint)
if msg:
    click.echo(click.style(msg, fg="red"))

notebook_name = treebeard_env["notebook_id"]
secrets_endpoint = f"{url}/secrets"
notebooks_endpoint = f"{url}/notebooks/{notebook_name}"
signup_endpoint = f"{url}/cli_signup"

credentials = treebeard_env

warnings.filterwarnings(
    "ignore", "Your application has authenticated using end user credentials"
)

# Instantiates a client
dir_path = os.path.dirname(os.path.realpath(__file__))


@click.group()
def cli():
    pass


@cli.resultcallback()
def process_result(*args: Any, **kwargs: Any):
    check_for_updates()


@cli.command()
@click.option("--email", prompt="Your email:")
@click.option("--key", prompt="Your API key:")
def configure(email: str, key: str):
    """Set initial credentials"""
    set_credentials(email, key, signup_endpoint)


@cli.command()
def version():
    """Shows treebeard package version"""
    click.echo(get_version())


@cli.command()
def info():
    """Shows treebeard credentials and project info"""
    click.echo(treebeard_env)


@cli.command()
@click.option("t", "--hourly", flag_value="hourly", help="Run notebook hourly")
@click.option("t", "--daily", flag_value="daily", help="Run notebook daily")
@click.option("t", "--weekly", flag_value="weekly", help="Run notebook weekly")
@click.option(
    "t", "--quarter-hourly", flag_value="quarter-hourly", help="Run quarter-hourly"
)
@click.option(
    "watch", "--watch", is_flag=True, help="Run and check completed build status"
)
@click.option(
    "ignore",
    "--ignore",
    help="Don't submit unneeded virtual envs and large files",
    multiple=True,
)
def run(t: str, watch: bool, ignore: List[str]):
    """
    Run a notebook and optionally schedule it to run periodically
    """

    validate_notebook_directory()

    params = {}
    if t:
        params["schedule"] = t

    spinner: Any = Halo(text="🌲  zipping directory", spinner="dots")
    spinner.start()

    # Create a temporary file for the compressed directory
    # compressed file accessible at f.name
    with tempfile.NamedTemporaryFile("wb", suffix=".tar.gz", delete=False) as f:
        with tarfile.open(fileobj=f, mode="w:gz") as tar:

            def zip_filter(info: tarfile.TarInfo):
                for ignored in ignore:
                    if info.name in glob.glob(ignored):
                        return None
                return info

            tar.add(
                os.getcwd(), arcname=os.path.basename(os.path.sep), filter=zip_filter
            )
            tar.add(config_path, arcname=os.path.basename(config_path))
    spinner.text = "🌲  submitting notebook to runner"

    size = os.path.getsize(f.name)
    max_upload_size = "100MB"
    if size > parse_size(max_upload_size):
        click.echo(
            click.style(
                (
                    f"Error: Compressed notebook directory is {format_size(size)},"
                    f" max upload size is {max_upload_size}. \nPlease ensure you ignore any virtualenv subdirectory"
                    " using `treebeard run --ignore venv`"
                ),
                fg="red",
            )
        )
        quit(1)

    response = requests.post(
        notebooks_endpoint,
        files={"repo": open(f.name, "rb")},
        params=params,
        headers=credentials,
    )

    if response.status_code != 200:
        raise click.ClickException(f"Request failed: {response.text}")

    spinner.stop()
    try:
        json_data = json.loads(response.text)
        click.echo(f"✨  Run has been accepted! {json_data['admin_url']}")
    except:
        click.echo("❗  Request to run failed")
        click.echo(sys.exc_info())

    if watch:
        # spinner = Halo(text='watching build', spinner='dots')
        # spinner.start()
        build_result = None
        while not build_result:
            time.sleep(5)
            response = requests.get(notebooks_endpoint, headers=credentials)
            json_data = json.loads(response.text)
            status = json_data["runs"][-1]["status"]
            click.echo(f"{get_time()} Build status: {status}")
            if status == "SUCCESS":
                build_result = status
                # spinner.stop()
                click.echo(f"Build result: {build_result}")
            elif status in ["FAILURE", "TIMEOUT", "INTERNAL_ERROR", "CANCELLED"]:
                click.echo(f"Build failed")
                build_result = status
                sys.exit(1)


@cli.command()
def cancel():
    """Cancels the current notebook build and schedule"""
    validate_notebook_directory()
    spinner: Any = Halo(text="cancelling", spinner="dots")
    click.echo(f"🌲  Cancelling {notebook_name}")
    spinner.start()
    requests.delete(notebooks_endpoint, headers=credentials)  # type: ignore
    spinner.stop()
    click.echo(f"🛑 Done!")


@cli.command()
def status():
    """Show the status of the current notebook"""
    validate_notebook_directory()
    response = requests.get(notebooks_endpoint, headers=credentials)
    if response.status_code != 200:
        raise click.ClickException(f"Request failed: {response.text}")

    json_data = json.loads(response.text)
    if len(json_data) == 0:
        click.echo(
            "This notebook has not been run. Try running it with `treebeard run`"
        )
        quit(1)
    click.echo("🌲  Recent runs:\n")

    max_results = 10
    status_emoji = {
        "SUCCESS": "✅",
        "QUEUED": "💤",
        "WORKING": "⏳",
        "FAILURE": "❌",
        "TIMEOUT": "⏰",
        "CANCELLED": "🛑",
    }

    for run in json_data["runs"][-max_results:]:
        now = parser.isoparse(datetime.utcnow().isoformat() + "Z")
        start_time = parser.isoparse(run["start_time"])
        time_string: str = timeago_format(start_time, now=now)
        click.echo(f"{status_emoji[run['status']]}  {time_string} {run['url']}")

    if "schedule" in json_data:
        click.echo(f"\n📅  Schedule: {json_data['schedule']}")


@cli.group()
def secrets():
    pass


@secrets.command()
@click.option("-f", "--file", type=click.File("r"), required=True)
def push(file: IO):
    """Uploads json document of secrets to Treebeard's servers. These will be available in your notebook at runtime
    via treebeard.secrets.get_secrets()"""
    click.echo(f"🌲 Pushing Secrets for project {treebeard_env['project_id']}")
    click.echo(file.name)
    s = file.read()
    try:
        secrets = json.loads(s)
    except:
        click.echo("Error: input file must be valid json")
        return

    response = requests.post(secrets_endpoint, json=secrets, headers=credentials)
    if response.status_code != 200:
        click.echo(
            f"Error: service failure pushing secrets, {response.status_code}: {response.text}"
        )
        return

    click.echo("🔐  done!")
