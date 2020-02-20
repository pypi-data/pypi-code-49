# GREENDECK

from requests_html import HTML

from scylla.database import ProxyIP
from .base_provider import BaseProvider
import json

class ProxyListDownloadProvider(BaseProvider):

    def parse(self, html: HTML) -> [ProxyIP]:
        try:
            ip_list: [ProxyIP] = []
            proxy_json = json.loads(html.html)
            for proxy_item in proxy_json[0]['LISTA']:
                p = ProxyIP(ip=proxy_item['IP'], port=proxy_item['PORT'])
                ip_list.append(p)

        except Exception as e:
            print(e)
            print("\n\n\n\n Cannot fetch from Your source \n\n\n\n")
        return ip_list

    def urls(self) -> [str]:
        return [
            'https://www.proxy-list.download/api/v0/get?l=en&t=https',
            'https://www.proxy-list.download/api/v0/get?l=en&t=http'
        ]
