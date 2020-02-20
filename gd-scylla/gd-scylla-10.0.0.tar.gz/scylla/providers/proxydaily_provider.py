#GREENDECK


import re

from requests_html import HTML

from scylla.database import ProxyIP
from .base_provider import BaseProvider
import json

class ProxyDailyProvider(BaseProvider):

    def parse(self, html: HTML) -> [ProxyIP]:
        ip_list: [ProxyIP] = []
        for ele in html.find('.freeProxyStyle'):
            list_of_ips_port = ele.html.split('\n')[1:]

            for ip_row in list_of_ips_port:
                try:
                        
                    ip, port = ip_row.split(':')
                    ip_list.append(ProxyIP(ip=ip, port=port))
                except Exception as e:
                    print(e)
                    pass
        return ip_list

    def urls(self) -> [str]:
        return ['https://proxy-daily.com/']


