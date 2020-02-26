""" Provides the user with access to the Access Point device. """
import logging

from binascii import unhexlify
from copy import deepcopy
from collections import namedtuple
from datetime import datetime, timezone
from enum import IntEnum
from uuid import uuid4

from conductor import INSTANCES
from conductor.airfinder.base import AirfinderSubject, DownlinkMessageSpec
from conductor.devices.module import Module
from conductor.devices.gateway import Gateway
from conductor.tokens import AppToken
from conductor.util import Version, parse_time, addr_to_mac

LOG = logging.getLogger(__name__)


class AccessPointMessageSpecV1_0_0(DownlinkMessageSpec):
    """ Message Spec for the Access Point v1.0.0 """

    header = {
        'def': ['msg_type', 'msg_len'],
        'struct': '>BB'
    }

    control_types = {
        'SET_AP_TYPE': {
            'type': 0x0002,
            'def': ['ap_type'],
            'struct': '>B',
        },
        'SET_LOCATION_GROUP': {
            'type': 0x0003,
            'def': ['loc_group'],
            'struct': '>B',
        },
        'SET_LOCATION_WEIGHT': {
            'type': 0x0004,
            'def': ['loc_weight'],
            'struct': '>B',
        },
        'SET_RSSI_ADJ': {
            'type': 0x0005,
            'def': ['rssi_adj'],
            'struct': '>B',
        },
        'SET_ADV_RATE': {
            'type': 0x0006,
            'def': ['adv_rate'],
            'struct': '>H',
        },
        'SET_ADV_REFRESH': {
            'type': 0x0007,
            'def': ['adv_refresh'],
            'struct': '>H',
        },
        'SET_TIME_SYNC_RATE': {
            'type': 0x0008,
            'def': ['sync_time_rate'],
            'struct': '>I',
        },
        'SET_CONN_TIMEOUT': {
            'type': 0x0009,
            'def': ['conn_timeout'],
            'struct': '>I',
        },
        'SET_STATUS_RATE': {
            'type': 0x000A,
            'def': ['status_rate'],
            'struct': '>I',
        },
        'SET_MAILBOX_RATE': {
            'type': 0x000B,
            'def': ['mailbox_int'],
            'struct': '>I',
        },
        'SET_QUEUE_SEND_RATE': {
            'type': 0x000C,
            'def': ['send_rate'],
            'struct': '>I',
         },
        'SET_QUEUE_THRESH': {
            'type': 0x000D,
            'def': ['send_threshold'],
            'struct': '>B',
        },
        'SET_ENABLE_BLE': {
            'type': 0x0100,
            'def': ['enable'],
            'struct': '>B',
        },
        'GET_STATUS': {
            'type': 0x0106,
        },
        'SET_ENABLE_LOCATION': {
            'type': 0x0107,
            'def': ['enable'],
            'struct': '>B',
        },
        'TRIGGER_ASSERT': {
            'type': 0x0500,
        }
    }

    msg_types = {
        'Unicast': {
            'def': ['endnode_addr', 'time_to_live_s', 'uuid', 'data'],
            'struct': '>6sHI{}s',
            'defaults': [None, 0x1e, None]
        },
        'Multicast': {
            'def': ['app_tok', 'time_to_live_s', 'uuid', 'data'],
            'struct': '>10sHI{}s',
            'defaults': [None, 0x13, None]
        },
        'Control': {
            'type': 0xA0,
            'def': ['ctrl_cmd', 'data'],
            'struct': '>H{}s'
        },
        'SetConfigMode': {
            'type': 0xB0,
            'def': ['timeout', 'net_tok', 'app_tok', 'key'],
            'struct': '>II10s16s',
            'defaults': [0x1e, None, None, None]
        }
    }


class AccessPointMessageSpecV1_0_1(AccessPointMessageSpecV1_0_0):
    """ Message Spec for the Access Point v1.0.1 """

    def __init__(self):
        super().__init__()
        self.control_types = deepcopy(self.control_types)
        self.control_types.update({
            'SET_SYNC_DC': {
                'type': 0x0012,
                'def': ['sync'],
                'struct': '>B'
            },
            'SET_SCHEDULE': {
                'type': 0x0020,
                'def': ['sched'],
                'struct': '>21s'
            },
            'SET_ACK_MODE': {
                'type': 0x0108,
                'def': ['mode'],
                'struct': '>B'
            },
            'SET_TX_POWER': {
                'type': 0x0109,
                'def': ['tx_pwr'],
                'struct': '>B'
            }
        })


class AccessPointMessageSpecV1_1_0(AccessPointMessageSpecV1_0_1):
    """ Message Spec for the Access Point v1.1.0 """
    pass  # Same as v1.0.1 for Downlink.


class AccessPointMessageSpecV2_0_0(AccessPointMessageSpecV1_1_0):
    """ Message Spec for the Access Point v2.0.0 """

    def __init__(self):
        super().__init__()
        self.header.update({
            'def': ['msg_type', 'msg_spec_vers_major', 'msg_spec_vers_minor',
                    'msg_spec_vers_tag', 'msg_len'],
            'struct': '>BBBBB',
            'defaults': [None, 0x02, 0x00, 0x00, None]
        })

        self.msg_types.update({
            'ConfigurationQuery': {
                'type': 0xA1,
                'def': ['uuid'],
                'struct': 'I'
            }
        })

        self.control_types.update({
            'CONFIG_BLE_FRONT_END': {
                'type': 0x010A,
                'def': ['config'],
                'struct': '>B'
            },
            'SAMPLE_BATT': {
                'type': 0x0103
            },
            'SET_DST': {
                'type': 0x0021,
                'def': ['enable'],
                'struct': '>B'
            },
            'SET_DUTY_CYCLE': {
                'type': 0x0022,
                'def': ['window'],
                'struct': '>B'
            }
        })


class AccessPointMessageSpecV2_0_1(AccessPointMessageSpecV2_0_0):
    """ Message Spec for the Access Point v2.0.1 """

    def __init__(self):
        super().__init__()

        self.control_types.update({
            'SET_NET_TOKEN': {
                'type': 0x0001,
                'def': ['net_tok'],
                'struct': '>I',
                'defaults': [0x4f50454e]
            },
            'SET_DL_BAND': {
                'type': 0x00A0,
                'def': ['band_edge_lower', 'band_edge_upper',
                        'band_edge_guard', 'band_edge_ch_step',
                        'band_edge_ch_offset'],
                'struct': '>IIIBB'
            },
            'SET_DS_NET_TOKEN': {
                'type': 0x00A1,
                'def': ['net_tok'],
                'struct': '>I',
                'defaults': [0x4f50454e]
            },
        })


