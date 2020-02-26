from urllib.parse import urlparse
from re import sub

import requests
from requests.exceptions import ConnectionError

from pylaunch.xmlparse import XMLFile, normalize


def _prepare_url(url):
    parsed = urlparse(url)
    if parsed.netloc == "":
        base, *path = parsed.path.split("/")
        url = (
            f"http://{base}:8060/{'/'.join(path)}"
            if ":" not in base
            else f"http://{base}/{'/'.join(path)}"
        )
        return url
    return f"http://{parsed.netloc}{parsed.path}"


class Controller:
    def __init__(self, address: str):
        self.bind(address)

    def bind(self, address: str) -> None:
        """
        A function called on __init__ to bind to a specific device.
        """
        url = _prepare_url(address)
        try:
            response = self.request.get(url)
            app_url = response.headers.get("Application-URL")

            self.address = _prepare_url(app_url) if app_url else url

            xml = XMLFile(response.text)
            for element in xml.find("device"):
                key, value = normalize(xml, element)
                setattr(self, key, value) if value else None
        except ConnectionError:
            self.address = url

    def __getitem__(self, prop):
        return self.__getattribute__(prop)

    def __enter__(self):
        self._session = requests.Session()
        return self

    def __exit__(self, *args):
        self._session.close()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.address!r})"

    @property
    def request(self) -> requests:
        if "_session" in dir(self):
            return self._session
        return requests
