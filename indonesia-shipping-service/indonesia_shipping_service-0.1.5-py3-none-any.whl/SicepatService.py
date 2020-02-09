import requests

from indonesia_shipping.ShippingService import ShippingService, ShippingResponse


class SicepatService(ShippingService):

    def __init__(self, api_key, base_url, req=None):
        self.api_key = api_key
        self.base_url = base_url
        self.req = req or requests
        self.response = None

    def get_awb(self, tracking_number):
        """
            return original response
        :param tracking_number:
        :return:
        """
        super().get_awb(tracking_number)
        params = {
            'api-key': self.api_key,
            'waybill': tracking_number
        }

        try:
            response = self.req.get(self.base_url + "/customer/waybill", params=params)
        except Exception as e:
            return {'description': '{}'.format(str(e))}

        if response.status_code == 200:
            self.response = response.json()
            return response.json()
        else:
            return None

    def mapping_response(self):
        """
            returning mapping for standarize response
        :return:
        """
        response = self.response
        if response:
            result = response.get('sicepat', None)
            if result:
                result = result.get('result', None)
                if result:
                    last_status = result.get('last_status', None)
                    if last_status:
                        status = last_status.get('status', None)
                        date_time = last_status.get('date_time', None)

                    return ShippingResponse(
                        waybill_number=result.get('waybill_number', None),
                        last_date_time=date_time,
                        last_status=status,
                        receiver_name=result.get('receiver_name', None),
                        receiver_address=result.get('receiver_address', None),
                        sender_name=result.get('sender_name', None),
                        sender_address=result.get('sender_address', None),
                        description=result.get('description', None)
                    )
            return None
        else:
            raise Exception("please run get_awb first")
