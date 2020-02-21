# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class Asuphoenix(KaitaiStruct):
    """:field src_ssid_raw_ssid_mask: ax25_frame.ax25_header.src_ssid_raw.ssid_mask
    :field pid: ax25_frame.payload.pid
    :field obc_disk_space_used_mb: ax25_frame.payload.ax25_info.healthbeacon_ascii.obc_disk_space_used_mb
    :field ants_deployed: ax25_frame.payload.ax25_info.healthbeacon_ascii.ants_deployed
    :field callsign: ax25_frame.ax25_header.dest_callsign_raw.callsign_ror.callsign
    :field current_5v_flt: ax25_frame.payload.ax25_info.healthbeacon_ascii.current_5v_flt
    :field total_obc_resets: ax25_frame.payload.ax25_info.healthbeacon_ascii.total_obc_resets
    :field brownouts: ax25_frame.payload.ax25_info.healthbeacon_ascii.brownouts
    :field current_bat_volt_flt: ax25_frame.payload.ax25_info.healthbeacon_ascii.current_bat_volt_flt
    :field src_ssid_raw_ssid: ax25_frame.ax25_header.src_ssid_raw.ssid
    :field eps_temp: ax25_frame.payload.ax25_info.healthbeacon_ascii.eps_temp
    :field bat_temp: ax25_frame.payload.ax25_info.healthbeacon_ascii.bat_temp
    :field comms_idx_int: ax25_frame.payload.ax25_info.healthbeacon_ascii.comms_idx_int
    :field eps_charge_volt_bat_flt: ax25_frame.payload.ax25_info.healthbeacon_ascii.eps_charge_volt_bat_flt
    :field ax100_rssi: ax25_frame.payload.ax25_info.healthbeacon_ascii.ax100_rssi
    :field obc_clock: ax25_frame.payload.ax25_info.healthbeacon_ascii.obc_clock
    :field gpio_state: ax25_frame.payload.ax25_info.healthbeacon_ascii.gpio_state
    :field ssid_mask: ax25_frame.ax25_header.dest_ssid_raw.ssid_mask
    :field ax100_board_temp: ax25_frame.payload.ax25_info.healthbeacon_ascii.ax100_board_temp
    :field ctl: ax25_frame.ax25_header.ctl
    :field eps_charge_current_bat: ax25_frame.payload.ax25_info.healthbeacon_ascii.eps_charge_current_bat
    :field ssid: ax25_frame.ax25_header.dest_ssid_raw.ssid
    :field current_3v3_flt: ax25_frame.payload.ax25_info.healthbeacon_ascii.current_3v3_flt
    :field magic: ax25_frame.payload.ax25_info.magic
    :field gps_sats_used: ax25_frame.payload.ax25_info.healthbeacon_ascii.gps_sats_used
    :field current_adcs_flt: ax25_frame.payload.ax25_info.healthbeacon_ascii.current_adcs_flt
    :field beacon_type_magic: ax25_frame.payload.ax25_info.healthbeacon_ascii.beacon_type_magic
    :field src_callsign_raw_callsign: ax25_frame.ax25_header.src_callsign_raw.callsign_ror.callsign
    
    
    Attention: `rpt_callsign` cannot be accessed because `rpt_instance` is an
    array of unknown size at the beginning of the parsing process! Left an
    example in here.
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.ax25_frame = self._root.Ax25Frame(self._io, self, self._root)

    class Ax25Frame(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ax25_header = self._root.Ax25Header(self._io, self, self._root)
            _on = (self.ax25_header.ctl & 19)
            if _on == 0:
                self.payload = self._root.IFrame(self._io, self, self._root)
            elif _on == 3:
                self.payload = self._root.UiFrame(self._io, self, self._root)
            elif _on == 19:
                self.payload = self._root.UiFrame(self._io, self, self._root)
            elif _on == 16:
                self.payload = self._root.IFrame(self._io, self, self._root)
            elif _on == 18:
                self.payload = self._root.IFrame(self._io, self, self._root)
            elif _on == 2:
                self.payload = self._root.IFrame(self._io, self, self._root)


    class Ax25Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.dest_callsign_raw = self._root.CallsignRaw(self._io, self, self._root)
            self.dest_ssid_raw = self._root.SsidMask(self._io, self, self._root)
            self.src_callsign_raw = self._root.CallsignRaw(self._io, self, self._root)
            self.src_ssid_raw = self._root.SsidMask(self._io, self, self._root)
            self.ctl = self._io.read_u1()


    class UiFrame(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.pid = self._io.read_u1()
            self._raw_ax25_info = self._io.read_bytes_full()
            io = KaitaiStream(BytesIO(self._raw_ax25_info))
            self.ax25_info = self._root.Ax25InfoData(io, self, self._root)


    class Callsign(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.callsign = (self._io.read_bytes(6)).decode(u"ASCII")


    class HealthBeaconT(KaitaiStruct):
        """http://phxcubesat.asu.edu/content/amateur-operations."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.beacon_type_magic = self._io.ensure_fixed_contents(b"\x68\x6B\x3A")
            self.int_comms_idx_str = (self._io.read_bytes_term(44, False, True, True)).decode(u"utf-8")
            self.total_obc_resets_str = (self._io.read_bytes_term(44, False, True, True)).decode(u"utf-8")
            self.current_bat_volt_int_str = (self._io.read_bytes_term(46, False, True, True)).decode(u"utf-8")
            self.current_bat_volt_frac_str = (self._io.read_bytes_term(44, False, True, True)).decode(u"utf-8")
            self.obc_disk_space_used_int_str = (self._io.read_bytes_term(46, False, True, True)).decode(u"utf-8")
            self.obc_disk_space_used_frac_str = (self._io.read_bytes_term(44, False, True, True)).decode(u"utf-8")
            self.obc_clock_str = (self._io.read_bytes_term(44, False, True, True)).decode(u"utf-8")
            self.current_3v3_int_str = (self._io.read_bytes_term(46, False, True, True)).decode(u"utf-8")
            self.current_3v3_frac_str = (self._io.read_bytes_term(44, False, True, True)).decode(u"utf-8")
            self.current_5v_int_str = (self._io.read_bytes_term(46, False, True, True)).decode(u"utf-8")
            self.current_5v_frac_str = (self._io.read_bytes_term(44, False, True, True)).decode(u"utf-8")
            self.current_adcs_int_str = (self._io.read_bytes_term(46, False, True, True)).decode(u"utf-8")
            self.current_adcs_frac_str = (self._io.read_bytes_term(44, False, True, True)).decode(u"utf-8")
            self.eps_charge_volt_bat_int_str = (self._io.read_bytes_term(46, False, True, True)).decode(u"utf-8")
            self.eps_charge_volt_bat_frac_str = (self._io.read_bytes_term(44, False, True, True)).decode(u"utf-8")
            self.eps_charge_current_bat_str = (self._io.read_bytes_term(44, False, True, True)).decode(u"utf-8")
            self.eps_temp_str = (self._io.read_bytes_term(44, False, True, True)).decode(u"utf-8")
            self.bat_temp_str = (self._io.read_bytes_term(44, False, True, True)).decode(u"utf-8")
            self.brownouts_str = (self._io.read_bytes_term(44, False, True, True)).decode(u"utf-8")
            self.ax100_rssi_str = (self._io.read_bytes_term(44, False, True, True)).decode(u"utf-8")
            self.ax100_board_temp_str = (self._io.read_bytes_term(44, False, True, True)).decode(u"utf-8")
            self.gps_sats_used_str = (self._io.read_bytes_term(44, False, True, True)).decode(u"utf-8")
            self.ants_deployed_str = (self._io.read_bytes_term(44, False, True, True)).decode(u"utf-8")
            self.gpio_state_str = (self._io.read_bytes(1)).decode(u"utf-8")

        @property
        def obc_clock(self):
            if hasattr(self, '_m_obc_clock'):
                return self._m_obc_clock if hasattr(self, '_m_obc_clock') else None

            self._m_obc_clock = int(self.obc_clock_str)
            return self._m_obc_clock if hasattr(self, '_m_obc_clock') else None

        @property
        def ax100_board_temp(self):
            if hasattr(self, '_m_ax100_board_temp'):
                return self._m_ax100_board_temp if hasattr(self, '_m_ax100_board_temp') else None

            self._m_ax100_board_temp = int(self.ax100_board_temp_str)
            return self._m_ax100_board_temp if hasattr(self, '_m_ax100_board_temp') else None

        @property
        def total_obc_resets(self):
            if hasattr(self, '_m_total_obc_resets'):
                return self._m_total_obc_resets if hasattr(self, '_m_total_obc_resets') else None

            self._m_total_obc_resets = int(self.total_obc_resets_str)
            return self._m_total_obc_resets if hasattr(self, '_m_total_obc_resets') else None

        @property
        def gps_sats_used(self):
            if hasattr(self, '_m_gps_sats_used'):
                return self._m_gps_sats_used if hasattr(self, '_m_gps_sats_used') else None

            self._m_gps_sats_used = int(self.gps_sats_used_str)
            return self._m_gps_sats_used if hasattr(self, '_m_gps_sats_used') else None

        @property
        def ax100_rssi(self):
            if hasattr(self, '_m_ax100_rssi'):
                return self._m_ax100_rssi if hasattr(self, '_m_ax100_rssi') else None

            self._m_ax100_rssi = int(self.ax100_rssi_str)
            return self._m_ax100_rssi if hasattr(self, '_m_ax100_rssi') else None

        @property
        def current_5v_flt(self):
            if hasattr(self, '_m_current_5v_flt'):
                return self._m_current_5v_flt if hasattr(self, '_m_current_5v_flt') else None

            self._m_current_5v_flt = (int(self.current_5v_int_str) + ((((int(int(self.current_5v_int_str) < 0) * -2) + 1) * int(self.current_5v_frac_str)) / 1000.0))
            return self._m_current_5v_flt if hasattr(self, '_m_current_5v_flt') else None

        @property
        def ants_deployed(self):
            if hasattr(self, '_m_ants_deployed'):
                return self._m_ants_deployed if hasattr(self, '_m_ants_deployed') else None

            self._m_ants_deployed = int(self.ants_deployed_str)
            return self._m_ants_deployed if hasattr(self, '_m_ants_deployed') else None

        @property
        def eps_temp(self):
            if hasattr(self, '_m_eps_temp'):
                return self._m_eps_temp if hasattr(self, '_m_eps_temp') else None

            self._m_eps_temp = int(self.eps_temp_str)
            return self._m_eps_temp if hasattr(self, '_m_eps_temp') else None

        @property
        def current_adcs_flt(self):
            if hasattr(self, '_m_current_adcs_flt'):
                return self._m_current_adcs_flt if hasattr(self, '_m_current_adcs_flt') else None

            self._m_current_adcs_flt = (int(self.current_adcs_int_str) + ((((int(int(self.current_adcs_int_str) < 0) * -2) + 1) * int(self.current_adcs_frac_str)) / 1000.0))
            return self._m_current_adcs_flt if hasattr(self, '_m_current_adcs_flt') else None

        @property
        def bat_temp(self):
            if hasattr(self, '_m_bat_temp'):
                return self._m_bat_temp if hasattr(self, '_m_bat_temp') else None

            self._m_bat_temp = int(self.bat_temp_str)
            return self._m_bat_temp if hasattr(self, '_m_bat_temp') else None

        @property
        def comms_idx_int(self):
            if hasattr(self, '_m_comms_idx_int'):
                return self._m_comms_idx_int if hasattr(self, '_m_comms_idx_int') else None

            self._m_comms_idx_int = int(self.int_comms_idx_str)
            return self._m_comms_idx_int if hasattr(self, '_m_comms_idx_int') else None

        @property
        def current_3v3_flt(self):
            if hasattr(self, '_m_current_3v3_flt'):
                return self._m_current_3v3_flt if hasattr(self, '_m_current_3v3_flt') else None

            self._m_current_3v3_flt = (int(self.current_3v3_int_str) + ((((int(int(self.current_3v3_int_str) < 0) * -2) + 1) * int(self.current_3v3_frac_str)) / 1000.0))
            return self._m_current_3v3_flt if hasattr(self, '_m_current_3v3_flt') else None

        @property
        def obc_disk_space_used_mb(self):
            if hasattr(self, '_m_obc_disk_space_used_mb'):
                return self._m_obc_disk_space_used_mb if hasattr(self, '_m_obc_disk_space_used_mb') else None

            self._m_obc_disk_space_used_mb = (int(self.obc_disk_space_used_int_str) + ((((int(int(self.obc_disk_space_used_int_str) < 0) * -2) + 1) * int(self.obc_disk_space_used_frac_str)) / 10.0))
            return self._m_obc_disk_space_used_mb if hasattr(self, '_m_obc_disk_space_used_mb') else None

        @property
        def gpio_state(self):
            if hasattr(self, '_m_gpio_state'):
                return self._m_gpio_state if hasattr(self, '_m_gpio_state') else None

            self._m_gpio_state = int(self.gpio_state_str)
            return self._m_gpio_state if hasattr(self, '_m_gpio_state') else None

        @property
        def current_bat_volt_flt(self):
            if hasattr(self, '_m_current_bat_volt_flt'):
                return self._m_current_bat_volt_flt if hasattr(self, '_m_current_bat_volt_flt') else None

            self._m_current_bat_volt_flt = (int(self.current_bat_volt_int_str) + ((((int(int(self.current_bat_volt_int_str) < 0) * -2) + 1) * int(self.current_bat_volt_frac_str)) / 100.0))
            return self._m_current_bat_volt_flt if hasattr(self, '_m_current_bat_volt_flt') else None

        @property
        def eps_charge_current_bat(self):
            if hasattr(self, '_m_eps_charge_current_bat'):
                return self._m_eps_charge_current_bat if hasattr(self, '_m_eps_charge_current_bat') else None

            self._m_eps_charge_current_bat = int(self.eps_charge_current_bat_str)
            return self._m_eps_charge_current_bat if hasattr(self, '_m_eps_charge_current_bat') else None

        @property
        def brownouts(self):
            if hasattr(self, '_m_brownouts'):
                return self._m_brownouts if hasattr(self, '_m_brownouts') else None

            self._m_brownouts = int(self.brownouts_str)
            return self._m_brownouts if hasattr(self, '_m_brownouts') else None

        @property
        def eps_charge_volt_bat_flt(self):
            if hasattr(self, '_m_eps_charge_volt_bat_flt'):
                return self._m_eps_charge_volt_bat_flt if hasattr(self, '_m_eps_charge_volt_bat_flt') else None

            self._m_eps_charge_volt_bat_flt = (int(self.eps_charge_volt_bat_int_str) + ((((int(int(self.eps_charge_volt_bat_int_str) < 0) * -2) + 1) * int(self.eps_charge_volt_bat_frac_str)) / 100.0))
            return self._m_eps_charge_volt_bat_flt if hasattr(self, '_m_eps_charge_volt_bat_flt') else None


    class IFrame(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.pid = self._io.read_u1()
            self._raw_ax25_info = self._io.read_bytes_full()
            io = KaitaiStream(BytesIO(self._raw_ax25_info))
            self.ax25_info = self._root.Ax25InfoData(io, self, self._root)


    class SsidMask(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ssid_mask = self._io.read_u1()

        @property
        def ssid(self):
            if hasattr(self, '_m_ssid'):
                return self._m_ssid if hasattr(self, '_m_ssid') else None

            self._m_ssid = ((self.ssid_mask & 15) >> 1)
            return self._m_ssid if hasattr(self, '_m_ssid') else None


    class Repeaters(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.rpt_callsign_raw = self._root.CallsignRaw(self._io, self, self._root)
            self.rpt_ssid_raw = self._root.SsidMask(self._io, self, self._root)


    class Repeater(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.rpt_instance = []
            i = 0
            while True:
                _ = self._root.Repeaters(self._io, self, self._root)
                self.rpt_instance.append(_)
                if (_.rpt_ssid_raw.ssid_mask & 1) == 1:
                    break
                i += 1


    class CallsignRaw(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_callsign_ror = self._io.read_bytes(6)
            self._raw_callsign_ror = KaitaiStream.process_rotate_left(self._raw__raw_callsign_ror, 8 - (0), 1)
            io = KaitaiStream(BytesIO(self._raw_callsign_ror))
            self.callsign_ror = self._root.Callsign(io, self, self._root)


    class Ax25InfoData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(4)
            self.healthbeacon_ascii = self._root.HealthBeaconT(self._io, self, self._root)