class AccessPointMessageSpecV2_0_2(AccessPointMessageSpecV2_0_1):
    """ Message Spec for the Access Point v2.0.2 """

    def __init__(self):
        super().__init__()
        self.header['defaults'] = [None, 0x02, 0x00, 0x02, None]

        self.control_types.update({
            'SET_SYM_GW_RSSI': {
                'type': 0x00B0,
                'def': ['rssi'],
                'struct': '>h'
            },
            'SET_SYM_SCAN_MODE': {
                'type': 0x00B1,
                'def': ['mode'],
                'struct': '>H'
            },
            'SET_SYM_SCAN_ATTEMPTS': {
                'type': 0x00B2,
                'def': ['attempts'],
                'struct': '>B'
            },
            'SET_SYM_HOP_INT': {
                'type': 0x00B3,
                'def': ['interval'],
                'struct': '>I'
            },
            'SET_MAX_GW_ERROR': {
                'type': 0x00B4,
                'def': ['max_err'],
                'struct': '>B'
            },
            'SET_SYM_INFO_SCAN_INT': {
                'type': 0x00B5,
                'def': ['interval'],
                'struct': '>I'
            }
        })


class AccessPointMessageSpecV2_0_3(AccessPointMessageSpecV2_0_1):
    """ Message Spec for the Access Point v2.0.3 """

    def __init__(self):
        super().__init__()
        self.header['defaults'] = [None, 0x02, 0x00, 0x03, None]


class CommandBase(IntEnum):
    """ Adds convience methods to Enums. """
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)


class AckMode(CommandBase):
    """ Which devices will acknowledge downlink. """
    DISABLED = 0x00
    TAG = 0x01
    ALL = 0xFF


class AntennaPort(CommandBase):
    """ Which Antenna Port to Utilize. """
    ANT_A = 0
    ANT_B = 1


class ApType(CommandBase):
    """ Whether an AP will funciton as a Location or an Access Point. """
    CONNECTABLE = 0x0,
    LOCATION = 0x01


class ScanMode(CommandBase):
    """ Types of Scans the AP can perform for GWs. """
    NORMAL = 0x01,
    INFO = 0x02


UplinkQueueStats = namedtuple('UplinkQueueStats', ["uplinkQueueFillLevel",
                                                   "uplinkQueueMsgCount"])

TaskStats = namedtuple('TaskStats', ['taskBHConnectionErrorCount',
                                     'taskBHTaskErrorCount',
                                     'taskBHTimeoutErrorCount',
                                     'taskBHTxErrorCount',
                                     'taskBLEConnectionCount',
                                     'taskBLEDisconnectionCount',
                                     'taskBLEErrorCount',
                                     'taskCacheErrorCount',
                                     'taskErrorCount'])
AssertInfo = namedtuple('AssertInfo', ['file_name', 'line_num'])
DownlinkCounts = namedtuple('DownlinkCounts', ['unicast', 'multicast'])


