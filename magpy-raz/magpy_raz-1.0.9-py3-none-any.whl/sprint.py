import datetime
import magpy.general as mg


class Sprint:
    '''
    A project iterration of ~3 weeks, with specific target and contents
    '''

    def __init__(self, gl_milestone, start_date, end_date):
        if gl_milestone is not None:
            # Milestone-based sprint
            self.name = gl_milestone.title
            self.milestone_id = gl_milestone.id
            self.budget = self.__budget(gl_milestone.description)
        else:
            # Default sprint
            self.name = ''
            self.milestone_id = 0
            self.budget = 0

        self.start_date = start_date
        self.end_date = end_date
        self.items = []
        self.number = -1

    def __budget(self, gl_milestone_desc):
        '''
        Extracts sprint budget from the milestone description, based
        on convention, for example: if thr first line includes ' = 4h',
        it means that the budget for the sprint is 4 hours.
        If convention is not followed, budget is set to 0 hours.
        '''
        try:
            desc_first_line = gl_milestone_desc.splitlines()[0]
            budget_total = desc_first_line.split(' = ')[1]
            budget = int(budget_total.split('h')[0])
        except BaseException:
            budget = 0

        return budget
