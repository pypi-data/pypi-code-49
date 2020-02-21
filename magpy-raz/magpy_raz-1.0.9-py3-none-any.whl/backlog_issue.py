import datetime
import magpy.general as mg


class BacklogIssue:
    '''
    A GitLab issue with no association to a milestone or assignee
    '''
    __TWO_WEEKS = 'Last Two Weeks'
    __ONE_MONTH = 'Last Month'
    __MORE_THAN_A_MONTH = 'Over a Month'

    def __init__(self, project, gl_issue):
        self.hub_name = project.hub_name
        self.project_name = project.name
        self.issue_number = gl_issue.iid
        self.issue_title = gl_issue.title
        self.date = mg.str_to_datetime(gl_issue.created_at).date()
        self.time = mg.str_to_datetime(gl_issue.created_at).time()
        self.age = self.__age(self.date)

    def __age(self, creation_date):
        '''
        '''

        today = datetime.date.today()
        age_days = (today - creation_date).days
        if age_days <= 14:
            return BacklogIssue.__TWO_WEEKS
        elif age_days < 30:
            return BacklogIssue.__ONE_MONTH
        else:
            return BacklogIssue.__MORE_THAN_A_MONTH
