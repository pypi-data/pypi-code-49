__author__ = "Wytze Bruinsma"

import json

from google.cloud import secretmanager_v1beta1 as secretmanager


class SecretsClient(object):

    def __init__(self, project_id):
        self.project_id = project_id
        self.secret_client = secretmanager.SecretManagerServiceClient()

    def get_secret(self, secret_id):
        version_id = 'latest'
        name = self.secret_client.secret_version_path(self.project_id, secret_id, version_id)
        response = self.secret_client.access_secret_version(name)
        return json.loads(response.payload.data.decode('UTF-8'))
