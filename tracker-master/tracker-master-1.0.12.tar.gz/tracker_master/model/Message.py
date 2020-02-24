from enum import Enum


class MessageType(Enum):
    ALARM = 1
    TEST = 2
    PING = 3

class Message:

    def __init__(self, hw_id, _type, charge):
        print('%s %s %s' % (hw_id, _type, charge))
        # slave hardware id
        self.hw_id = hw_id
        # MessageType
        self.type = MessageType(_type)
        # Amount of slave charge
        self.charge = charge

    def __str__(self):
        return "%s %s %s" % (self.hw_id, self.type.name, self.charge)
