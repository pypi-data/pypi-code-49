from django.core import mail
from django.template.loader import render_to_string

from rest_framework import status


class TestEmailMixin:

    def assert_email_has_been_sent(
        self,
        # to,
        # subject,
        template_path_txt,
        template_path_html,
        template_context
    ):
        expected_text = render_to_string(
            template_path_txt, template_context)

        expected_html = render_to_string(
            template_path_html, template_context)

        sent_mail = mail.outbox[0]
        self.assertIsNotNone(sent_mail)

        # self.assertEqual(sent_mail.to, to)
        # self.assertEqual(sent_mail.subject, subject)
        self.assertEqual(sent_mail.body, expected_text)

        sent_html = None
        for alternative in sent_mail.alternatives:
            # (<h1>Some email html</h1>, 'text/html')
            if alternative[1] == 'text/html':
                sent_html = alternative[0]
                break
        self.assertIsNotNone(sent_html)
        self.assertEqual(sent_html, expected_html)


class GenericAPITestCase:

    expected_status_code = status.HTTP_200_OK
    expected_return_json = {}
    method = 'get'

    def setUp(self):
        self.response = getattr(self.client, self.method)(
            self.end_point,
            self.payload
        )

    @property
    def end_point(self):
        raise NotImplementedError()

    @property
    def payload(self):
        return None

    def test_expected_response(self):
        self.assertEqual(self.response.status, self.expected_status_code)
        self.assertDictEqual(self.response.json(), self.expected_return_json)


class TestAuthenticationMixin:

    use_authenticated_client = True

    @classmethod
    def setUpTestData(cls):
        # print(cls.client)
        cls.user = UserFactory()
        cls.not_registered_user = factory.build(
            dict, FACTORY_CLASS=UserFactory)

        super().setUpTestData()

    def setUp(self):

        if self.use_authenticated_client:
            self.client.force_login(self.user)

        super().setUp()
