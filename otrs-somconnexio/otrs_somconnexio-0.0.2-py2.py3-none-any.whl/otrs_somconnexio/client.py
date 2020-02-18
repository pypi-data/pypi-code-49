import os

from pyotrs import Client
from pyotrs.lib import APIError, HTTPError, ResponseParseError, SessionNotCreated, ArgumentMissingError

from otrs_somconnexio.responses.ticket_creation import OTRSCreationTicketResponse
from otrs_somconnexio.otrs_models.process_ticket import ProcessTicket

from otrs_somconnexio.exceptions import TicketNotCreated, ErrorCreatingSession, TicketNotFoundError, \
    OTRSIntegrationUnknownError


class OTRSClient():
    @staticmethod
    def _password():
        return os.environ['OTRS_PASSW']

    @staticmethod
    def _user():
        return os.environ['OTRS_USER']

    @staticmethod
    def _url():
        return os.environ['OTRS_URL']

    @staticmethod
    def _create_client_with_session():
        """ Create a OTRS Client with session open to play calls.

        This method call to the OTRS API to create a session to play another requests with authentication done.
        Raise User errors to show the problem with the request if it is fault.

        Return a client with the session opens.
        """
        try:
            client = Client(
                baseurl=OTRSClient._url(),
                username=OTRSClient._user(),
                password=OTRSClient._password())
            client.session_create()
        except (HTTPError, APIError, ResponseParseError) as error:
            raise ErrorCreatingSession(error.message)
        return client

    def create_otrs_process_ticket(self, ticket, article, dynamic_fields):
        """ Create a OTRS Process Ticket to manage the provisioning.

        This method call to the OTRS API to create a ticket with all the information of the econtract.
        If the Ticket is created, return the response to save the ID and the number in the EticomContract
        model to keep the relation between systems.
        Else, raise an error with the needed information to fix the EticomContract and rerun the process.

        TODO: In the future, this method enqueue a job to call the OTRS API in asynchronous process.
        """
        client = self._create_client_with_session()
        try:
            client_response = client.ticket_create(
                ticket=ticket,
                article=article,
                dynamic_fields=dynamic_fields)
        except (HTTPError, APIError, ResponseParseError, SessionNotCreated, ArgumentMissingError) as error:
            raise TicketNotCreated(error.message)
        return OTRSCreationTicketResponse(client_response)

    def get_otrs_process_ticket(self, ticket_id):
        """ Search a OTRS Process Ticket by ID.

        This method call to the OTRS API to search a ticket with all the information of the provisioning process.
        If the Ticket is founded, return the Ticket object.
        Else, raise an TicketNotFoundError with error message returned.

        Return a PyOTRS Ticket object.
        """
        client = self._create_client_with_session()
        try:
            ticket = client.ticket_get_by_id(ticket_id, dynamic_fields=True)
        except APIError as error:
            raise TicketNotFoundError(error.message)
        except Exception as error:
            raise OTRSIntegrationUnknownError(error.message)
        if not ticket:
            raise TicketNotFoundError(error.message)
        return ProcessTicket(ticket)

    def search_tickets(self, **params):
        tickets = []

        client = self._create_client_with_session()
        ticket_ids = client.ticket_search(**params)
        for ticket_id in ticket_ids:
            ticket = client.ticket_get_by_id(ticket_id, dynamic_fields=True)
            tickets.append(ProcessTicket(ticket))

        return tickets

    def update_ticket(self, ticket_id, article):
        client = self._create_client_with_session()
        client.ticket_update(ticket_id, article)
