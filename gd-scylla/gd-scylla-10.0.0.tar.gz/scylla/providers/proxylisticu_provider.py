#GREENDECK

import re

from requests_html import HTML

from scylla.database import ProxyIP
from .base_provider import BaseProvider
import json

class ProxyListIcuProvider(BaseProvider):

    def parse(self, html: HTML) -> [ProxyIP]:
        ip_list: [ProxyIP] = []
        for ele in html.find('table tbody tr'):
            try:

                ip_port = str(ele.html)[8:].split('<')[0]
                ip,port = ip_port.split(':')
                ip_list.append(ProxyIP(ip=ip, port=port))
            except Exception as e:
                    print(e)
                    pass

        return ip_list

    def urls(self) -> [str]:
        return ['https://proxylist.icu/']


