import requests


class BasicManager:

    def __init__(self, client):
        self.client = client

    def fetch_raw_data(self, object_name, imis_id=None):
        headers = {'Authorization': self.client.auth.authorization_header}
        url = self.client.url + f'/api/{object_name}'
        if imis_id:
            url += f'/{imis_id}'
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def update_raw_data(self, object_name, imis_id, data):
        headers = {'Authorization': self.client.auth.authorization_header}
        url = self.client.url + f'/api/{object_name}/{imis_id}'
        response = requests.put(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()
