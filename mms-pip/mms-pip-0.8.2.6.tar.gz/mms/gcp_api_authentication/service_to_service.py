import requests
import google.auth.transport.requests as r
from google.oauth2 import id_token
import time
import pickle


class GCPJWT(object):
    def __init__(self, receiving_service_url):
        self.receiving_service_url = receiving_service_url
        self.metadata_server_token_url = 'http://metadata/computeMetadata/v1/instance/service-accounts/default/identity?audience='

    def _create_jwt_token(self):
        # Set up metadata server request
        # See https://cloud.google.com/compute/docs/instances/verifying-instance-identity#request_signature
        token_request_url = self.metadata_server_token_url + self.receiving_service_url
        token_request_headers = {'Metadata-Flavor': 'Google'}
        # Fetch the token
        token_response = requests.get(token_request_url, headers=token_request_headers)
        jwt = token_response.content.decode("utf-8")
        print(jwt)
        return jwt

    def _verify_token(self, token, get_only_exp=True):
        request = r.Request()
        payload = id_token.verify_token(token, request=request, audience=self.receiving_service_url)
        if get_only_exp is True:
            return payload.get('exp')
        else:
            return payload

    def get_token(self):
        token = self._create_jwt_token()
        exp = self._verify_token(token)
        return token, exp

    def check_if_token_is_exp(self, expiration_unix_time):
        unix_time_now = int(time.time())
        if unix_time_now < expiration_unix_time:
            return False
        else:
            return True

    def save_dict_to_local(self, df_dict, pickle_path):
        with open(pickle_path, 'wb') as f:
            pickle.dump(df_dict, f)

    def read_dict_from_local(self, pickle_path):
        try:
            with open(pickle_path, 'rb') as handle:
                df_dict = pickle.load(handle)
        except Exception as exc:
            df_dict = None
        return df_dict

