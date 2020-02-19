from django.core.exceptions import ObjectDoesNotExist
import os
import requests
import logging

logger = logging.getLogger(__name__)


class GiosgHttpApi:
    CHAT_HOST = os.environ.get('SERVICE_GIOSG_COM', 'https://service.giosg.com')

    def __init__(self, org_id, installation_model):
        try:
            conf = installation_model.objects.get(installed_org_uuid=org_id)
        except ObjectDoesNotExist:
            raise ValueError('Cannot instantiate Giosg API without persistent token. '
                             'Either app has not been installed for this org, '
                             'or the token was not saved on app install.')
        self.auth_headers = {'Authorization': '{} {}'.format(conf.persistent_token_prefix, conf.persistent_bot_token)}

    def get(self, endpoint, params={}, headers={}):
        try:
            response = requests.get(self.CHAT_HOST+endpoint,
                                    params=params,
                                    headers=dict(self.auth_headers, **headers))
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logger.exception(e)
            logger.exception(e.response.content)
            raise e
        return response

    def post(self, endpoint, json, headers={}):
        try:
            response = requests.post(self.CHAT_HOST+endpoint,
                                     json=json,
                                     headers=dict(self.auth_headers, **{'content-type': 'application/json'}, **headers))
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logger.exception(e)
            logger.exception(e.response.content)
            raise e
        return response

    def patch(self, endpoint, json, headers={}):
        try:
            response = requests.patch(self.CHAT_HOST+endpoint,
                                      json=json,
                                      headers=dict(self.auth_headers, **{'content-type': 'application/json'}, **headers))
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logger.exception(e)
            logger.exception(e.response.content)
            raise e
        return response

    def put(self, endpoint, json, headers={}):
        try:
            response = requests.put(self.CHAT_HOST+endpoint,
                                    json=json,
                                    headers=dict(self.auth_headers, **{'content-type': 'application/json'}, **headers))
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logger.exception(e)
            logger.exception(e.response.content)
            raise e
        return response

    def delete(self, endpoint, params={}, headers={}):
        try:
            response = requests.delete(self.CHAT_HOST+endpoint,
                                       params=params,
                                       headers=dict(self.auth_headers, **headers))
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logger.exception(e)
            logger.exception(e.response.content)
            raise e
        return response
