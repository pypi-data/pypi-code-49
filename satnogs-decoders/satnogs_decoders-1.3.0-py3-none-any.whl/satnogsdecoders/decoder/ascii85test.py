# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO
import satnogsdecoders.process


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class Ascii85test(KaitaiStruct):
    """:field encoded: textstring.b85encstring.encoded
    :field decoded: b85string.b85decstring.decoded
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self._raw_textstring = self._io.read_bytes_term(10, False, True, True)
        io = KaitaiStream(BytesIO(self._raw_textstring))
        self.textstring = self._root.B85enc(io, self, self._root)
        self._raw_b85string = self._io.read_bytes_term(10, False, True, True)
        io = KaitaiStream(BytesIO(self._raw_b85string))
        self.b85string = self._root.B85dec(io, self, self._root)

    class B85enc(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_b85encstring = self._io.read_bytes_full()
            _process = satnogsdecoders.process.B85encode()
            self._raw_b85encstring = _process.decode(self._raw__raw_b85encstring)
            io = KaitaiStream(BytesIO(self._raw_b85encstring))
            self.b85encstring = self._root.Base85string(io, self, self._root)


    class B85dec(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw__raw_b85decstring = self._io.read_bytes_full()
            _process = satnogsdecoders.process.B85decode()
            self._raw_b85decstring = _process.decode(self._raw__raw_b85decstring)
            io = KaitaiStream(BytesIO(self._raw_b85decstring))
            self.b85decstring = self._root.Textstring(io, self, self._root)


    class Base85string(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.encoded = (self._io.read_bytes_full()).decode(u"ASCII")


    class Textstring(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.decoded = (self._io.read_bytes_full()).decode(u"ASCII")



