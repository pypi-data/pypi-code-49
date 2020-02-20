#GREENDECK

import re

from requests_html import HTML

from scylla.database import ProxyIP
from .base_provider import BaseProvider
import json

class SeoToolsProvider(BaseProvider):

    def parse(self, html: HTML) -> [ProxyIP]:
        ip_list: [ProxyIP] = []
        for ele in html.find('.table-striped tbody tr')[:-1]:

            try:
                list_of_ips_port = ele.html.split('\n')[2:]
                ip = list_of_ips_port[0].strip()[4:].split('<')[0]
                port = list_of_ips_port[1].strip()[4:].split('<')[0]
                ip_list.append(ProxyIP(ip=ip, port=port))


            except Exception as e:
                print(e)
                pass

        return ip_list

    def urls(self) -> [str]:
        return ['https://seotoolsblog.com/free-proxy-list']
