""" A base for airfinder classes. """
import logging
import struct

from collections import namedtuple
from copy import deepcopy
from datetime import datetime, timedelta

from conductor.event_count import EventCount
from conductor.devices.gateway import Gateway
from conductor.devices.module import ModuleUplinkMessage, \
                                     LTEmModuleUplinkMessage
from conductor.tokens import AppToken, NetToken
from conductor.util import get_device_type, DeviceType
from conductor.subject import UplinkSubject, DownlinkSubject, UplinkMessage

LOG = logging.getLogger(__name__)


class AirfinderUplinkMessage(UplinkMessage):
    """ An intuitive wrapper to the metadata properties
    expected for Airfinder Uplink Messages."""

    SignalData = namedtuple('SignalData', ['rssi'])

    @property
    def _md(self):
        """ Full metadata for the uplink message. """
        return self._data.get('metadata').get('props')

    @property
    def signal_data(self):
        vals = self._data.get('value').get('avgSignalMetadata')
        if vals and 'rssi' in vals:
            return self.SignalData(int(vals.get('rssi')))
        return None

    @property
    def source_message(self):
        uuid = self._md.get('sourceMessageId')
        time = self._md.get('sourceMessageTimestamp')
        url = '{}/data/uplinkPayload/event/{}/{}'.format(self.client_edge_url,
                                                         uuid, time)
        data = self._get(url)
        node_type = get_device_type(self._data.get('value').get('module'))
        if node_type == DeviceType.Module:
            return ModuleUplinkMessage(self.session, data.get('uuid'),
                                       self.instance, data)
        elif node_type == DeviceType.LTEmModule:
            return LTEmModuleUplinkMessage(self.session, data.get('uuid'),
                                           self.instance, data)
        else:
            return TypeError(node_type)

    @property
    def gateway(self):
        vals = self._data.get('value')
        return Gateway(self.session, vals.get('gateway'), self.instance)

    @property
    def application_token(self):
        return AppToken(self.session, self._md.get('app_tok'),
                        self.instance)

    @property
    def network_token(self):
        return NetToken(self.session, self._md.get('net_tok'),
                        self.instance)


class InvalidDownlinkMessageType(Exception):
    """ Attempted to build a message type that is not supported. """
    pass


class MissingDownlinkArgument(Exception):
    """ Attempted to build a message with an unkown argument. """
    pass


class ControlMessageNotSupported(Exception):
    """ Attempted to build a control message with an unknown command. """
    pass


class DownlinkMessageSpec():
    """ Base Class for Message Specification Implementations. """

    # Will be compiled in the beggining of every message.
    header = {
        'def': ['msg_type'],  # named_tuple, defining fields.
        'struct': '>B'        # struct, defining field data types.
    }

    msg_types = None  # All Supported Downlink Message Types.
