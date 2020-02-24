import logging

import requests

from atl_cache_warmer._utils import AtlNavigation


class ConfluenceSite(object):
    def __init__(self, confluence_url: str, confluence_username: str, confluence_password: str,
                 confluence_target_space: str, iterate: bool = False):
        self.confluence_url = confluence_url.rstrip('/')
        self.confluence_username = confluence_username
        self.confluence_password = confluence_password
        if confluence_target_space is not None:
            self.confluence_target_space = confluence_target_space.lstrip('/')
        else:
            self.confluence_target_space = None
        self.cookies = None
        self.session = requests.session()
        self.login()
        self.iterate_space = iterate

    def run(self):
        if self.iterate_space is False:
            response = self.session.request(method="GET",
                                            url=f'{self.confluence_url}/display/{self.confluence_target_space}',
                                            cookies=self.session.cookies)
            logging.debug(response.text.encode('utf8'))
        else:
            try:
                pages = self.get_pages_in_space()
            except Exception as ex:
                logging.exception(ex)
                raise ex

            for page in pages:
                try:
                    response = self.session.request(method="GET", url=page)
                    logging.debug(response.text.encode('utf8'))
                except Exception as ex:
                    logging.exception(ex)
            logging.info(f"finished running through pages in {self.confluence_target_space}")

    def login(self):
        url = f"{self.confluence_url}/dologin.action"
        logging.info(f"attempting login to Confluence using url: {url} ")

        payload = f'login=Log%20in&os_destination=&os_password={self.confluence_password}&os_username={self.confluence_username}'
        headers = {
            'Origin': f'{self.confluence_url}',
            'Upgrade-Insecure-Requests': '1',
            'DNT': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'Sec-Fetch-User': '?1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        }
        response = self.session.request("POST", url, headers=headers, data=payload)
        logging.debug(response.text.encode('utf8'))

        self.cookies = response.cookies  # save cookies
        logging.debug(response.cookies)
        # if response.status_code != 302:
        #     raise AuthenticationException()

    def get_pages_in_space(self):
        if self.confluence_target_space is None:
            return
        url = f"{self.confluence_url}/rest/api/content"
        parameters = {
            "spaceKey": f"{self.confluence_target_space}"
        }

        try:
            response = self.session.request("GET", url=url, params=parameters)
        except Exception as ex:
            logging.exception(ex)
            raise ex

        try:
            j = AtlNavigation(self.session, response.json())
        except Exception as ex:
            logging.exception(ex)
            raise ex
        try:
            flat = j.flatten_web_ui_list()
        except Exception as ex:
            logging.exception(ex)
            raise ex

        return flat
