# coding: utf-8
import logging

from pyotrs.lib import Article, DynamicField, Ticket

from otrs_somconnexio.client import OTRSClient

from otrs_somconnexio.ticket_exceptions import CustomerIDMissing, CustomerUserMissing, CustomerMailMissing,\
    CustomerVatNumberMissing


log = logging.getLogger('otrs_somconnexio')


class InternetTicket():

    # This dict is to map the telecom companies from Tryton to OTRS.
    # The key is the name in Tryton and the value is the name in OTRS.
    telecom_companies_mapping = {
        'Jazztel': 'Jazztel',
        'MasMovil': 'MasMovil',
        'Movistar': 'Movistar',
        'Aire / Nubip': 'Nubip',
        'Orange': 'Orange',
        'Parlem': 'Parlem',
        'PepePhone': 'PepePhone',
        'Vodafone': 'Vodafone',
        'Yoigo': 'Yoigo'
    }

    def __init__(self, econtract, otrs_configuration):
        self.eticom_contract = econtract
        self.otrs_configuration = otrs_configuration

    def build(self):
        """
        In this build, create a OTRSClient instance and send the request to create a Ticket. After update the EContract.
        This method must be the unic method exposed by this class.
        """
        otrs_ticket = OTRSClient().create_otrs_process_ticket(
            self._build_ticket(),
            self._build_article(),
            self._build_dynamic_fields())
        return otrs_ticket

    def _build_ticket(self):
        return Ticket({
            "Title": "Sol·licitud {} {}".format(self.service_type(), self.eticom_contract.id),
            "Type": self._ticket_type(),
            "Queue": self._ticket_queue(),
            "State": self._ticket_state(),
            "Priority": self._ticket_priority(),
            "CustomerUser": self._customer_user(),
            "CustomerID": self._customer_id()
        })

    def _build_dynamic_fields(self):
        """ Return list of OTRS DynamicFields to create a OTRS Process Ticket from Eticom Contract. """
        dynamic_fields = [
            self._df_process_id(),
            self._df_activity_id(),
            self._df_econtract_id(),
            self._df_customer_name(),
            self._df_surname1(),
            self._df_vat_number(),
            self._df_phone(),
            self._df_mail(),
            self._df_previous_service(),
            self._df_previous_provider(),
            self._df_landline_number(),
            self._df_address(),
            self._df_city(),
            self._df_zip(),
            self._df_subdivision(),
            self._df_shipment_address(),
            self._df_shipment_city(),
            self._df_shipment_subdivision(),
            self._df_shipment_zip(),
            self._df_owner_vat_number(),
            self._df_owner_name(),
            self._df_owner_surname1(),
            self._df_notes(),
        ]
        dynamic_fields += self._build_specific_dynamic_fields()
        return [field for field in dynamic_fields if field is not None]

    def _customer_id(self):
        if not self.eticom_contract.party:
            raise CustomerIDMissing(self.eticom_contract.id)
        return self._mail()

    def _customer_user(self):
        if not self.eticom_contract.party:
            raise CustomerUserMissing(self.eticom_contract.id)
        return self._mail()

    def _customer_lang(self):
        if not self.eticom_contract.party:
            return 'es_ES'
        return self.eticom_contract.party.lang.code

    def _build_article(self):
        """ Return a instance of OTRS Article to create a OTRS Ticket from Eticom Contract. """
        fields = {
            "Subject": "Sol·licitud {} {}".format(self.service_type(), self.eticom_contract.id),
            "Body": "",
            "ContentType": "text/plain; charset=utf8"
        }
        return Article(fields)

    def _df_process_id(self):
        """ Return the ProcessManagementProcessID DynamicField needed to create a OTRS Process Ticket """
        return DynamicField(name="ProcessManagementProcessID", value=self._ticket_process_id())

    def _df_activity_id(self):
        """ Return the ProcessManagementActivityID DynamicField needed to create a OTRS Process Ticket """
        return DynamicField(name="ProcessManagementActivityID", value=self._ticket_activity_id())

    def _df_econtract_id(self):
        return DynamicField(name="IDContracte", value=self.eticom_contract.id)

    def _df_customer_name(self):
        if self.eticom_contract.party.party_type == 'person':
            customer_name = self.eticom_contract.party.first_name
        else:
            customer_name = self.eticom_contract.party.name
        return DynamicField(name="nomSoci", value=customer_name)

    def _df_surname1(self):
        if self.eticom_contract.party.party_type == 'person':
            return DynamicField(name="cognom1", value=self.eticom_contract.party.name)

    def _df_vat_number(self):
        vat = self.eticom_contract.party.get_identifier()
        if vat:
            return DynamicField(name="NIFNIESoci", value=vat.code)
        raise CustomerVatNumberMissing(self.eticom_contract.id)

    def _phone(self):
        """ Return the phone value. If the party does not have phone return 0. """
        phone = self.eticom_contract.party.get_contact_phone()
        if phone:
            return phone.value
        return None

    def _df_phone(self):
        if self._phone():
            return DynamicField(name="telefonContacte", value=self._phone())

    def _mail(self):
        mail = self.eticom_contract.party.get_contact_email()
        if mail:
            return mail.value
        raise CustomerMailMissing(self.eticom_contract.id)

    def _df_mail(self):
        return DynamicField(name="correuElectronic", value=self._mail())

    def _df_previous_service(self):
        internet_now = self.eticom_contract.internet_now
        if internet_now == 'adsl':
            value = 'ADSL'
        elif internet_now == 'fibre':
            value = 'Fibra'
        else:
            value = 'None'
        return DynamicField(name="serveiPrevi", value=value)

    def _df_previous_provider(self):
        if not self.eticom_contract.internet_telecom_company:
            return DynamicField(name="proveidorPrevi", value='None')
        key = self.eticom_contract.internet_telecom_company.name
        return DynamicField(
            name="proveidorPrevi",
            value=self.telecom_companies_mapping.get(key, 'Other'))

    def _df_landline_number(self):
        if self.eticom_contract.internet_phone_now:
            return DynamicField(
                name='telefonFixVell',
                value=self.eticom_contract.internet_phone_now)

    def _df_address(self):
        return DynamicField(name="direccioServei", value=self.eticom_contract.internet_street)

    def _df_city(self):
        return DynamicField(name="poblacioServei", value=self.eticom_contract.internet_city)

    def _df_zip(self):
        return DynamicField(name="CPservei", value=self.eticom_contract.internet_zip)

    def _df_subdivision(self):
        subdivision = self.eticom_contract.internet_subdivision
        if subdivision:
            subdivision = subdivision.name
        return DynamicField(name="provinciaServei", value=subdivision)

    def _df_shipment_address(self):
        delivery_street = self.eticom_contract.internet_delivery_street
        if not delivery_street:
            delivery_street = self.eticom_contract.internet_street
        return DynamicField(name="direccioEnviament", value=delivery_street)

    def _df_shipment_city(self):
        delivery_city = self.eticom_contract.internet_delivery_city
        if not delivery_city:
            delivery_city = self.eticom_contract.internet_city
        return DynamicField(name="poblacioEnviament", value=delivery_city)

    def _df_shipment_subdivision(self):
        delivery_subdivision = self.eticom_contract.internet_delivery_subdivision
        if not delivery_subdivision:
            delivery_subdivision = self.eticom_contract.internet_subdivision
        if delivery_subdivision:
            delivery_subdivision = delivery_subdivision.name
        return DynamicField(name="provinciaEnviament", value=delivery_subdivision)

    def _df_shipment_zip(self):
        delivery_zip = self.eticom_contract.internet_delivery_zip
        if not delivery_zip:
            delivery_zip = self.eticom_contract.internet_zip
        return DynamicField(name="CPenviament", value=delivery_zip)

    def _df_owner_vat_number(self):
        if not self.eticom_contract.internet_vat_number:
            return None
        return DynamicField(name="NIFNIEtitular", value=self.eticom_contract.internet_vat_number)

    def _titular(self):
        """ Concatenate name, surname and lastname. """
        name = self.eticom_contract.internet_name
        surname = self.eticom_contract.internet_surname
        lastname = self.eticom_contract.internet_lastname
        return u"{} {} {}".format(name, surname, lastname)

    def _df_owner_name(self):
        return DynamicField(name="titular", value=self._titular().encode('utf8'))

    def _df_owner_surname1(self):
        value = u"{} {}".format(self.eticom_contract.internet_surname, self.eticom_contract.internet_lastname)
        return DynamicField(
            name="cognom1Titular",
            value=value.encode('utf8'))

    def _df_notes(self):
        if self.eticom_contract.notes:
            return DynamicField(name="notes", value=self.eticom_contract.notes)
