import unittest
from datetime import datetime

from pyotrs import Ticket

from otrs_somconnexio.otrs_models.process_ticket import ProcessTicket

from tests.data.otrs_raw_responses import OTRSTicketGetResponse


class OTRSTicketResponseTestCase(unittest.TestCase):
    'Test OTRS Ticket response parser'

    def test_otrs_ticket_get_parse_response(self):
        'Instantiate a OTRSTicket from otrs_ticket_get_response'
        ticket = ProcessTicket(Ticket(OTRSTicketGetResponse))

        # Ticket
        self.assertEqual("2", ticket.id)
        self.assertEqual("2018081300000002", ticket.number)

        # Contract
        self.assertEqual("1022", ticket.contract_id)

        # Soci
        self.assertEqual("Pere", ticket.partner_name)
        self.assertEqual("Pablo", ticket.partner_surname)
        self.assertEqual("123456789", ticket.partner_vat_number)
        self.assertEqual("123456789", ticket.owner_vat_number)

        # Service
        self.assertEqual("666666666", ticket.msisdn)
        self.assertEqual("Cap", ticket.previous_provider)
        self.assertEqual("Street 1234", ticket.service_address)
        self.assertEqual("Barcelona", ticket.service_city)
        self.assertEqual("Barcelona", ticket.service_subdivision)
        self.assertEqual("08123", ticket.service_zip)
        self.assertEqual("1234", ticket.extid)
        self.assertEqual("123456789", ticket.mac_address)
        self.assertEqual("1907", ticket.reference)
        self.assertEqual("user", ticket.endpoint_user)
        self.assertEqual("passw", ticket.endpoint_password)
        self.assertEqual("user", ticket.ppp_user)
        self.assertEqual("ababab", ticket.ppp_password)
        self.assertEqual("adsl", ticket.service_technology)
        # ADSL
        self.assertEqual("no_phone", ticket.landline)
        self.assertEqual("100", ticket.landline_minutes)
        self.assertEqual("dont_apply", ticket.keep_landline_number)
        # Fiber
        self.assertEqual(None, ticket.speed)

        expected_date = datetime.strptime("2018-12-10 00:00:00", "%Y-%m-%d %H:%M:%S")
        self.assertEqual(expected_date, ticket.invoices_start_date)
        self.assertEqual("Notes...", ticket.notes)

    def test_otrs_ticket_is_confirmed(self):
        'Instantiate a OTRSTicket from otrs_ticket_get_response and check if is confirmed'
        OTRSTicketGetResponse['State'] = "closed successful"
        ticket = ProcessTicket(Ticket(OTRSTicketGetResponse))

        self.assertTrue(ticket.confirmed())

    def test_otrs_ticket_is_cancelled(self):
        'Instantiate a OTRSTicket from otrs_ticket_get_response and check if is cancelled'
        OTRSTicketGetResponse['State'] = "closed unsuccessful"
        ticket = ProcessTicket(Ticket(OTRSTicketGetResponse))

        self.assertTrue(ticket.cancelled())
