import magpy.general as mg
from magpy.events.base import Event


class LabelEvent(Event):
    '''
    Events of label change on an issue
    '''

    def __init__(self,
                 hub_name,
                 project_name,
                 sprint_start_dates,
                 issue_number,
                 issue_title,
                 label_event):

        user_name = label_event.user.get(mg.LABEL_EVENT_NAME)
        super().__init__(hub_name,
                         project_name,
                         user_name,
                         sprint_start_dates,
                         label_event.created_at)

        self.target_type = Event.TARGET_TYPE_GITLAB
        self.action_name = 'Changed status'
        if label_event.action == mg.EVENT_ACTION_REMOVE:
            action_text = '<<<'
        else:
            action_text = '>>>'
        label = label_event.label.get(mg.LABEL_EVENT_NAME)
        self.action = f'{action_text} {label}'
        self.number = issue_number
        self.title = issue_title
