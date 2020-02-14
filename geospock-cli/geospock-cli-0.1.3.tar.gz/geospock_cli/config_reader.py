# Copyright (c) 2014-2020 GeoSpock Ltd.

import json
import os
from pathlib import Path
from time import time

import click
from pkg_resources import resource_string
from typing import Optional


class ConfigReaderAndWriter:
    GEOSPOCK_DIR = Path.home().joinpath(".geospock")
    GEOSPOCK_FILE = GEOSPOCK_DIR.joinpath("credentials")
    CONFIG_FILE = GEOSPOCK_DIR.joinpath("config.json")
    MESSAGES = json.loads(resource_string('geospock_cli', "messages.json").decode("utf-8"))

    def __init__(self, profile: str, show_browser: bool):
        self.profile = profile
        self.show_browser = show_browser
        self.config = None
        self.credentials = None

    def write_to_config(self, client_id: str, audience: str, auth0url: str, request_address: str) -> None:
        if not os.path.exists(self.GEOSPOCK_DIR):
            os.mkdir(self.GEOSPOCK_DIR)

        if os.path.exists(self.CONFIG_FILE) and os.path.getsize(self.CONFIG_FILE) > 0:
            with open(self.CONFIG_FILE) as json_file:
                try:
                    current_config = json.load(json_file)
                except json.JSONDecodeError:
                    exit(click.secho(ConfigReaderAndWriter.MESSAGES["invalidConfig"], fg="red"))
                if self.profile in current_config:
                    if current_config[self.profile]["client_id"] == client_id and \
                            current_config[self.profile]["audience"] == audience and \
                            current_config[self.profile]["auth0_url"] == auth0url and \
                            current_config[self.profile]["request_address"] == request_address:
                        click.echo("No change to configuration")
                    else:
                        click.echo("Change in configuration - please rerun 'geospock get-credentials{}'"
                                   .format(" --profile " + self.profile if self.profile != "default" else ""))
                        with open(self.GEOSPOCK_FILE, "r") as current_geospock_file:
                            credentials = json.load(current_geospock_file)
                            credentials.pop(self.profile, None)
                        with open(self.GEOSPOCK_FILE, "w+") as current_geospock_file:
                            current_geospock_file.write(json.dumps(credentials, indent=4))
        else:
            current_config = dict()

        current_config[self.profile] = dict(client_id=client_id, audience=audience, auth0_url=auth0url,
                                            request_address=request_address)

        with open(self.CONFIG_FILE, "w") as config_file_write:
            config_file_write.write(json.dumps(current_config, indent=4))

    def save_tokens(self, tokens: dict, refresh_token=None) -> None:
        if tokens is None:
            click.secho("Failed to authenticate", fg="red")
            return
        if not os.path.exists(self.GEOSPOCK_DIR):
            exit(click.secho(ConfigReaderAndWriter.MESSAGES["credentialsDirectory"], fg="red"))
        tokens["creation_time"] = int(time())
        if refresh_token is not None:
            tokens["refresh_token"] = refresh_token

        if os.path.exists(self.GEOSPOCK_FILE) and os.path.getsize(self.GEOSPOCK_FILE) > 0:
            with open(self.GEOSPOCK_FILE) as json_file:
                current_geospock_file = json.load(json_file)
        else:
            current_geospock_file = dict()
        current_geospock_file[self.profile] = tokens
        with open(self.GEOSPOCK_FILE, "w+") as output_file:
            output_file.write(json.dumps(current_geospock_file, indent=4))

    def get_config(self) -> dict:
        if os.path.exists(self.CONFIG_FILE):
            with open(self.CONFIG_FILE) as json_file:
                try:
                    config_all = json.load(json_file)
                except json.JSONDecodeError:
                    exit(click.secho(ConfigReaderAndWriter.MESSAGES["invalidConfig"], fg="red"))
            if self.profile in config_all:
                self.config = config_all[self.profile]
            return config_all
        else:
            exit(click.secho("Error opening config file", fg="red"))

    def get_all_credentials_from_file(self) -> Optional[dict]:
        if not self.config:
            exit(click.secho("Error opening config file", fg="red"))
        elif os.path.exists(self.GEOSPOCK_FILE) and os.path.getsize(self.GEOSPOCK_FILE) > 0:
            with open(self.GEOSPOCK_FILE) as file:
                try:
                    all_credentials = json.load(file)
                except json.JSONDecodeError:
                    exit(click.secho(ConfigReaderAndWriter.MESSAGES["invalidCredentials"], fg="red"))
                return all_credentials
        else:
            return None