#   Example Definition...
#   {
#           # Name of the Downlink Message in the index that correlates
#           # with its msg type value.
#           'NONE': {
#               'type': None,      # The message type value.
#               'def': None,       # named_tuple, defining fields.
#               'struct': None,    # struct, defining field data types.
#               'defaults': None,  # The default values for the def.
#           }
#   }

    control_types = None

    def __init__(self):
        # Always make deep copies of the message data for inheritance.
        if self.header:
            self.header = deepcopy(self.header)
            for x in ['def', 'defaults']:
                if self.header.get(x):
                    self.header[x] = deepcopy(self.header[x])
        if self.msg_types:
            self.msg_types = deepcopy(self.msg_types)
            for x in ['def', 'defaults']:
                if self.msg_types.get(x):
                    self.msg_types[x] = deepcopy(self.msg_types[x])
        if self.control_types:
            self.control_types = deepcopy(self.control_types)
            for x in ['def', 'defaults']:
                if self.control_types.get(x):
                    self.control_types[x] = deepcopy(self.control_types[x])

    def _build_header(self, msg_type, **kwargs):
        """ Builds the header of the message.

        Args:
            msg_type (string): The name, in the message type struct, that
                should be built.
            msg_len (int): The total size of the method, will be placed into
                the header if there is a field that requires it.
            kwargs: Any other header values will come from the keyword args.

        Returns:
            bytearray - The compiled header.
        """
        hdr_definition = self.header.get('def')
        hdr_structure = self.header.get('struct')
        hdr_defaults = self.header.get('defaults')

        if not hdr_structure or not hdr_definition:
            return bytearray()  # No Header Definition.

        # Allocate Buffer based on specifications.
        hdr_len = struct.calcsize(hdr_structure)
        buff = bytearray(b'\x00' * hdr_len)

        w_list = []
        for i in range(len(hdr_definition)):
            key = hdr_definition[i]
            val = kwargs.get(key)

            if val is None:
                if key == 'msg_type':
                    # Use type field when avalible.
                    if 'type' in self.msg_types[msg_type]:
                        val = self.msg_types[msg_type]['type']
                    else:
                        # Default to the index of the message, otherwise.
                        val = list(self.msg_types.keys()).index(msg_type)+1
                elif hdr_defaults:
                    val = hdr_defaults[i]
                    LOG.debug("{}: {} [DEFAULT]".format(key, val))
                else:
                    raise ValueError("Missing Value ", key)
            else:
                LOG.debug("{}: {} [SPECIFIED]".format(key, val))

            w_list.append(val)
        # LOG.debug("Writing Header: {} into {}".format(w_list, hdr_structure))
        struct.pack_into(hdr_structure, buff, 0, *w_list)
        # LOG.debug("Header:".format(buff))
        return buff

    def _build_body(self, msg_type, msg_struct, **kwargs):
        """ Builds the body of the control message.

        Args:
            msg_type (string): The message type from the message definitions
                to build.
            msg_struct (string): Allows the build message method to redefine
                the message structure to accomidate variable length data.
            kwargs: All other keyword args for the message definition.

        Returns:
            payload (bytearray): Compiled message.
        """
        msg_definition = self.msg_types[msg_type].get('def')
        msg_defaults = self.msg_types[msg_type].get('defaults')
        msg_len = struct.calcsize(msg_struct)

        # Allocate new buffer to append the header.
        buff = bytearray(b'\x00' * msg_len)
        w_list = []  # Bytes, in order, to write into struct.

        # The value that will be reported when an error occurs.
        mask = None
        mask_idx = None
        if 'mask' in msg_definition and 'mask' not in kwargs:
            LOG.debug("Calculating Change Mask...")
            mask_idx = msg_definition.index('mask')
            mask = list('0'*(struct.calcsize(msg_struct[mask_idx+1])*8))
            LOG.debug("Mask IDX: {} Size: {}".format(mask_idx, len(mask)))

        # Iterate through each field of the message.
        for i in range(len(msg_definition)):
            key = msg_definition[i]
            val = kwargs.get(key)

            if val is None:  # When a value is not specified...
                if key == 'mask':
                    # Placeholder for calculated mask in w_list at mask_idx
                    val = None
                elif key == 'data':
                    continue  # Don't write null data.
                elif msg_defaults:
                    # Use default value for unspecified field.
                    val = msg_defaults[i]
                    LOG.debug("{}: {} [DEFAULT]".format(key, val))
                    if mask:  # Exclude field from change mask.
                        LOG.debug("Clearing Mask Bit for {}: idx {}..."
                                  .format(key, i-1))
                        mask[i-1] = '0'
                        LOG.debug(''.join(mask))
                        LOG.debug((' '*(i-1))+'^')
                else:
                    # No default fallback for missing field.
                    raise MissingDownlinkArgument(key)
            else:
                LOG.debug("{}: {} [SPECIFIED]".format(key, val))
                if mask:  # Include field in change mask.
                    LOG.debug("Setting Mask Bit for {}: idx {}..."
                              .format(key, i-1))
                    mask[i-1] = '1'
                    LOG.debug(''.join(mask))
                    LOG.debug((' '*(i-1))+'^')

            # Add value to the list of bytes to write.
            w_list.append(val)

        if mask:  # Build and insert Change Mask.
            mask.reverse()  # Mask is written LSB to MSB.
            w_list[mask_idx] = int(''.join(mask), 2)
            LOG.debug("Generated Mask {} @ idx {}".format(''.join(mask),
                                                          mask_idx))

        # LOG.debug("Writing: {} into {}".format(w_list, msg_struct))
        struct.pack_into(msg_struct, buff, 0, *w_list)
        # LOG.debug("Body: {}".format(buff))
        return buff

    def build_message(self, msg_type, **kwargs):
        """ Constructs a Downlink Message based on the definition.

        Args:
            msg_type (int):
                The message type of the message to construct.
            kwargs:
                Must be equal to the definitions given in the message type.

        Returns:
            payload (bytearray): The constructed message.

        Raises:
            :class:`.InvalidDownlinkArgument`:
                Could not find the referenced keywork argument.
            :class:`.InvalidDownlinkMessageType`:
                Message Type was not defined.
        """
        LOG.debug("Building {}: {}".format(msg_type, kwargs))
        if not self.msg_types:
            raise InvalidDownlinkMessageType("No Message Types Avalaible")

        # Validate Input
        if msg_type not in self.msg_types:
            raise InvalidDownlinkMessageType(msg_type)

        msg_definition = self.msg_types[msg_type].get('def')
        msg_struct = self.msg_types[msg_type].get('struct')
        msg_len = 0

        if msg_definition:
            # Calculate Variable Length Elements when nessisary.
            if 'data' in msg_definition:
                if 'data' in kwargs:
                    data = kwargs.get('data')
                    if data:
                        # Write size of data.
                        msg_struct = msg_struct.format(len(data))
                    else:
                        # Remove Data Element.
                        msg_struct = msg_struct.replace('{}s', '')
                    LOG.debug("updated struct: {}".format(msg_struct))
                else:
                    raise MissingDownlinkArgument('data')
            msg_len = struct.calcsize(msg_struct)

        # Build Header
        buff = self._build_header(msg_type, msg_len=msg_len, **kwargs)

        if not msg_definition or not msg_struct:
            return buff  # Nothing more to build...

        # Build Message Body
        buff.extend(self._build_body(msg_type, msg_struct, **kwargs))
        LOG.debug("Message: {}".format(buff))
        return buff

    def build_ctrl_message(self, ctrl_cmd, **kwargs):
        """ Builds a control message.

        Args:
            ctrl_cmd (string): The control message from the control types.
            kwargs: keyword arguments to build into the ctrl message.

        Returns:
            payload (bytearray): The constructed control message.
        """
        if not self.control_types or 'Control' not in self.msg_types:
            raise Exception("No Control Types Defined!")

        ctrl_msg = self.control_types.get(ctrl_cmd)
        if not ctrl_msg:
            raise ControlMessageNotSupported()

        ctrl_def = ctrl_msg.get('def')
        ctrl_struct = ctrl_msg.get('struct')
        cmd = ctrl_msg.get('type')
        buff = None

        if ctrl_def and ctrl_struct:
            ctrl_len = struct.calcsize(ctrl_struct)
            buff = bytearray(b'\x00' * ctrl_len)
            w_list = []

            # Build Control Message
            for i in range(len(ctrl_def)):
                key = ctrl_def[i]
                val = kwargs.get(key)

                if val is None:
                    raise MissingDownlinkArgument(key)
                else:
                    LOG.debug("{}: {} [SPECIFIED]".format(key, val))

                w_list.append(val)
                LOG.debug(w_list)

            LOG.debug("Writing: {} into {}".format(w_list, ctrl_struct))
            struct.pack_into(ctrl_struct, buff, 0, *w_list)

        return self.build_message('Control', ctrl_cmd=cmd, data=buff)


