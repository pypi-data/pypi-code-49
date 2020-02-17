#!/usr/bin/python3

from volcano.general.bin import bytes_to_str, check_crc16, get_crc16_as_bytes

from . import base_ctx
from .merk_nzif_common import NackException, BadDataException, RequestResponseMismatch


class MerkNzifCtx(base_ctx.BaseCtx):
    def __init__(self, channel, is_merk: bool):
        super().__init__(channel)

        self.is_merk_ = is_merk

        self.req__reply_sz_no_add_no_crc = None
        self.req__expecting_status_reply = None
        self.req__addr = None
        self.req__comment = None

        self.reply_data = None  # no slave nb, no crc

    def get_nack_comment_n(self, nack_code: int) -> (None, str):
        raise NotImplementedError()

    def data_cb(self, data: (bytes, bytearray)):
        assert isinstance(data, (bytes, bytearray)), data

        reply_sz = self.req__reply_sz_no_add_no_crc + 1 + 2
        if len(data) > reply_sz:
            raise BadDataException(
                "{}: Reply is too long (expected {} bytes with crc, got {}): {}".format(self.req__comment, reply_sz,
                                                                                        len(data),
                                                                                        bytes_to_str(data)))

        if len(data) < reply_sz:
            # nack?
            if not self.req__expecting_status_reply and len(data) == 4 and data[0] == self.req__addr and data[1] != 0 and check_crc16(data):
                code = data[1]
                code_comment = self.get_nack_comment_n(code)
                if code_comment:
                    raise NackException('{}: Nack (code={} - {})'.format(self.req__comment, code, code_comment), code)
                else:
                    raise NackException('{}: Nack (code={})'.format(self.req__comment, code), code)
            else:
                return None  # need more data

        if not check_crc16(data):
            raise BadDataException('{}: crc error in {}'.format(self.req__comment, bytes_to_str(data)))

        if data[0] != self.req__addr:
            raise RequestResponseMismatch(
                '{}: Slave number mismatch. Request={}; reply={}'.format(self.req__comment, self.req__addr, data[0]))

        if self.req__expecting_status_reply:
            self.reply_data = None
            code = data[1]
            if code != 0:  # nack
                code_comment = self.get_nack_comment_n(code)
                if code_comment:
                    raise NackException('{}: Nack (code={} - {})'.format(self.req__comment, code, code_comment), code)
                else:
                    raise NackException('{}: Nack (code={})'.format(self.req__comment, code), code)
        else:
            self.reply_data = data[1:]

        return True  # return anything but None

    # reply_data_sz: without address and crc
    # always prints exception text
    # closes channel on commfail and baddata
    def send_rcv(self, data_no_crc: (bytes, bytearray), reply_data_sz_n: (None, int), comment: str, log) -> None:
        assert isinstance(data_no_crc, (bytes, bytearray)), data_no_crc
        assert reply_data_sz_n is None or isinstance(reply_data_sz_n, int), reply_data_sz_n
        assert isinstance(comment, str), comment

        # should not append_crc to data because data can immutable bytes
        data = data_no_crc + get_crc16_as_bytes(data_no_crc)

        self.req__comment = comment
        self.req__addr = data[0]
        if reply_data_sz_n is None:  # we expect status reply
            self.req__reply_sz_no_add_no_crc = 1
            self.req__expecting_status_reply = True
        else:
            self.req__reply_sz_no_add_no_crc = reply_data_sz_n
            self.req__expecting_status_reply = False

        self.send_rcv_raw(data, comment, log)
        
    # data has no slave nb and no crc. data(0) gives first byte after slave nb
    def data(self, byte_idx: int = None):
        return self.reply_data if byte_idx is None else self.reply_data[byte_idx]
