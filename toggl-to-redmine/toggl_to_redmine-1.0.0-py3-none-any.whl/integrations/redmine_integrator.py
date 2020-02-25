from redminelib import Redmine
from toggl_to_redmine.app.time_entry import TimeEntry, activities
from redminelib.exceptions import AuthError, ValidationError, ServerError
from toggl_to_redmine.app.exceptions import RedmineAuthException, RedmineValidationError, RedmineServerError


class RedmineIntegrator():
    def __init__(self, config: dict):
        url = config.get('redmine_url')
        if RedmineIntegrator.__doesnt_end_with_slash(url):
            url += '/'
        api_key = config.get('redmine_api_key')
        self.redmine = Redmine(url, key=api_key)

    def save_entry(self, entry: TimeEntry):
        try:
            self.__try_to_save_entry(entry)
        except AuthError as e:
            raise RedmineAuthException from e
        except ServerError as e:
            raise RedmineServerError from e
        except ValidationError as e:
            raise RedmineValidationError from e

    def __try_to_save_entry(self, entry: TimeEntry):
        self.redmine.time_entry.create(
            issue_id=entry.issue_id,
            spent_on=entry.start_date,
            hours=entry.worked_hours,
            activity_id=activities[entry.activity],
            comments=entry.comment
        )

    @staticmethod
    def __doesnt_end_with_slash(string: str):
        return string[-1] != '/'
