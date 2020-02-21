import datetime
import magpy.sprint_items.base as ms


class SprintProgress(ms.SprintItem):
    '''
    '''

    __PROGRESS_NAME = 'היום'
    __PROGRESS_TITLE = 'התקדמות צפויה'

    def __init__(self, project, sprint):
        super().__init__(project, sprint)

        self.type = SprintProgress.__PROGRESS_NAME
        self.title = SprintProgress.__PROGRESS_TITLE
        today = datetime.date.today()
        days_from_today = today - sprint.start_date
        days_of_sprint = sprint.end_date - sprint.start_date
        progress = min(round(days_from_today / days_of_sprint, 2), 1.0)
        self.work = progress if sprint.start_date < today else 0.0
