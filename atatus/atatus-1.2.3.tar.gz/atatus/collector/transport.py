
import json
import requests
from .builder import Builder
from atatus.utils import compat
from atatus.utils.logging import get_logger


class BaseTransport(object):
    def __init__(self, config, metadata):
        self._config = config
        self._error_logger = get_logger("atatus.errors")
        self._notify_host = config.notify_host if config.notify_host.endswith("/") else config.notify_host + "/"
        self._builder = Builder(config, metadata)
        self._session = requests.Session()
        self._blocked = False

    def _post(self, endpoint, data):
        if (self._blocked is True) and (endpoint != 'track/apm/hostinfo'):
            return

        try:
            r = self._session.post(self._notify_host + endpoint, timeout=30, json=data)

            if self._blocked is True:
                self._blocked = False

            if r.status_code != 200:
                self._error_logger.error(
                    "Atatus transport status non-200 response from backend [status_code: %r]" % r.status_code)

            if r.status_code == 400:
                c = r.content
                if not c:
                    self._error_logger.error("Atatus transport status 400, failed without content")
                    return

                if compat.PY3:
                    c = c.decode('UTF-8')

                resp = json.loads(c)
                if resp:
                    if "blocked" in resp:
                        self._blocked = resp["blocked"]
                        if self._blocked is True:
                            if "errorMessage" in resp:
                                self._error_logger.error(
                                    "Atatus blocked from sending data as: %s ", resp["errorMessage"])
                                return

                self._error_logger.error("Atatus transport status 400, failed with content: %r", c)
        except Exception as e:
            self._error_logger.error(
                "Atatus transport [%r] failed with exception: %r", self._notify_host + endpoint, e)
            raise

    def hostinfo(self, start_time):
        payload = self._builder.hostinfo(start_time)
        self._post('track/apm/hostinfo', payload)

    def txns(self, start_time, end_time, data):
        payload = self._builder.txns(start_time, end_time, data)
        self._post('track/apm/txn', payload)

    def traces(self, start_time, end_time, data):
        payload = self._builder.traces(start_time, end_time, data)
        self._post('track/apm/trace', payload)

    def error_metrics(self, start_time, end_time, metrics_data, requests_data):
        payload = self._builder.error_metrics(start_time, end_time, metrics_data, requests_data)
        self._post('track/apm/error_metric', payload)

    def errors(self, start_time, end_time, error_data):
        payload = self._builder.errors(start_time, end_time, error_data)
        self._post('track/apm/error', payload)

    def metrics(self, start_time, end_time, metrics_data):
        payload = self._builder.metrics(start_time, end_time, metrics_data)
        self._post('track/apm/metric', payload)
