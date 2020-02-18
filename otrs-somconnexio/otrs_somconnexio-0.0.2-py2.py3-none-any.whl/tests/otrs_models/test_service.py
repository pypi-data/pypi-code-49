# coding: utf-8
import unittest

from pyotrs import Ticket

from otrs_somconnexio.otrs_models.service import Service

from tests.data.otrs_raw_responses import OTRSTicketGetResponse


class ServiceTestCase(unittest.TestCase):

    def test_adsl_without_coverage(self):
        OTRSTicketGetResponse['DynamicField'] = [
            {"Name": "TecDelServei", "Value": "ADSL"},
            {"Name": "coberturaADSL", "Value": "NoServei"},
        ]

        service = Service(Ticket(OTRSTicketGetResponse))

        self.assertFalse(service.has_coverage())

    def test_adsl100_without_coverage(self):
        OTRSTicketGetResponse['DynamicField'] = [
            {"Name": "TecDelServei", "Value": "ADSL+100min"},
            {"Name": "coberturaADSL", "Value": "NoServei"},
        ]

        service = Service(Ticket(OTRSTicketGetResponse))

        self.assertFalse(service.has_coverage())

    def test_adsl1000_without_coverage(self):
        OTRSTicketGetResponse['DynamicField'] = [
            {"Name": "TecDelServei", "Value": "ADSL+1000min"},
            {"Name": "coberturaADSL", "Value": "NoServei"},
        ]

        service = Service(Ticket(OTRSTicketGetResponse))

        self.assertFalse(service.has_coverage())

    def test_adsl_has_coverage(self):
        OTRSTicketGetResponse['DynamicField'] = [
            {"Name": "TecDelServei", "Value": "ADSL"},
            {"Name": "coberturaADSL", "Value": "24M"},
        ]

        service = Service(Ticket(OTRSTicketGetResponse))

        self.assertTrue(service.has_coverage())

    def test_adsl100_has_coverage(self):
        OTRSTicketGetResponse['DynamicField'] = [
            {"Name": "TecDelServei", "Value": "ADSL+100min"},
            {"Name": "coberturaADSL", "Value": "24M"},
        ]

        service = Service(Ticket(OTRSTicketGetResponse))

        self.assertTrue(service.has_coverage())

    def test_adsl1000_has_coverage(self):
        OTRSTicketGetResponse['DynamicField'] = [
            {"Name": "TecDelServei", "Value": "ADSL+1000min"},
            {"Name": "coberturaADSL", "Value": "24M"},
        ]

        service = Service(Ticket(OTRSTicketGetResponse))

        self.assertTrue(service.has_coverage())

    def test_fibre_has_without_coverage(self):
        OTRSTicketGetResponse['DynamicField'] = [
            {"Name": "TecDelServei", "Value": "Fibra"},
            {"Name": "coberturaFibraMM", "Value": "NoFibra"},
            {"Name": "coberturaFibraVdf", "Value": "NoFibraVdf"},
        ]

        service = Service(Ticket(OTRSTicketGetResponse))

        self.assertFalse(service.has_coverage())

    def test_fibre_without_coverage_fibra_indirecta(self):
        OTRSTicketGetResponse['DynamicField'] = [
            {"Name": "TecDelServei", "Value": "Fibra"},
            {"Name": "coberturaFibraMM", "Value": "fibraIndirecta"},
            {"Name": "coberturaFibraVdf", "Value": "NoFibraVdf"},
        ]

        service = Service(Ticket(OTRSTicketGetResponse))

        self.assertFalse(service.has_coverage())

    def test_fibre_has_coverage_MM(self):
        OTRSTicketGetResponse['DynamicField'] = [
            {"Name": "TecDelServei", "Value": "Fibra"},
            {"Name": "coberturaFibraMM", "Value": "Coaxial"},
            {"Name": "coberturaFibraVdf", "Value": "NoFibraVdf"},
        ]

        service = Service(Ticket(OTRSTicketGetResponse))

        self.assertTrue(service.has_coverage())

    def test_fibre_has_coverage_Vdf(self):
        OTRSTicketGetResponse['DynamicField'] = [
            {"Name": "TecDelServei", "Value": "Fibra"},
            {"Name": "coberturaFibraMM", "Value": "NoFibra"},
            {"Name": "coberturaFibraVdf", "Value": "CoaxialVdf"},
        ]

        service = Service(Ticket(OTRSTicketGetResponse))

        self.assertTrue(service.has_coverage())
