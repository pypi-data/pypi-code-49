import magpy.sprint_items as ms


class SprintBalance(ms.base.SprintItem):
    '''
    '''
    __BALANCE_TYPE = 'Balance'
    __BALANCE_TITLE = 'זמן פנוי למשימות'

    def __init__(self, project, sprint, balance):
        super().__init__(project, sprint)

        self.type = SprintBalance.__BALANCE_TYPE
        self.title = SprintBalance.__BALANCE_TITLE
        self.work = balance