class AirfinderUplinkSubject(UplinkSubject):
    """ Airfinder Uplink Subject with built-in multicast capabilities. """

    @classmethod
    def get_all_messages_time_range(self, start, stop=None):
        """ """
        pass

    @classmethod
    def get_all_recent_messages(self, mins_back):
        """ Gets the messages received in the last `mins_back` minutes. """
        now = datetime.utcnow()
        td_mb = timedelta(minutes=mins_back)
        return self.get_all_messages_time_range(now - td_mb)

    @classmethod
    def get_all_last_messages(self, count=1):
        """ Gets the last message the :class:`.ConductorSubject` uplinked, up
        to the count number of messages.

        Args:
            count (int): How many messages to receive.

        Returns:
            List of the last uplink messages for the
            :class:`.ConductorSubject`.
        """
        base_url = '{}/data/{}/ctionnode/{}/mostRecentEvents' \
                   .format(self.client_edge_url, self.uplink_type,
                           self.subject_id)
        params = {"maxResults": count}
        messages = [self._get_msg_obj(self.session, m.get('uuid'),
                                      self.instance, m)
                    for m in self._get(base_url, params=params)['results']]
        return sorted(messages, key=lambda m: m.receive_time)

    @classmethod
    def _app_addr(self):
        """ Returns:
            Converts the 'application' property of the AirfinderSubject to a
            Conductor-Friendly format to issue commands.
        """
        if not self.application:
            return None
        return '$401${}-{}-{}-{:0>9}'.format(self.application[:8],
                                             self.application[8:16],
                                             0, self.application[16:])


