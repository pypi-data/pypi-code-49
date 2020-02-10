import logging

import requests

log = logging.getLogger(__name__)


def custom_request(url, method, data=dict(), headers=None, timeout=5, return_type='json'):
    log.info('request detail: \n{}'.format(dict(url=url, method=method, headers=headers)))
    context = dict(headers=headers, timeout=timeout)
    try:
        if method == 'POST':
            req = requests.post(url, json=data, **context)
        elif method == 'GET':
            req = requests.get(url, params=data, **context)
        elif method == 'PUT':
            req = requests.put(url, json=data, **context)
        else:
            raise ValueError(method)
        if return_type == 'json':
            res = req.json()
        else:
            res = req.text
        return res
    except requests.exceptions.HTTPError as err:
        log.error(f'http error: status_code={err}')
    except Exception as err:
        log.error(f'request error: {err}')
