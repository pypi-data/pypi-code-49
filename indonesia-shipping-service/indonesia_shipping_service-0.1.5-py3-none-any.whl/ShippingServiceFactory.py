from enum import Enum

from indonesia_shipping.SicepatService import SicepatService


class CourierType(Enum):
    SICEPAT = 1
    SAP = 2

    @classmethod
    def from_string(cls, name):
        if name.lower() == 'sicepat':
            return cls.SICEPAT
        elif name.lower() == 'sap express':
            return cls.SAP


class InvalidCourierException(Exception):
    pass


class CourierFactory:

    @classmethod
    def create(cls, courier_type, config):
        if courier_type == CourierType.SICEPAT:
            return SicepatService(**config)
        elif courier_type == CourierType.SAP:
            raise NotImplemented
        else:
            raise InvalidCourierException("No Courier Available")
