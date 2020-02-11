# coding: utf-8
import unittest
from mock import Mock

from otrs_somconnexio.ticket_exceptions import ServiceTypeNotAllowedError
from otrs_somconnexio.otrs_models.ticket_adsl import ADSLTicket
from otrs_somconnexio.otrs_models.ticket_fibre import FibreTicket
from otrs_somconnexio.otrs_models.mobile_ticket import MobileTicket

from otrs_somconnexio.otrs_models.ticket_factory import TicketFactory


class TicketFactoryTestCase(unittest.TestCase):

    def setUp(self):
        self.eticom_contract = Mock(spec=[])
        self.otrs_configuration = Mock(spec=[])

    def test_build_raise_service_type_not_allowed_error(self):
        ticket_factory = TicketFactory(
            "no allowed_type",
            self.eticom_contract,
            self.otrs_configuration
        )
        with self.assertRaises(ServiceTypeNotAllowedError):
            ticket_factory.build()

    def test_build_mobile_ticket(self):
        service_type = "mobile"
        ticket = TicketFactory(
            service_type,
            self.eticom_contract,
            self.otrs_configuration
        ).build()
        self.assertIsInstance(ticket, MobileTicket)

    def test_build_adsl_ticket(self):
        service_type = "adsl"
        ticket = TicketFactory(
            service_type,
            self.eticom_contract,
            self.otrs_configuration
        ).build()
        self.assertIsInstance(ticket, ADSLTicket)

    def test_build_fibre_ticket(self):
        service_type = "fiber"
        ticket = TicketFactory(
            service_type,
            self.eticom_contract,
            self.otrs_configuration
        ).build()
        self.assertIsInstance(ticket, FibreTicket)
