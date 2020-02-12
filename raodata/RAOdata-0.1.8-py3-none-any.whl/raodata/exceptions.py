#!/usr/bin/env python3

'''RAO data exceptions'''


class CannotConnect(Exception):
    code = "CANNOTCONNECT"


class CannotParseArguments(Exception):
    code = "CANNOTPARSEARGUMENTS"


class InstrumentNotString(Exception):
    code = "INSTUMENTNOTSTRING"


class FiletypeNotString(Exception):
    code = "FILETYPENOTSTRING"


class InvalidTime(Exception):
    code = "INVALIDTIME"


class CannotDownloadFile(Exception):
    code = "CANNOTDOWNLOADFILE"


class InvalidFileHash(Exception):
    code = "INVALIDFILEHASH"


class InvalidInstrumentOrType(Exception):
    code = "INVALIDINSTUMENTORTYPE"


class CannotCreateDirectory(Exception):
    code = "CANNOTCREATEDIRECTORY"


class NoDataForThePeriod(Exception):
    code = "NODATAFORTHEPERIOD"
