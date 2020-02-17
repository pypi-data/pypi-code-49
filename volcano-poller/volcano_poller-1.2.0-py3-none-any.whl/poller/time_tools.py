#!/usr/bin/python3

import time


class Timer:
    def __init__(self):
        self.time_ = time.perf_counter()

    def set_now(self):
        self.time_ = time.perf_counter()

    def secs(self):
        rval = time.perf_counter() - self.time_
        return rval if rval >= 0.0 else 0.0


class Timeout:
    def __init__(self, timeout_sec=0.0, expired=False):
        self.timeout_sec_ = timeout_sec
        self.expired_ = expired
        if not self.expired_:
            self.t1_ = time.perf_counter()

    def is_expired(self):
        return self.remain_sec() == 0.0

    def remain_sec(self):
        if self.expired_:
            return 0.0
        passed_sec = time.perf_counter() - self.t1_
        if passed_sec > self.timeout_sec_:
            self.expired_ = True
            return 0.0
        return passed_sec

    def start(self, timeout_sec=None):
        if timeout_sec is not None:
            self.timeout_sec_ = timeout_sec
        self.expired_ = self.timeout_sec_ <= 0.0
        if not self.expired_:
            self.t1_ = time.perf_counter()
