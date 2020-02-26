__author__ = "Wytze Bruinsma"

import json
import os

from google.cloud import secretmanager_v1beta1 as secretmanager

project_id = os.getenv('GCP_PROJECT')


def get_secret(secret_id):
    version_id = 'latest'
    client = secretmanager.SecretManagerServiceClient()
    name = client.secret_version_path(project_id, secret_id, version_id)
    response = client.access_secret_version(name)
    return json.loads(response.payload.data.decode('UTF-8'))
