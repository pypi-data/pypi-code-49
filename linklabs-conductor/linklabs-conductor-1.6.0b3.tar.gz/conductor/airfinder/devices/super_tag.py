""" Represents a Supertag and its functionality. """

from conductor.airfinder.base import DownlinkMessageSpec
from conductor.airfinder.devices.tag import Tag


class SupertagDownlinkMessageSpecV1(DownlinkMessageSpec):
    """ Supertag Message Specification v1.0.0. """

    header = {
        'def': ['msg_type', 'msg_spec_vers'],
        'struct': '>BB',
        'defaults': [0x00, 0x01]
    }

    msg_types = {
        'Configuration': {
            'def': ['mask', 'heartbeat', 'no_ap_heartbeat', 'no_sym_heartbeat',
                    'loc_upd', 'no_ap_loc_upd', 'no_sym_loc_upd',
                    'scans_per_fix', 'max_wifi_aps', 'max_cell_ids',
                    'loc_upd_order', 'net_lost_timeout', 'ref_lost_timeout',
                    'net_scan_int'],
            'struct': '>HIIIIIIBBBBHHH',
            'defaults': [0x0000, 0x0000003c, 0x00015180, 0x00015180,
                         0x0000000b, 0x00005460, 0x00005460, 0x04,
                         0x0a, 0x00, 0x1b, 0x0258, 0x0258, 0x00b4]
        }
    }


class SupertagDownlinkMessageSpecV2(SupertagDownlinkMessageSpecV1):
    """ Supertag Message Specification v2.0.0"""

    def __init__(self):
        super().__init__()

        # Update Message Spec Version.
        self.header.update({'defaults': [0x00, 0x02]})

        # Update Configuration Message.
        #   - Increase Change Mask Size
        #   - Added Help Mode fields
        #   - Added Accelerometer fields
        #   - Added Caching fields
        #   - Added GPS Power Settings
        self.msg_types['Configuration'].update({
            'def': ['mask', 'heartbeat', 'no_ap_heartbeat', 'no_sym_heartbeat',
                    'loc_upd', 'no_ap_loc_upd', 'no_sym_loc_upd',
                    'help_loc_upd', 'scans_per_fix', 'max_wifi_aps',
                    'max_cell_ids', 'loc_upd_order', 'acc_en', 'acc_dur',
                    'acc_thresh', 'shock_thresh', 'cache_en', 'cache_len',
                    'gps_pwr_mode', 'gps_timeout', 'net_lost_timeout',
                    'ref_lost_timeout', 'net_scan_int'],
            'struct': '>IIIIIIIIBBBBBHHHBBBHHHH',
            'defaults': [0x00000000, 0x0000003c, 0x00015180, 0x00015180,
                         0x0000000b, 0x0000003c, 0x00005460, 0x0000000b, 0x04,
                         0x0a, 0x00, 0x1b, 0x01, 0x0003, 0x0050, 0x00a0, 0x00,
                         0x00, 0x00, 0x00b4, 0x0258, 0x0258, 0x00b4]
        })

        # Add new Message Types
        #   - Test Mode Enable
        #   - Help Mode Ack
        self.msg_types.update({
            'EnableTestMode': {},
            'Ack': {
                'def': ['help_rxed'],
                'struct': '>H',
                'defaults': [0x1105]
            }
        })


