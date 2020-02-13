import enum

from . import rg_logger


class Enum(enum.Enum):

    @classmethod
    def from_string(cls, str_value: str):
        try:
            if str_value:
                return cls[str_value.title()]
        except Exception as e:
            rg_logger.exception(e, "Enum.parse_string()")

    @classmethod
    def is_valid(cls, enum_value) -> bool:
        if enum_value:
            for _value in cls:
                if _value == enum_value:
                    return True
        else:
            pass

        return False

