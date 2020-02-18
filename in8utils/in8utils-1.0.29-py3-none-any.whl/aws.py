from typing import Optional

import requests


class Aws:
    @staticmethod
    def get_az() -> Optional[str]:
        try:
            return requests.get('http://169.254.169.254/latest/meta-data/placement/availability-zone').text.upper().rsplit('-', 1)[1]
        except:
            return None

    @staticmethod
    def get_public_ip() -> str:
        try:
            return requests.get('http://169.254.169.254/latest/meta-data/public-ipv4').text
        except:
            return '127.0.0.1'

    @staticmethod
    def get_private_ip() -> str:
        try:
            return requests.get('http://169.254.169.254/latest/meta-data/local-ipv4').text
        except:
            return '127.0.0.1'
