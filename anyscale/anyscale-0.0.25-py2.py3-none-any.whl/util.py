import click
import datetime
import json
import os
import requests

import anyscale.conf
from anyscale.common import ENDPOINTS


def confirm(msg, yes):
    return None if yes else click.confirm(msg, abort=True)


def get_endpoint(endpoint):
    route = ENDPOINTS[endpoint]
    return "{}{}".format(anyscale.conf.ANYSCALE_HOST, route)


def load_credentials():
    path = os.path.expanduser("~/.anyscale/credentials.json")
    if not os.path.exists(path):
        raise click.ClickException(
            "Please create a token by going to {}/cli"
            .format(anyscale.conf.ANYSCALE_HOST))
    with open(path) as f:
        try:
            credentials = json.load(f)
        except json.JSONDecodeError as e:
            raise click.ClickException(e)
    if "cli_token" not in credentials:
        raise click.ClickException(
            "Credential file not valid, please regenerate it.")
    return credentials["cli_token"]


def send_json_request(endpoint, json_args, post=False):
    if anyscale.conf.CLI_TOKEN is None:
        anyscale.conf.CLI_TOKEN = load_credentials()

    url = get_endpoint(endpoint)
    cookies = {"cli_token": anyscale.conf.CLI_TOKEN}
    try:
        if post:
            resp = requests.post(url, json=json_args, cookies=cookies)
        else:
            resp = requests.get(url, params=json_args, cookies=cookies)
    except requests.exceptions.ConnectionError:
        raise click.ClickException(
            "Failed to connect to anyscale server at {}".format(url))

    if not resp.ok:
        raise click.ClickException(
            "{}: {}.".format(resp.status_code, resp.text))
    json_resp = resp.json()
    if "error" in json_resp:
        raise click.ClickException("{}".format(json_resp["error"]))

    return json_resp


def serialize_datetime(d):
    # Make sure that overwriting the tzinfo in the line below is fine.
    # Note that we have to properly convert the timezone if one is
    # already specified. This can be done with the .astimezone method.
    assert d.tzinfo is None
    return d.replace(tzinfo=datetime.timezone.utc).isoformat()


def deserialize_datetime(s):
    return datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.%f+00:00")


def humanize_timestamp(timestamp):
    delta = datetime.datetime.utcnow() - timestamp
    offset = delta.seconds + (delta.days * 60 * 60 * 24)
    delta_s = int(offset % 60)
    offset /= 60
    delta_m = int(offset % 60)
    offset /= 60
    delta_h = int(offset % 24)
    offset /= 24
    delta_d = int(offset)

    if delta_d >= 1:
        return "{} day{} ago".format(delta_d, "s" if delta_d > 1 else "")
    if delta_h > 0:
        return "{} hour{} ago".format(delta_h, "s" if delta_h > 1 else "")
    if delta_m > 0:
        return "{} minute{} ago".format(delta_m, "s" if delta_m > 1 else "")
    else:
        return "{} second{} ago".format(delta_s, "s" if delta_s > 1 else "")


def execution_log_name(session_command_id):
    return ("/tmp/ray_command_output_{session_command_id}"
            .format(session_command_id=session_command_id))


def startup_log_name(session_id):
    return ("/tmp/session_startup_logs_{session_id}"
            .format(session_id=session_id))
