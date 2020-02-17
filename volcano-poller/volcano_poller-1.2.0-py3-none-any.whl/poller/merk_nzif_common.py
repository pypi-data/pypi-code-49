#!/usr/bin/python3


class ProtocolException(Warning):
    pass


class BadDataException(ProtocolException):
    pass


class RequestResponseMismatch(ProtocolException):
    pass


class NackException(ProtocolException):
    def __init__(self, msg, code):
        super().__init__(msg)
        self.nack_code = code
