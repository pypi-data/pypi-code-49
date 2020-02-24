# currently unused
import logging
from collections import Iterator

import requests


class AuthenticationException(Exception):
    def __init__(self):
        pass


class AtlNavigation(object):
    def __init__(self, authenticated_session: requests.session, initial_json):
        self.session = authenticated_session
        self.current_response = None
        self.next = None
        self.prev = None
        self.base = None
        self.current = None
        self.results = list()
        try:
            self._setup_response(initial_json)
        except Exception as ex:
            logging.exception(ex)
            raise ex

    def _setup_response(self, json_response):
        self.current_response = json_response
        _links = self.current_response["_links"]
        try:
            self.base = _links["base"]
        except:
            pass
        try:
            self.next = _links["next"]
        except:
            pass
        try:
            self.prev = _links["prev"]
        except:
            pass
        try:
            self.current = _links["self"]
        except:
            pass

        current_results: list = self.current_response["results"]
        if len(current_results) > 0:
            self.results.extend(current_results)

    def next_page(self):
        if self.current_response["size"] < self.current_response["limit"]:
            raise StopIteration()
        r = self.session.request("GET", f"{self.base}{self.next}")
        self._setup_response(r.json())

    def collect_results(self):
        while True:
            try:
                self.next_page()
            except StopIteration:
                break
            except Exception as ex:
                logging.error(ex)

    def flatten_web_ui_list(self, func_selector=None):
        try:
            self.collect_results()
        except Exception as ex:
            logging.exception(ex)
            raise ex
        if func_selector is not None:
            ui_urls: Iterator[str] = map(lambda x: f'{self.base}{x["_links"]["webui"]}',
                                         filter(func_selector, self.results))
        else:
            ui_urls: Iterator[str] = map(lambda x: f'{self.base}{x["_links"]["webui"]}', self.results)
        return ui_urls
