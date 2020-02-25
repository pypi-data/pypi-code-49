import requests
from requests.auth import HTTPBasicAuth
from toggl_to_redmine.app.config import AppConfig
from toggl_to_redmine.app.time_entry import TimeEntry
from toggl_to_redmine.app.exceptions import TogglCommunicationException, TogglCredentialsException


class TogglIntegrator():
    """ Used to integrate with Toggl and get time entries """

    base_url = 'https://toggl.com/reports/api/v2/details?'

    def __init__(self, config):
        params = TogglIntegrator.__get_time_entries_params(config)
        self.url = TogglIntegrator.base_url + params
        self.token = config.get('toggl_api_token')

    def fetch_time_entries(self):
        try:
            response = requests.get(
                self.url, auth=HTTPBasicAuth(self.token, 'api_token'))
        except ConnectionError:
            raise TogglCommunicationException()

        if not response.ok:
            raise TogglCredentialsException(response.json())

        time_entries = []
        for time_entry_data in response.json()['data']:
            time_entries.append(TimeEntry(time_entry_data))
        return time_entries

    @staticmethod
    def __get_time_entries_params(config):
        params = {
            "user_agent": config.get('toggl_user'),
            "workspace_id": config.get('toggl_workspace_id'),
            "since": config.get('toggl_start_date')
        }

        params_array = []
        for key in params:
            params_array.append(f'{key}={params[key]}')

        return '&'.join(params_array)
