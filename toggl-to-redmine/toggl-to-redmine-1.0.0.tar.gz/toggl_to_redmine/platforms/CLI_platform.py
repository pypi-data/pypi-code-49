from pathlib import Path
from .base_platform import BasePlatform
from toggl_to_redmine.app.exceptions import *
from .CLI_config_manager import CLIConfigManager
import click
import logging


class CLIPlatform(BasePlatform):
    """ Concrete class to provide CLI functionality to Toggl to Redmine """

    def __init__(self):
        self.config_manager = CLIConfigManager()
        self.entries_saved = []

    def entry_point(self):
        try:
            self.config = self.config_manager.get_config()
            self.entries_saved = self.run_app()
            self.show_entries_saved()
        except ConfigException:
            self.handle_config_problem()
        except (TogglCommunicationException, RedmineServerError):
            self.handle_services_unavailable()
        except (TogglCredentialsException, RedmineAuthException) as e:
            self.handle_credentials_problem(e)
        except TimeEntryValidationError as e:
            self.handle_time_entry_validation_problem(e)
        except Exception as e:
            self.handle_the_unknown(e)

    def show_entries_saved(self):
        click.echo("\nRegistros salvos:")
        for entry in self.entries_saved:
            click.echo(
                f'{entry.issue_id}: {entry.comment} ({entry.timestamp})')
        click.echo()

    def handle_config_problem(self):
        click.echo('\nHello! We need to setup your configs on Toggl-to-Redmine.')
        self.config_manager.reset_config()
        self.entry_point()

    def handle_services_unavailable(self):
        click.echo("\nIt looks like Toggl or Redmine App are not available.")
        click.echo("\nCheck if these services are online and try again.")

    def handle_credentials_problem(self, exception: Exception):
        message = exception.args[0]['error']['message']
        click.echo("\nThere was a problem with your credentials.")
        click.echo(f"Error message: {message}")

        if click.confirm("\nWould you like to inform your config data again?"):
            self.handle_config_problem()
        else:
            click.echo("\nYou could take a look in the config file, then.")

    def handle_time_entry_validation_problem(self, exception: Exception):
        click.echo(
            "\nThere was a problem with at least one of your Time Entries.")
        click.echo(
            "One of them is not following the pattern required for the import.")
        click.echo("You can try again after fixing it.")
        click.echo(f'Error message: {exception}\n')

    def handle_the_unknown(self, exception: Exception):
        click.echo(
            "Something unexpected happened. Contact the package maintainer.\n")
        if click.confirm('Would you like to see the exception?'):
            logging.exception(exception)
