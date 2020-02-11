# coding: utf-8
from pyotrs.lib import DynamicField

from otrs_somconnexio.otrs_models.ticket_internet import InternetTicket


class FibreTicket(InternetTicket):

    def service_type(self):
        return 'fiber'

    def _build_specific_dynamic_fields(self):
        """ Return list of OTRS DynamicFields to create a OTRS Process Ticket from Eticom Contract.
        Return only the specifics fields of Fiber Ticket. """
        return [
            self._df_speed(),
        ]

    def _ticket_type(self):
        return self.otrs_configuration.fiber_ticket_type

    def _ticket_queue(self):
        return self.otrs_configuration.fiber_ticket_queue

    def _ticket_state(self):
        return self.otrs_configuration.fiber_ticket_state

    def _ticket_priority(self):
        return self.otrs_configuration.fiber_ticket_proprity

    def _ticket_activity_id(self):
        return self.otrs_configuration.fiber_activity_id

    def _ticket_process_id(self):
        return self.otrs_configuration.fiber_process_id

    def _df_speed(self):
        return DynamicField(
            name="velocitatSollicitada",
            value=self.eticom_contract.internet_speed)