class SercommDownlinkMessageSpecV1(SupertagDownlinkMessageSpecV2):
    """ Sercomm Message Spec V1.5.0. """

    def __init__(self):
        super().__init__()

        # Update Message Spec Version
        self.header.update({'defaults': [0x00, 0x01]})

        # Remove Ack from Message Spec.
        self.msg_types.pop('Ack')

        # Update new message types
        #   - Update Configuration
        #       + Removed Shock Threshold
        #       + Added Sym Retries
        #       + Added Network Token
        #   - Added Battery Consumption Window
        #   - Added Setting Diagnostic Mode
        #   - Added Requesting Consumption
        #   - Added Setting Throttling
        #   - Added FTP Information
        self.msg_types.update({
            'Configuration': {
                'def': ['mask', 'heartbeat', 'no_ap_heartbeat',
                        'no_sym_heartbeat', 'loc_upd', 'no_ap_loc_upd',
                        'no_sym_loc_upd', 'help_loc_upd', 'scans_per_fix',
                        'max_wifi_aps', 'max_cell_ids', 'loc_upd_order',
                        'acc_en', 'acc_dur', 'acc_thresh', 'cache_en',
                        'cache_len', 'gps_pwr_mode', 'gps_timeout',
                        'net_lost_timeout', 'ref_lost_timeout', 'net_scan_int',
                        'sym_retries', 'net_tok'],
                'struct': '>IIIIIIIIBBBBBHHBBBHHHHBI',
                'defaults': [0x00000000, 0x0000003c, 0x00015180, 0x00015180,
                             0x0000000b, 0x0000003c, 0x00005460, 0x0000000b,
                             0x04, 0x0a, 0x00, 0x1b, 0x01, 0x0003, 0x0050,
                             0x00, 0x00, 0x00, 0x00b4, 0x0258, 0x0258, 0x00b4,
                             0x05, 0x4f50454e]

            },
            'BattConsumptionWindow': {
                'def': ['mask', 'batt_cap', 'start_up_pwr', 'alive_time_pwr',
                        'loc_upd_pwr', 'net_scan_pwr', 'ble_conn_pwr',
                        'lte_success_pwr', 'lte_failed_pwr', 'gps_avg_pwr',
                        'wifi_avg_pwr', 'temp_read_pwr', 'batt_read_pwr',
                        'led_pwr', 'ftp_pwr'],
                'struct': '>IIIIHHHIIIIHHII',
                'defaults': [0x00000000, 0x00000000, 0x00000000, 0x00000000,
                             0x0000, 0x0000, 0x0000, 0x00000000, 0x00000000,
                             0x00000000, 0x00000000, 0x0000, 0x0000,
                             0x00000000, 0x00000000]
            },
            'SetDiagnosticMode': {
                'def': ['enable'],
                'struct': '>B',
                'defaults': [0x00]
            },
            'ConsumptionRequest': {},
            'SetThrottling': {
                'def': ['mask', 'enable', 'mode', 'win_len', 'min_batt',
                        'win_limit', 'batt_cap'],
                'struct': '>HBBIIBI',
                'defaults': [0x00, 0x00, 0x01, 0x0000001e, 0x00011940, 0x5a,
                             0x01010100]
            },
            'FtpAvailable': {
                'def': ['app_vers_major', 'app_vers_minor', 'app_vers_tag',
                        'modem_vers_major', 'modem_vers_minor',
                        'modem_vers_tag'],
                'struct': '>BBHBBH',
                'defaults': [0x00, 0x00, 0x0000, 0x00, 0x00, 0x0000]
            }
        })


class SercommDownlinkMessageSpecV2(SupertagDownlinkMessageSpecV1):
    """ Sercomm Message Spec V2.0.0. """

    def __init__(self):
        super().__init__()

        # Update Message Spec Version
        self.header.update({'defaults': [0x00, 0x02]})

        # Update new message types
        #   - Update Configuration
        #       + Added Transition Base Update
        #       + Added Transition Increasing Int En
        #   - Added CoAP Server Downlink
        #   - Update Battery Consumption
        #       + Shipping Mode Power
        #       + PSM Sleep Power
        #       
        self.msg_types.update({

        })


class Supertag(Tag):
    """ """
    application = "20028716136f69533e19"
    virtual_ap_app = "91fd9564b752338eac77"

    @classmethod
    def _get_spec(cls, vers):
        if vers.major == 1:
            return SupertagDownlinkMessageSpecV1()
        elif vers.major == 2:
            return SupertagDownlinkMessageSpecV2()
        else:
            raise Exception("No Supported Message Specification.")

    def configure(self, time_to_live_s=60.0, access_point=None, **kwargs):
        """ TODO: docs
            'batt_cap', 'start_up_pwr', 'alive_time_pwr',
            'loc_upd_pwr', 'net_scan_pwr', 'ble_conn_pwr',
            'lte_success_pwr', 'lte_failed_pwr', 'gps_avg_pwr',
            'wifi_avg_pwr', 'temp_read_pwr', 'batt_read_pwr',
            'led_pwr', 'ftp_pwr'
        """
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_message("Configuration", **kwargs)
        return self._send_message(pld, time_to_live_s)

    @classmethod
    def multicast_configure(cls, vers, gws, time_to_live_s=60.0,
                            access_point=None, ap_vers=None,  **kwargs):
        pld = cls._get_spec(vers).build_message("Configuration", **kwargs)
        return cls._send_multicast_message(pld, time_to_live_s, ap_vers, gws)

    def ack(self, time_to_live_s=60.0, access_point=None):
        """ TODO """
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_message("Ack")
        return self._send_message(pld, time_to_live_s)

    @classmethod
    def multicast_ack(cls, vers, gws, time_to_live_s=60.0, access_point=None,
                      ap_vers=None):
        """ TODO """
        pld = cls._get_spec(vers).build_message("Ack")
        return cls._send_message(pld, time_to_live_s)

    def activate_test_mode(self, time_to_live_s=60.0, access_point=None):
        """ TODO """
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_message("EnableTestMode")
        return self._send_message(pld, time_to_live_s)

    @classmethod
    def multicast_activate_test_mode(cls, time_to_live_s=60.0,
                                     access_point=None, ap_vers=None):
        """ TODO """
        pld = cls.get_spec().build_message("EnableTestMode")
        return cls._send_message(pld, time_to_live_s)


