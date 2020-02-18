import unittest
from mock import Mock, patch

from otrs_somconnexio.otrs_models.ticket_factory import TicketFactory
from otrs_somconnexio.otrs_models.ticket_adsl import ADSLTicket
from otrs_somconnexio.otrs_models.ticket_fibre import FibreTicket


class TicketFactoryIntegrationTestCase(unittest.TestCase):

    @patch('otrs_somconnexio.otrs_models.mobile_ticket.OTRSClient')
    def test_build_mobile_ticket_factory(self, MockOTRSClient):
        contract_type = 'mobile'

        party = Mock(spec=[
            'get_contact_email',
            'first_name',
            'name'
            ])

        eticom_contract = Mock(spec=[
            'id',
            'party',
            'mobile_phone_number',
            'mobile_sc_icc',
            'mobile_icc_number',
            'mobile_min',
            'mobile_internet',
            'mobile_option'
        ])
        eticom_contract.id = 123
        eticom_contract.party = party
        eticom_contract.mobile_option = 'new'
        eticom_contract.mobile_min = '0'

        otrs_configuration = Mock(spec=[
            'mobile_ticket_type',
            'mobile_ticket_queue',
            'mobile_ticket_state',
            'mobile_ticket_priority'
            'mobile_process_id'
            'mobile_activity_id'
        ])
        otrs_configuration.mobile_ticket_type = 'mobile'
        otrs_configuration.mobile_ticket_queue = 'mobile_queue'
        otrs_configuration.mobile_ticket_state = 'mobile_state'
        otrs_configuration.mobile_ticket_priority = 'mobile_priority'
        otrs_configuration.mobile_process_id = 'mobile_process_id'
        otrs_configuration.mobile_activity_id = 'mobile_activity_id'

        otrs_process_ticket = Mock(spec=['id'])
        otrs_process_ticket.id = 234

        mock_otrs_client = Mock(spec=['create_otrs_process_ticket'])
        mock_otrs_client.create_otrs_process_ticket.return_value = otrs_process_ticket
        MockOTRSClient.return_value = mock_otrs_client

        ticket_factory = TicketFactory(contract_type, eticom_contract, otrs_configuration)
        otrs_ticket = ticket_factory.build()
        ticket = otrs_ticket.build()

        self.assertEquals(ticket.id, 234)

    def test_build_adsl_ticket_factory(self):
        contract_type = 'adsl'
        eticom_contract = Mock(spec=[''])
        otrs_configuration = Mock(spec=[''])

        ticket_factory = TicketFactory(contract_type, eticom_contract, otrs_configuration)

        otrs_ticket = ticket_factory.build()

        self.assertIsInstance(otrs_ticket, ADSLTicket)
        self.assertTrue(otrs_ticket.build)

    def test_build_fibre_ticket_factory(self):
        contract_type = 'fiber'
        eticom_contract = Mock(spec=[''])
        otrs_configuration = Mock(spec=[''])

        ticket_factory = TicketFactory(contract_type, eticom_contract, otrs_configuration)

        otrs_ticket = ticket_factory.build()

        self.assertIsInstance(otrs_ticket, FibreTicket)
        self.assertTrue(otrs_ticket.build)
