#!/usr/bin/python3
# -*- coding: utf-8 -*-
# import _4quila

import contextlib
import requests
import json
from .common import logger


class Session:
    def __init__(self, domain, cookies=None, headers=None):
        self._session = requests.session()
        self.domain = domain
        self.cookies = cookies or {}
        self.headers = headers or {}
        if "User-Agent" not in self.headers:
            self.headers["User-Agent"] = (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML,"
                " like Gecko) Ubuntu Chromium/69.0.3497.81 Chrome/69.0.3497.81 Safari/537.36"
            )

    def close(self):
        self._session.close()

    def _request(self, method, path, params=None, data=None, headers=None):
        params = params or {}
        data = data or {}
        headers = headers or {}
        logger.info(
            "%s ing %s" % (method, self.domain + path,)
            + (" params %s" % params if params else "")
            + (" data %s" % data if data else "")
            + (" headers %s" % headers if headers else "")
        )
        headers.update(self.headers)
        response = self._session.request(
            method,
            self.domain + path,
            data=json.dumps(data),
            params=params,
            cookies=self.cookies,
            headers=headers,
        )
        try:
            response_json = response.json()
            logger.info("responding json:\n%s" % json.dumps(response_json, indent=4))
            return response_json
        except Exception:
            logger.info("responding text:\n%s" % ("".join(response.text.splitlines())))
            return response.text

    def get(self, path, params=None, headers=None):
        return self._request("GET", path, params=params, headers=headers)

    def post(self, path, data=None, headers=None):
        return self._request("POST", path, data=data, headers=headers)

    def head(self, path, params=None, headers=None):
        return self._request("HEAD", path, params=params, headers=headers)


@contextlib.contextmanager
def session(domain, cookies=None, headers=None):
    _session = Session(domain, cookies=cookies, headers=headers)
    yield _session
    _session.close()
