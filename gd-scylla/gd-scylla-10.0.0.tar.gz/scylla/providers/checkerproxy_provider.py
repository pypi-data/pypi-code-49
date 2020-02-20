#GREENDECK

from requests_html import HTML

from scylla.database import ProxyIP
from .base_provider import BaseProvider
import json
from datetime import datetime,timedelta

class CheckerProxyProvider(BaseProvider):

    def parse(self, html: HTML) -> [ProxyIP]:
        ip_list: [ProxyIP] = []

        for i,ip_row in enumerate(json.loads(html.text)):

            try:

                ip, port = str(ip_row['addr']).split(':')
                p = ProxyIP(ip=ip, port=port)

                ip_list.append(p)
            except Exception as e:
                print(e)

        return ip_list

    def urls(self) -> [str]:
        today_date = str(datetime.now().strftime("%Y-%m-%d"))
        yesterday_date = str((datetime.now()-timedelta(days=1)).strftime("%Y-%m-%d"))
    
        base_url = 'https://checkerproxy.net/api/archive/'
        return [
            base_url+today_date,
            base_url+yesterday_date

        ]
        
    @staticmethod
    def should_render_js() -> bool:
        return False