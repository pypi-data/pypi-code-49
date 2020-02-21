# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class Duchifat3(KaitaiStruct):
    """:field dest_callsign: ax25_frame.ax25_header.dest_callsign_raw.callsign_ror.callsign
    :field src_callsign: ax25_frame.ax25_header.src_callsign_raw.callsign_ror.callsign
    :field src_ssid: ax25_frame.ax25_header.src_ssid_raw.ssid
    :field dest_ssid: ax25_frame.ax25_header.dest_ssid_raw.ssid
    :field rpt_callsign: ax25_frame.ax25_header.repeater.rpt_instance[0].rpt_callsign_raw.callsign_ror.callsign
    :field ctl: ax25_frame.ax25_header.ctl
    :field pid: ax25_frame.payload.pid
    :field type: ax25_frame.payload.ax25_info.type
    :field subtype: ax25_frame.payload.ax25_info.subtype
    :field length: ax25_frame.payload.ax25_info.length
    :field time_unix: ax25_frame.payload.ax25_info.time_unix
    :field vbatt: ax25_frame.payload.ax25_info.data.vbatt
    :field batt_current: ax25_frame.payload.ax25_info.data.batt_current
    :field current3v3: ax25_frame.payload.ax25_info.data.current3v3
    :field current5v: ax25_frame.payload.ax25_info.data.current5v
    :field lo_trxvu_temp: ax25_frame.payload.ax25_info.data.lo_trxvu_temp
    :field pa_trxvu_temp: ax25_frame.payload.ax25_info.data.pa_trxvu_temp
    :field temp_eps_0: ax25_frame.payload.ax25_info.data.temp_eps_0
    :field temp_eps_1: ax25_frame.payload.ax25_info.data.temp_eps_1
    :field temp_eps_2: ax25_frame.payload.ax25_info.data.temp_eps_2
    :field temp_eps_3: ax25_frame.payload.ax25_info.data.temp_eps_3
    :field temp_batt_0: ax25_frame.payload.ax25_info.data.temp_batt_0
    :field temp_batt_1: ax25_frame.payload.ax25_info.data.temp_batt_1
    :field rx_doppler: ax25_frame.payload.ax25_info.data.rx_doppler
    :field rx_rssi: ax25_frame.payload.ax25_info.data.rx_rssi
    :field tx_refl: ax25_frame.payload.ax25_info.data.tx_refl
    :field tx_forw: ax25_frame.payload.ax25_info.data.tx_forw
    :field empty_0: ax25_frame.payload.ax25_info.data.empty_0
    :field empty_1: ax25_frame.payload.ax25_info.data.empty_1
    :field empty_2: ax25_frame.payload.ax25_info.data.empty_2
    :field file_system_last_error: ax25_frame.payload.ax25_info.data.file_system_last_error
    :field empty_3: ax25_frame.payload.ax25_info.data.empty_3
    :field number_of_delayed_commands: ax25_frame.payload.ax25_info.data.number_of_delayed_commands
    :field number_of_resets: ax25_frame.payload.ax25_info.data.number_of_resets
    :field last_resets: ax25_frame.payload.ax25_info.data.last_resets
    :field flags: ax25_frame.payload.ax25_info.data.flags
    
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
            if (self.src_ssid_raw.ssid_mask & 1) == 0:
                self.repeater = self._root.Repeater(self._io, self, self._root)

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


    class Duchifat3BeaconData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.vbatt = self._io.read_u2be()
            self.batt_current = self._io.read_u2be()
            self.current3v3 = self._io.read_u2be()
            self.current5v = self._io.read_u2be()
            self.lo_trxvu_temp = self._io.read_u2be()
            self.pa_trxvu_temp = self._io.read_u2be()
            self.temp_eps_0 = self._io.read_s2be()
            self.temp_eps_1 = self._io.read_s2be()
            self.temp_eps_2 = self._io.read_s2be()
            self.temp_eps_3 = self._io.read_s2be()
            self.temp_batt_0 = self._io.read_s2be()
            self.temp_batt_1 = self._io.read_s2be()
            self.rx_doppler = self._io.read_u2be()
            self.rx_rssi = self._io.read_u2be()
            self.tx_refl = self._io.read_u2be()
            self.tx_forw = self._io.read_u2be()
            self.empty_0 = self._io.read_s2be()
            self.empty_1 = self._io.read_s2be()
            self.empty_2 = self._io.read_s2be()
            self.file_system_last_error = self._io.read_u1()
            self.empty_3 = self._io.read_u1()
            self.number_of_delayed_commands = self._io.read_u1()
            self.number_of_resets = self._io.read_u4be()
            self.last_resets = self._io.read_u4be()
            self.flags = self._io.read_u1()


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
            self._raw_callsign_ror = KaitaiStream.process_rotate_left(self._raw__raw_callsign_ror, 8 - (1), 1)
            io = KaitaiStream(BytesIO(self._raw_callsign_ror))
            self.callsign_ror = self._root.Callsign(io, self, self._root)


    class Ax25InfoData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.type = self._io.read_u1()
            self.subtype = self._io.read_u1()
            self.length = self._io.read_u2be()
            self.time_unix = self._io.read_u4be()
            _on = self.type
            if _on == 3:
                self.data = self._root.Duchifat3BeaconData(self._io, self, self._root)



