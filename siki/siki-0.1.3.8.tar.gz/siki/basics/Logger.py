# -*- coding: utf-8 -*-
# Author: Orlando Chen
# Create: May 31, 2018
# Modifi: Sep 13, 2018

from enum import Enum

from siki.basics import FileUtils as fileutil
from siki.basics import SystemUtils as sysutil
from siki.basics import Convert as convert
from siki.basics import TimeTicker as timetick
from siki.basics import Hashcode as hashcode
from siki.basics.Exceptions import NullPointerException, InvalidParamException


m_bStdOut = False
m_bUseLog = False
m_file = None
m_dir  = None

class Priority(Enum):
    INFO = 0
    DEBUG = 1
    WARNING = 2
    ERROR = 3


def _gen_logfile(dir, file):
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y%m%d")
    #return fileutil.gen_path(dir, file, "log", timestamp)
    return fileutil.gen_filepath(dir, file, "log", timestamp)


def init(b_stdout, b_log, dir = None, file = None):
    global m_file, m_dir, m_bStdOut, m_bUseLog
    m_bStdOut = b_stdout
    m_bUseLog = b_log
    if m_bUseLog:
        fileutil.mkdir(dir)
        m_file = file
        m_dir  = dir


def _check_valid_file(dir, file):
    if dir is None or file is None:
        raise NullPointerException("Invalid operation, call init first")
    return _gen_logfile(dir, file)


def _priority_name(priority):
    if type(priority) is not Priority:
        raise InvalidParamException("'priority' must be an instance of Priority")
    if priority == Priority.INFO:
        return "INFO"
    elif priority == Priority.DEBUG:
        return "DEBUG"
    elif priority == Priority.WARNING:
        return "WARNING"
    elif priority == Priority.ERROR:
        return "ERROR"


def file_path():
    import datetime
    global m_dir, m_file
    return _check_valid_file(m_dir, m_file)


def message(priority, title = None, msg = None, exception = None):
    import traceback
    global m_dir, m_file, m_bStdOut, m_bUseLog

    # check log is validate
    if m_bUseLog:
        f = _check_valid_file(m_dir, m_file)

    errline = "{0} <{1}>".format(timetick.current_timestamp(), _priority_name(priority))
    if title is not None:
        errline += "\t[{0}]".format(title)
    if msg is not None:
        errline += "\t{0}".format(msg)

    if sysutil.is_windows():
        errline += "\r\n"
    else:
        errline += "\n"

    if exception is not None:
        error = ''.join(traceback.format_exception(etype=type(exception), value=exception, tb=exception.__traceback__))
        if sysutil.is_windows():
            errline += "{0}".format(error)
        else:
            errline += "{0}".format(error)
    
    if m_bUseLog:
        fileutil.write_file(f, convert.string_to_binary(errline), True)
    if m_bStdOut:
        print(errline)


def _compute_base64(data):
    import base64
    from Basics import convert
    r = base64.b64encode(data.encode("UTF8"))
    return convert.binary_to_string(r)


def data_in_base64(priority, title, data):
    global m_dir, m_file, m_bStdOut, m_bUseLog
    # check log is validate
    f = _check_valid_file(m_dir, m_file)
    line = "{0} <{1}> [{2}]".format(timetick.current_timestamp(), _priority_name(priority), title)

    if sysutil.is_windows():
        line += "\r\n    Data: {0}\r\n".format(_compute_base64(data))
    else:
        line += "\n    Data: {0}\n".format(_compute_base64(data))

    if m_bUseLog:
        fileutil.write_file(f, convert.string_to_binary(line), True)
    if m_bStdOut:
        print(line)


def data_in_hashcode(priority, title, data):
    global m_dir, m_file, m_bStdOut, m_bUseLog
    # check log is validate
    f = _check_valid_file(m_dir, m_file)
    line = "{0} <{1}> [{2}]".format(timetick.current_timestamp(), _priority_name(priority), title)

    if sysutil.is_windows():
        line += "\r\n    Data: {0}\r\n".format(hashcode.md5(data))
    else:
        line += "\n    Data: {0}\n".format(hashcode.md5(data))

    if m_bUseLog:
        fileutil.write_file(f, convert.string_to_binary(line), True)
    if m_bStdOut:
        print(line)
