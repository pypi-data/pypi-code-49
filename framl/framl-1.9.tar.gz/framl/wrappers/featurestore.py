import json
import subprocess

import requests
from framl.config_cli import ConfigFraml


class FeatureStore:
    HOST = "https://feature-store-api-rzhg37iauq-ew.a.run.app"

    @staticmethod
    def _get_bearer() -> str:
        env = ConfigFraml.get_env()
        if env.lower() != "production":
            result = subprocess.run(["gcloud", "auth", "print-identity-token"], stdout=subprocess.PIPE)
            jwt = result.stdout.decode('utf-8').replace("\n", "")
            return jwt

        metadata_server_token_url = 'http://metadata/computeMetadata/v1/instance/service-accounts/default/identity?audience='

        token_request_url = metadata_server_token_url + FeatureStore.HOST
        token_request_headers = {'Metadata-Flavor': 'Google'}

        # Fetch the token
        token_response = requests.get(token_request_url, headers=token_request_headers)
        jwt = token_response.content.decode("utf-8")

        return jwt

    @staticmethod
    def get(universe: str, id: str) -> dict:
        # Provide the token in the request to the receiving service
        receiving_service_headers = {
            'Authorization': f'bearer {FeatureStore._get_bearer()}',
            'Content-type':  'application/json; charset=utf-8'
        }

        # sending the request. Please make sure the payload is a valid json string
        response = requests.get(url=f"{FeatureStore.HOST}/universes/{universe}/entities/{id}",
                                headers=receiving_service_headers)

        if response.status_code != 200:
            raise Exception(f'Error while requesting the FeatureStore:{response} status_code:{response.status_code}')
        return json.loads(response.content)