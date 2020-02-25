class ConfigException(Exception):
    """ Exception used when the stored config is corrupted """
    pass


class TimeEntryValidationError(Exception):
    """ Exception used to express a validation problem on Time Entry """
    pass


class TogglCommunicationException(Exception):
    """ Exception used when the communication with Toggl Failed """
    pass


class TogglCredentialsException(Exception):
    """ Exception used when Toggl rejected user credentials """
    pass


class RedmineIntegrationException(Exception):
    """ Base class for integration problems with Redmine. Don't use it directly. """

    def set_pending_entries(self, entries):
        self.pending_entries = entries


class RedmineAuthException(RedmineIntegrationException):
    """ It represents an authorization problem with redmine. """
    pass


class RedmineValidationError(RedmineIntegrationException):
    pass


class RedmineServerError(RedmineIntegrationException):
    """ Server error on redmine. """
    pass