class AccessPoint(Module, AirfinderSubject):
    """ Represents a SymBLE Access Point. """
    subject_name = 'node'
    af_subject_name = 'accesspoint'
    application = '5578ab6f7997519df80b'

    def __init__(self, **kwargs):
        """ AccessPoint Constructor.

        Note:
            The `session`, `subject_id` and `instance` fields are not required
            when the `module` field is provided. Additionally, they will be
            ignored if supplied with a `module`.

            When manually supplying these fields, they must be consistent with
            the object creating the AccessPoint

        Args:
            module (conductor.Module): Can be the only argument if supplied,
                otherwise, all of the other arguments are required.
            session (requests.session): Represents the authenticated requests
                session required to interface with conductor/airfinder.
            subject_id (str or :class`.Module`): The Conductor Address of the
                AccessPoint.
            instance (str): The conductor instance that the session is using.
            _data (str): Optional when module is supplied, will override if
                module's are empty. Will be generated if not found.

        Returns:
            :class`.AccessPoint`
        """
        module = kwargs.get('module')
        session = kwargs.get('session')
        subject_id = kwargs.get('subject_id')
        instance = kwargs.get('instance')
        _data = kwargs.get('_data')

        # Apply module members when applicable
        if module:
            session = module.session
            subject_id = module.subject_id
            instance = module.instance
            _data = module._data if module._data else _data

        # Validate and construct object.
        if not session or not subject_id or instance not in INSTANCES:
            raise Exception("Invalid Construction of an Access Point!")

        super().__init__(session, subject_id, instance, _data)

        # Apply data if unavailable
        if not _data:
            url = '{}/airfinder/{}/{}'.format(self.network_asset_url,
                                              self.af_subject_name,
                                              self.subject_id)
            resp = session.get(url)
            resp.raise_for_status()
            self._data = resp.json()

    ###########################################################################
    # Core Methods.
    ###########################################################################

    @classmethod
    def _get_spec(cls, vers):
        if vers.major == 1:
            if vers.minor == 0:
                if vers.tag == 0:
                    return AccessPointMessageSpecV1_0_0()
                elif vers.tag == 1:
                    return AccessPointMessageSpecV1_0_1()
                else:
                    return Exception("Unsupported Message Specification!")
            elif vers.minor == 1:
                return AccessPointMessageSpecV1_1_0()
            else:
                return Exception("Unsupported Message Specification!")
        elif vers.major == 2:
            if vers.tag == 0:
                return AccessPointMessageSpecV2_0_0()
            elif vers.tag == 1:
                return AccessPointMessageSpecV2_0_1()
            elif vers.tag == 2:
                return AccessPointMessageSpecV2_0_2()
            elif vers.tag == 3:
                return AccessPointMessageSpecV2_0_3()
            else:
                return Exception("Unsupported Message Specification!")
        else:
            return Exception("Unsupported Message Specification!")

    @classmethod
    def _issue_multicast(cls, payload, time_to_live_s, vers, gateways):
        """ Issues a multicast message targeted at all Access Points.

        Args:
            payload (bytes): The data to send to the Access Points.
            time_to_live_s (int): The amount of time the message will
                remain valid.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.

        Returns:
            :class`conductor.subject.DownlinkMessage`
        """
        # Validate Arguments.
        if not gateways:
            raise ValueError("Must specify gateway to multicast to!")
        gw = gateways[0]
        if not isinstance(gw, Gateway):
            raise ValueError("Gateway must be an instantiated Gateway"
                             " Object!")
        if not isinstance(vers, Version):
            raise ValueError("AP Version must be a Version object!")

        # Note: Class Method does not have any member variables so we
        # need an instantiated object's session and instance.
        app_tok = AppToken(gw.session, cls.application, gw.instance)
        return app_tok.send_message(payload, gateways, False, time_to_live_s)

    def send_unicast_message(self, endnode, payload, ble_ttl_s, uuid=None,
                             gateway_addr=None, time_to_live_s=60.0, port=0,
                             priority=10):
        """ Sends a message targeted at the SymBLE endnode to the AP.

        Args:
            endnode (:class:`.conductor.airfinder.devices.node`):
                The Endnode to send the payload to.
            payload (bytearray):
                The data payload to send to the endnodes.
            ble_ttl_s (int):
                The number of seconds that the endnodes have to recieve the
                mailbox message on the AP, before the message expires.
            uuid (bytearray):
                A Universally Unique Id, to prevent the symble endnodes from
                recieving the same message more than once.
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class`conductor.subject.DownlinkMessage`
        """
        addr = unhexlify(addr_to_mac(endnode.subject_id).replace(':', ''))
        if not uuid:
            uuid = uuid4().fields[0]
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_message('Unicast',
                                                 endnode_addr=addr,
                                                 time_to_live_s=ble_ttl_s,
                                                 uuid=uuid,
                                                 data=payload)
        return self.send_message(pld, gateway_addr=gateway_addr,
                                 time_to_live_s=time_to_live_s,
                                 port=port, priority=priority)

    def send_multicast_message(self, app_token, payload, ble_ttl_s, uuid,
                               gateway_addr=None, time_to_live_s=60.0, port=0,
                               priority=10):
        """ Sends a message targeted at a SymBLE endnode's application token
        to the AP, for all avalible endnodes to recieve.

        Args:
            app_token (:class:`.conductor.tokens.AppToken`):
                The Application Token to send the payload to.
            payload (bytearray):
                The data payload to send to the endnodes.
            ble_ttl_s (int):
                The number of seconds that the endnodes have to recieve the
                mailbox message on the AP, before the message expires.
            uuid (bytearray):
                A Universally Unique Id, to prevent the symble endnodes from
                recieving the same message more than once.
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class`conductor.subject.DownlinkMessage`
        """
        vers = self.msg_spec_version
        app_tok_hex = bytearray.fromhex(app_token)
        pld = self._get_spec(vers).build_message('Multicast',
                                                 app_tok=app_tok_hex,
                                                 time_to_live_s=ble_ttl_s,
                                                 uuid=uuid,
                                                 data=payload)
        return self.send_message(pld, gateway_addr=gateway_addr,
                                 time_to_live_s=time_to_live_s,
                                 port=port, priority=priority)

    ###########################################################################
    # Access Point Properties.
    ###########################################################################

    @property
    def name(self):
        """ Returns:
            The user issued name of the Subject.
        """
        return self._data.get('name')

    @property
    def device_type(self):
        """ Represents the human-readable Application Token that identifies
        which data parser the device is using. """
        return self._md.get('deviceType')

    @property
    def msg_spec_version(self):
        """ Message Spec Version of the AP """
        # Note: v1 APs did not report version.
        return Version(1, 0, 1)

    @property
    def assert_count(self):
        """ Returns the assert count of the AccessPoint when available, None
        otherwise. """
        val = self._md.get('assertCount')
        return int(val) if val else None

    @property
    def last_assert_info(self):
        """ Returns conductor.airfinder.access_point.AssertInfo when an assert
        has occured, otherwise None. """
        assert_occured = self._md.get('assertOccured')
        line_num = self._md.get('assertLineNumber')
        file_name = self._md.get('assertFileName')

        try:
            if bool(assert_occured):
                return AssertInfo(file_name, int(line_num))
        except TypeError:
            return None
        return None

    @property
    def avg_rssi(self):
        """ Returns the average RSSI of the AccessPoint. """
        val = self._md.get('averageRssi')
        return float(val) if val else None

    @property
    def battery_percent(self):
        """ Returns the battery percentage of the AccessPoint. """
        val = self._md.get('batteryPercentage')
        return float(val) if val else None

    @property
    def blacklist_len(self):
        """ Returns the length of the AccessPoint's blacklist. """
        val = self._md.get('dbBlacklistLength')
        return int(val) if val else None

    @property
    def node_count(self):
        """ Returns the number of Nodes connected through the AccessPoint. """
        val = self._md.get('dbNodeCount')
        return int(val) if val else None

    @property
    def downlink_counts(self):
        """ Returns conductor.airfinder.access_point.DownlinkCounts when
        available, None otherwise. """
        uni = self._md.get('downlinkUnicastCount')
        multi = self._md.get('downlinkMulticastCount')

        try:
            uni = int(uni)
            multi = int(multi)
        except TypeError:
            return None

        return DownlinkCounts(uni, multi)

    @property
    def is_lost(self):
        """ Returns if the AccessPoint is lost. """
        val = self._md.get('isLost')
        return bool(val) if val else None

    @property
    def last_event_time(self):
        """ Returns the last event time if available, otherwise, None. """
        val = self._md.get('lastEventTime')
        return parse_time(val) if val else None

    @property
    def last_msg_type(self):
        """ Returns the last message type if available, None otherwise. """
        # NOTE: "msgType" is also valid, possibly equal?
        val = self._md.get('lastMsgType')
        return int(val, 16) if val else None

    @property
    def coordinates(self):
        """ Returns the coorindate of the Access Point. """
        value = self._md.get("mapPoint").split(',')
        return (float(value[0]), float(value[1])) if value else None

    @property
    def last_reset_cause(self):
        """ Returns the last reset cause when available, None otherwise. """
        val = self._md.get('lastResetCause')
        # TODO: Human-Readable Reset Causes per device.
        return int(val) if val else None

    @property
    def msg_count(self):
        """ Returns the message count when available, None otherwise. """
        val = self._md.get('msgCounter')
        return int(val) if val else None

    @property
    def network_loading(self):
        """ Returns the network loading when available, None otherwise. """
        val = self._md.get('networkLoading')
        return int(val) if val else None

    @property
    def reset_count(self):
        """ Returns the reset count of the AccessPoint when avalibale, None
        otherwise. """
        val = self._md.get('resetCount')
        return int(val) if val else None

    @property
    def rp_count(self):
        """ Returns the number of RPs connected to the AccessPoint when
        available, None otherwise. """
        val = self._md.get('rpCount')
        return int(val) if val else None

    @property
    def rssi_collect_time(self):
        """ Returns the datetime.datetime that the rssi was collected when
        available, None otherwise. """
        val = self._md.get('rssiCollectTime')
        return parse_time(val) if val else None

    @property
    def last_payload_len(self):
        """ Returns the last payload length when available, None otherwise. """
        val = self._md.get('symMsgPayloadLength')
        return int(val) if val else None

    @property
    def version(self):
        """ Returns the firmware version of the AccessPoint when available,
        None otherwise."""
        major = self._md.get('symbleAPFirmwareVersionMajor')
        minor = self._md.get('symbleAPFirmwareVersionMinor')
        tag = self._md.get('symbleAPFirmwareVersionTag')
        if not major or not minor or not tag:
            return None
        return Version(int(major), int(minor), int(tag))

    @property
    def symble_version(self):
        """ Returns the SymBLE Version when available, None otherwise. """
        val = self._md.get('symbleVersion')
        return Version(int(val)) if val else None

    @property
    def sys_time(self):
        """ Returns the datetime.datetime System Time of AccessPoint when
        available, None otherwise. """
        val = self._md.get('systemTimestamp_epochSeconds')
        # NOTE: Should we use "systemTimestamp_epochMilliseconds" too?
        return datetime.fromtimestamp(int(val), timezone.utc) if val else None

    @property
    def task_stats(self):
        """ Returns conductor.airfinder.access_point.TaskStats when available,
        None otherwise."""
        try:
            return TaskStats(
                int(self._md.get("taskBHConnectionErrorCount")),
                int(self._md.get("taskBHTaskErrorCount")),
                int(self._md.get("taskBHTimeoutErrorCount")),
                int(self._md.get("taskBHTxErrorCount")),
                int(self._md.get("taskBLEConnectionCount")),
                int(self._md.get("taskBLEDisconnectionCount")),
                int(self._md.get("taskBLEErrorCount")),
                int(self._md.get("taskCacheErrorCount")),
                int(self._md.get("taskErrorCount")))
        except ValueError:
            return None

