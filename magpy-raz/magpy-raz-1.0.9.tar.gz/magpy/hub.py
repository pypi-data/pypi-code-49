import magpy.general as mg


class Hub:
    '''
    '''

    def __init__(self, name, group_id, start_date, end_date):
        self.name = name
        self.group_id = int(group_id)
        self.start_date = mg.str_to_date(start_date)
        self.end_date = mg.str_to_date(end_date)
