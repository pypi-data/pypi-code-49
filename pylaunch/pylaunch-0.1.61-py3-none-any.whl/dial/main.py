from typing import List, Callable
from re import sub
from urllib.parse import unquote, urlencode

from requests import Response

from pylaunch.core import Controller
from pylaunch.ssdp import SimpleServiceDiscoveryProtocol, ST_DIAL
from pylaunch.xmlparse import XMLFile


class AppNotFoundError(Exception):
    pass


def discover(timeout: int = 3) -> List["Dial"]:
    """
    Scans network for dial compatible devices and returns a list.
    """
    results = []
    SimpleServiceDiscoveryProtocol.settimeout(timeout)
    ssdp = SimpleServiceDiscoveryProtocol(ST_DIAL)
    response = ssdp.broadcast()
    for resp in response:
        location = resp.headers.get("location")
        if not location:
            continue
        results.append(Dial(location))
    return results


class Dial(Controller):
    def __init__(self, address: str):
        self.bind(address)
        self.instance_url = None
        self.refresh_url = None

    def __str__(self):
        return f"{self.friendly_name} ({self.address})"

    def bind(self, address: str) -> None:
        """
        A function called on __init__ to bind to a specific device.
        """
        resp = self.request.get(address)
        self.address = resp.headers.get("Application-URL")
        xml = XMLFile(resp.text)
        key = (
            lambda element: "_".join(sub("([a-z])([A-Z])", r"\1 \2", element).split())
            .lower()
            .replace("-", "_")
        )
        value = lambda element: xml.find(element).text
        tag_name = lambda element: element.tag.replace(xml.namespace, "")

        for element in [tag_name(el) for el in xml.find("device")]:
            try:
                k = key(element)
                v = value(element)
            except TypeError as e:
                print(e)
            finally:
                setattr(self, k, v) if v != "\n" else None

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

    def get_app_status(self, app_name: str) -> dict:
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

    def refresh_instance(self, inplace: bool = False) -> str:
        """
        Makes a request using the refresh_url stored in the instance
        of this class.
        """
        if not self.refresh_url:
            raise Exception("No refresh_url found in the dial instance.")
        resp = self.request.post(self.refresh_url)
        instance_url = resp.headers.get("location")
        if inplace:
            self.instance_url = instance_url
        else:
            return instance_url
