from toggl_to_redmine.app.exceptions import ConfigException
from toggl_to_redmine.app.toggl_to_redmine import toggl_to_redmine


class BasePlatform():
    """ Base class to implement this application in several platforms (web, cli etc) """

    def __init__(self):
        self.config = {}

    def entry_point(self):
        """ This is where the application should start. """
        raise NotImplementedError

    def run_app(self):
        return toggl_to_redmine(self.config)
