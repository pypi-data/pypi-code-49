from enum import Enum


class NotListedEnum(Enum):


    @property
    def special_value(self):
        try:
            return self.__getattribute__('_special_value_')

        except AttributeError:
            pass

    @classmethod
    def _missing_(cls, value):
        try:
            instance = cls.__getitem__('_NOT_LISTED')

        except KeyError:
            raise AttributeError(f"Add '_NOT_LISTED' attribute to your {cls.__name__} Enum")

        instance._special_value_ = value

        return instance


class Currency(NotListedEnum):
    _NOT_LISTED = 0

    KZT = 398
    RUB = 643
    CHF = 756
    USD = 840
    TJS = 972
    EUR = 978
    UAH = 980


class Provider(NotListedEnum):
    _NOT_LISTED = 0


print(Provider(10))