class AirfinderSubject(AirfinderUplinkSubject, DownlinkSubject, EventCount):
    """ Base class for Airfinder objects, not intended to be used directly. """
    msgObj = AirfinderUplinkMessage
    application = ''

    def _get_registered_af_asset(self, subject_name, subject_id):
        """ Base function for getting a registered asset from the Airfinder
        Network Asset API.

        Args:
            subject_name (str): The coresponding name of the asset class.
            subject_id (str): The asset ID.

        Raises:
            FailedAPICallException: When a failure occurs.

        Returns:
            A list of registered asset from the Airfinder Network Asset API.
        """
        return self._get('{}/{}/{}'.format(self._af_network_asset_url,
                                           subject_name, subject_id))

    def _get_registered_af_assets(self, subject_name):
        """ Base function for getting list of registered assets from the
        Airfinder Network Asset API.

        Args:
            subject_name (str): The coresponding name of the asset class.

        Raises:
            FailedAPICallException: When a failure occurs.

        Returns:
            A list of registered assets (json) from the Airfinder Network
            Asset API.
        """
        url = '{}/{}'.format(self._af_network_asset_url, subject_name)
        params = {'accountId': self.account_id, 'lifecycle': 'registered'}
        return self._get(url, params)

    @property
    def _af_network_asset_url(self):
        """ Returns:
            Instance-based, Client Edge URL for Airfinder.
        """
        return ''.join([self.network_asset_url, '/airfinder'])

    @property
    def _af_client_edge_url(self):
        """ Returns:
            Instance-based, Client Edge URL for Airfinder.
        """
        return ''.join([self.client_edge_url, '/airfinder'])

    @property
    def name(self):
        """ Returns:
            The user issued name of the Subject.
        """
        return self._data.get('value')

    @property
    def subject_type(self):
        """ Returns:
            The type of subject.
        """
        val = self._data.get('type')
        return val

    def __repr__(self):
        return '{}({}: {})'.format(self.__class__.__name__, self.name, self)


class AirfinderAppToken(AppToken):

    def _build_symble_multicast_payload(self, msg_spec_version):
        pass
