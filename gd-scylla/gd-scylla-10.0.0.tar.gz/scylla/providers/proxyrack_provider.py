#GREENDECK
import re

from requests_html import HTML

from scylla.database import ProxyIP
from .base_provider import BaseProvider
import json

class ProxyRackProvider(BaseProvider):

    def parse(self, html: HTML) -> [ProxyIP]:
        ip_list: [ProxyIP] = []

        for ip_row in (json.loads(html.text)['records']):
            try:
                ip_list.append(ProxyIP(ip=ip_row['ip'], port=ip_row['port']))

            except Exception as e:
                print(e)
        return ip_list

    def urls(self) -> [str]:
        return ['https://www.proxyrack.com/proxyfinder/proxies.json?page=1&perPage=20000&offset=0']


