import magpy.csv_files.base as mc


class SprintFile(mc.CsvFile):
    '''
    '''
    __NAME = 'sprints.csv'
    __HEADER = ('מוקד',
                'פרויקט',
                'ספרינט',
                'סוג',
                'מספר',
                'משימה',
                'חניך',
                'סטטוס',
                'שעות')

    def __init__(self, sprints):
        super().__init__(file_name=SprintFile.__NAME,
                         header=SprintFile.__HEADER,
                         row=lambda sprint_item: (sprint_item.hub_name,
                                                  sprint_item.project_name,
                                                  sprint_item.sprint_name,
                                                  sprint_item.type,
                                                  sprint_item.number,
                                                  sprint_item.title,
                                                  sprint_item.assignee,
                                                  sprint_item.status,
                                                  sprint_item.work),
                         data_list=sprints)
