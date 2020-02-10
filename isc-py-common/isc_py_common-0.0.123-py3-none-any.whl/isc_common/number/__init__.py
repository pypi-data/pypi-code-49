from bitfield import BitHandler, Bit

from isc_common import setAttr


def StrToNumber(s):
    if s == None:
        return None
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError as ex:
            raise ex


def DelProps(value):
    if isinstance(value, dict):
        for key, _value in value.items():
            if isinstance(_value, BitHandler):
                setAttr(value, key, _value._value)
            elif isinstance(_value, Bit):
                setAttr(value, key, _value.is_set)
        return value
    else:
        value


def GetPropsInt(value):
    if isinstance(value, BitHandler):
        return value._value
    else:
        value
