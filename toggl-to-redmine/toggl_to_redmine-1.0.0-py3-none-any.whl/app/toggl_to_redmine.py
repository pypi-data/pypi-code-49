import logging
import click
from .config import AppConfig
from .exceptions import ConfigException, RedmineIntegrationException
from .time_entry import TimeEntry
from toggl_to_redmine.integrations.redmine_integrator import RedmineIntegrator
from toggl_to_redmine.integrations.toggl_integrator import TogglIntegrator

logging.basicConfig(
    format='%(asctime)s %(levelname)s: %(message)s', level=logging.INFO)


def toggl_to_redmine(config):
    """ A program to automaticaly import Toggl time entries to a Redmine app """
    app_config = AppConfig(config)
    redmine = RedmineIntegrator(app_config.redmine_config())
    toggl = TogglIntegrator(app_config.toggl_config())

    time_entries = toggl.fetch_time_entries()

    entries_logged = []
    entries_not_logged = []
    redmine_exception = None

    all_previous_entries_were_saved = True

    for time_entry in time_entries:
        if all_previous_entries_were_saved:
            try:
                redmine.save_entry(time_entry)
                entries_logged.append(time_entry)
            except RedmineIntegrationException as e:
                entries_not_logged.append(time_entry)
                all_previous_entries_were_saved = False
                redmine_exception = e
        else:
            entries_not_logged.append(time_entry)

    if redmine_exception != None:
        redmine_exception.set_pending_entries(entries_not_logged)
        raise redmine_exception

    return entries_logged
