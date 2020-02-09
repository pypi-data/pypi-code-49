import unittest

from indonesia_shipping.SicepatService import SicepatService


class TestResponseAWBSicepat(unittest.TestCase):

    def test_response_sicepat_service(self):
        waybill_number = 'fake-airwaybill'

        sicepat_service = SicepatService('fake-api', 'fake-url')
        response = sicepat_service.get_awb(waybill_number)

        self.assertEqual(response['waybill_number'], waybill_number)


if __name__ == '__main__':
    unittest.main()
