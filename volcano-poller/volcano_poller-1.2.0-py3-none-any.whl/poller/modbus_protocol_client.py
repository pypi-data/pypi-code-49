from volcano.general.bin import get_crc16_as_bytes
from volcano.general.modbus import MbError, ErrorCode, MbFunctionCode, MbLimits, MbException


def word_ml(ba: (bytes, bytearray), offset: int) -> int:
    assert isinstance(ba, (bytes, bytearray)), ba
    assert isinstance(offset, int), offset
    assert len(ba) > (offset + 1)

    return (ba[offset] << 8) | ba[offset + 1]


def lo(w: int) -> int:
    assert isinstance(w, int), w
    return w & 0xff


def hi(w: int) -> int:
    assert isinstance(w, int), w
    return (w >> 8) & 0xff


def _wrap_req(trans_id: (int, None), rtu_data: (bytes, bytearray)) -> bytes:
    assert trans_id is None or isinstance(trans_id, int), trans_id
    assert isinstance(rtu_data, (bytes, bytearray)), rtu_data

    if trans_id is None:  # rtu
        return bytes(rtu_data) + get_crc16_as_bytes(rtu_data)
    else:
        if trans_id < 0 or trans_id > 0xffff:
            raise MbError(ErrorCode.BadData)

        return bytes([hi(trans_id), lo(trans_id), 0, 0, hi(len(rtu_data)), lo(len(rtu_data))]) + bytes(rtu_data)


# Raise MbError if parameters are incorrect
def build_req_read_words(trans_id_none: int, slave_nb: int, fn_nb: int, addr: int, nb_words: int) -> bytes:
    assert trans_id_none is None or isinstance(trans_id_none, int), trans_id_none
    assert isinstance(slave_nb, int), slave_nb
    assert isinstance(fn_nb, int), fn_nb
    assert isinstance(addr, int), addr
    assert isinstance(nb_words, int), nb_words

    # REQ: Slave,Fn,AddrH,AddrL,NbWordsH,NbWordsL
    if slave_nb < 0 or slave_nb > 0xff:
        raise MbError(ErrorCode.BadData)

    if fn_nb not in (MbFunctionCode.MB_FN_READ_OUT_WORDS_3, MbFunctionCode.MB_FN_READ_IN_WORDS_4):
        raise MbError(ErrorCode.BadData)

    if addr < 0 or nb_words <= 0 or nb_words > MbLimits.MAX_READ_WORDS_NB or (addr + nb_words - 1) > 0xffff:
        raise MbError(ErrorCode.BadData)

    return _wrap_req(trans_id_none, bytes([slave_nb, fn_nb, hi(addr), lo(addr), 0, nb_words]))


