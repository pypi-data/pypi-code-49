import os
import sys
from getpass import getpass

import click
from click_shell import shell
from pyfiglet import Figlet
from termcolor import colored
from colorama import init

from galileo_sdk import GalileoSdk
from .jobs import jobs_cli
from .machines import machines_cli
from .profiles import profiles_cli
from .projects import projects_cli
from .stations import stations_cli

init()


graphic = Figlet(font="slant").renderText("Galileo")
intro = "Welcome to Galileo! (? for help)\n"


@shell(prompt=colored("galileo$ ", "cyan"), intro=f"{graphic}\n{intro}")
@click.option(
    "-u",
    "--username",
    default=lambda: os.environ.get("GALILEO_USER", ""),
    type=str,
    help="Galileo username.",
)
@click.option(
    "-p",
    "--password",
    default=lambda: os.environ.get("GALILEO_PASSWORD", ""),
    type=str,
    help="Galileo password.",
)
@click.option(
    "-t",
    "--token",
    default=lambda: os.environ.get("GALILEO_TOKEN", ""),
    type=str,
    help="Auth0 access token.",
)
@click.option(
    "-rt",
    "--refresh_token",
    default=lambda: os.environ.get("GALILEO_REFRESH_TOKEN", ""),
    type=str,
    help="Auth0 refresh token.",
)
@click.option(
    "-m",
    "--mode",
    default="production",
    help="Either in 'production' or 'development' mode",
)
def main(username, password, token, refresh_token, mode):
    if not username and not password and not token and not refresh_token:
        click.echo(
            "You didn't give us a (username and password) or (token and refresh token) combination. Try again!"
        )
        sys.exit()

    if token and not refresh_token:
        refresh_token = input("Refresh token: ")

    if username and not password:
        password = getpass("Password: ")

    galileo = GalileoSdk(
        username=username,
        password=password,
        auth_token=token,
        refresh_token=refresh_token,
        config=mode,
    )

    @main.command()
    def exit():
        os._exit(0)

    @main.command()
    def quit():
        os._exit(0)

    click.echo(f"Connected to {galileo.backend}!")

    profiles_cli(main, galileo)
    machines_cli(main, galileo)
    projects_cli(main, galileo)
    stations_cli(main, galileo)
    jobs_cli(main, galileo)
