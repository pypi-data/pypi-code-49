from otrs_somconnexio.ticket_exceptions import ServiceTypeNotAllowedError
from otrs_somconnexio.otrs_models.ticket_adsl import ADSLTicket
from otrs_somconnexio.otrs_models.ticket_fibre import FibreTicket
from otrs_somconnexio.otrs_models.mobile_ticket import MobileTicket


class TicketFactory(object):
    """ This factory is to generate the concrete ticket with his internal logic based on
        the service of the EticomContract.
    """
    def __init__(self, contract_type, econtract, otrs_configuration):
        self.contract_type = contract_type
        self.otrs_configuration = otrs_configuration
        self.econtract = econtract

    def build(self):
        """ Create a OTRS Process Ticket with the information of the EticomContract and return it. """
        if self.contract_type not in ("adsl", "fiber", "mobile"):
            raise ServiceTypeNotAllowedError(self.contract_type)

        if self.contract_type == 'adsl':
            ticket = ADSLTicket(self.econtract, self.otrs_configuration)
        elif self.contract_type == 'fiber':
            ticket = FibreTicket(self.econtract, self.otrs_configuration)
        elif self.contract_type == 'mobile':
            ticket = MobileTicket(self.econtract, self.otrs_configuration)

        return ticket
