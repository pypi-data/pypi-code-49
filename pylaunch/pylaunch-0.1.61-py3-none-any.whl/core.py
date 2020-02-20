import requests
from urllib.parse import urlparse


class Controller:
    def __init__(self, address):
        parsed_url = urlparse(address)
        self.address = f"http://{parsed_url.netloc}"

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
