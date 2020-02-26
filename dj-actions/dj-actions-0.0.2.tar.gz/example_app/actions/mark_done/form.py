from django import forms
from django.conf import settings

# resource actionform provides deault functionality for this resource:
# from example_app.actions.mixins import TodoActionFormMixin
from actions.forms.mixins import ActionFormMixin
from actions.fields import CommaSeparatedCharField
from example_app.models import Todo

class MarkDoneForm(ActionFormMixin, forms.Form):
    """
    action_id: mark_done
    """
    action_id = 'todo:mark_done'
        # fields go here:
    # ...
    def get_object(self, pk):
        return Todo.objects.get(pk=pk)

    def get_stream_message(self, todo):
        return 'mark_done todo {}'.format(
            todo.title
        )

    def save(self, request, pk=None):

        todo = self.get_object(pk)
        # self.verify_has_permissions(request.user, [todo])

        ## Implement your action here
        todo.status = 'D'
        todo.save()

        # self.perform_post_process(request, todo)
        # extra info to send back to the client, e.g.: count, batch_id etc
        meta = {}
        return (meta, todo)