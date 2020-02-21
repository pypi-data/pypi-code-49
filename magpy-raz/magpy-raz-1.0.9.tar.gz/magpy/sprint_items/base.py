class SprintItem:
    '''
    '''

    def __init__(self, project, sprint):
        self.hub_name = project.hub_name
        self.project_name = project.name
        self.sprint_name = f'ספרינט {str(sprint.number)}'
        self.number = 0
        self.assignee = ''
        self.status = ''
