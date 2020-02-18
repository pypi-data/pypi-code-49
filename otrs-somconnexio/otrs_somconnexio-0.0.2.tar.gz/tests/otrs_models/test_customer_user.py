# coding: utf-8
import unittest
from mock import Mock

from otrs_somconnexio.otrs_models.customer_user import CustomerUser


class CustomerUserTestCase(unittest.TestCase):

    def test_change_language(self):
        new_lang = 'ca'
        customer_id = 'customer@test.coop'
        preference_key = 'UserLanguage'

        MockClient = Mock(spec=['set_preference'])

        CustomerUser(customer_id, MockClient).change_language(new_lang)

        MockClient.set_preference.assert_called_once_with(
            preference_key, customer_id, new_lang)
