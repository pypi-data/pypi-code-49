from abc import ABC, abstractmethod
from urllib.parse import urljoin

import requests


class SixgillBaseRequest(ABC):
    SIXGILL_API_BASE_URL = 'https://api.cybersixgill.com/'

    def __init__(self, *args, **kwargs):
        self.request = requests.Request(self.method, **kwargs)
        self.request.headers['Cache-Control'] = 'no-cache'

    @property
    @abstractmethod
    def end_point(self):
        pass

    @property
    @abstractmethod
    def method(self):
        pass

    def _get_url(self):
        return urljoin(self.SIXGILL_API_BASE_URL, self.end_point)

    def prepare(self):
        self.request.url = self._get_url()
        return self.request.prepare()
