import logging
import sys

import requests
from requests.exceptions import RequestException


class AppCenterWrapperException(Exception):
    pass


class AppCenter:
    def __init__(self, token: str, owner: str) -> None:
        self.token = token
        self.owner = owner
        self.headers = {
            'Content-Type': 'application/json',
            'X-API-Token': self.token
        }
        self.base_url = 'https://api.appcenter.ms'

    def get_new_idids(self, app_name: str, distr_grp_name: str) -> list():
        url = f'{self.base_url}/v0.1/apps/{self.owner}/{app_name}/distribution_groups/{distr_grp_name}/devices'
        try:
            req = requests.get(url, headers=self.headers)
        except RequestException as e:
            logging.error(e)
            sys.exit(1)
        if req.status_code == 200:
            to_provision = [d for d in req.json() if d.get('status') != 'provisioned']
            return to_provision
        else:
            logging.error(req.text)


if __name__ == '__main__':
    pass
