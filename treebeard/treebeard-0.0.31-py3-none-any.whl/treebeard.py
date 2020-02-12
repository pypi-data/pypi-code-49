#! python
from treebeard.helper import get_treebeard_env, fetch_credentials, set_credentials
from halo import Halo
import warnings
import click
import shutil
import time
import os
import base64
import tarfile
import json
import os.path
import subprocess
import secrets
import requests
import timeago
from datetime import datetime
import sys
import humanfriendly
from dateutil import parser
import glob
import tempfile
from pathlib import Path
home = str(Path.home())

config_path = f'{home}/.treebeard'

treebeard_env = get_treebeard_env(config_path)
url = 'http://localhost:8080/notebooks/'
url = "https://scheduler-cvee2224cq-ew.a.run.app/notebooks/"

notebook_name = treebeard_env['notebook_id']
endpoint = f"{url}{notebook_name}"

credentials = {
    'api_key': treebeard_env['api_key'], 'project_id': treebeard_env['project_id']
}

warnings.filterwarnings(
    "ignore", "Your application has authenticated using end user credentials")

# Instantiates a client
dir_path = os.path.dirname(os.path.realpath(__file__))


def get_time():
    return datetime.now().strftime("%H:%M:%S")


@click.group()
def cli():
    pass
    # click.echo('Debug mode is %s' % ('on' if debug else 'off'))


@cli.command()
@click.option('--email', prompt='Your email:')
@click.option('--key', prompt='Your API key:')
def configure(email, key):
    """Set initial credentials"""
    set_credentials(email, key, config_path)


@cli.command()
@click.option('t', '--hourly', flag_value='hourly', help='Run notebook hourly')
@click.option('t', '--daily', flag_value='daily', help='Run notebook daily')
@click.option('t', '--weekly', flag_value='weekly', help='Run notebook weekly')
@click.option('t', '--quarter-hourly', flag_value='quarter-hourly', help='Run quarter-hourly')
@click.option('watch', '--watch', is_flag=True, help='Run and check completed build status')
@click.option('ignore', '--ignore', help='Don\'t submit unneeded virtual envs and large files', multiple=True)
def run(t, watch, ignore):
    """
    Run a notebook and optionally schedule it to run periodically
    """
    if treebeard_env['project_id'] == '':
        quit(1)

    params = {}
    if t:
        params['schedule'] = t

    spinner = Halo(text='zipping directory', spinner='dots')
    spinner.start()

    # Create a temporary file for the compressed directory
    # compressed file accessible at f.name
    with tempfile.NamedTemporaryFile('wb', suffix='.tar.gz', delete=False) as f:
        with tarfile.open(fileobj=f, mode="w:gz") as tar:
            def zip_filter(info: tarfile.TarInfo):
                for ignored in ignore:
                    if info.name in glob.glob(ignored):
                        return None
                return info

            tar.add(os.getcwd(), arcname=os.path.basename(
                os.path.sep), filter=zip_filter)
            tar.add(config_path, arcname=os.path.basename(config_path))
    spinner.text = "submitting notebook to runner"

    size = os.path.getsize(f.name)
    max_upload_size = '100MB'
    if size > humanfriendly.parse_size(max_upload_size):
        click.echo(click.style(
            (f"Error: Compressed notebook directory is {humanfriendly.format_size(size)},"
             f" max upload size is {max_upload_size}. \nPlease ensure you ignore any virtualenv subdirectory"
             " using `treebeard run --ignore venv`"), fg="red"))
        quit(1)

    response = requests.post(
        endpoint,
        files={'repo': open(f.name, 'rb')},
        params=params,
        headers=credentials)

    spinner.stop()
    try:
        json_data = json.loads(response.text)
        click.echo(f"Run has been accepted! {json_data['admin_url']}")
    except:
        click.echo("Run failed.")
        click.echo(sys.exc_info())

    if watch:
        # spinner = Halo(text='watching build', spinner='dots')
        # spinner.start()
        build_result = None
        while not build_result:
            time.sleep(5)
            response = requests.get(endpoint, headers=credentials)
            json_data = json.loads(response.text)
            status = json_data['runs'][-1]['status']
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
    if treebeard_env['project_id'] == '':
        quit(1)
    """Cancels the current notebook build and schedule"""
    spinner = Halo(text='cancelling', spinner='dots')
    click.echo(f"Cancelling {notebook_name}")
    spinner.start()
    requests.delete(endpoint, headers=credentials)
    spinner.stop()
    click.echo(f"cancelled {notebook_name}!")


@cli.command()
def status():
    if treebeard_env['project_id'] == '':
        quit(1)
    """Show the status of the current notebook"""
    response = requests.get(endpoint, headers=credentials)
    json_data = json.loads(response.text)
    if len(json_data) == 0:
        click.echo(
            'This notebook has not been run. Try running it with `treebeard run`')
        quit(1)
    click.echo('Recent runs:')
    for run in json_data['runs']:
        now = parser.isoparse(datetime.utcnow().isoformat() + 'Z')
        start_time = parser.isoparse(run['start_time'])
        time_string = timeago.format(start_time, now=now)
        click.echo(f"{run['url']} {time_string}")

    if 'schedule' in json_data:
        click.echo(f"Schedule: {json_data['schedule']}")


@cli.command()
def version():
    """Shows treebeard package version"""
    import pkg_resources  # part of setuptools
    version = pkg_resources.require("treebeard")[0].version
    click.echo(version)


@cli.command()
def info():
    """Shows treebeard credentials and project info"""
    click.echo(treebeard_env)
