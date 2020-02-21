import gitlab as gl
import datetime
import pytz
import tzlocal

DATE_FORMAT = '%Y-%m-%d'
UTC_TIME_FORMAT = 'T%H:%M:%S.%fZ'

ISSUE_STATE_CLOSED = 'closed'
ISSUE_STATE_OPENED = 'opened'

LABEL_TO_DO = 'To Do'
LABEL_IN_PROGRESS = 'In Progress'
LABEL_DONE = 'Done'
STATUS_LABELS = (LABEL_TO_DO, LABEL_IN_PROGRESS, LABEL_DONE)

EVENT_NAME = 'name'

MILESTONE_ID = 'id'

EVENT_ACTION_COMMENTED_ON = 'commented on'
EVENT_ACTION_CREATED = 'created'
EVENT_ACTION_OPENED = 'opened'
EVENT_ACTION_CLOSED = 'closed'
EVENT_ACTION_PUSHED_NEW = 'pushed new'
EVENT_ACTION_PUSHED_TO = 'pushed to'
EVENT_ACTION_DELETED = 'deleted'
EVENT_ACTION_REMOVE = 'remove'

NOTEABLE_TYPE = 'noteable_type'
NOTEABLE_IID = 'noteable_iid'

PUSH_REF = 'ref'
PUSH_REF_TYPE = 'ref_type'
PUSH_COMMIT_TITLE = 'commit_title'

LABEL_EVENT_REMOVE = 'remove'
LABEL_EVENT_NAME = 'name'

ISSUE_ASSIGNEE_NAME = 'name'
ISSUE_TIME_ESTIMATE = 'time_estimate'
ISSUE_TIME_SPENT = 'total_time_spent'


class MagGitlab:
    '''
    Gitlab connection and common functions
    '''

    def __init__(self, token_file):
        self.gitlab = None
        try:
            with open(token_file, 'r') as token_file:
                token = token_file.read().replace('\n', '')
                self.gitlab = gl.Gitlab(
                    'https://gitlab.com', private_token=token)
        except FileNotFoundError:
            print(f'File {token_file} not found.')
            exit(1)


def str_to_date(gitlab_date):
    '''
    Convert Gitlab date string to date
    '''
    return datetime.datetime.strptime(gitlab_date, DATE_FORMAT).date()


def str_to_datetime(gitlab_datetime):
    '''
    Convert GitLab UTC date-time string to local date-time
    '''
    utc_datetime = datetime.datetime.strptime(gitlab_datetime,
                                              DATE_FORMAT + UTC_TIME_FORMAT)
    return tzlocal.get_localzone().fromutc(utc_datetime)
