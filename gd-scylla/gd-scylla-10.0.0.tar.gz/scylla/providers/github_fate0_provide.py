# GREENDECK

from requests_html import HTML

from scylla.database import ProxyIP
from .base_provider import BaseProvider
import json

class GithubFate0Provider(BaseProvider):

    def parse(self, html: HTML) -> [ProxyIP]:

        print("\n\n -----------------------IN GITHUB FATE PROVIDER---------------------\n\n\n")

        try:
            ip_list: [ProxyIP] = []
            for json_line in html.text.split('\n'):
                try:
                    proxy_json = json.loads(json_line.strip())
                    p = ProxyIP(ip=proxy_json['IP'], port=proxy_json['PORT'])
                    ip_list.append(p)
                except:
                    pass
        except Exception as e:
            print(e)
            print("\n\n\n\n Cannot fetch from Your source \n\n\n\n")
            
        return ip_list
        # for proxy_item in proxy_json[0]['LISTA']:
        #     p = ProxyIP(ip=proxy_item['IP'], port=proxy_item['PORT'])
        #     ip_list.append(p)


    def urls(self) -> [str]:
        return [
            'https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list',
        ]
