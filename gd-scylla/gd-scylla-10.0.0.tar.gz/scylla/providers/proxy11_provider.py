# GREENDECK

from requests_html import HTML

from scylla.database import ProxyIP
from .base_provider import BaseProvider
import json

class ProxyElevenProvider(BaseProvider):

    def parse(self, html: HTML) -> [ProxyIP]:
        try:
            ip_list: [ProxyIP] = []
            json_data = json.loads(html.text)
            for json_line in json_data['data']:
                try:
                    p = ProxyIP(ip = json_line['ip'], port = json_line['port'])
                    ip_list.append(p)
                except:
                    pass

        except Exception as e:
            print(e)
            print("\n\n\n\n Cannot fetch from Your source \n\n\n\n")

        return ip_list

    def urls(self) -> [str]:
        return [
            'https://proxy11.com/api/demoweb/proxy.json',
        ]
