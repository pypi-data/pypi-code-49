import requests


class Manager:

    def __init__(self, client):
        self.client = client

    def fetch_raw_data(self, imis_id):
        headers = {'Authorization': self.client.auth.authorization_header}
        url = self.client.url + f'/api/Party/{imis_id}'
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def update_raw_data(self, imis_id, data):
        headers = {'Authorization': self.client.auth.authorization_header}
        url = self.client.url + f'/api/Party/{imis_id}'
        response = requests.put(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()