# TODO: Is this field valuable? Or a duplicate of sys_time?
#    @property
#    def last_timestamp(self):
#        """ """
#        return self._md.get('')
#
#        "timestamp_milliseconds": "496",
#        "timestamp_seconds": "1563812972",

# TODO: Is this field valuable? Or completely non-functional?
#        "temperature": "27080",

    @property
    def uplink_queue_stats(self):
        """ Returns the uplink queue stats of the AccessPoint if available,
        None otherwise. """
        try:
            return UplinkQueueStats(
                    int(self._md.get("uplinkQueueFillLevel")),
                    int(self._md.get("uplinkQueueMsgCount")))
        except ValueError:
            return None

    @property
    def uptime(self):
        """ Returns the uptime of the AccessPoint when available,
        None otherwise. """
        val = self._md.get('uptime')
        return int(val) if val else None

    ###########################################################################
    # Configuration Methods.
    ###########################################################################

    def set_config_mode(self, timeout, app_token, net_token, key,
                        gateway_addr=None, acked=True,
                        time_to_live_s=60.0, port=0, priority=10):
        """ Requests that the AP enters Configuration Mode.

        Args:
            timeout (int):
                How many seconds the AP will stay in config mode.
            app_token (:class:`.conductor.tokens.AppToken`):
                The application token to target?
            net_token (:class:`.conductor.tokens.NetToken`):
                The new network token to set?
            key (bytearray):
                Key required to perform operation.
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class`conductor.subject.DownlinkMessage`
        """
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_message('SetConfigMode',
                                                 timeout=timeout,
                                                 app_tok=bytearray(app_token),
                                                 net_tok=bytearray(net_token),
                                                 key=key)
        return self.send_message(pld, gateway_addr=gateway_addr,
                                 time_to_live_s=time_to_live_s,
                                 port=port, priority=priority)

    @classmethod
    def multicast_set_config_mode(cls, timeout, app_token, net_token, key,
                                  time_to_live_s, vers, gateways, port=0,
                                  priority=10):
        """ Requests that the AP enters Configuration Mode.

        Args:
            timeout (int):
                How many seconds the AP will stay in config mode.
            app_token (:class:`.conductor.tokens.AppToken`):
                The application token to target?
            net_token (:class:`.conductor.tokens.NetToken`):
                The new network token to set?
            key (bytearray):
                Key required to perform operation.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class`conductor.subject.DownlinkMessage`
        """
        pld = cls._get_spec(vers).build_message('SetConfigMode',
                                                timeout=timeout,
                                                app_tok=bytearray(app_token),
                                                net_tok=bytearray(net_token),
                                                key=key)
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)

    def set_ap_type(self, ap_type, gateway_addr=None, acked=True,
                    time_to_live_s=60.0, port=0, priority=10):
        """
        Sends a SET_AP_TYPE message

        Args:
            ap_type (int): AP type
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_ctrl_message("SET_AP_TYPE",
                                                      ap_type=ap_type)
        return self.send_message(pld, gateway_addr, acked, time_to_live_s,
                                 port, priority)

    @classmethod
    def multicast_set_ap_type(cls, ap_type, time_to_live_s, vers,
                              gateways, port=0, priority=10):
        """
        Sends a SET_AP_TYPE message

        Args:
            ap_type (int): AP type
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        pld = cls._get_spec(vers).build_ctrl_message("SET_AP_TYPE",
                                                     ap_type=ap_type)
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)

    def set_location_group(self, group, gateway_addr=None, acked=True,
                           time_to_live_s=60.0, port=0, priority=10):
        """
        Sends a SET_LOCATION_GROUP message

        Args:
            group (int): The location group.
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_ctrl_message("SET_LOCATION_GROUP",
                                                      loc_group=group)
        return self.send_message(pld, gateway_addr, acked, time_to_live_s,
                                 port, priority)

    @classmethod
    def multicast_set_location_group(cls, group, time_to_live_s, vers,
                                     gateways, port=0, priority=10):
        """
        Sends a SET_LOCATION_GROUP message

        Args:
            group (int): The location group.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        pld = cls._get_spec(vers).build_ctrl_message("SET_LOCATION_GROUP",
                                                     loc_group=group)
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)

    def set_location_weight(self, weight, gateway_addr=None, acked=True,
                            time_to_live_s=60.0, port=0, priority=10):
        """
        Sends a SET_LOCATION_WEIGHT message

        Args:
            weight (int): The Location Weight.
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_ctrl_message("SET_LOCATION_WEIGHT",
                                                      loc_weight=weight)
        return self.send_message(pld, gateway_addr, acked, time_to_live_s,
                                 port, priority)

    @classmethod
    def multicast_set_location_weight(cls, weight, time_to_live_s, vers,
                                      gateways, port=0, priority=10):
        """
        Sends a SET_LOCATION_WEIGHT message

        Args:
            weight (int): The Location Weight.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        pld = cls._get_spec(vers).build_ctrl_message("SET_LOCATION_WEIGHT",
                                                     loc_weight=weight)
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)

    def set_rssi_adj(self, offset, gateway_addr=None, acked=True,
                     time_to_live_s=60.0, port=0, priority=10):
        """
        Sends a SET_RSSI_ADJ message

        Args:
            offset (int): TX power adjustment offset.
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        # TODO: Data Validation?
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_ctrl_message("SET_RSSI_ADJ",
                                                      rss_adj=offset)
        return self.send_message(pld, gateway_addr, acked, time_to_live_s,
                                 port, priority)

    @classmethod
    def multicast_set_rssi_adj(cls, offset, time_to_live_s, vers, gateways,
                               port=0, priority=10):
        """
        Sends a SET_RSSI_ADJ message

        Args:
            offset (int): TX power adjustment offset.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        # TODO: Data Validation?
        pld = cls._get_spec(vers).build_ctrl_message("SET_RSSI_ADJ",
                                                     rss_adj=offset)
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)

    def set_adv_rate(self, rate, gateway_addr=None, acked=True,
                     time_to_live_s=60.0, port=0, priority=10):
        """
        Sends a SET_ADV_RATE message

        Args:
            rate (int): The Advertising Rate in ms.
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if (rate < 20) or (rate > 10000):
            raise ValueError(
                    'Advertising rate must be in the range 20-10000ms!')
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_ctrl_message("SET_ADV_RATE",
                                                      adv_rate=rate)
        return self.send_message(pld, gateway_addr, acked, time_to_live_s,
                                 port, priority)

    @classmethod
    def multicast_set_adv_rate(cls, rate, time_to_live_s, vers, gateways,
                               port=0, priority=10):
        """
        Sends a SET_ADV_RATE message

        Args:
            rate (int): The Advertising Rate in ms.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if (rate < 20) or (rate > 10000):
            raise ValueError(
                    'Advertising rate must be in the range 20-10000ms!')
        pld = cls._get_spec(vers).build_ctrl_message("SET_ADV_RATE",
                                                     adv_rate=rate)
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)

    def set_adv_refresh(self, interval, gateway_addr=None, acked=True,
                        time_to_live_s=60.0, port=0, priority=10):
        """
        Sends a SET_ADV_REFRESH message

        Args:
            interval (int): The Advertising Refresh Interval in ms.
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if (interval < 200) or (interval > 10000):
            raise ValueError('Advertising refresh interval must be in the '
                             'range of 200-10000ms!')
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_ctrl_message("SET_ADV_REFRESH",
                                                      adv_refresh=interval)
        return self.send_message(pld, gateway_addr, acked, time_to_live_s,
                                 port, priority)

    @classmethod
    def multicast_set_adv_refresh(cls, interval, time_to_live_s, vers,
                                  gateways, port=0, priority=10):
        """
        Sends a SET_ADV_REFRESH message

        Args:
            interval (int): The Advertising Refresh Interval in ms.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if (interval < 200) or (interval > 10000):
            raise ValueError('Advertising refresh interval must be in the '
                             'range of 200-10000ms!')
        pld = cls._get_spec(vers).build_ctrl_message("SET_ADV_REFRESH",
                                                     adv_refresh=interval)
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)

    def set_time_sync_rate(self, rate, gateway_addr=None, acked=True,
                           time_to_live_s=60.0, port=0, priority=10):
        """
        Sends a SET_TIME_SYNC_RATE message.

        Args:
            rate (int): The Time Sync Rate in seconds.
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if (rate < 5) or (rate > 86400):
            raise ValueError('Time sync rate must be in the range 5-86400s!')
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_ctrl_message("SET_TIME_SYNC_RATE",
                                                      sync_time_rate=rate)
        return self.send_message(pld, gateway_addr, acked, time_to_live_s,
                                 port, priority)

    @classmethod
    def multicast_set_time_sync_rate(cls, rate, time_to_live_s, vers,
                                     gateways, port=0, priority=10):
        """
        Sends a SET_TIME_SYNC_RATE message.

        Args:
            rate (int): The Time Sync Rate in seconds.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if (rate < 5) or (rate > 86400):
            raise ValueError('Time sync rate must be in the range 5-86400s!')
        pld = cls._get_spec(vers).build_ctrl_message("SET_TIME_SYNC_RATE",
                                                     sync_time_rate=rate)
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)

    def set_conn_timeout(self, interval, gateway_addr=None, acked=True,
                         time_to_live_s=60.0, port=0, priority=10):
        """
        Sends a SET_CONN_TIMEOUT message

        Args:
            interval (int): The Connection Timeout Interval in ms.
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if (interval < 500) or (interval > 300000):
            raise ValueError('Connection timeout interval must be in the range'
                             ' 500-300000ms!')
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_ctrl_message("SET_CONN_TIMEOUT",
                                                      conn_timeout=interval)
        return self.send_message(pld, gateway_addr, acked, time_to_live_s,
                                 port, priority)

    @classmethod
    def multicast_set_conn_timeout(cls, interval, time_to_live_s, vers,
                                   gateways, port=0, priority=10):
        """
        Sends a SET_CONN_TIMEOUT message

        Args:
            interval (int): The Connection Timeout Interval in ms.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if (interval < 500) or (interval > 300000):
            raise ValueError('Connection timeout interval must be in the range'
                             ' 500-300000ms!')
        pld = cls._get_spec(vers).build_ctrl_message("SET_CONN_TIMEOUT",
                                                     conn_timeout=interval)
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)

    def set_status_rate(self, rate, gateway_addr=None, acked=True,
                        time_to_live_s=60.0, port=0, priority=10):
        """
        Sends a SET_STATUS_RATE message

        Args:
            rate (int): The Status Message Rate in seconds.
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if (rate < 60) or (rate > 86400):
            raise ValueError('Status message interval must be in the range'
                             ' 60-86400s!')
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_ctrl_message("SET_STATUS_RATE",
                                                      status_rate=rate)
        return self.send_message(pld, gateway_addr, acked, time_to_live_s,
                                 port, priority)

    @classmethod
    def multicast_set_status_rate(cls, rate, time_to_live_s, vers, gateways,
                                  port=0, priority=10):
        """
        Sends a SET_STATUS_RATE message

        Args:
            rate (int): The Status Message Rate in seconds.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if (rate < 60) or (rate > 86400):
            raise ValueError('Status message interval must be in the range'
                             ' 60-86400s!')
        pld = cls._get_spec(vers).build_ctrl_message("SET_STATUS_RATE",
                                                     status_rate=rate)
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)

    def set_mailbox_rate(self, rate, gateway_addr=None, acked=True,
                         time_to_live_s=60.0, port=0, priority=10):
        """
        Sends a SET_MAILBOX_RATE message

        Args:
            rate: int
                The Mailbox Check Rate in seconds.
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if (rate < 60) or (rate > 86400):
            raise ValueError('Mailbox check rate must be in the range'
                             ' 60-86400s!')
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_ctrl_message("SET_MAILBOX_RATE",
                                                      mailbox_int=rate)
        return self.send_message(pld, gateway_addr, acked, time_to_live_s,
                                 port, priority)

    @classmethod
    def multicast_set_mailbox_rate(cls, rate, time_to_live_s, vers, gateways,
                                   port=0, priority=10):
        """
        Sends a SET_MAILBOX_RATE message

        Args:
            rate: int
                The Mailbox Check Rate in seconds.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if (rate < 60) or (rate > 86400):
            raise ValueError('Mailbox check rate must be in the range'
                             ' 60-86400s!')
        pld = cls._get_spec(vers).build_ctrl_message("SET_MAILBOX_RATE",
                                                     mailbox_int=rate)
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)

    def set_queue_send_rate(self, rate, gateway_addr=None, acked=True,
                            time_to_live_s=60.0, port=0, priority=10):
        """
        Sends a SET_QUEUE_SEND_RATE message

        Args:
            rate (int): The Queue Send Rate in ms.
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if (rate < 5000) or (rate > 1800000):
            raise ValueError('Queue send rate must be in the range '
                             '10000-1800000s!')
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_ctrl_message("SET_QUEUE_SEND_RATE",
                                                      send_rate=rate)
        return self.send_message(pld, gateway_addr, acked, time_to_live_s,
                                 port, priority)

    @classmethod
    def multicast_set_queue_send_rate(cls, rate, time_to_live_s, vers,
                                      gateways, port=0, priority=10):
        """
        Sends a SET_QUEUE_SEND_RATE message

        Args:
            rate (int): The Queue Send Rate in ms.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if (rate < 5000) or (rate > 1800000):
            raise ValueError('Queue send rate must be in the range '
                             '10000-1800000s!')
        pld = cls._get_spec(vers).build_ctrl_message("SET_QUEUE_SEND_RATE",
                                                     send_rate=rate)
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)

    def set_queue_threshold(self, thresh, gateway_addr=None, acked=True,
                            time_to_live_s=60.0, port=0, priority=10):
        """
        Sends a SET_QUEUE_THRESH message

        Args:
            thresh (int): The Queue Send Threshold.
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if thresh > 100:
            raise ValueError('Queue threshold cannot be > 100%!')
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_ctrl_message("SET_QUEUE_THRESH",
                                                      send_threshold=thresh)
        return self.send_message(pld, gateway_addr, acked, time_to_live_s,
                                 port, priority)

    @classmethod
    def multicast_set_queue_threshold(cls, thresh, time_to_live_s, vers,
                                      gateways, port=0, priority=10):
        """
        Sends a SET_QUEUE_THRESH message

        Args:
            thresh (int): The Queue Send Threshold.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if thresh > 100:
            raise ValueError('Queue threshold cannot be > 100%!')
        pld = cls._get_spec(vers).build_ctrl_message("SET_QUEUE_THRESH",
                                                     send_threshold=thresh)
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)

    def set_enable_ble(self, enable, gateway_addr=None, acked=True,
                       time_to_live_s=60.0, port=0, priority=10):
        """
        Sends a SET_ENABLE_BLE message

        Args:
            enable (bool): Enable BLE?
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_ctrl_message("SET_ENABLE_BLE",
                                                      enable=enable)
        return self.send_message(pld, gateway_addr, acked, time_to_live_s,
                                 port, priority)

    @classmethod
    def multicast_set_enable_ble(cls, enable, time_to_live_s, vers, gateways,
                                 port=0, priority=10):
        """
        Sends a SET_ENABLE_BLE message

        Args:
            enable (bool): Enable BLE?
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        pld = cls._get_spec(vers).build_ctrl_message("SET_ENABLE_BLE",
                                                     enable=enable)
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)

    def request_status(self, gateway_addr=None, acked=True,
                       time_to_live_s=60.0, port=0, priority=10):
        """
        Sends a GET_STATUS message

        Args:
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_ctrl_message("GET_STATUS")
        return self.send_message(pld, gateway_addr, acked, time_to_live_s,
                                 port, priority)

    @classmethod
    def multicast_request_status(cls, time_to_live_s, vers, gateways,
                                 port=0, priority=10):
        """
        Sends a GET_STATUS message

        Args:
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        pld = cls._get_spec(vers).build_ctrl_message("GET_STATUS")
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)

    def enable_location(self, enable, gateway_addr=None, acked=True,
                        time_to_live_s=60.0, port=0, priority=10):
        """
        Sends a SET_ENABLE_LOCATION message

        Args:
            enable (bool): Enable AP Location Flag?
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if type(enable) != bool:
            raise TypeError('enable must be True or False')
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_ctrl_message("SET_ENABLE_LOCATION",
                                                      enable=enable)
        return self.send_message(pld, gateway_addr, acked, time_to_live_s,
                                 port, priority)

    @classmethod
    def multicast_enable_location(cls, enable, time_to_live_s, vers, gateways,
                                  port=0, priority=10):
        """
        Sends a SET_ENABLE_LOCATION message

        Args:
            enable (bool): Enable AP Location Flag?
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if type(enable) != bool:
            raise TypeError('enable must be True or False')
        pld = cls._get_spec(vers).build_ctrl_message("SET_ENABLE_LOCATION",
                                                     enable=enable)
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)

    def set_ack_mode(self, mode, gateway_addr=None, acked=True,
                     time_to_live_s=60.0, port=0, priority=10):
        """
        Sends a SET_ACK_MODE message

        Args:
            mode (:class`.AckMode`): The ACK mode.
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if not AckMode.has_value(mode):
            raise ValueError('{} is not a valid ACK mode'.format(mode))
        ack_mode = AckMode(mode)
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_ctrl_message("SET_ACK_MODE",
                                                      mode=ack_mode)
        return self.send_message(pld, gateway_addr, acked, time_to_live_s,
                                 port, priority)

    @classmethod
    def multicast_set_ack_mode(cls, mode, time_to_live_s, vers, gateways,
                               port=0, priority=10):
        """
        Sends a SET_ACK_MODE message

        Args:
            mode (:class`.AckMode`): The ACK mode.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if not AckMode.has_value(mode):
            raise ValueError('{} is not a valid ACK mode'.format(mode))
        ack_mode = AckMode(mode)
        pld = cls._get_spec(vers).build_ctrl_message("SET_ACK_MODE",
                                                     mode=ack_mode)
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)

    def set_tx_power(self, power, gateway_addr=None, acked=True,
                     time_to_live_s=60.0, port=0, priority=10):
        """
        Sends a SET_TX_POWER message

        Args:
            power (int): The TX power level
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        # TODO: Add parameter checking
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_ctrl_message("SET_TX_POWER",
                                                      tx_pwr=power)
        return self.send_message(pld, gateway_addr, acked, time_to_live_s,
                                 port, priority)

    @classmethod
    def multicast_set_tx_power(cls, power, time_to_live_s, vers, gateways,
                               port=0, priority=10):
        """
        Sends a SET_TX_POWER message

        Args:
            power (int): The TX power level
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        # TODO: Add parameter checking
        pld = cls._get_spec(vers).build_ctrl_message("SET_TX_POWER",
                                                     tx_pwr=power)
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)

    def trigger_assert(self, gateway_addr=None, acked=True, time_to_live_s=60,
                       port=0, priority=10):
        """
        Triggers an assert in the AP

        Args:
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_ctrl_message("TRIGGER_ASSERT")
        return self.send_message(pld, gateway_addr, acked, time_to_live_s,
                                 port, priority)

    @classmethod
    def multicast_trigger_assert(cls, time_to_live_s, vers, gateways,
                                 port=0, priority=10):
        """
        Triggers an assert in the AP

        Args:
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        pld = cls._get_spec(vers).build_ctrl_message("TRIGGER_ASSERT")
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)


