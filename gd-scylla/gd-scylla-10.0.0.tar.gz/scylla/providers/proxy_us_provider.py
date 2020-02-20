# GREENDECK

from requests_html import HTML

from scylla.database import ProxyIP
from .base_provider import BaseProvider
import json
from lxml.html import fromstring

class ProxyUSProvider(BaseProvider):

    def parse(self, html: HTML) -> [ProxyIP]:
        ip_list: [ProxyIP] = []
        try:
            parser = fromstring(str(html)) #changed
            for i in parser.xpath('//tbody/tr'):
                if i.xpath('.//td[7][contains(text(),"yes")]'):
                    p = ProxyIP(ip = i.xpath('.//td[1]/text()')[0], port = i.xpath('.//td[2]/text()')[0])
                    ip_list.append(p)
                else:
                    p = ProxyIP(ip = i.xpath('.//td[1]/text()')[0], port = i.xpath('.//td[2]/text()')[0])
                    ip_list.append(p)
        except IndexError as e:
            print(e)
            for i in parser.xpath('//tbody/tr'):
                if i.xpath('.//td[7][contains(text(),"yes")]'):
                    p = ProxyIP(ip = i.xpath('.//td[1]/text()')[0], port = i.xpath('.//td[2]/text()')[0])
                    ip_list.append(p)
                else:
                    p = ProxyIP(ip = i.xpath('.//td[1]/text()')[0], port = i.xpath('.//td[2]/text()')[0])
                    ip_list.append(p)
        except Exception as e:
            print(e)
            print("\n\n\n\n Cannot fetch from Your source \n\n\n\n")

        return ip_list


    def urls(self) -> [str]:
        return [
            'https://www.us-proxy.org/',
        ]

