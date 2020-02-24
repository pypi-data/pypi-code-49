from typing import List

import urllib3
from requests import Session

from .models.digi import DigiList
from .models.tools import PortScanResp, SendMail


class FailedToLogin(Exception):
    pass


class FailedRequest(Exception):
    pass


class Netauto:

    def __init__(self, netauto_url: str, api_version: int, username: str, password: str):
        self._session = Session()
        self._session.verify = False
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self._base_url = f"{netauto_url}/api/v{api_version}"
        self._username = username
        self._password = password
        self._login()

    def _login(self) -> None:
        user_data = {"username": self._username, "password": self._password}
        r = self._session.post(url=f"{self._base_url}/auth", data=user_data)
        if r.status_code != 201:
            raise FailedToLogin(r.text)
        else:
            self._access_token = r.json()["access_token"]
            self._session.headers["Authorization"] = f"Bearer {self._access_token}"
            return None

    def reboot_digi(self, ip: str) -> bool:
        r = self._session.post(url=f"{self._base_url}/digi/reboot/?ip={ip}")
        if r.status_code != 200:
            return False
        else:
            return True

    def get_all_digi(self) -> DigiList:
        r = self._session.get(url=f"{self._base_url}/digi/")
        if r.status_code != 200:
            raise FailedRequest(r.text)
        else:
            return DigiList(**r.json())

    def port_scan(self, ip: str, port: int) -> PortScanResp:
        r = self._session.post(url=f"{self._base_url}/tools/port_scan/?ip={ip}&port={port}")
        if r.status_code != 200:
            raise FailedRequest(r.text)
        else:
            return PortScanResp(**r.json())

    def send_mail(self, to: List[str], subject: str, content: str) -> SendMail:
        data = {"to": to, "subject": subject, "content": content}
        r = self._session.post(url=f"{self._base_url}/tools/send_mail/", json=data)
        if r.status_code != 200:
            raise FailedRequest(r.text)
        else:
            return SendMail(**r.json())
