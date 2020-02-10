import time
import jwt
import json
import requests
import urllib

# https://medium.com/@stephen.darling/oauth2-authentication-with-google-cloud-run-700015a092c2


# TODO maybe see
#  - https://medium.com/google-cloud/authenticating-using-google-openid-connect-tokens-e7675051213b
#  - https://cloud.google.com/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/generateAccessToken


class APICalls(object):

    def __init__(self, service_url, sa_key_dict=None, sa_key_path=None):
        self.service_url = service_url
        self.sa_key_dict = sa_key_dict
        self.sa_key_path = sa_key_path

        if sa_key_dict is None and sa_key_path is None:
            raise ValueError("You have to specify either sa_key_dict or sa_key_path")

        if sa_key_dict is None:
            self.credentials = self.__read_sa_file()
        else:
            self.credentials = sa_key_dict

        self.__exp = None
        self.__signed_jwt = None
        self.__id_token = None

        self.__update_token()

    def __read_sa_file(self):
        with open(self.sa_key_path) as json_file:
            data = json.load(json_file)
        return data

    # create access token we can use as a Bearer token in future REST requests:
    def __exchange_jwt_for_token(self):
        body = {
            'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer',
            'assertion': self.__signed_jwt
        }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        token_request = requests.post(
            url='https://www.googleapis.com/oauth2/v4/token',
            headers=headers,
            data=urllib.parse.urlencode(body)
        )
        result = token_request.json()
        self.__id_token = result['id_token']

    # create the locally-signed JWT:
    def __create_signed_jwt(self):
        iat = time.time()
        exp = iat + 3600
        payload = {
            'iss': self.credentials['client_email'],
            'sub': self.credentials['client_email'],
            'target_audience': self.service_url,
            'aud': 'https://www.googleapis.com/oauth2/v4/token',
            'iat': iat,
            'exp': exp
        }
        additional_headers = {'kid': self.credentials['private_key_id']}
        self.__signed_jwt = jwt.encode(payload, self.credentials['private_key'], headers=additional_headers, algorithm='RS256')

    def __get_token_info(self):
        url = "https://oauth2.googleapis.com/tokeninfo?id_token={}".format(self.__id_token)
        r = requests.get(url=url)
        return json.loads(r.content.decode('utf-8'))

    def __update_token(self):
        time_now = time.time()
        if (self.__id_token is None) or (time_now >= self.__exp):
            self.__create_signed_jwt()
            self.__exchange_jwt_for_token()
            token_info = self.__get_token_info()
            self.__exp = float(token_info.get("exp"))

    def get_request(self, url):
        self.__update_token()
        return requests.get(url=url, headers={'Authorization': f'Bearer {self.__id_token}'})

    def post_request(self, url, request_body):
        self.__update_token()
        return requests.post(url=url,  data=json.dumps(request_body), headers={'Authorization': f'Bearer {self.__id_token}'})


if __name__ == '__main__':

    run_service_url = "https://test-api-h3e6iof3xq-ew.a.run.app/"
    auth_handler = APICalls(service_url=run_service_url, sa_key_path="sa-file.json")

    r1 = auth_handler.get_request(url="https://test-api-h3e6iof3xq-ew.a.run.app/apis/test2")

    request_body = {"test_dict:": 1, "test_dict1:": "Dast ist ein Test"}

    r4 = auth_handler.post_request(url="https://test-api-h3e6iof3xq-ew.a.run.app/apis/test1", request_body=request_body)
    response_body = json.loads(r4.content.decode('utf-8'))
    status = r4.status_code


    print("test")