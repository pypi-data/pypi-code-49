import functools
import time
from typing import Dict

from selenium.webdriver.common.proxy import ProxyType


@functools.total_ordering
class ProxyInfo:
    def __init__(self, observer, host, type, response_time=999.0):
        self.__observer = observer
        self.__host = host
        self.__type = type
        self.__response_time = response_time

        self.failure = 0
        self.__using = False
        self.__close_time = -1

    def get_host(self):
        return self.__host

    def get_type(self):
        return self.__type

    def is_busy(self, delay):
        return self.__using or time.time() < self.__close_time + delay

    def get_response_time(self):
        return self.__response_time

    def set_response_time(self, new_time):
        self.__response_time = new_time
        self.__observer.notify(self)

    def get_as_url(self):
        return "{}://{}".format(self.__type, self.__host)

    def request_style_proxies_dict(self, protocol):
        formatted_host = "{}://{}".format(self.__type, self.__host)
        return {protocol: formatted_host}

    def __add_to_capabilities(self, capabilities, **kwargs):
        """
        Adds proxy information as capability in specified capabilities.

        :Args:
         - capabilities: The capabilities to which proxy will be added.
        """
        proxy_caps = {}
        proxy_caps['proxyType'] = kwargs['proxyType']['string']
        if 'autodetect' in kwargs:
            proxy_caps['autodetect'] = kwargs['autodetect']
        if 'ftpProxy' in kwargs:
            proxy_caps['ftpProxy'] = kwargs['ftpProxy']
        if 'httpProxy' in kwargs:
            proxy_caps['httpProxy'] = kwargs['httpProxy']
        if 'proxyAutoconfigUrl' in kwargs:
            proxy_caps['proxyAutoconfigUrl'] = kwargs['proxyAutoconfigUrl']
        if 'sslProxy' in kwargs:
            proxy_caps['sslProxy'] = kwargs['sslProxy']
        if 'noProxy' in kwargs:
            proxy_caps['noProxy'] = kwargs['noProxy']
        if 'socksProxy' in kwargs:
            proxy_caps['socksProxy'] = kwargs['socksProxy']
        if 'socksVersion' in kwargs:
            proxy_caps['socksVersion'] = kwargs['socksVersion']
        if 'socksUsername' in kwargs:
            proxy_caps['socksUsername'] = kwargs['socksUsername']
        if 'socksPassword' in kwargs:
            proxy_caps['socksPassword'] = kwargs['socksPassword']
        capabilities['proxy'] = proxy_caps

    def apply_to_selenium_capabilities(self, proxy_type: ProxyType, compatibilities: Dict):
        val = "{}".format(self.__host)

        self.__add_to_capabilities(compatibilities,
                                   proxyType=proxy_type,
                                   sslProxy=val,
                                   httpProxy=val if self.__type == 'http' or self.__type == 'https' else None,
                                   socksProxy=val if self.__type == 'socks4' or self.__type == 'socks5' else None,
                                   socksVersion=4 if self.__type == 'socks4' else 5)

    def success(self):
        self.__observer.notify(self)

    def fail(self):
        self.failure += 1
        self.__observer.notify(self)

    def close(self):
        self.__close_time = time.time()

    def __eq__(self, other):
        return self.__response_time == other.response_time and self.failure == other.failure

    def __lt__(self, other):
        if self.failure < other.failure:
            return True
        elif self.failure > other.failure:
            return False
        else:
            return self.__response_time < other.__response_time

    def __repr__(self):
        return str(self.__host) + ", " + str(self.__type) + ", [" + str(self.failure) + " fails & " + str(
            self.__response_time) + "s]"

    def __enter__(self):
        self.__using = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.success()
        else:
            self.fail()

        self.__using = False
        self.close()
