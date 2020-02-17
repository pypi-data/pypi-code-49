# -*- coding: utf-8 -*-
# @CreateTime : 2019/11/4 11:36
# @Author     : Liu Gang
# @File       : compat.py.py
# @Software   : PyCharm

"""
modification history
--------------------
V1.00.00, 04Nov2019, Liu Gang written
--------------------
"""

import sys
import os
import platform
import io
import struct
import socket
import time
import telnetlib

try:
    import ConfigParser as compat_conf
except ImportError:
    import configparser as compat_conf

COMPAT_VER = "V1.00.00"

NoSectionError = compat_conf.NoSectionError
NoOptionError = compat_conf.NoOptionError

is_py2 = sys.version_info[0] == 2
is_py3 = sys.version_info[0] == 3
PY_VER = 2 if is_py2 else 3
is_winxp = platform.win32_ver()[0] != "XP"

open_file = open if is_py3 else io.open
text_read_mode = 'r' if is_py3 else 'rU'
APPEND_WRITE = "ab+" if is_py2 else "a+"
READ = "rb" if is_py2 else "r"

# In Python 3 built-in function raw_input() was renamed to just 'input()'.
try:
    stdin_input = raw_input
except NameError:
    stdin_input = input


# Set and get environment variables does not handle unicode strings correctly
# on Windows.

# Acting on os.environ instead of using getenv()/setenv()/unsetenv(),
# as suggested in <http://docs.python.org/library/os.html#os.environ>:
# "Calling putenv() directly does not change os.environ, so it's
# better to modify os.environ." (Same for unsetenv.)

def getenv(name, default=None):
    """
    Returns unicode string containing value of environment variable 'name'.
    """
    return os.environ.get(name, default)


def setenv(name, value):
    """
    Accepts unicode string and set it as environment variable 'name' containing
    value 'value'.
    """
    os.environ[name] = value


def unsetenv(name):
    """
    Delete the environment variable 'name'.
    """
    # Some platforms (e.g. AIX) do not support `os.unsetenv()` and
    # thus `del os.environ[name]` has no effect onto the real
    # environment. For this case we set the value to the empty string.
    os.environ[name] = ""
    del os.environ[name]


def chrtobyte(in_list):
    """
    in_list(char) -> out_str(string)
    :param in_list:
    :return:out_list (string)
    """
    if is_py3:
        out_str = bytes(in_list)
    else:
        out_str = str()
        for c in in_list:
            out_str += struct.pack('B', c)

    return out_str


def fit_str(str_data):
    if is_py3:
        if isinstance(str_data, bytes):
            ret_str = str_data
        else:
            ret_str = bytes(str_data, encoding='utf-8')
    else:
        ret_str = str_data

    return ret_str


def int2list(num_int, n_byte):
    """

    :param num_int:integer
    :param n_byte: sizeof(num_int)
    :return:list[high,low]
    """
    ret_list = list()
    for process in range(n_byte - 1, -1, -1):
        cacl_rslt = (num_int >> 8 * process) & 0xFF
        ret_list.append(cacl_rslt)

    return ret_list


def list2int(in_list):
    """

    :param in_list:[high,low]
    :return:
    """
    ret_int = 0
    n_byte = len(in_list)
    for process in range(0, n_byte):
        cacl_rslt = in_list[process] << 8 * (n_byte - process - 1)
        ret_int += cacl_rslt

    return ret_int


class compat_socket(socket.socket):
    def __init__(self, *args):
        socket.socket.__init__(self, *args)

    def compat_recvfrom(self, buflen=1024, flags=0):
        """
        return byte string.
        :param buflen:
        :param flags:
        :return: if py2, char str, py3, bytes
        """
        data, addr_info = self.recvfrom(buflen, flags)
        if is_py2:
            ret_data_str = ""
            for d in data:
                ret_data_str += struct.unpack('s', d)[0]
        else:
            ret_data_str = data

        return ret_data_str, addr_info

    def compat_sendto(self, in_data, addr):
        """
        send data_list
        :param in_data: data_list(int list) to send or str
        :param addr:
        :return:
        """
        if isinstance(in_data, list):
            # if is_py3:
            #     out_str = bytes(in_data)
            # else:
            #     out_str = ""
            #     for c in in_data:
            #         out_str += struct.pack('B', c)
            out_str = chrtobyte(in_data)

        elif isinstance(in_data, str):
            if is_py3:
                out_str = fit_str(in_data)
            else:
                out_str = in_data
        else:
            out_str = in_data
        return self.sendto(out_str, addr)


class compat_telnet(telnetlib.Telnet):
    def __init__(self, *args):
        telnetlib.Telnet.__init__(self, *args)

    def write(self, buffer):
        """

        :param buffer: type str
        :return:
        """
        buffer = fit_str(buffer)
        return telnetlib.Telnet.write(self, buffer)

    def read_until(self, match, timeout=None):
        """

        :param match type str
        :param timeout:
        :return: type str
        """
        match = fit_str(match)
        ret = telnetlib.Telnet.read_until(self, match, timeout)
        if is_py3:
            ret = str(ret, "utf-8")
        return ret


def gettime(time_format=0):
    """
    get system current time
    :param time_format: the format for return value
    :return:
    """
    if time_format == 0:
        return time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    elif time_format == 1:
        return time.strftime("%Y%m%d", time.localtime(time.time()))
    elif time_format == 2:
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


def sleep(sec):
    return time.sleep(sec)
