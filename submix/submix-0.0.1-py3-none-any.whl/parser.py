"""
Considering that "base64 sheme" is the defacto format of subscription config,
it will be the only supported format in the foreseeable future,
so this module is the parser for "base64 scheme subscription config"
"""

import json
import base64
from typing import List
from urllib.parse import urlparse, ParseResult


class ProxyURL:
    raw: str
    parsed: ParseResult
    scheme: str
    data_str: str
    data: dict
    name: str

    def __init__(self, raw):
        self.raw = raw
        self.parsed = urlparse(self.raw)
        self.scheme = self.parsed.scheme
        self.data_str = base64.b64decode(self.parsed.netloc.encode()).decode()
        self.data = json.loads(self.data_str)
        if self.scheme == 'vmess':
            self.name = self.data['ps']
        else:
            self.name = ''
        #print(self.data)


def parse_raw_config(raw: bytes) -> List[ProxyURL]:
    purls = []
    cfg_str = base64.b64decode(raw).decode()
    #print(cfg_str)
    for line in cfg_str.split('\n'):
        if not line:
            continue
        purl = ProxyURL(line)
        print(f'{purl.name}:\n  {purl.raw}')
        purls.append(purl)
    return purls
