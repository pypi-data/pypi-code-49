from django.test import TestCase
from django.contrib.auth import get_user_model
from actions.tests.testutils import (
    get_instance_action_url,
    get_bulk_action_url
)
from actions.models import ActionEvent
from example_app.models import Todo
from django.contrib.auth import get_user_model

class TestMarkDoneApiTestCase(TestCase):

    def perform_action(self, action_id, payload, performed_by):
        url = get_instance_action_url(
            self.resource,
            self.todo.id,
            action_id,
            context = self.context
        )
        return self.client.post(
            url,
            data = payload,
            context_type='application/json'
        )

    def setUp(self):
        self.context = ''
        self.resource = 'todos'
        self.user = get_user_model().objects.create(username='joe', password='soap')
        self.todo = Todo.objects.create(owner=self.user, title='example todo')

    def test_mark_done(self):
        payload = {}
        res = self.perform_action('mark_done', payload, performed_by=self.user)
        evts = ActionEvent.objects.all()
        import ipdb; ipdb.set_trace()