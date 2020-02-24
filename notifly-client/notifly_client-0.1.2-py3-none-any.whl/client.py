import requests
from requests.auth import HTTPBasicAuth


class NotiflyClient:
    def __init__(self, host, app_id, app_secret):
        self.host = host
        self.app_id = app_id
        self.app_secret = app_secret

    def _post(self, endpoint, payload):
        url = f'{self.host}{endpoint}'
        return requests.post(
            url, json=payload, auth=HTTPBasicAuth(self.app_id, self.app_secret)
        )

    def send_notification(self, external_id, notification_type, link=None, metadata={}):
        return self._post(
            '/api/notification',
            {
                'type': notification_type,
                'link': link,
                'externalId': str(external_id),
                'metadata': metadata,
            },
        )

    def create_user(self, external_id, email):
        return self._post(
            '/api/user', {'externalId': str(external_id), 'email': email},
        )
