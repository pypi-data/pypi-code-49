# coding: utf-8
from pyotrs.lib import Ticket

from otrs_somconnexio.client import OTRSClient
from otrs_somconnexio.otrs_models.mobile_article import MobileArticle
from otrs_somconnexio.otrs_models.mobile_dynamic_fields import MobileDynamicFields
from otrs_somconnexio.ticket_exceptions import CustomerMailMissing, CustomerUserMissing, CustomerIDMissing


class MobileTicket():
    def __init__(self, econtract, otrs_configuration):
        self.eticom_contract = econtract
        self.otrs_configuration = otrs_configuration

    def build(self):
        otrs_ticket = OTRSClient().create_otrs_process_ticket(
            self._build_ticket(),
            self._build_article(),
            self._build_dynamic_fields())
        return otrs_ticket

    def _build_ticket(self):
        return Ticket({
            "Title": "Sol·licitud {} {}".format(
                self.service_type(),
                self.eticom_contract.id
            ),
            "Type": self._ticket_type(),
            "Queue": self._ticket_queue(),
            "State": self._ticket_state(),
            "Priority": self._ticket_priority(),
            "CustomerUser": self._customer_user(),
            "CustomerID": self._customer_id()
        })

    def _build_article(self):
        mobile_article = MobileArticle(
            self.service_type(),
            self.eticom_contract
        )
        return mobile_article.call()

    def _build_dynamic_fields(self):
        return MobileDynamicFields(
            self.eticom_contract,
            self.otrs_configuration.mobile_process_id,
            self.otrs_configuration.mobile_activity_id
        ).all()

    def service_type(self):
        return 'mobile'

    def _ticket_type(self):
        return self.otrs_configuration.mobile_ticket_type

    def _ticket_queue(self):
        return self.otrs_configuration.mobile_ticket_queue

    def _ticket_state(self):
        return self.otrs_configuration.mobile_ticket_state

    def _ticket_priority(self):
        return self.otrs_configuration.mobile_ticket_priority

    def _customer_id(self):
        if not self.eticom_contract.party:
            raise CustomerIDMissing(self.eticom_contract.id)
        return self._mail()

    def _customer_user(self):
        if not self.eticom_contract.party:
            raise CustomerUserMissing(self.eticom_contract.id)
        return self._mail()

    def _mail(self):
        mail = self.eticom_contract.party.get_contact_email()
        if mail:
            return mail.value
        raise CustomerMailMissing(self.eticom_contract.id)
