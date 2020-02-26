from pathlib import Path
import click
import os
import configparser
import time
import requests
import json
import sys


def get_config_path():
    home = str(Path.home())
    return f"{home}/.treebeard"


config_path = get_config_path()


def get_notebook_name():
    if not os.path.isfile(f"{os.getcwd()}/main.ipynb"):
        return None
    return Path(os.getcwd()).name


def get_treebeard_env():
    """Reads variables from a local file, credentials.cfg"""
    config = configparser.RawConfigParser()
    treebeard_project_id = None
    run_id = None
    email = None
    api_key = None

    try:
        config.read(config_path)
        email = config.get("credentials", "TREEBEARD_EMAIL")
        treebeard_project_id = config.get("credentials", "TREEBEARD_PROJECT_ID")
        api_key = config.get("credentials", "TREEBEARD_API_KEY")

        run_id = os.getenv("TREEBEARD_RUN_ID")
        if run_id is None:
            run_id = f"local-{int(time.time())}"
    except:
        pass  # Default values indicate error occurred
    treebeard_env = {
        "notebook_id": get_notebook_name(),
        "project_id": treebeard_project_id,
        "run_id": run_id,
        "email": email,
        "api_key": api_key,
    }
    return treebeard_env


def set_credentials(email: str, key: str, signup_endpoint: str):
    """Create user credentials"""
    # key = secrets.token_urlsafe(16)
    config = configparser.RawConfigParser()
    config.add_section("credentials")
    config.set("credentials", "TREEBEARD_EMAIL", email)
    # Project id is last 10 numbers of hash of email

    click.echo(signup_endpoint)
    response = requests.post(signup_endpoint, headers={"api_key": key, "email": email},)

    if response.status_code != 200:
        raise click.ClickException(f"Request failed: {response.text}")

    try:
        json_data = json.loads(response.text)
        project_id = json_data["project_id"]
        # click.echo(f"✨  Run has been accepted! {json_data['admin_url']}")
    except:
        click.echo("❗  Request to configure failed")
        click.echo(sys.exc_info())
        if response:
            click.echo(response.text)
        return

    config.set("credentials", "TREEBEARD_PROJECT_ID", project_id)
    config.set("credentials", "TREEBEARD_API_KEY", key)
    with open(config_path, "w") as configfile:
        config.write(configfile)
    click.echo(f"🔑  Config saved in {config_path}")
    return project_id


def get_run_path():
    treebeard_env = get_treebeard_env()
    print(f"Treebeard env is {treebeard_env}")
    return f"{treebeard_env['project_id']}/{treebeard_env['notebook_id']}/{treebeard_env['run_id']}"
