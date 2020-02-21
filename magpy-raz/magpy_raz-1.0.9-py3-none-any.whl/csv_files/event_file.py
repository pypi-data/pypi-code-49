import magpy.csv_files.base as mc


class EventFile(mc.CsvFile):
    '''
    '''

    __NAME = 'events.csv'
    __HEADER = ('מוקד',
                'פרויקט',
                'תאריך',
                'זמן',
                'חניך',
                'ספרינט',
                'שבוע',
                'ספרינט-שבוע',
                'סוג פעולה',
                'נושא',
                'פעולה',
                'מספר',
                'שם')

    def __init__(self, events):
        super().__init__(file_name=EventFile.__NAME,
                         header=EventFile.__HEADER,
                         row=lambda event: (event.hub_name,
                                            event.project_name,
                                            event.date,
                                            event.time,
                                            event.student_name,
                                            event.sprint_number,
                                            event.week,
                                            event.sprint_week,
                                            event.action_name,
                                            event.target_type,
                                            event.action,
                                            event.number,
                                            event.title),
                         data_list=events)