class SercommSupertag(Supertag):
    """ """
    application = "d29b3be8f2cc9a1a7051"

    @classmethod
    def _get_spec(cls, vers):
        if vers.major == 1:
            return SercommDownlinkMessageSpecV1()
        else:
            raise Exception("No Supported Message Specification.")

    def set_batt_window(self, time_to_live_s=60.0, access_point=None,
                        **kwargs):
        """ TODO """
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_message("BattConsumptionWindow",
                                                 **kwargs)
        return self._send_message(pld, time_to_live_s)

    @classmethod
    def multicast_set_batt_window(cls, vers, gws, time_to_live_s=60.0,
                                  access_point=None, ap_vers=None,
                                  **kwargs):
        """ TODO """
        pld = cls._get_spec(vers).build_message("BattConsumptionWindow",
                                                **kwargs)
        return cls._send_multicast_message(pld, time_to_live_s, ap_vers, gws)

    def set_diag_mode(self, en, time_to_live_s=60.0, access_point=None):
        """ TODO """
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_message("SetDiagnosticMode",
                                                 enable=en)
        return self._send_message(pld, time_to_live_s)

    @classmethod
    def multicast_set_diag_mode(cls, en, vers, gws, time_to_live_s=60.0,
                                access_point=None, ap_vers=None):
        """ TODO """
        pld = cls._get_spec(vers).build_message("SetDiagnosticMode", enable=en)
        return cls._send_multicast_message(pld, time_to_live_s, ap_vers, gws)

    def req_batt_consumption(self, time_to_live_s=60.0, access_point=None):
        """ TODO: docs
        kwargs:
            'batt_cap', 'start_up_pwr', 'alive_time_pwr',
            'loc_upd_pwr', 'net_scan_pwr', 'ble_conn_pwr',
            'lte_success_pwr', 'lte_failed_pwr', 'gps_avg_pwr',
            'wifi_avg_pwr', 'temp_read_pwr', 'batt_read_pwr',
            'led_pwr', 'ftp_pwr'
        """
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_message("ConsumptionRequest")
        return self._send_message(pld, time_to_live_s)

    @classmethod
    def multicast_req_batt_consumption(cls, vers, gws, time_to_live_s=60.0,
                                       access_point=None, ap_vers=None):
        """ TODO """
        pld = cls._get_spec(vers).build_message("ConsumptionRequest")
        return cls._send_multicast_message(pld, time_to_live_s, ap_vers, gws)

    def set_throttling(self, time_to_live_s=60.0, access_point=None,
                       ap_vers=None, **kwargs):
        """ TODO: docs
        kwargs:
            'enable', 'mode', 'win_len', 'min_batt',
            'win_limit', 'batt_cap'
        """
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_message("SetThrottling", **kwargs)
        return self._send_message(pld, time_to_live_s)

    @classmethod
    def multicast_set_throttling(cls, vers, gws, time_to_live_s=60.0,
                                 access_point=None, ap_vers=None, **kwargs):
        """ TODO  """
        pld = cls._get_spec(vers).build_message("SetThrottling", **kwargs)
        return cls._send_multicast_message(pld, time_to_live_s, ap_vers, gws)

    def ftp_notify(self, time_to_live_s=60.0, access_point=None, **kwargs):
        """ TODO: docs
        kwargs:
            'app_vers_major', 'app_vers_minor', 'app_vers_tag',
            'modem_vers_major', 'modem_vers_minor',
            'modem_vers_tag'
        """
        vers = self.msg_spec_version
        pld = self._get_spec(vers).build_message("FtpAvailable", **kwargs)
        return self._send_message(pld, time_to_live_s)

    @classmethod
    def multicast_ftp_notify(cls, vers, gws, time_to_live_s=60.0,
                             access_point=None, ap_vers=None, **kwargs):
        """ TODO """
        pld = cls._get_spec(vers).build_message("FtpAvailable", **kwargs)
        return cls._send_multicast_message(pld, time_to_live_s, ap_vers, gws)

    def ack(self, time_to_live_s=60.0, access_point=None):
        """ TODO """
        raise NotImplementedError

    @classmethod
    def multicast_ack(cls, vers, gws, time_to_live_s=60.0, access_point=None,
                      ap_vers=None):
        """ TODO """
        raise NotImplementedError
