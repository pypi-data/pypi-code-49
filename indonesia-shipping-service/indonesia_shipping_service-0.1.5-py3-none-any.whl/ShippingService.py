from abc import ABCMeta
from collections import namedtuple


class RequiredTrackingNumberException(Exception):
    pass


class IShippingService:
    __metaclass__ = ABCMeta

    def get_awb(self, tracking_number):
        raise NotImplemented


class ShippingService(IShippingService):

    def get_awb(self, tracking_number):
        self.tracking_number_must_exists(tracking_number)

    def tracking_number_must_exists(self, tracking_number):
        if tracking_number is None or tracking_number == "":
            raise RequiredTrackingNumberException("Tracking Number must be required")


ShippingResponse = namedtuple("ShippingResponse",
                              ["waybill_number", "last_date_time", "last_status", "receiver_name", "receiver_address",
                               "sender_name", "sender_address", "description"]
                              )