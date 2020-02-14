# Copyright (c) 2014-2020 GeoSpock Ltd.

import json
import webbrowser
from time import time, sleep
from geospock_cli.config_reader import ConfigReaderAndWriter
from geospock_cli.message_sender import MessageSender

import click


class Authorizer:
    # 10s leeway added to prevent using token after expiry time by requesting it just before
    LEEWAY = 10

    def __init__(self, config_reader: ConfigReaderAndWriter):
        self.config_reader = config_reader

    def show_verification_uri_message(self,device_code_response: dict) -> None:
        click.echo(self.config_reader.MESSAGES["verificationInstruction"])
        click.secho(device_code_response["verification_uri_complete"] + "\n", fg="green")

    def get_device_code(self) -> dict:
        headers = {"content-type": "application/json"}
        body = {
            "client_id": self.config_reader.config["client_id"],
            "scope": "offline_access",
            "audience": self.config_reader.config["audience"]
        }
        res = MessageSender.make_request(self.config_reader.config["auth0_url"], "/oauth/device/code", "POST", json.dumps(body), headers)
        return json.loads(res)

    def get_token(self, device_code: str) -> dict:
        headers = {"content-type": "application/json"}
        body = {
            "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
            "device_code": device_code,
            "client_id": self.config_reader.config["client_id"]
        }

        res = MessageSender.make_request(self.config_reader.config["auth0_url"], "/oauth/token", "POST", json.dumps(body), headers)
        return json.loads(res)

    def poll_token(self, device_code_response: dict) -> dict:
        device_code = device_code_response["device_code"]
        interval = device_code_response["interval"]
        expires_in = device_code_response["expires_in"]
        start_time = time()
        try:
            # Repeatedly try to use our temporary device code to get an auth token until the device code expires
            token_response = self.get_token(device_code)
            while int(time() - start_time) < expires_in:
                if "error" in token_response and token_response["error"] == "authorization_pending":
                    # Device code is still valid but user has not yet logged in with their GeoSpock username/password
                    click.echo(token_response["error_description"])
                    self.show_verification_uri_message(device_code_response)
                    if self.config_reader.show_browser:
                        webbrowser.open_new_tab(device_code_response["verification_uri_complete"])
                        self.config_reader.show_browser = False
                elif "error" in token_response:
                    exit(click.secho(token_response["error_description"], fg="red"))
                else:
                    # User has logged in and we have got a valid response
                    return token_response
                sleep(interval)
                token_response = self.get_token(device_code)
        except Exception as e:
            # If we cannot poll for our auth token (e.g. auth server is offline) then report this to the user
            exit(click.secho(ConfigReaderAndWriter.MESSAGES["pollingError"].format(e), fg="red"))
        exit(click.secho(ConfigReaderAndWriter.MESSAGES["pollingError"].format("Device code expired"), fg="red"))

    def init_credentials(self) -> dict:
        # First get a temporary device code and show the verification url to the user
        device_code_response = self.get_device_code()
        # Wait for the user to complete the verification using their GeoSpock credentials, and then save the auth tokens
        token_response = self.poll_token(device_code_response)
        self.config_reader.save_tokens(token_response)
        return token_response

    def refresh_token(self, refresh_token: str) -> dict:
        headers = {"content-type": "application/json"}
        body = {
            "grant_type": "refresh_token",
            "client_id": self.config_reader.config["client_id"],
            "refresh_token": refresh_token,
        }
        res = MessageSender.make_request(self.config_reader.config["auth0_url"], "/oauth/token", "POST", json.dumps(body), headers)
        return json.loads(res)

    def renew_credentials(self) -> dict:
        with open(ConfigReaderAndWriter.GEOSPOCK_FILE) as json_file:
            tokens = json.load(json_file)[self.config_reader.profile]
        if "creation_time" in tokens and "expires_in" in tokens and "access_token" in tokens:
            if int(time() - tokens["creation_time"] + self.LEEWAY) > tokens["expires_in"]:
                try:
                    token_response = self.refresh_token(tokens["refresh_token"])
                    self.config_reader.save_tokens(token_response, tokens["refresh_token"])
                    return token_response
                except Exception as e:
                    exit(click.secho("Exception: {}".format(e), fg="red"))
            else:
                return tokens
        else:
            try:
                token_response = self.refresh_token(tokens["refresh_token"])
                self.config_reader.save_tokens(token_response, tokens["refresh_token"])
                return token_response
            except Exception as e:
                exit(click.secho("Exception: {}".format(e), fg="red"))