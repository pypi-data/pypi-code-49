# coding: utf-8
import unittest
from mock import Mock, patch

from otrs_somconnexio.otrs_models.mobile_ticket import MobileTicket
from otrs_somconnexio.ticket_exceptions import CustomerMailMissing, CustomerUserMissing


class MobileTicketTestCase(unittest.TestCase):

    @patch('otrs_somconnexio.otrs_models.mobile_ticket.Ticket')
    def test_build_ticket(self, MockTicket):
        party = Mock(spec=[
            'get_contact_email'
        ])
        email = Mock(spec=['value'])
        email.value = 'contact@mail.com'
        party.get_contact_email.return_value = email

        eticom_contract = Mock(spec=[
            'id',
            'party'
        ])
        eticom_contract.id = 123
        eticom_contract.party = party

        otrs_configuration = Mock(spec=[
            'mobile_ticket_type',
            'mobile_ticket_queue',
            'mobile_ticket_state',
            'mobile_ticket_priority',
            'mobile_process_id',
            'mobile_activity_id',
            ])
        otrs_configuration.mobile_ticket_type = 'mobile_ticket_type'
        otrs_configuration.mobile_ticket_queue = 'mobile_ticket_queue'
        otrs_configuration.mobile_ticket_state = 'mobile_ticket_state'
        otrs_configuration.mobile_ticket_priority = 'mobile_ticket_priority'
        otrs_configuration.mobile_process_id = 'mobile_process_id'
        otrs_configuration.mobile_activity_id = 'mobile_activity_id'

        expected_ticket_arguments = {
            "Title": "Sol·licitud mobile {}".format(eticom_contract.id),
            "Type": otrs_configuration.mobile_ticket_type,
            "Queue": otrs_configuration.mobile_ticket_queue,
            "State": otrs_configuration.mobile_ticket_state,
            "Priority": otrs_configuration.mobile_ticket_priority,
            "CustomerUser": 'contact@mail.com',
            "CustomerID": 'contact@mail.com'
        }

        MobileTicket(eticom_contract, otrs_configuration)._build_ticket()
        MockTicket.assert_called_with(expected_ticket_arguments)

    @patch('otrs_somconnexio.otrs_models.mobile_ticket.Ticket')
    def test_build_ticket_raise_CustomerMailMissing_error(self, MockTicket):
        party = Mock(spec=[
            'get_contact_email'
        ])
        party.get_contact_email.return_value = None

        eticom_contract = Mock(spec=[
            'id',
            'party'
        ])
        eticom_contract.id = 123
        eticom_contract.party = party

        otrs_configuration = Mock(spec=[
            'mobile_ticket_type',
            'mobile_ticket_queue',
            'mobile_ticket_state',
            'mobile_ticket_priority',
            'mobile_process_id',
            'mobile_activity_id',
            ])
        otrs_configuration.mobile_ticket_type = 'mobile_ticket_type'
        otrs_configuration.mobile_ticket_queue = 'mobile_ticket_queue'
        otrs_configuration.mobile_ticket_state = 'mobile_ticket_state'
        otrs_configuration.mobile_ticket_priority = 'mobile_ticket_priority'
        otrs_configuration.mobile_process_id = 'mobile_process_id'
        otrs_configuration.mobile_activity_id = 'mobile_activity_id'

        with self.assertRaises(CustomerMailMissing):
            MobileTicket(eticom_contract, otrs_configuration)._build_ticket()

    @patch('otrs_somconnexio.otrs_models.mobile_ticket.Ticket')
    def test_build_ticket_raise_CustomerUserMissing_error(self, MockTicket):
        eticom_contract = Mock(spec=[
            'id',
            'party'
        ])
        eticom_contract.id = 123
        eticom_contract.party = None

        otrs_configuration = Mock(spec=[
            'mobile_ticket_type',
            'mobile_ticket_queue',
            'mobile_ticket_state',
            'mobile_ticket_priority',
            'mobile_process_id',
            'mobile_activity_id',
            ])
        otrs_configuration.mobile_ticket_type = 'mobile_ticket_type'
        otrs_configuration.mobile_ticket_queue = 'mobile_ticket_queue'
        otrs_configuration.mobile_ticket_state = 'mobile_ticket_state'
        otrs_configuration.mobile_ticket_priority = 'mobile_ticket_priority'
        otrs_configuration.mobile_process_id = 'mobile_process_id'
        otrs_configuration.mobile_activity_id = 'mobile_activity_id'

        with self.assertRaises(CustomerUserMissing):
            MobileTicket(eticom_contract, otrs_configuration)._build_ticket()

    @patch('otrs_somconnexio.otrs_models.mobile_ticket.MobileArticle')
    def test_build_article(self, MockMobileArticle):
        eticom_contract = Mock(spec=['id'])
        eticom_contract.id = 123

        otrs_configuration = Mock(spec=[])

        mock_mobile_article = MockMobileArticle.return_value

        MobileTicket(eticom_contract, otrs_configuration)._build_article()

        MockMobileArticle.assert_called_with('mobile', eticom_contract)
        mock_mobile_article.call.assert_called_once()

    @patch('otrs_somconnexio.otrs_models.mobile_ticket.MobileDynamicFields')
    def test_build_dynamic_fields(self, MockMobileDynamicFields):
        eticom_contract = Mock(spec=[])

        otrs_configuration = Mock(spec=[
            'mobile_process_id'
            'mobile_activity_id'
        ])
        otrs_configuration.mobile_process_id = 'mobile_process_id'
        otrs_configuration.mobile_activity_id = 'mobile_activity_id'

        mock_mobile_dynamic_fields = MockMobileDynamicFields.return_value

        MobileTicket(eticom_contract, otrs_configuration)._build_dynamic_fields()

        MockMobileDynamicFields.assert_called_with(
            eticom_contract,
            otrs_configuration.mobile_process_id,
            otrs_configuration.mobile_activity_id,
        )
        mock_mobile_dynamic_fields.all.assert_called_once()

    @patch('otrs_somconnexio.otrs_models.mobile_ticket.OTRSClient')
    def test_build(self, MockOTRSClient):
        eticom_contract = Mock(spec=[
            'id',
            'party'
            'mobile_phone_number',
            'mobile_sc_icc',
            'mobile_icc_number',
            'mobile_min',
            'mobile_internet',
            'mobile_option',
        ])
        eticom_contract.party = Mock(spec=[
            'get_contact_email',
            'first_name',
            'name',
        ])
        eticom_contract.mobile_phone_number = "666666666"
        eticom_contract.mobile_option = "new"
        eticom_contract.mobile_min = "0"

        otrs_configuration = Mock(spec=[
            'mobile_ticket_type',
            'mobile_ticket_queue',
            'mobile_ticket_state',
            'mobile_ticket_priority',
            'mobile_process_id',
            'mobile_activity_id',
        ])

        mock_otrs_client = Mock(spec=['create_otrs_process_ticket'])
        MockOTRSClient.return_value = mock_otrs_client

        MobileTicket(eticom_contract, otrs_configuration).build()

        MockOTRSClient.assert_called_once_with()
        mock_otrs_client.create_otrs_process_ticket.assert_called_once()
