import unittest
from mock import Mock

from otrs_somconnexio.otrs_models.mobile_dynamic_fields import MobileDynamicFields


def dynamic_fields_to_dct(dynamic_fields):
    """
    Convert the MobileDynamicFields object in a dict with the name of the dynamic
    field as key and the value as value.
    Only used to test the MobileDynamicFields object.
    """
    dct = {}
    for df in dynamic_fields:
        dct[df.name] = df.value
    return dct


class MobileDynamicFieldsTestCase(unittest.TestCase):
    def setUp(self):
        self.party = Mock(spec=['first_name', 'name'])
        self.eticom_contract = Mock(spec=[
            'party',
            'mobile_phone_number',
            'mobile_sc_icc',
            'mobile_icc_number',
            'mobile_min',
            'mobile_internet',
            'mobile_option',
        ])
        self.eticom_contract.mobile_option = 'new'
        self.eticom_contract.mobile_min = '0'

        self.mobile_otrs_process_id = "MobileProcessID"
        self.mobile_otrs_activity_id = "MobileActivityID"

    def test_process_id_field(self):
        dynamic_fields = MobileDynamicFields(
            self.eticom_contract,
            self.mobile_otrs_process_id,
            self.mobile_otrs_activity_id
        ).all()

        dynamic_fields_dct = dynamic_fields_to_dct(dynamic_fields)
        self.assertEqual(dynamic_fields_dct["ProcessManagementProcessID"], "MobileProcessID")

    def test_activity_id_field(self):
        dynamic_fields = MobileDynamicFields(
            self.eticom_contract,
            self.mobile_otrs_process_id,
            self.mobile_otrs_activity_id
        ).all()

        dynamic_fields_dct = dynamic_fields_to_dct(dynamic_fields)
        self.assertEqual(dynamic_fields_dct["ProcessManagementActivityID"], "MobileActivityID")

    def test_first_name_field(self):
        self.party.first_name = 'First Name'

        self.eticom_contract.party = self.party

        dynamic_fields = MobileDynamicFields(
            self.eticom_contract,
            self.mobile_otrs_process_id,
            self.mobile_otrs_activity_id
        ).all()

        dynamic_fields_dct = dynamic_fields_to_dct(dynamic_fields)
        self.assertEqual(dynamic_fields_dct["nomSoci"], "First Name")

    def test_name_field(self):
        self.party.name = 'Name'

        self.eticom_contract.party = self.party

        dynamic_fields = MobileDynamicFields(
            self.eticom_contract,
            self.mobile_otrs_process_id,
            self.mobile_otrs_activity_id
        ).all()

        dynamic_fields_dct = dynamic_fields_to_dct(dynamic_fields)
        self.assertEqual(dynamic_fields_dct["cognom1"], "Name")

    def test_line_field(self):
        self.eticom_contract.mobile_phone_number = '666666666'

        dynamic_fields = MobileDynamicFields(
            self.eticom_contract,
            self.mobile_otrs_process_id,
            self.mobile_otrs_activity_id
        ).all()

        dynamic_fields_dct = dynamic_fields_to_dct(dynamic_fields)
        self.assertEqual(dynamic_fields_dct["liniaMobil"], "666666666")

    def test_icc_sc_field(self):
        self.eticom_contract.mobile_sc_icc = '1234'

        dynamic_fields = MobileDynamicFields(
            self.eticom_contract,
            self.mobile_otrs_process_id,
            self.mobile_otrs_activity_id
        ).all()

        dynamic_fields_dct = dynamic_fields_to_dct(dynamic_fields)
        self.assertEqual(dynamic_fields_dct["ICCSC"], "1234")

    def test_icc_donor_field(self):
        self.eticom_contract.mobile_icc_number = '4321'

        dynamic_fields = MobileDynamicFields(
            self.eticom_contract,
            self.mobile_otrs_process_id,
            self.mobile_otrs_activity_id
        ).all()

        dynamic_fields_dct = dynamic_fields_to_dct(dynamic_fields)
        self.assertEqual(dynamic_fields_dct["ICCdonant"], "4321")

    def test_minutes_field_0min(self):
        self.eticom_contract.mobile_min = '0'

        dynamic_fields = MobileDynamicFields(
            self.eticom_contract,
            self.mobile_otrs_process_id,
            self.mobile_otrs_activity_id
        ).all()

        dynamic_fields_dct = dynamic_fields_to_dct(dynamic_fields)
        self.assertEqual(dynamic_fields_dct["minutsMobil"], "0min")

    def test_minutes_field_100min(self):
        self.eticom_contract.mobile_min = '100'

        dynamic_fields = MobileDynamicFields(
            self.eticom_contract,
            self.mobile_otrs_process_id,
            self.mobile_otrs_activity_id
        ).all()

        dynamic_fields_dct = dynamic_fields_to_dct(dynamic_fields)
        self.assertEqual(dynamic_fields_dct["minutsMobil"], "100min")

    def test_minutes_field_200min(self):
        self.eticom_contract.mobile_min = '200'

        dynamic_fields = MobileDynamicFields(
            self.eticom_contract,
            self.mobile_otrs_process_id,
            self.mobile_otrs_activity_id
        ).all()

        dynamic_fields_dct = dynamic_fields_to_dct(dynamic_fields)
        self.assertEqual(dynamic_fields_dct["minutsMobil"], "200min")

    def test_minutes_field_unlimited(self):
        self.eticom_contract.mobile_min = 'unlimited'

        dynamic_fields = MobileDynamicFields(
            self.eticom_contract,
            self.mobile_otrs_process_id,
            self.mobile_otrs_activity_id
        ).all()

        dynamic_fields_dct = dynamic_fields_to_dct(dynamic_fields)
        self.assertEqual(dynamic_fields_dct["minutsMobil"], "unlim")

    def test_data_field(self):
        self.eticom_contract.mobile_internet = '5GB'

        dynamic_fields = MobileDynamicFields(
            self.eticom_contract,
            self.mobile_otrs_process_id,
            self.mobile_otrs_activity_id
        ).all()

        dynamic_fields_dct = dynamic_fields_to_dct(dynamic_fields)
        self.assertEqual(dynamic_fields_dct["dadesMobil"], "5GB")

    def test_data_field_unlimited(self):
        self.eticom_contract.mobile_internet = None
        self.eticom_contract.mobile_internet_unlimited = '10GB'

        dynamic_fields = MobileDynamicFields(
            self.eticom_contract,
            self.mobile_otrs_process_id,
            self.mobile_otrs_activity_id
        ).all()

        dynamic_fields_dct = dynamic_fields_to_dct(dynamic_fields)
        self.assertEqual(dynamic_fields_dct["dadesMobil"], "10GB")

    def test_service_type_field_new(self):
        self.eticom_contract.mobile_option = "new"

        dynamic_fields = MobileDynamicFields(
            self.eticom_contract,
            self.mobile_otrs_process_id,
            self.mobile_otrs_activity_id
        ).all()

        dynamic_fields_dct = dynamic_fields_to_dct(dynamic_fields)
        self.assertEqual(dynamic_fields_dct["tipusServeiMobil"], "altaNova")

    def test_service_type_field_portability(self):
        self.eticom_contract.mobile_option = "portability"

        dynamic_fields = MobileDynamicFields(
            self.eticom_contract,
            self.mobile_otrs_process_id,
            self.mobile_otrs_activity_id
        ).all()

        dynamic_fields_dct = dynamic_fields_to_dct(dynamic_fields)
        self.assertEqual(dynamic_fields_dct["tipusServeiMobil"], "portabilitat")
