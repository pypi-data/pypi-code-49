import magpy.csv_files.base as mc


class BacklogFile(mc.CsvFile):
    '''
    '''
    __NAME = 'backlog.csv'
    __HEADER = ('מוקד',
                'פרויקט',
                'תאריך',
                'זמן',
                'גיל',
                'מספר',
                'משימה')

    def __init__(self, backlog):
        super().__init__(file_name=BacklogFile.__NAME,
                         header=BacklogFile.__HEADER,
                         row=lambda backlog_issue: (backlog_issue.hub_name,
                                                    backlog_issue.project_name,
                                                    backlog_issue.date,
                                                    backlog_issue.time,
                                                    backlog_issue.age,
                                                    backlog_issue.issue_number,
                                                    backlog_issue.issue_title),
                         data_list=backlog)
