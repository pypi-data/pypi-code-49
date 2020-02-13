import click

from cli.command_utils import info_message, list_to_table
from disco import Repository

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def repository():
    """Manage repositories."""


@repository.command('list', context_settings=CONTEXT_SETTINGS, short_help="List of repositories for the current user.")
def list_repositories():
    """
    List of repositories for the current user.

    $ disco repository list
    """
    repositories = Repository.list_repositories()
    if len(repositories) > 0:
        _display_repositories(repositories)
    else:
        info_message("There are no set repositories for your account")

def _display_repositories(repositories_list):
    """
    Display repositories as table
    Args:
        repositories_list: list of repositories details

    Returns:
    """
    repository_table = [[rep.id, rep.name] for rep in repositories_list]
    info_message(list_to_table(repository_table, headers=["ID", "Name"]))
