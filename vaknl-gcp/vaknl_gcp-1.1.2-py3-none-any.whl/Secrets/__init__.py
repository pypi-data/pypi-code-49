__author__ = "Wytze Bruinsma"

import json
import os

from google.cloud import secretmanager_v1beta1 as secretmanager

project_id = os.getenv('GOOGLE_CLOUD_PROJECT')
SECRET_CLIENT = secretmanager.SecretManagerServiceClient()


def get_secret(secret_id):
    version_id = 'latest'
    name = SECRET_CLIENT.secret_version_path(project_id, secret_id, version_id)
    response = SECRET_CLIENT.access_secret_version(name)
    return json.loads(response.payload.data.decode('UTF-8'))
