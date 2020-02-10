import requests


class WhatIsMyIp:
    def get_ip(self) -> str:
        sources = (
            "http://icanhazip.com",
            "http://ident.me",
            "http://whatismyip.akamai.com",
            "http://ip.tyk.nu",
            "http://wgetip.com"
        )

        for source in sources:
            try:
                resp = requests.get(source)
                if resp.status_code == 200:
                    return resp.text.replace(' ', '').replace('\n', '').replace('\t', '')
            except:
                pass

        raise ConnectionError("Could not retrieve own IP from defined sources.")