from peek_core_device._private.PluginNames import deviceTuplePrefix
from vortex.Tuple import addTupleType, TupleField, Tuple


@addTupleType
class ClientSettingsTuple(Tuple):
    """ Client Settings Tuple

    This tuple is for the client UI settings.

    """
    __tupleType__ = deviceTuplePrefix + "ClientSettingsTuple"

    fieldEnrollmentEnabled: bool = TupleField(defaultValue=False)
    officeEnrollmentEnabled: bool = TupleField(defaultValue=False)

