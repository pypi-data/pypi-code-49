import magpy.general as mg
from magpy.events.base import Event


class ProjectEvent(Event):
    '''
    GitLab project event
    '''
    __NEW_PROJECT = 'new project'

    def __init__(self,
                 hub_name,
                 project_name,
                 user_name,
                 sprint_start_dates,
                 gl_event):

        super().__init__(hub_name,
                         project_name,
                         user_name,
                         sprint_start_dates,
                         gl_event.created_at)

        self.action_name = gl_event.action_name.capitalize()
        self.target_type = self.__target_type(gl_event.target_type)
        self.action, self.number, self.title = \
            self.__action_details(gl_event)

    def __target_type(self, target_type):
        '''
        Event can be either a Gitlab event or a Repository one
        '''
        if target_type is None:
            return Event.TARGET_TYPE_REPOSITOTY

        return Event.TARGET_TYPE_GITLAB

    def __action_details(self, gl_event):
        '''
        Returns a string with the event action details
        '''
        # Reference number (issue/merge request)
        ref_number = None
        if gl_event.action_name in (mg.EVENT_ACTION_OPENED,
                                    mg.EVENT_ACTION_CLOSED):
            ref_number = gl_event.target_iid
        elif gl_event.action_name == mg.EVENT_ACTION_COMMENTED_ON:
            ref_number = gl_event.note.get(mg.NOTEABLE_IID)

        action_text = gl_event.action_name.capitalize()
        if gl_event.target_type is not None:
            if gl_event.action_name == mg.EVENT_ACTION_COMMENTED_ON:
                action_subject = gl_event.note.get(mg.NOTEABLE_TYPE)
                action_text += f' {action_subject.lower()}'
            else:
                action_text += f' {gl_event.target_type.lower()}'
            if gl_event.target_title is not None and ref_number is None:
                action_text += f': {gl_event.target_title}'

        # Pushed to repository
        commit_title = None
        if gl_event.action_name == mg.EVENT_ACTION_PUSHED_TO:
            action_text += f' {gl_event.push_data.get(mg.PUSH_REF_TYPE)}'
            action_text += f' {gl_event.push_data.get(mg.PUSH_REF)}'
            commit_title = gl_event.push_data.get(mg.PUSH_COMMIT_TITLE)

        # Pushed new / delete branch
        if gl_event.action_name in (mg.EVENT_ACTION_PUSHED_NEW,
                                    mg.EVENT_ACTION_DELETED):
            action_text += ' ' + gl_event.push_data.get(mg.PUSH_REF_TYPE)
            branch_name = gl_event.push_data.get(mg.PUSH_REF)
            if branch_name is not None:
                action_text += f' {branch_name}'

        # Created new branch/repository
        if gl_event.action_name == mg.EVENT_ACTION_CREATED:
            action_text += f' {ProjectEvent.__NEW_PROJECT}'

        if ref_number is not None:
            ref_title = gl_event.target_title
        elif commit_title is not None:
            ref_title = commit_title
        else:
            ref_title = None
        return (action_text, ref_number, ref_title)
