from __future__ import annotations
from typing import Callable, List

from pylaunch.core import Controller
from pylaunch.ssdp import ST_ROKU, SimpleServiceDiscoveryProtocol
from pylaunch.xmlparse import XMLFile, normalize
from pylaunch.roku.apps import Application


class Roku(Controller):
    @classmethod
    def discover(cls, timeout: int = 3) -> List[Roku]:
        """
        Scans the network for roku devices.
        """
        results = []
        SimpleServiceDiscoveryProtocol.settimeout(timeout)
        ssdp = SimpleServiceDiscoveryProtocol(ST_ROKU)
        response = ssdp.broadcast()
        for resp in response:
            location = resp.headers.get("location")
            if not location:
                continue
            results.append(cls(location))
        return results

    @property
    def active_app(self):
        request_url = f"{self.address}/query/active-app"
        response = self.request.get(request_url)
        xml = XMLFile(response.text)
        element = xml.find("app")
        return Application(
            name=element.text,
            id=element.attrib.get("id"),
            type=element.attrib.get("type"),
            subtype=element.attrib.get("subtype"),
            version=element.attrib.get("version"),
            roku=self,
        )

    @property
    def apps(self) -> List[Application]:
        applications = {}
        request_url = f"{self.address}/query/apps"
        response = self.request.get(request_url)
        xml = XMLFile(response.text)
        for element in xml.find("apps"):
            app = Application(
                name=element.text,
                id=element.attrib.get("id"),
                type=element.attrib.get("type"),
                subtype=element.attrib.get("subtype"),
                version=element.attrib.get("version"),
                roku=self,
            )
            applications[app.name] = app
        return applications

    @property
    def info(self):
        device_info = {}
        request_url = f"{self.address}/query/device-info"
        response = self.request.get(request_url)
        xml = XMLFile(response.text)
        for element in xml.find("device-info"):
            key, value = normalize(xml, element)
            device_info[key] = value
        return device_info

    def install_app(self, id: str, **kwargs) -> None:
        request_url = f"{self.address}/install/{str(id)}"
        response = self.request.post(
            request_url, params=kwargs, headers={"Content-Length": "0"}
        )

    def key_press(self, key: str, callback: Callable[[None], dict] = None) -> None:
        request_url = f"{self.address}/keypress/{str(key)}"
        response = self.request.post(request_url)
        if callback:
            results = {"request_url": request_url, "status_code": response.status_code}
            callback(results)

    def power(self):
        power_modes = {"PowerOn": "Headless", "Headless": "PowerOn"}
        toggle_power_mode = (
            lambda x: setattr(self, "power_mode", power_modes[self.power_mode])
            if x["status_code"] == 200
            else None
        )

        self.key_press("power", toggle_power_mode)
