import magpy.general as mg
import magpy.sprint_items.base as ms


class SprintIssue(ms.SprintItem):
    '''
    '''

    def __init__(self, project, sprint, gitlab_issue):
        super().__init__(project, sprint)

        self.title = gitlab_issue.title
        self.number = gitlab_issue.iid
        self.assignee = ''
        if gitlab_issue.assignee is not None:
            self.assignee = self.__user_name(
                gitlab_issue.assignee.get(
                    mg.ISSUE_ASSIGNEE_NAME))
        self.assignee = self.assignee.strip().title()
        self.status, self.type = self.__status(gitlab_issue)
        self.work = self.__work(gitlab_issue)

    def __user_name(self, user_name):
        '''
        Returns the name of the user
        '''
        name = user_name.strip().title().split()
        student_name = name[0]
        # Last name initial (if exists)
        if len(name) > 1:
            student_name += f' {name[1][0]}.'

        return student_name

    def __status(self, gitlab_issue):
        '''
        Returns the status of an issue
        '''
        issue_is_closed = gitlab_issue.state == mg.ISSUE_STATE_CLOSED
        issue_is_done = mg.LABEL_DONE in gitlab_issue.labels
        issue_is_in_progress = mg.LABEL_IN_PROGRESS in gitlab_issue.labels
        if issue_is_closed or issue_is_done:
            return ('Done', mg.LABEL_DONE)
        elif issue_is_in_progress:
            return ('In Progress', mg.LABEL_IN_PROGRESS)
        else:
            return ('To Do', mg.LABEL_TO_DO)

    def __work(self, gitlab_issue):
        '''
        Returns the estimated (or spent) work time of an issue, in hours
        '''
        estimate = gitlab_issue.time_stats().get(mg.ISSUE_TIME_ESTIMATE) / 3600
        spent = gitlab_issue.time_stats().get(mg.ISSUE_TIME_SPENT) / 3600
        return spent if spent > 0 else estimate