class NordicAccessPoint(AccessPoint):

    ###########################################################################
    # Nordic Access Point Properties.
    ###########################################################################

    application = 'c47e949cc0428bdac390'

    @property
    def msg_spec_version(self):
        """ Message Spec Version of the AP """
        major = self._md.get('msgSpecVersionMajor')
        minor = self._md.get('msgSpecVersionMinor')
        tag = self._md.get('msgSpecVersionTag')
        if not major or not minor or not tag:
            return Version(2, 0, 0)
        return Version(int(major), int(minor), int(tag))

    ###########################################################################
    # Configuration Methods.
    ###########################################################################

    def send_configuration_query(self, gateway_addr=None,
                                 time_to_live_s=60.0, port=0, priority=10):
        """ Sends a message targeted at the SymBLE endnode to the AP.

        Args:
            uuid (bytearray):
                A Universally Unique Id, to prevent the symble endnodes from
                recieving the same message more than once.
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class`conductor.subject.DownlinkMessage`

        """
        # TODO: Not unit-tested.
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_message('ConfigurationQuery',
                                                 uuid=uuid4().fields[0])
        return self.send_message(pld, gateway_addr=gateway_addr,
                                 time_to_live_s=time_to_live_s,
                                 port=port, priority=priority)

    @classmethod
    def mulicast_configuration_query(cls, time_to_live_s, vers,
                                     gateways, port=0, priority=10):
        """ Sends a message targeted at the SymBLE endnode to the AP.

        Args:
            uuid (bytearray):
                A Universally Unique Id, to prevent the symble endnodes from
                recieving the same message more than once.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class`conductor.subject.DownlinkMessage`

        """
        # TODO: Not unit-tested.
        pld = cls._get_spec(vers).build_message('ConfigurationQuery',
                                                uuid=uuid4().fields[0])
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)

    def config_ble_front_end(self, enable, antenna, gateway_addr=None,
                             acked=True, time_to_live_s=60.0, port=0,
                             priority=10):
        """
        Sends a CONFIG_BLE_FRONT_END message

        Args:
            enable (bool): True if front-end is to be enabled.
            antenna (:type`.AntennaPort`): Antenna port setting
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        val = 0x01 if enable else 0x00
        val += 0x02 if antenna == AntennaPort.ANT_B else 0x00
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_ctrl_message("CONFIG_BLE_FRONT_END",
                                                      config=val)
        return self.send_message(pld, gateway_addr, acked, time_to_live_s,
                                 port, priority)

    @classmethod
    def multicast_config_ble_front_end(cls, enable, antenna, time_to_live_s,
                                       vers, gateways, port=0, priority=10):
        """
        Sends a CONFIG_BLE_FRONT_END message

        Args:
            enable (bool): True if front-end is to be enabled.
            antenna (:type`.AntennaPort`): Antenna port setting
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.


            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        val = 0x01 if enable else 0x00
        val += 0x02 if antenna == AntennaPort.ANT_B else 0x00
        pld = cls._get_spec(vers).build_ctrl_message("CONFIG_BLE_FRONT_END",
                                                     config=val)
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)

    def sample_batt(self, gateway_addr=None, acked=True, time_to_live_s=60.0,
                    port=0, priority=10):
        """
        Sends a SAMPLE_BATT message

        Args:
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_ctrl_message("SAMPLE_BATT")
        return self.send_message(pld, gateway_addr, acked, time_to_live_s,
                                 port, priority)

    @classmethod
    def multicast_sample_batt(cls, time_to_live_s, vers, gateways,
                              port=0, priority=10):
        """
        Sends a SAMPLE_BATT message

        Args:
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.


            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        pld = cls._get_spec(vers).build_ctrl_message("SAMPLE_BATT")
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)

    def sync_duty_cycle(self, duty_cycle, gateway_addr=None, acked=True,
                        time_to_live_s=60.0, port=0, priority=10):
        """
        Sends a SET_SYNC_DC message

        Args:
            duty_cycle (int): The Sync Advertisement Duty Cycle.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if duty_cycle > 3:
            raise ValueError('Sync duty cycle cannot be > 3 (10/100)!')
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_ctrl_message("SET_DUTY_CYCLE",
                                                      window=duty_cycle)
        return self.send_message(pld, gateway_addr, acked, time_to_live_s,
                                 port, priority)

    @classmethod
    def multicast_sync_duty_cycle(cls, duty_cycle, time_to_live_s, vers,
                                  gateways, port=0, priority=10):
        """
        Sends a SET_SYNC_DC message

        Args:
            duty_cycle (int): The Sync Advertisement Duty Cycle.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.


            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if duty_cycle > 3:
            raise ValueError('Sync duty cycle cannot be > 3 (10/100)!')
        pld = cls._get_spec(vers).build_ctrl_message("SET_DUTY_CYCLE",
                                                     window=duty_cycle)
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)

    def set_min_gw_rssi(self, rssi, gateway_addr=None, acked=True,
                        time_to_live_s=60.0, port=0, priority=10):
        """
        Sends a SET_SYM_GW_RSSI message

        Args:
            rssi (int): The minimum RSSI to connnect to a Gateway.
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if rssi < -121 or rssi > -40:
            raise ValueError('RSSI must be within -121 and -40!')
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_ctrl_message("SET_SYM_GW_RSSI",
                                                      rssi=rssi)
        return self.send_message(pld, gateway_addr, acked, time_to_live_s,
                                 port, priority)

    @classmethod
    def multicast_set_min_gw_rssi(cls, rssi, time_to_live_s, vers,
                                  gateways, port=0, priority=10):
        """
        Sends a SET_SYM_GW_RSSI message

        Args:
            rssi (int): The minimum RSSI to connnect to a Gateway.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if rssi < -121 or rssi > -40:
            raise ValueError('RSSI must be within -121 and -40!')
        pld = cls._get_spec(vers).build_ctrl_message("SET_SYM_GW_RSSI",
                                                     rssi=rssi)
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)

    def set_scan_mode(self, scan_mode, gateway_addr=None, acked=True,
                      time_to_live_s=60.0, port=0, priority=10):
        """
        Sends a SET_SYM_SCAN_MODE message

        Args:
            scan_mode (int): The ScanMode of the Module.
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if not ScanMode.has_value(scan_mode):
            raise ValueError('Scan mode must be in ScanMode Enum!')
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_ctrl_message("SET_SYM_SCAN_MODE",
                                                      mode=scan_mode)
        return self.send_message(pld, gateway_addr, acked, time_to_live_s,
                                 port, priority)

    @classmethod
    def multicast_set_scan_mode(cls, scan_mode, time_to_live_s, vers,
                                gateways, port=0, priority=10):
        """
        Sends a SET_SYM_SCAN_MODE message

        Args:
            scan_mode (int): The ScanMode of the Module.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if not ScanMode.has_value(scan_mode):
            raise ValueError('Scan mode must be in ScanMode Enum!')
        pld = cls._get_spec(vers).build_ctrl_message("SET_SYM_SCAN_MODE",
                                                     mode=scan_mode)
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)

    def set_max_scan_attempts(self, attempts, gateway_addr=None, acked=True,
                              time_to_live_s=60.0, port=0, priority=10):
        """
        Sends a SET_SYM_SCAN_ATTEMPTS message

        Args:
            attempts (int): The maximum amount of scan attempts.
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if attempts < 2 or attempts > 10:
            raise ValueError('Scan attempts must be between 2 and 10!')
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_ctrl_message("SET_SYM_SCAN_ATTEMPTS",
                                                      attempts=attempts)
        return self.send_message(pld, gateway_addr, acked, time_to_live_s,
                                 port, priority)

    @classmethod
    def mulicast_set_max_scan_attempts(cls, attempts, time_to_live_s, vers,
                                       gateways, port=0, priority=10):
        """
        Sends a SET_SYM_SCAN_ATTEMPTS message

        Args:
            attempts (int): The maximum amount of scan attempts.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.


            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if attempts < 2 or attempts > 10:
            raise ValueError('Scan attempts must be between 2 and 10!')
        pld = cls._get_spec(vers).build_ctrl_message("SET_SYM_SCAN_ATTEMPTS",
                                                     attempts=attempts)
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)

    def set_hop_interval(self, interval, gateway_addr=None, acked=True,
                         time_to_live_s=60.0, port=0, priority=10):
        """
        Sends a SET_SYM_HOP_INT message

        Args:
            interval (int): The interval to connect to a new gateway.
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if interval < 600 or interval > 1382400:
            raise ValueError('Hop Interval must range from 600 - 1382400'
                             ' seconds (16 days)!')
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_ctrl_message("SET_SYM_HOP_INT",
                                                      interval=interval)
        return self.send_message(pld, gateway_addr, acked, time_to_live_s,
                                 port, priority)

    @classmethod
    def multicast_set_hop_interval(cls, interval, time_to_live_s, vers,
                                   gateways, port=0, priority=10):
        """
        Sends a SET_SYM_HOP_INT message

        Args:
            interval (int): The interval to connect to a new gateway.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if interval < 600 or interval > 1382400:
            raise ValueError('Hop Interval must range from 600 - 1382400'
                             ' seconds (16 days)!')
        pld = cls._get_spec(vers).build_ctrl_message("SET_SYM_HOP_INT",
                                                     interval=interval)
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)

    def set_max_gw_errors(self, errors, gateway_addr=None, acked=True,
                          time_to_live_s=60.0, port=0, priority=10):
        """
        Sends a SET_MAX_GW_ERROR message

        Args:
            errors (int): The maxmimum amount of errors the AP will accept
                before switching gateways.
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if errors < 2 or errors > 50:
            raise ValueError('Error must be from (2-50)!')
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_ctrl_message("SET_MAX_GW_ERROR",
                                                      max_err=errors)
        return self.send_message(pld, gateway_addr, acked, time_to_live_s,
                                 port, priority)

    @classmethod
    def multicast_set_max_gw_errors(cls, errors, time_to_live_s, vers,
                                    gateways, port=0, priority=10):
        """
        Sends a SET_MAX_GW_ERROR message

        Args:
            errors (int): The maxmimum amount of errors the AP will accept
                before switching gateways.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        if errors < 2 or errors > 50:
            raise ValueError('Error must be from (2-50)!')
        pld = cls._get_spec(vers).build_ctrl_message("SET_MAX_GW_ERROR",
                                                     max_err=errors)
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)

    def set_network_token(self, net_tok, gateway_addr=None, acked=True,
                          time_to_live_s=60.0, port=0, priority=10):
        """ Sets the Network Token of the Access Point.

        Args:
            net_tok(int): The network token that the AccessPoint should have.
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_ctrl_message("SET_NET_TOKEN",
                                                      net_tok=net_tok)
        return self.send_message(pld, gateway_addr, acked, time_to_live_s,
                                 port, priority)

    @classmethod
    def multicast_set_network_token(cls, net_tok, time_to_live_s, vers,
                                    gateways, port=0, priority=10):
        """ Sets the Network Token of many Access Points.

        Args:
            net_tok(int): The network token that the AccessPoint should have.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        pld = cls._get_spec(vers).build_ctrl_message("SET_NET_TOKEN",
                                                     net_tok=net_tok)
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)

    def set_dl_band(self, edge_lower, edge_upper, edge_guard, edge_ch_step,
                    edge_ch_offset, gateway_addr=None, acked=True,
                    time_to_live_s=60.0, port=0, priority=10):
        """
        Sets the Downlink Link Band Configuration for the Symphony Link Module.

        Args:
            edge_lower (int): band edge lower frequency.
            edge_upper (int): band edge upper frequency.
            edge_guard (int): band edge guard.
            step_size (int): channel step size.
            step_offset: (int) channel step offset.
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_ctrl_message(
                "SET_DL_BAND", band_edge_lower=edge_lower,
                band_edge_upper=edge_upper,
                band_edge_guard=edge_guard,
                band_edge_ch_step=edge_ch_step,
                band_edge_ch_offset=edge_ch_offset)
        return self.send_message(pld, gateway_addr, acked, time_to_live_s,
                                 port, priority)

    @classmethod
    def multicast_set_dl_band(cls, edge_lower, edge_upper, edge_guard,
                              edge_ch_step, edge_ch_offset, time_to_live_s,
                              vers, gateways, port=0, priority=10):
        """
        Sets the Downlink Link Band Configuration for the Symphony Link Module.

        Args:
            edge_lower (int): band edge lower frequency.
            edge_upper (int): band edge upper frequency.
            edge_guard (int): band edge guard.
            step_size (int): channel step size.
            step_offset: (int) channel step offset.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        pld = cls._get_spec(vers).build_ctrl_message(
                "SET_DL_BAND", band_edge_lower=edge_lower,
                band_edge_upper=edge_upper,
                band_edge_guard=edge_guard,
                band_edge_ch_step=edge_ch_step,
                band_edge_ch_offset=edge_ch_offset)
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)

    def set_ds_network_token(self, net_tok, gateway_addr=None, acked=True,
                             time_to_live_s=60.0, port=0, priority=10):
        """
        Sets the SymBLE Network Token that SymBLE Endnodes see when
        connecting to an Access Point.

        Args:
            net_tok(int): The downstream network token.
            gateway_addr (str or :class`.Gateway`): [Optional] Will only route
                the DownlinkMessage through the given gateway address when
                supplied. Defaults to `None` to send through all possible
                routes.
            acked (bool): [Optional] Determines whether the AccessPoint will
                return an acknowledgement upon recieving the DownlinkMessage.
                Defaults to True.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_ctrl_message("SET_DS_NET_TOKEN",
                                                      net_tok=net_tok)
        return self.send_message(pld, gateway_addr, acked, time_to_live_s,
                                 port, priority)

    @classmethod
    def multicast_set_ds_network_token(cls, net_tok, time_to_live_s, vers,
                                       gateways, port=0, priority=10):
        """
        Sets the SymBLE Network Token that SymBLE Endnodes see when
        connecting to an Access Point.

        Args:
            net_tok(int): The downstream network token.
            time_to_live_s (int): [Optional] The number of seconds that the
                AccessPoint has to check its mailbox before the message becomes
                `expired` and will no longer be valid to send to the
                AccessPoint. Defaults to 60 seconds, one minute.
            vers (:clas:`.Version`): The AP message spec version of the
                message to build.
            gateways (list): The list of :class:`.Gateway` objects that
                should recieve the multicast message.
            port (int): [Optional] The Symphony Link port to send the
                DownlinkMessage on. Defaults to 0.
            priority (int): [Optional] The Symphony Link priority of the
                message. Higher priority messages will be sent before lower
                priority messages when multiple are queued. Default is 10.

        Returns:
            :class:`conductor.subject.DownlinkMessage`
        """
        pld = cls._get_spec(vers).build_ctrl_message("SET_DS_NET_TOKEN",
                                                     net_tok=net_tok)
        return cls._issue_multicast(cls, pld, time_to_live_s, vers, gateways)


class RPiAccessPoint(AccessPoint):
    """ Represents the legacy Raspberry Pi Access Point. """
    application = "8da02bc5df23f5b9017b"

    @classmethod
    def _get_spec(cls, vers):
        raise NotImplementedError
