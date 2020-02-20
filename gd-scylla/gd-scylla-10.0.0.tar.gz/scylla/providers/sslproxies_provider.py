#GREENDECK

from requests_html import HTML

from scylla.database import ProxyIP
from .base_provider import BaseProvider
import json

class SslProxiesProvider(BaseProvider):

    def parse(self, html: HTML) -> [ProxyIP]:
        try:
            ip_list: [ProxyIP] = []
            list_of_tds = list(html.find('#proxylisttable tbody tr td'))

            for i in range(0, len(list_of_tds),8):

                try:
                    ip_td = list_of_tds[i].html
                    ip_port = list_of_tds[i+1].html
                    ip = ip_td[4:-5]
                    port = ip_port[4:-5]
                    p = ProxyIP(ip = ip, port = port)
                    ip_list.append(p)

                except Exception as e:
                    print(e)
                    
        except Exception as e:
            print(e)
            print("Can not fetch")

        return ip_list

    def urls(self) -> [str]:
        return [
            'https://www.sslproxies.org/',
        ]
