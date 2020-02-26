from datetime import datetime
import requests
import json
import click
from treebeard.version import get_version
import sys

from treebeard.helper import get_treebeard_env
from typing import Optional

treebeard_env = get_treebeard_env()


def get_time():
    return datetime.now().strftime("%H:%M:%S")


def validate_notebook_directory():
    if treebeard_env["project_id"] is None:
        click.echo(
            click.style(
                "This library will not function without credentials.\nPlease email alex@treebeard.io to obtain an API key then run `treebeard configure`",
                fg="red",
            )
        )
        sys.exit(1)
    if treebeard_env["notebook_id"] is None:
        click.echo(
            "Fatal: This command must be run in a directory containing a main.ipynb file"
        )
        sys.exit(1)


def check_for_updates():
    version = get_version()

    pypi_data = requests.get("https://pypi.org/pypi/treebeard/json")
    latest_version = json.loads(pypi_data.text)["info"]["version"]

    if latest_version != version:
        click.echo(
            click.style(
                "🌲 Warning: you are not on the latest version of Treebeard, update with `pip install --upgrade treebeard`",
                fg="yellow",
            )
        )


def get_service_status_message(service_status_url: str) -> Optional[str]:
    data = json.loads(requests.get(service_status_url).text)
    if "message" in data:
        return data["message"]
    return None
