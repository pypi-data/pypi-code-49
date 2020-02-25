import requests

from fattureincloud.exceptions import FattureInCloudHttpError

__title__ = "python-fattureincloud"
__version__ = "0.0.2"
__author__ = "Federico Torresan"


class FattureInCloud(object):
    """
    Main API object for fattura24
    """
    def __init__(self, api_uid, api_key):
        self.api_uid = api_uid
        self.api_key = api_key
        self.base_url = 'https://api.fattureincloud.it/v1/'

        # Endpoints definitions
        import importlib
        objects = importlib.import_module("invoice.fattureincloud.objects")
        self._objects = objects

        self.documento = objects.DocumentoManager(self)
        self.anagrafica = objects.AnagraficaManager(self)

    def _build_url(self, path=None):
        url = '%s' % self.base_url

        if path is not None:
            url = '%s%s' % (url, path)

        return url

    def http_request(self, path, data=None):
        if data is None:
            data = {}
        data['api_uid'] = self.api_uid
        data['api_key'] = self.api_key

        result = requests.post(self._build_url(path), json=data)
        error_message = result.content
        if 200 <= result.status_code < 300:
            json_response = result.json()
            if 'error' in json_response:
                error_message = json_response['error']
            else:
                return json_response

        raise FattureInCloudHttpError(
            response_code=result.status_code,
            error_message=error_message,
            response_body=result.content,
        )

