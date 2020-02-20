#GREENDECK

from requests_html import HTML

from scylla.database import ProxyIP
from .base_provider import BaseProvider
import json

class HideMyIpProvider(BaseProvider):

    def parse(self, html: HTML) -> [ProxyIP]:
        ip_list: [ProxyIP] = []

        new_lines = []
        for line in (html.find('script')[8].html).split('\n')[2:]:
            if ";&lt;!-" not in line:
                new_lines.append(line)
            else:
                break
              
        for i,ip_row in enumerate(new_lines):
            #ip_row is string, removing last character(,)

            try:

                if '['==ip_row[0]:
                    ip_row = ip_row[1:]
                ip_row = ip_row[:-1]
                ip_row = json.loads(ip_row,)

                p = ProxyIP(ip=ip_row['i'], port=ip_row['p'])

                ip_list.append(p)
            except Exception as e:
                print(e)
                pass

        return ip_list

    def urls(self) -> [str]:
        return [
            'https://www.hide-my-ip.com/proxylist.shtml'
        ]
        
    @staticmethod
    def should_render_js() -> bool:
        return False