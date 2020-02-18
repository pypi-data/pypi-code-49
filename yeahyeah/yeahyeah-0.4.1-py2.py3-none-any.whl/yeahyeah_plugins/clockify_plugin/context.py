"""Context that gets passed around to this yeahyeah_plugins' functions

"""
import datetime

import click
from clockifyclient.api import APIServer
from clockifyclient.client import APISession


class ClockifyPluginContext:
    """Context that gets passed to each clockify_plugin function

    """

    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key
        self.session = APISession(api_server=APIServer(api_url), api_key=api_key)

    @classmethod
    def init_from_dict(cls, dict_in):
        return cls(api_key=dict_in["api_key"], api_url=dict_in["api_url"])

    def to_dict(self):
        return {"api_key": self.api_key, "api_url": self.api_url}


pass_clockify_context = click.make_pass_decorator(ClockifyPluginContext)
default_context = ClockifyPluginContext(
    api_key="<clockify API key>", api_url="<clockify API url>"
)
default_settings_file_name = "clockify.json"
