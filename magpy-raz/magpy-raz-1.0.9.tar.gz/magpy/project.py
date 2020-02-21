import datetime
import operator
import time
import magpy.general as mg
from magpy.events.project_event import ProjectEvent
from magpy.events.label_event import LabelEvent
from magpy.sprint_items.sprint_issue import SprintIssue
from magpy.sprint_items.sprint_balance import SprintBalance
from magpy.sprint_items.sprint_progress import SprintProgress
from magpy.sprint import Sprint
from magpy.backlog_issue import BacklogIssue
from concurrent.futures import ThreadPoolExecutor


class Project:
    '''
    Represents a Magshimim project, with all its data
    '''

    def __init__(self, gl, hub_name, project_id, start_date, end_date):
        start = time.time()

        # Project
        self.gl_project = gl.gitlab.projects.get(project_id)
        self.name = self.gl_project.name
        self.start_date = start_date
        self.end_date = end_date
        issues = self.gl_project.issues.list(all=True, simple=True)
        events = self.gl_project.events.list(all=True)

        # Group
        self.group = gl.gitlab.groups.get(self.gl_project.namespace.get('id'))

        # Hub name
        self.hub_name = hub_name

        # Sprints
        self.sprints = self.__sprints(issues)

        # Events
        self.events = self.__project_events(events)
        self.events += self.__label_events(issues)

        # Backlog
        self.backlog = self.__backlog(issues)

        elapsed = round(time.time() - start, 1)
        print(f'{self.hub_name}: {self.name} loaded in {elapsed}s')

    def __project_events(self, gl_events):
        '''
        Returns a list of project events
        '''
        events = []
        sprint_start_dates = [s.start_date for s in self.sprints]
        for gl_event in gl_events:
            user_name = gl_event.author.get(mg.EVENT_NAME)
            event = ProjectEvent(hub_name=self.hub_name,
                                 project_name=self.name,
                                 user_name=user_name,
                                 sprint_start_dates=sprint_start_dates,
                                 gl_event=gl_event)
            events.append(event)
        return events

    def __label_events(self, gl_issues):
        '''
        Returns a list of label events, for each related issue
        '''
        sprint_start_dates = [s.start_date for s in self.sprints]
        args = [[gl_issue, self.hub_name, self.name, sprint_start_dates]
                for gl_issue in gl_issues]

        # Start labal event threads
        with ThreadPoolExecutor(20) as executor:
            res = executor.map(self.get_label_events, args)

        # Merge thread results into a single list
        events = [event for issue_events in list(res)
                  for event in issue_events]

        return events

    def __backlog(self, issues):
        '''
        Returns the project backlog
        '''
        backlog = []
        for issue in issues:
            issue_is_open = issue.state == mg.ISSUE_STATE_OPENED
            not_in_milestone = issue.milestone is None
            # only open issues, unassociated with a milestone
            # are considered as a backlog issue
            if issue_is_open and not_in_milestone:
                backlog.append(BacklogIssue(self, issue))

        return backlog

    def __sprints(self, issues):
        '''
        Returns a list of sprints and their associated issues.
        If no valid sprint (milestones) exists, consider the entire
        project as sprint 0.
        '''
        # Start date
        sprints = []
        for milestone in self.gl_project.milestones.list():
            if milestone.start_date is not None and milestone.due_date is not None:
                # Milestones with start and due dates can be made into sprints
                start_date = mg.str_to_date(milestone.start_date)
                end_date = mg.str_to_date(milestone.due_date)
                sprint = Sprint(milestone, start_date, end_date)
                sprints.append(sprint)

        if len(sprints) > 0:
            sprints.sort(key=operator.attrgetter('start_date'))
        else:
            # No valid milestones => entire project is sprint 0
            sprints.append(Sprint(None, self.start_date, self.end_date))

        # Collect data for all sprint issues
        for n, sprint in enumerate(sprints):
            sprint.number = n
            allocated = 0

            # Sprint issues
            for gl_issue in issues:
                if gl_issue.milestone is None:
                    continue

                milestone_id = gl_issue.milestone.get(mg.MILESTONE_ID)
                if milestone_id != sprint.milestone_id:
                    continue

                issue = SprintIssue(self, sprint, gl_issue)
                sprint.items.append(issue)

                allocated += issue.work

            # Sprint balance: unallocated time vs budget
            if sprint.budget > 0:
                balance = sprint.budget - allocated
                if balance != 0:
                    sprint_balance = SprintBalance(self, sprint, balance)
                    sprint.items.append(sprint_balance)

            # Sprint progress: estimated percentage of sprint at current time
            progress = SprintProgress(self, sprint)
            sprint.items.append(progress)

        return sprints

    def get_label_events(self, args):
        '''
        Get all the label changes of an issue.
        '''
        gl_issue, hub_name, project_name, sprint_start_dates = args
        events = []
        label_events = gl_issue.resourcelabelevents.list()

        for label_event in label_events:
            if label_event.label is not None:
                label = label_event.label.get(mg.LABEL_EVENT_NAME)
                if label in mg.STATUS_LABELS:
                    event = LabelEvent(hub_name=hub_name,
                                       project_name=project_name,
                                       sprint_start_dates=sprint_start_dates,
                                       issue_number=gl_issue.iid,
                                       issue_title=gl_issue.title,
                                       label_event=label_event)

                    events.append(event)

        return events
