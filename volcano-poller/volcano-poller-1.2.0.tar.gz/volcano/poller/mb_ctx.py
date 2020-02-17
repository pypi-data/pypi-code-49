from . import base_ctx
from .modbus_protocol_client import build_req_read_words, parse_res_tcp


class MbCtx(base_ctx.BaseCtx):
    def __init__(self, channel):
        super().__init__(channel)
        self.log = None
        self.trans_id_ = 0
        self.request_ = None

    def data_cb(self, data):
        return parse_res_tcp(data, 0, len(data), self.request_)

    # returns:
    #  - bytearray() with words
    #  * MbException
    #  * MbError
    #  * ConnectionError, TimeoutError
    def read_words(self, slave_nb: int, fn_nb: int, addr: int, nb_words: int, comment: str, log):
        self.trans_id_ = (self.trans_id_ + 1) & 0xffff
        self.request_ = (self.trans_id_, slave_nb, fn_nb, addr, nb_words)

        req = build_req_read_words(self.trans_id_, slave_nb, fn_nb, addr, nb_words)

        trans_id, slave_nb, fn_nb, data_bytes = self.send_rcv_raw(req, comment, log)        # pylint: disable=unused-variable

        return data_bytes
