from enum import Enum


class SocketErrorCases(Enum):
    IP_PORT_ERROR = 0
    IP_CANT_FIND = 1
    IP_VALUE_ERROR = 2
    PORT_VALUE_ERROR = 3
    DNS_ERROR = 4
    LOGIN_FAILED = 5
    USERNAME_ERROR = 6
    PASSWORD_ERROR = 7
    NOT_LOGIN_ERROR = 8
    VIEW_PPG_ERROR = 9
    DOWNLOAD_PPG_ERROR = 10
    SOCKET_CONNECTION_TIMEOUT = 11


class SocketError(Exception):
    def __init__(self, case, note=""):
        self.__note = note
        self.case = case
        self.__message = ""
        if case == SocketErrorCases.IP_PORT_ERROR:
            self.__message = "Ip or Port format Error, both of them need to be string."
        elif case == SocketErrorCases.IP_CANT_FIND:
            self.__message = "Can't find the IP address."
        elif case == SocketErrorCases.LOGIN_FAILED:
            self.__message = "Log in has failed."
        elif case == SocketErrorCases.USERNAME_ERROR:
            self.__message = "Username can not be found."
        elif case == SocketErrorCases.PASSWORD_ERROR:
            self.__message = "Password is wrong."
        elif case == SocketErrorCases.NOT_LOGIN_ERROR:
            self.__message = "Need to log in first."
        elif case == SocketError(SocketErrorCases.VIEW_PPG_ERROR):
            self.__message = "View PPG has failed."
        elif case == SocketErrorCases.DOWNLOAD_PPG_ERROR:
            self.__message = "Download PPG has failed."
        elif case == SocketErrorCases.SOCKET_CONNECTION_TIMEOUT:
            self.__message = "Connection Timeout."
        else:
            self.__message = "Check IP and Port has Failed."

    def __str__(self):
        return self.__message + " Note: %s" % self.__note
