"""
python manage.py test example_app.tests.actionforms.test_mark_done_form
"""

from django.test import TestCase
from example_app.actions.mark_done.form import MarkDoneForm
from example_app.actions.action_registry import ACTIONS
from actions.util import get_action_form

from django.contrib.auth import get_user_model
from django.test.client import RequestFactory
import mock

from example_app.models import Todo

# BulkAddCodesForm
# use this constant rather than hard importing the form so
# that this code can operate based solely on the registry
ACTION_FORM = get_action_form(ACTIONS, 'mark_done')

class TestMarkDoneFormTestCase(TestCase):

    def submit_form(self, user, payload, pk=None, url='/', expect_errors=False):
        rf = RequestFactory()
        req = rf.post(url, payload)
        req.user = user
        form = ACTION_FORM(payload)
        if form.is_valid():
            return form.save(req, pk)
        else:
            if not expect_errors:
                assert False, 'Did not expect to get form errors. Got: {}'.format(form.errors)

    def setUp(self):
        self.user = get_user_model().objects.create(username='joe', password='soap')
        self.todo = Todo.objects.create(owner=self.user, title='test')

    def test_successful_form_submission(self):
        payload = {}
        res = self.submit_form(self.user, payload, pk=self.user.pk)

        import ipdb; ipdb.set_trace()
        # assert ...
