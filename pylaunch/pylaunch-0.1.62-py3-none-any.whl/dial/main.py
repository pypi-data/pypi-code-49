from __future__ import annotations
from typing import List, Dict, Callable
from re import sub
from urllib.parse import unquote, urlencode

from requests import Response

from pylaunch.core import Controller
from pylaunch.ssdp import SimpleServiceDiscoveryProtocol, ST_DIAL
from pylaunch.xmlparse import XMLFile, normalize


class AppNotFoundError(Exception):
    pass


class Dial(Controller):
    @classmethod
    def discover(cls, timeout: int = 3) -> List[Dial]:
        """
        Scans network for dial compatible devices and returns a list.
        """
        results = []
        ssdp = SimpleServiceDiscoveryProtocol(ST_DIAL)
        ssdp.settimeout(timeout)
        response = ssdp.broadcast()
        for resp in response:
            location = resp.headers.get("location")
            if not location:
                continue
            results.append(cls(location))
        return results

    @classmethod
    def from_xml(cls, xml_text) -> Dial:
        xml = XMLFile(xml_text)
        for element in xml.find("device"):
            key, value = normalize(xml, element)
            setattr(cls, key, value) if value else None

    def _build_app_url(self, app_name: str = None) -> str:
        """
        Simple helper function to build app urls.
        """
        return "/".join([self.address, app_name])

    def launch_app(
        self, app_name: str, callback: Callable[[None], Response] = None, **kwargs
    ) -> None:
        """
        Launches specified application.
        """
        url = self._build_app_url(app_name)
        data = unquote(urlencode(kwargs))
        headers = (
            {"Content-Type": "text/plain; charset=utf-8"}
            if kwargs
            else {"Content-Length": "0"}
        )
        resp = self.request.post(url, data=data, headers=headers)

        if resp.status_code < 300:
            self.instance_url = resp.headers.get("location")
            self.refresh_url = unquote(resp.text)
            callback(resp) if callback else None
        elif resp.status_code == 404:
            raise AppNotFoundError(f"No application found with name {app_name}")
        else:
            resp.raise_for_status()

    def kill_app(
        self, app_name: str = None, callback: Callable[[None], Response] = None
    ) -> None:
        """
        This will kill any active application tracked by this 
        instance if one exists and will return True if successful 
        otherwise it will return False.
        """
        if app_name:
            app_url = self._build_app_url(app_name) + "/run"
        elif not app_name and not self.instance_url:
            raise Exception("There is no instance found to kill.")
        else:
            app_url = self.instance_url
        resp = self.request.delete(app_url)
        if resp.status_code in [200, 204]:
            self.instance_url = None
            self.refresh_url = None
        elif resp.status_code == 404:
            raise Exception(f"There is no running {app_name} instance.")
        callback(resp) if callback else None

    def get_app_status(self, app_name: str) -> Dict[str, str]:
        """
        Makes a request to the DIAL device with a application name parameter and returns
        a dictionary including the supported DIAL version, app name and state.
        State examples: running, stopped or installable
        """
        url = self._build_app_url(app_name)
        resp = self.request.get(url, headers={"Content-Type": "text/plain"})
        if resp.status_code == 404:
            raise AppNotFoundError(f"No application found with name {app_name}")
        xml = XMLFile(resp.text)
        return {
            "version": xml.find("service").attrib.get("dialVer"),
            "name": xml.find("name").text,
            "state": xml.find("state").text,
        }