# request: (trans_id, slave_nb, fn_nb, ...)
# resp:
#   None:   not enough data
#   MbException, MbError
#   f1, f2: (trans_id, slave_nb, fn_nb, (bit1: bool, bit2: bool, ...))
#   f3, f4: (trans_id, slave_nb, fn_nb, data_bytes)
def parse_res_tcp(ba: (bytes, bytearray), offset: int, nb: int, request=None) -> (None, tuple):
    assert isinstance(ba, (bytes, bytearray)), ba
    assert isinstance(offset, int), offset
    assert isinstance(nb, int), nb
    assert request is None or isinstance(request, tuple), request

    if nb < 6:
        return None

    rtu_size = word_ml(ba, offset + 4)
    tcp_size = rtu_size + 6

    if nb < tcp_size:
        return None

    if rtu_size < 2:
        raise MbError(ErrorCode.BadData)

    rtu_offset = 6
    trans_id = word_ml(ba, offset + 0)
    slave_nb = ba[rtu_offset + 0]
    fn_nb = ba[rtu_offset + 1] & 0x7f

    if request:
        r_trans_id, r_slave_nb, r_fn_nb, *r_data = request
        if r_trans_id != trans_id:  # Если запрос был rtu, r_trans_id=None; none != int
            raise MbError(ErrorCode.MismatchTrId)

        if r_slave_nb != slave_nb:
            raise MbError(ErrorCode.MismatchSlave)

        if r_fn_nb != fn_nb:
            raise MbError(ErrorCode.MismatchFn)

    if ba[rtu_offset + 1] & 0x80:
        if rtu_size != 3:
            raise MbError(ErrorCode.BadData)

        exc_nb = ba[rtu_offset + 2]

        raise MbException(exc_nb)

    if fn_nb in (MbFunctionCode.MB_FN_READ_OUT_BITS_1, MbFunctionCode.MB_FN_READ_IN_BITS_2):
        # REPLY: Slave,Fn,NbBytes,DATA
        if rtu_size < 3:
            raise MbError(ErrorCode.BadData)

        nb_bytes = ba[rtu_offset + 2]

        if rtu_size != (3 + nb_bytes) or nb_bytes == 0:
            raise MbError(ErrorCode.BadData)

        # nb_bytes = nb_bytes;
        # this->read_bits.Bytes	= RtuData + 3;

        if request:
            # r_addr = r_data[0]
            r_nb_bits = r_data[1]
            nb_bytes_requested = (r_nb_bits + 7) // 8
            if nb_bytes != nb_bytes_requested:
                raise MbError(ErrorCode.MismatchData)

        return tcp_size

    elif fn_nb in (MbFunctionCode.MB_FN_READ_OUT_WORDS_3, MbFunctionCode.MB_FN_READ_IN_WORDS_4):
        # REPLY: Slave,Fn,NbBytes,DATA
        if rtu_size < 3:
            raise MbError(ErrorCode.BadData)

        nb_bytes = ba[rtu_offset + 2]

        if rtu_size != (3 + nb_bytes) or nb_bytes == 0 or (nb_bytes % 2) != 0:
            raise MbError(ErrorCode.BadData)

        nb_words = nb_bytes // 2
        words_offs = rtu_offset + 3

        if request:
            # r_addr = r_data[0]
            r_nb_words = r_data[1]
            if nb_words != r_nb_words:
                raise MbError(ErrorCode.MismatchData)

        return trans_id, slave_nb, fn_nb, ba[words_offs:]

    elif fn_nb == MbFunctionCode.MB_FN_WRITE_BIT_5:
        # REPLY: Slave,Fn,AddrH,AddrL,Value(0/FF),0  - just a copy of request
        if rtu_size != 6:
            raise MbError(ErrorCode.BadData)

        addr = word_ml(ba, rtu_offset + 2)
        value = ba[rtu_offset + 4]

        if request:
            val = 0xff if request.write_bit.Value else 0x00
            if request.write_bit.addr != addr or val != value:
                raise MbError(ErrorCode.MismatchData)

        return tcp_size

    elif fn_nb == MbFunctionCode.MB_FN_WRITE_WORD_6:
        # REPLY: Slave,Fn,AddrH,AddrL,ValueH,ValueL - just a copy of request
        if rtu_size != 6:
            raise MbError(ErrorCode.BadData)

        addr = word_ml(ba, rtu_offset + 2)
        value = word_ml(ba, rtu_offset + 4)

        if request:
            if request.write_word.addr != addr or request.write_word.value != value:
                raise MbError(ErrorCode.MismatchData)

        return tcp_size

    elif fn_nb == MbFunctionCode.MB_FN_WRITE_BITS_15:
        # REPLY: Slave,Fn,AddrH,AddrL,NbBitsH,NbBitsL
        if rtu_size != 6:
            raise MbError(ErrorCode.BadData)

        addr = word_ml(ba, rtu_offset + 2)
        nb_bits = word_ml(ba, rtu_offset + 4)

        if request:
            if request.write_bits.addr != addr or request.write_bits.nb_bits != nb_bits:
                raise MbError(ErrorCode.MismatchData)

        return tcp_size

    elif fn_nb == MbFunctionCode.MB_FN_WRITE_WORDS_16:
        # REPLY: Slave,Fn,AddrH,AddrL,NbWordsH,NbWordsL
        if rtu_size != 6:
            raise MbError(ErrorCode.BadData)

        addr = word_ml(ba, rtu_offset + 2)
        nb_words = word_ml(ba, rtu_offset + 4)

        if request:
            if request.write_words.addr != addr or request.write_words.nb_words != nb_words:
                raise MbError(ErrorCode.MismatchData)

        return tcp_size
    else:
        assert False, fn_nb
        return None
