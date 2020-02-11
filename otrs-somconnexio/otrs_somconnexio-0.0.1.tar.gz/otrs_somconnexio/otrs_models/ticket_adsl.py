# coding: utf-8
from pyotrs.lib import DynamicField

from otrs_somconnexio.otrs_models.ticket_internet import InternetTicket


class ADSLTicket(InternetTicket):

    def service_type(self):
        return 'adsl'

    def _build_specific_dynamic_fields(self):
        """ Return list of OTRS DynamicFields to create a OTRS Process Ticket from Eticom Contract.
        Return only the specifics fields of ADSL Ticket. """
        return [
            self._df_landline(),
            self._df_landline_minutes(),
            self._df_keep_landline_number(),
        ]

    def _ticket_type(self):
        return self.otrs_configuration.adsl_ticket_type

    def _ticket_queue(self):
        return self.otrs_configuration.adsl_ticket_queue

    def _ticket_state(self):
        return self.otrs_configuration.adsl_ticket_state

    def _ticket_priority(self):
        return self.otrs_configuration.adsl_ticket_proprity

    def _ticket_activity_id(self):
        return self.otrs_configuration.adsl_activity_id

    def _ticket_process_id(self):
        return self.otrs_configuration.adsl_process_id

    def _df_landline(self):
        return DynamicField(name="serveiFix", value=self.eticom_contract.internet_phone)

    def _df_landline_minutes(self):
        return DynamicField(name="minutsInclosos", value=self.eticom_contract.internet_phone_minutes)

    def _keep_landline_number(self):
        if self.eticom_contract.internet_phone == 'no_phone':
            return 'dont_apply'
        return self.eticom_contract.internet_phone_number

    def _df_keep_landline_number(self):
        return DynamicField(name="mantenirFix", value=self._keep_landline_number())
