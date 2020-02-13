from requests import ConnectionError as RequestsConnectionError, HTTPError
import click
from disco.core.exceptions import NoCredentials
import cli.utilities.utils as utils
from cli.command_utils import error_message
from cli import auth_commands, cluster_commands, job_commands, version_commands, repository_commands, \
    docker_image_commands

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    """
    Root CLI Command
    """


def setup_cli():
    """
    Setup CLI
    """
    cli.add_command(auth_commands.login)
    cli.add_command(auth_commands.logout)
    cli.add_command(cluster_commands.cluster_commands)
    cli.add_command(job_commands.job_commands)
    cli.add_command(version_commands.cli_version)
    cli.add_command(repository_commands.repository)
    cli.add_command(docker_image_commands.docker)

def check_version():
    """
    Check if there's a newer version of the CLI
    """
    if utils.is_update_needed():
        click.echo(click.style(
            "There is a newer version. \nPlease upgrade using: pip install disco --upgrade\n",
            fg='yellow', bold='True'))


def main():
    """
    Main CLI
    """
    check_version()
    try:
        setup_cli()
    except Exception:  # pylint: disable=broad-except
        print("Error while setting up cli")

    try:
        cli()
    except HTTPError:
        error_message("Unknown error received from server")
    except RequestsConnectionError:
        error_message("Couldn't establish internet connection. "
                      "Please connect to the internet and try again")
    except NoCredentials:
        error_message("You must be logged in to perform this operation")
    except Exception:  # pylint: disable=broad-except
        error_message("Unknown error occurred")


if __name__ == '__main__':
    main()
