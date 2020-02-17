#!/usr/bin/python3

import time

from volcano.general.bin import bytes_to_str

from . import time_tools


class BaseCtx:
    def __init__(self, channel):
        self.silence_sec = 0.0
        self.timeout_sec = 1.0
        #self.abort_cb = None

        self.log_ = None
        self.channel_ = channel
        self.comment_ = None

    def log(self):
        return self.log_

    def close_channel(self):
        self.channel_.safe_close()

    def is_open(self):
        return self.channel_.is_open()

    def test_abort(self):
        #if self.abort_cb and self.abort_cb():
        #    raise SystemExit()
        pass

    # None  => continue listen
    # Any   => return as result of send_rcv()
    # Exception => if channel is open, retry (swallow exception), else fail (re-raise)
    def data_cb(self, data: (bytes, bytearray)):
        raise NotImplementedError()

    # rval:
    #
    #   success         =>  rval from data_cb()
    #
    #   * SystemExit        =>  aborted by abort_cb()
    #   * ConnectionError   =>  Any problems with channel
    #   * TimeoutError
    #   * AnyException from data_cb()
    def _send_rcv_once(self, data_to_send: (bytes, bytearray)):
        assert isinstance(data_to_send, (bytes, bytearray)), data_to_send

        if self.silence_sec > 0.0:
            self.test_abort()  # *SystemExit
            time.sleep(self.silence_sec)
            self.test_abort()  # *SystemExit

        ch = self.channel_

        ch.reset_rcv_buf_x(self.log_)  # *ConnectionError

        if self.log_:
            if self.comment_:
                self.log_.debug('S> {} [{}]'.format(bytes_to_str(data_to_send), self.comment_))
            else:
                self.log_.debug('S> {}'.format(bytes_to_str(data_to_send)))

        ch.write_all_x(data_to_send, self.log_)  # *ConnectionError

        timeout = time_tools.Timeout(self.timeout_sec)

        rcvd = b''

        while not timeout.is_expired():
            self.test_abort()  # *SystemExit

            # b'' if not data
            portion = ch.read_x(timeout.remain_sec(), self.log_)  # *ConnectionError
            assert isinstance(portion, (bytes, bytearray)), portion

            if portion:
                if self.log_:
                    self.log_.debug('R< {}'.format(bytes_to_str(portion)))
                rcvd += portion

                r_process = self.data_cb(rcvd)

                if r_process is not None:
                    return r_process

        if self.comment_:
            raise TimeoutError('{}: Timeout'.format(self.comment_))
        else:
            raise TimeoutError('Timeout')

    # rval:
    #
    #   success         =>  rval from data_cb()
    #
    #   * SystemExit        =>  aborted by abort_cb()
    #   * ConnectionError   =>  Any problems with channel
    #   * TimeoutError
    #   * AnyException from data_cb()
    def send_rcv_raw(self, data_to_send: (bytes, bytearray), comment_n: str, log, nb_attempts: int = 2):
        assert isinstance(data_to_send, (bytes, bytearray)), data_to_send
        assert comment_n is None or isinstance(comment_n, str), comment_n
        assert isinstance(nb_attempts, int), nb_attempts

        try:
            self.log_ = log
            self.comment_ = comment_n

            cr_attempt_nb = 1
            while True:
                try:
                    return self._send_rcv_once(data_to_send)
                except Exception as e:
                    if not self.channel_.is_open():
                        raise e

                    cr_attempt_nb += 1
                    if cr_attempt_nb > nb_attempts:
                        raise e

        finally:
            self.log_ = None
            self.comment_ = None
