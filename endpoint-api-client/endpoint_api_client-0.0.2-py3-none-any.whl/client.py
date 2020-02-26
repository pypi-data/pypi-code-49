from typing import Tuple
from urllib.parse import urljoin

import requests


class StorageAPI:

    DEFAULT_HEADERS = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }

    def __init__(self, collection_url: str, headers: dict = None):
        headers_ = headers or self.DEFAULT_HEADERS
        self._sess = requests.Session()
        self._sess.headers = headers_

        if collection_url.endswith('/'):
            self.base_url = collection_url
            self.url = collection_url[:-1]
        else:
            self.base_url = collection_url + '/'
            self.url = collection_url

    def get_documents(self, **kwargs) -> requests.Response:
        resp = self._sess.get(self.url, **kwargs)
        return resp

    def put_document(self, doc_id, doc_payload, **kwargs) -> requests.Response:
        doc_url = urljoin(self.base_url, doc_id)
        resp = self._sess.put(doc_url, json=doc_payload, **kwargs)
        return resp

    def patch_document(self, doc_id, doc_payload, **kwargs) -> requests.Response:
        doc_url = urljoin(self.base_url, doc_id)
        resp = self._sess.put(doc_url, json=doc_payload, **kwargs)
        return resp

    def post_document(self, document: dict, **kwargs) -> requests.Response:
        resp = self._sess.post(self.url, json=document, **kwargs)
        return resp

    def post_documents(self, documents: Tuple[dict]) -> requests.Response:
        resp = self._sess.post(self.url, json=documents)
        return resp

    def delete_collection(self, **kwargs) -> requests.Response:
        resp = self._sess.delete(self.url, **kwargs)
        return resp

