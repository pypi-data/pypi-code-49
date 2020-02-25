from datetime import datetime
from decimal import Decimal
from toggl_to_redmine.app.exceptions import TimeEntryValidationError

activities = {'Design': 8,
              'Development': 9,
              'Analysis': 11,
              'Management': 15,
              'Documentation': 16,
              'Testing': 17,
              'Meeting': 18,
              'Training': 19,
              'Infrastructure': 20}


class TimeEntry():
    """ It represents a time entry object on Redmine """

    def __init__(self, time_entry_data):
        self.data = time_entry_data
        self.validate_tags()
        self.set_issue_id()
        self.set_activity()
        self.set_start_date()
        self.set_worked_hours()
        self.set_comment()
        self.set_timestamp()

    def validate_tags(self):
        if 'tags' not in self.data or len(self.data['tags']) < 2:
            raise TimeEntryValidationError('Entry tags not set properly.')

    def set_issue_id(self):
        self.issue_id = self.data['tags'][0].strip()
        try:
            int(self.issue_id)
        except ValueError:
            raise TimeEntryValidationError('Issue id is not an integer.')

    def set_activity(self):
        self.activity = self.data['tags'][1].strip()
        if self.activity not in activities:
            raise TimeEntryValidationError(
                'Activity is not in the possible values.')

    def set_start_date(self):
        start_date_time = datetime.fromisoformat(self.data['start'])
        self.start_date = start_date_time.date().isoformat()

    def set_worked_hours(self):
        hours_in_millis = Decimal(self.data['dur'])
        hours_in_seconds = hours_in_millis / 1000
        hours = hours_in_seconds / 3600
        self.worked_hours = float(round(hours, 2))

    def set_comment(self):
        self.comment = self.data['description']

    def set_timestamp(self):
        hours_in_millis = self.data['dur']
        hours_in_seconds = hours_in_millis / 1000
        hours = int(hours_in_seconds // 3600)
        remaining_seconds = hours_in_seconds - hours * 3600
        minutes = int(remaining_seconds // 60)
        seconds = int(remaining_seconds - minutes * 60)
        self.timestamp = f"{hours}:{minutes}:{seconds}"

    def log(self):
        return f'Issue Id: {self.issue_id} | Data: {self.start_date} | Hora: {self.worked_hours} | Comment: {self.comment} | Activity: {self.activity}'
