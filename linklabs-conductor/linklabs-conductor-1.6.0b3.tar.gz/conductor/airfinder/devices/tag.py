import logging

from conductor.airfinder.devices.node import Node
from conductor.airfinder.base import DownlinkMessageSpec

LOG = logging.getLogger(__name__)


class TagDownlinkMessageSpecV1_2(DownlinkMessageSpec):
    """ Message Spec for the Alert Tag v1.2.0. """

    header = {
        'def': ['msg_type', 'msg_spec_version'],
        'struct': '>BB',
        'defaults': [0x00, 0x01]
    }

    msg_types = {
            'Configuration': {
                'def': ['mask', 'heartbeat', 'alert_heartbeat',
                        'alert_loc_upd', 'net_lost_scan_count',
                        'net_lost_scan_int', 'max_symble_retries',
                        'button_hold_len', 'audible_alarm_en'],
                'struct': '>BHBBBHBBB',
                'defaults': [0x00, 0x0258, 0x1e, 0x0f, 0x03,
                             0x012c, 0x03, 0x03, 0x01]
            },
            'Ack': {'type': 6},
            'Close': {'type': 7}
    }


class TagDownlinkMessageSpecV1_3(TagDownlinkMessageSpecV1_2):
    """ Message Spec for the Alert Tag v1.3.0. """
    pass


class TagDownlinkMessageSpecV1_4(TagDownlinkMessageSpecV1_3):
    """ Message Spec for the Alert Tag v1.4.0. """
    pass


class TagDownlinkMessageSpecV2_0(TagDownlinkMessageSpecV1_4):
    """ Message Spec for the Alert Tag v2.0.0. """
    pass


class Tag(Node):
    """ Represents a SymBLE Tag. C7 and E7 Hardware platforms. """
    application = "9f333a1ade8500df888f"

    @classmethod
    def _get_spec(cls, vers):
        if vers.major == 1:
            if vers.minor == 2:
                return TagDownlinkMessageSpecV1_2()
            elif vers.minor == 3:
                return TagDownlinkMessageSpecV1_3()
            elif vers.minor == 4:
                return TagDownlinkMessageSpecV1_4()
            else:
                return Exception("Unsupported message spec!")
        elif vers.major == 2:
            if vers.minor == 0:
                return TagDownlinkMessageSpecV2_0()
        raise NotImplementedError


class NordicThingy(Tag):
    """ Represents the Nordic Thingy Test Tag. """
    application = "6c030f3dcaf3055b1098"

    @classmethod
    def _get_spec(cls, vers):
        raise NotImplementedError


class S1Tag(Tag):
    """ Represents the legacy S1 Tag. """
    application = "4068973f7f00791a61f0"

    @classmethod
    def _get_spec(cls, vers):
        raise NotImplementedError


class S1TagGen2(S1Tag):
    """ S1 Tag with temperature """
    application = "150285a4e29b7856c7cc"

    @classmethod
    def _get_spec(cls, vers):
        raise NotImplementedError


class TestTag(Tag):
    """ Development and Testing Tag. """
    application = "9a6d019a9385b231f658"

    @classmethod
    def _get_spec(cls, vers):
        raise NotImplementedError
